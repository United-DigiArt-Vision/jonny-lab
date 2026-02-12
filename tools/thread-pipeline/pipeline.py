#!/usr/bin/env python3
"""Thread Pipeline — Status-Tracking & Dedupe for x-threads/"""

import argparse, hashlib, json, os, re, sqlite3, sys
from datetime import datetime, timedelta
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent.parent
DB_PATH = WORKSPACE / "mission-control" / "threads.db"
THREADS_DIR = WORKSPACE / "x-threads"
VALID_STATUSES = {"pitched", "accepted", "rejected", "produced", "posted", "duplicate"}

# ── DB ────────────────────────────────────────────────────────────────

def get_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA journal_mode=WAL")
    conn.row_factory = sqlite3.Row
    conn.execute("""CREATE TABLE IF NOT EXISTS threads (
        id INTEGER PRIMARY KEY,
        file_path TEXT UNIQUE,
        title TEXT NOT NULL,
        tags TEXT DEFAULT '[]',
        status TEXT DEFAULT 'pitched',
        content_hash TEXT,
        keywords TEXT DEFAULT '[]',
        notes TEXT,
        created_at TEXT DEFAULT (datetime('now')),
        updated_at TEXT DEFAULT (datetime('now'))
    )""")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_threads_status ON threads(status)")
    conn.commit()
    return conn

# ── Helpers ───────────────────────────────────────────────────────────

def make_keywords(title, tags_str=""):
    words = set(re.findall(r'[a-z0-9]+', (title + " " + tags_str).lower()))
    stops = {"the","a","an","and","or","of","in","on","to","for","is","it","with","as","at","by","from","that","this","how","why","what","are","was","be"}
    return sorted(words - stops)

def content_hash(path):
    try:
        return hashlib.sha256(Path(path).read_bytes()).hexdigest()
    except Exception:
        return None

def extract_title_from_file(filepath):
    try:
        for line in Path(filepath).read_text(errors="replace").splitlines():
            line = line.strip()
            if line.startswith("# "):
                return line.lstrip("# ").strip()
    except Exception:
        pass
    return Path(filepath).stem

def extract_tags_from_filename(filename):
    stem = Path(filename).stem
    # Remove date prefix
    stem = re.sub(r'^\d{4}-\d{2}-\d{2}[-_]?', '', stem)
    parts = re.split(r'[-_]', stem)
    return [p.lower() for p in parts if p and len(p) > 1]

def jaccard(a, b):
    if not a and not b:
        return 0.0
    sa, sb = set(a), set(b)
    inter = sa & sb
    union = sa | sb
    return len(inter) / len(union) if union else 0.0

# ── Actions ───────────────────────────────────────────────────────────

def action_register(args, conn):
    filepath = args.file
    if not os.path.isabs(filepath):
        filepath = str(WORKSPACE / filepath)
    if not Path(filepath).exists():
        print(f"ERROR: File not found: {filepath}", file=sys.stderr)
        return 1
    rel = str(Path(filepath).relative_to(WORKSPACE)) if filepath.startswith(str(WORKSPACE)) else filepath
    title = args.title or extract_title_from_file(filepath)
    tags_str = args.tags or ",".join(extract_tags_from_filename(filepath))
    tags_list = [t.strip() for t in tags_str.split(",") if t.strip()]
    status = args.status or "pitched"
    if status not in VALID_STATUSES:
        print(f"ERROR: Invalid status '{status}'. Valid: {VALID_STATUSES}", file=sys.stderr)
        return 1
    kw = make_keywords(title, tags_str)
    ch = content_hash(filepath)
    try:
        conn.execute("INSERT INTO threads (file_path,title,tags,status,content_hash,keywords) VALUES (?,?,?,?,?,?)",
                      (rel, title, json.dumps(tags_list), status, ch, json.dumps(kw)))
        conn.commit()
        print(f"✅ Registered: {title} [{status}]")
    except sqlite3.IntegrityError:
        print(f"⚠️  Already registered: {rel}")
    return 0

def action_check(args, conn):
    title = args.title or ""
    tags_str = args.tags or ""
    kw_new = make_keywords(title, tags_str)
    title_words = set(re.findall(r'[a-z0-9]+', title.lower()))
    rows = conn.execute("SELECT id,title,tags,status,keywords FROM threads").fetchall()
    matches = []
    for r in rows:
        existing_kw = json.loads(r["keywords"]) if r["keywords"] else []
        existing_title_words = set(re.findall(r'[a-z0-9]+', r["title"].lower()))
        kw_sim = jaccard(kw_new, existing_kw)
        title_sim = jaccard(title_words, existing_title_words)
        score = 0.3 * kw_sim + 0.7 * title_sim
        if score > 0.4:
            matches.append({"id": r["id"], "title": r["title"], "score": round(score, 3), "status": r["status"]})
    matches.sort(key=lambda x: x["score"], reverse=True)
    result = {"is_duplicate": len(matches) > 0, "matches": matches}
    print(json.dumps(result, indent=2))
    return 0

def action_list(args, conn):
    query = "SELECT id,title,status,tags,created_at FROM threads WHERE 1=1"
    params = []
    if args.status:
        query += " AND status=?"
        params.append(args.status)
    if args.days:
        cutoff = (datetime.now() - timedelta(days=int(args.days))).isoformat()
        query += " AND created_at>=?"
        params.append(cutoff)
    query += " ORDER BY created_at DESC"
    rows = conn.execute(query, params).fetchall()
    if not rows:
        print("No threads found.")
        return 0
    print(f"| {'ID':>3} | {'Title':<50} | {'Status':<10} | {'Tags':<30} | {'Date':<16} |")
    print(f"|{'---':->5}|{'---':-<52}|{'---':-<12}|{'---':-<32}|{'---':-<18}|")
    for r in rows:
        tags = ", ".join(json.loads(r["tags"])) if r["tags"] else ""
        date = r["created_at"][:16] if r["created_at"] else ""
        title = r["title"][:48] + ".." if len(r["title"]) > 50 else r["title"]
        print(f"| {r['id']:>3} | {title:<50} | {r['status']:<10} | {tags:<30} | {date:<16} |")
    print(f"\nTotal: {len(rows)} threads")
    return 0

def action_update(args, conn):
    if not args.id:
        print("ERROR: --id required", file=sys.stderr); return 1
    if args.status and args.status not in VALID_STATUSES:
        print(f"ERROR: Invalid status. Valid: {VALID_STATUSES}", file=sys.stderr); return 1
    sets, params = ["updated_at=datetime('now')"], []
    if args.status:
        sets.append("status=?"); params.append(args.status)
    if args.notes:
        sets.append("notes=?"); params.append(args.notes)
    params.append(args.id)
    cur = conn.execute(f"UPDATE threads SET {','.join(sets)} WHERE id=?", params)
    conn.commit()
    if cur.rowcount:
        print(f"✅ Updated thread #{args.id}")
    else:
        print(f"ERROR: Thread #{args.id} not found", file=sys.stderr); return 1
    return 0

def action_stats(args, conn):
    total = conn.execute("SELECT COUNT(*) c FROM threads").fetchone()["c"]
    print(f"📊 Thread Stats\n{'='*40}\nTotal: {total}\n")
    print("By Status:")
    for r in conn.execute("SELECT status, COUNT(*) c FROM threads GROUP BY status ORDER BY c DESC"):
        print(f"  {r['status']:<12} {r['c']}")
    cutoff = (datetime.now() - timedelta(days=30)).isoformat()
    recent = conn.execute("SELECT COUNT(*) c FROM threads WHERE created_at>=?", (cutoff,)).fetchone()["c"]
    print(f"\nLast 30 days: {recent}")
    print("\nTag Distribution:")
    tag_counts = {}
    for r in conn.execute("SELECT tags FROM threads"):
        for t in json.loads(r["tags"]) if r["tags"] else []:
            tag_counts[t] = tag_counts.get(t, 0) + 1
    for tag, count in sorted(tag_counts.items(), key=lambda x: -x[1])[:15]:
        print(f"  {tag:<20} {count}")
    return 0

def action_scan(args, conn):
    if not THREADS_DIR.exists():
        print(f"ERROR: {THREADS_DIR} not found", file=sys.stderr); return 1
    existing = {r["file_path"] for r in conn.execute("SELECT file_path FROM threads").fetchall()}
    count = 0
    for f in sorted(THREADS_DIR.glob("*.md")):
        rel = str(f.relative_to(WORKSPACE))
        if rel in existing:
            continue
        title = extract_title_from_file(f)
        tags = extract_tags_from_filename(f.name)
        kw = make_keywords(title, ",".join(tags))
        ch = content_hash(f)
        conn.execute("INSERT INTO threads (file_path,title,tags,status,content_hash,keywords) VALUES (?,?,?,?,?,?)",
                      (rel, title, json.dumps(tags), "pitched", ch, json.dumps(kw)))
        count += 1
        print(f"  + {rel}")
    conn.commit()
    print(f"\n✅ Scanned: {count} new threads registered")
    return 0

# ── Main ──────────────────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser(description="Thread Pipeline")
    p.add_argument("--action", required=True, choices=["register","check","list","update","stats","scan"])
    p.add_argument("--file", help="Thread file path")
    p.add_argument("--title", help="Thread title")
    p.add_argument("--tags", help="Comma-separated tags")
    p.add_argument("--status", help="Thread status")
    p.add_argument("--id", type=int, help="Thread ID")
    p.add_argument("--notes", help="Notes")
    p.add_argument("--days", type=int, help="Filter by days")
    args = p.parse_args()
    conn = get_db()
    actions = {"register": action_register, "check": action_check, "list": action_list,
               "update": action_update, "stats": action_stats, "scan": action_scan}
    sys.exit(actions[args.action](args, conn))

if __name__ == "__main__":
    main()
