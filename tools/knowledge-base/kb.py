#!/usr/bin/env python3
"""RAG Knowledge Base — ingest, search, list, stats. Pure stdlib + curl."""

import argparse, hashlib, json, math, os, re, sqlite3, subprocess, sys, time, fcntl
from pathlib import Path
from urllib.parse import urlparse, urlencode, parse_qs

DB_PATH = Path(__file__).resolve().parent.parent.parent / "mission-control" / "knowledge.db"
LOCK_PATH = str(DB_PATH) + ".lock"
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
EMBED_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-001:embedContent?key={GEMINI_API_KEY}"

CHUNK_SIZE, CHUNK_OVERLAP, CHUNK_MIN = 800, 200, 100
ERROR_WORDS = ["access denied", "captcha", "cloudflare", "404 not found", "403 forbidden", "just a moment"]

# ── helpers ──────────────────────────────────────────────────────────────

def _lock():
    f = open(LOCK_PATH, "w")
    fcntl.flock(f, fcntl.LOCK_EX)
    return f

def _unlock(f):
    fcntl.flock(f, fcntl.LOCK_UN)
    f.close()

def get_db():
    db = sqlite3.connect(str(DB_PATH))
    db.execute("PRAGMA journal_mode=WAL")
    db.execute("PRAGMA foreign_keys=ON")
    db.row_factory = sqlite3.Row
    db.executescript("""
        CREATE TABLE IF NOT EXISTS sources (
            id INTEGER PRIMARY KEY,
            url TEXT UNIQUE,
            title TEXT,
            source_type TEXT DEFAULT 'article',
            content TEXT,
            content_hash TEXT UNIQUE,
            tags TEXT DEFAULT '[]',
            created_at TEXT DEFAULT (datetime('now'))
        );
        CREATE TABLE IF NOT EXISTS chunks (
            id INTEGER PRIMARY KEY,
            source_id INTEGER REFERENCES sources(id) ON DELETE CASCADE,
            chunk_index INTEGER,
            content TEXT,
            embedding TEXT,
            created_at TEXT DEFAULT (datetime('now'))
        );
        CREATE INDEX IF NOT EXISTS idx_chunks_source ON chunks(source_id);
        CREATE INDEX IF NOT EXISTS idx_sources_type ON sources(source_type);
    """)
    return db

def normalize_url(url):
    if not url:
        return url
    p = urlparse(url)
    host = p.hostname or ""
    if host.startswith("www."):
        host = host[4:]
    qs = parse_qs(p.query)
    qs = {k: v for k, v in qs.items() if not k.startswith("utm_")}
    query = urlencode(qs, doseq=True)
    path = p.path.rstrip("/") or ""
    return f"{p.scheme}://{host}{path}{'?' + query if query else ''}"

def content_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def validate_content(text):
    if len(text.strip()) < 50:
        return False, "Content too short (<50 chars)"
    hits = sum(1 for w in ERROR_WORDS if w in text.lower())
    if hits >= 2:
        return False, f"Looks like error page ({hits} error markers found)"
    return True, ""

def strip_html(html):
    text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.S | re.I)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.S | re.I)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'&[a-zA-Z]+;', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def chunk_text(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks, current, pos = [], "", 0
    for sent in sentences:
        if len(current) + len(sent) + 1 > CHUNK_SIZE and len(current) >= CHUNK_MIN:
            chunks.append(current.strip())
            # overlap: keep last CHUNK_OVERLAP chars
            current = current[-CHUNK_OVERLAP:] + " " + sent
        else:
            current = (current + " " + sent).strip()
    if len(current.strip()) >= CHUNK_MIN:
        chunks.append(current.strip())
    if not chunks and text.strip():
        chunks = [text.strip()]
    return chunks

def get_embedding(text):
    if not GEMINI_API_KEY:
        print("ERROR: GEMINI_API_KEY not set", file=sys.stderr)
        sys.exit(1)
    body = json.dumps({"content": {"parts": [{"text": text[:8000]}]}})
    r = subprocess.run(
        ["curl", "-s", "-X", "POST", EMBED_URL,
         "-H", "Content-Type: application/json", "-d", body],
        capture_output=True, text=True, timeout=30
    )
    data = json.loads(r.stdout)
    if "embedding" not in data:
        print(f"Embedding error: {r.stdout[:300]}", file=sys.stderr)
        return None
    return data["embedding"]["values"]

def cosine_sim(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)

# ── fetchers ─────────────────────────────────────────────────────────────

def fetch_tweet(url):
    m = re.search(r'/status/(\d+)', url)
    if not m:
        return None, None
    tid = m.group(1)
    r = subprocess.run(
        ["curl", "-s", f"https://api.fxtwitter.com/status/{tid}"],
        capture_output=True, text=True, timeout=15
    )
    data = json.loads(r.stdout)
    tweet = data.get("tweet", {})
    text = tweet.get("text", "")
    author = tweet.get("author", {}).get("name", "")
    title = f"Tweet by {author}" if author else "Tweet"
    return title, text

def fetch_generic(url):
    r = subprocess.run(
        ["curl", "-sL", "-A", "Mozilla/5.0", "--max-time", "15", url],
        capture_output=True, text=True, timeout=20
    )
    return strip_html(r.stdout)

def detect_type(url):
    if not url:
        return "note"
    host = urlparse(url).hostname or ""
    if any(h in host for h in ["twitter.com", "x.com"]):
        return "tweet"
    if "youtube.com" in host or "youtu.be" in host:
        return "video"
    return "article"

# ── actions ──────────────────────────────────────────────────────────────

def action_ingest(args):
    url = normalize_url(args.url)
    stype = args.type or detect_type(url)
    tags = json.dumps([t.strip() for t in args.tags.split(",") if t.strip()]) if args.tags else "[]"

    # Fetch content
    if stype == "tweet":
        title, content = fetch_tweet(url)
        title = args.title or title
    elif stype == "video":
        title = args.title or f"Video: {url}"
        content = title  # minimal — transcript added separately
    else:
        content = fetch_generic(url)
        title = args.title or url

    if not content:
        print("ERROR: No content fetched"); return

    ok, reason = validate_content(content)
    if not ok:
        print(f"REJECTED: {reason}"); return

    chash = content_hash(content)
    lf = _lock()
    try:
        db = get_db()
        try:
            db.execute(
                "INSERT INTO sources (url, title, source_type, content, content_hash, tags) VALUES (?,?,?,?,?,?)",
                (url, title, stype, content, chash, tags)
            )
        except sqlite3.IntegrityError as e:
            print(f"DUPLICATE: {e}"); db.close(); return
        src_id = db.execute("SELECT last_insert_rowid()").fetchone()[0]

        chunks = chunk_text(content)
        for i, ch in enumerate(chunks):
            emb = get_embedding(ch)
            if emb is None:
                print(f"WARNING: embedding failed for chunk {i}"); continue
            db.execute(
                "INSERT INTO chunks (source_id, chunk_index, content, embedding) VALUES (?,?,?,?)",
                (src_id, i, ch, json.dumps(emb))
            )
            print(f"  Chunk {i+1}/{len(chunks)} embedded ✓")

        db.commit()
        db.close()
        print(f"✅ Ingested: \"{title}\" ({stype}) — {len(chunks)} chunks")
    finally:
        _unlock(lf)

def action_ingest_note(args):
    if not args.title or not args.content:
        print("ERROR: --title and --content required"); return
    tags = json.dumps([t.strip() for t in args.tags.split(",") if t.strip()]) if args.tags else "[]"
    content = args.content
    chash = content_hash(content)
    url = f"note://{hashlib.md5(content.encode()).hexdigest()[:12]}"

    lf = _lock()
    try:
        db = get_db()
        try:
            db.execute(
                "INSERT INTO sources (url, title, source_type, content, content_hash, tags) VALUES (?,?,?,?,?,?)",
                (url, args.title, "note", content, chash, tags)
            )
        except sqlite3.IntegrityError as e:
            print(f"DUPLICATE: {e}"); db.close(); return
        src_id = db.execute("SELECT last_insert_rowid()").fetchone()[0]

        chunks = chunk_text(content)
        for i, ch in enumerate(chunks):
            emb = get_embedding(ch)
            if emb is None:
                continue
            db.execute(
                "INSERT INTO chunks (source_id, chunk_index, content, embedding) VALUES (?,?,?,?)",
                (src_id, i, ch, json.dumps(emb))
            )
        db.commit()
        db.close()
        print(f"✅ Note ingested: \"{args.title}\" — {len(chunks)} chunks")
    finally:
        _unlock(lf)

def action_search(args):
    query_emb = get_embedding(args.query)
    if not query_emb:
        print("ERROR: could not embed query"); return

    lf = _lock()
    try:
        db = get_db()
        type_filter = ""
        params = []
        if args.type:
            type_filter = "AND s.source_type = ?"
            params.append(args.type)

        rows = db.execute(f"""
            SELECT c.content, c.embedding, c.source_id, s.title, s.url, s.source_type, s.tags
            FROM chunks c JOIN sources s ON c.source_id = s.id
            WHERE c.embedding IS NOT NULL {type_filter}
        """, params).fetchall()
        db.close()
    finally:
        _unlock(lf)

    scored = []
    for r in rows:
        emb = json.loads(r["embedding"])
        sim = cosine_sim(query_emb, emb)
        scored.append((sim, r))

    scored.sort(key=lambda x: -x[0])

    # Dedup by source
    seen, results = set(), []
    for sim, r in scored:
        if r["source_id"] in seen:
            continue
        seen.add(r["source_id"])
        results.append((sim, r))
        if len(results) >= (args.limit or 5):
            break

    if not results:
        print("No results found."); return

    print(f"🔍 Search: \"{args.query}\" — {len(results)} results\n")
    for sim, r in results:
        tags = json.loads(r["tags"]) if r["tags"] else []
        excerpt = r["content"][:500]
        print(f"  [{sim:.3f}] {r['title']}")
        print(f"    Type: {r['source_type']} | Tags: {', '.join(tags) if tags else '-'}")
        if r["url"] and not r["url"].startswith("note://"):
            print(f"    URL: {r['url']}")
        print(f"    {excerpt}\n")

def action_list(args):
    lf = _lock()
    try:
        db = get_db()
        q = "SELECT * FROM sources"
        params = []
        if args.type:
            q += " WHERE source_type = ?"
            params.append(args.type)
        q += " ORDER BY created_at DESC LIMIT ?"
        params.append(args.limit or 20)
        rows = db.execute(q, params).fetchall()
        db.close()
    finally:
        _unlock(lf)

    print(f"📋 Knowledge Base — {len(rows)} sources\n")
    for r in rows:
        tags = json.loads(r["tags"]) if r["tags"] else []
        print(f"  • {r['title']}")
        print(f"    Type: {r['source_type']} | Tags: {', '.join(tags) if tags else '-'} | {r['created_at']}")
        if r["url"] and not r["url"].startswith("note://"):
            print(f"    {r['url']}")
        print()

def action_stats(args):
    lf = _lock()
    try:
        db = get_db()
        src_count = db.execute("SELECT COUNT(*) FROM sources").fetchone()[0]
        chunk_count = db.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
        by_type = db.execute("SELECT source_type, COUNT(*) FROM sources GROUP BY source_type").fetchall()
        total_size = db.execute("SELECT COALESCE(SUM(LENGTH(content)),0) FROM sources").fetchone()[0]
        db.close()
    finally:
        _unlock(lf)

    print("📊 Knowledge Base Stats")
    print(f"  Sources: {src_count}")
    print(f"  Chunks:  {chunk_count}")
    print(f"  Size:    {total_size / 1024:.1f} KB")
    print(f"  By type:")
    for r in by_type:
        print(f"    {r[0]}: {r[1]}")

# ── main ─────────────────────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser(description="RAG Knowledge Base")
    p.add_argument("--action", required=True, choices=["ingest", "ingest-note", "search", "list", "stats"])
    p.add_argument("--url", default="")
    p.add_argument("--title", default="")
    p.add_argument("--content", default="")
    p.add_argument("--tags", default="")
    p.add_argument("--type", default="")
    p.add_argument("--query", default="")
    p.add_argument("--limit", type=int, default=0)
    args = p.parse_args()

    {"ingest": action_ingest, "ingest-note": action_ingest_note,
     "search": action_search, "list": action_list, "stats": action_stats}[args.action](args)

if __name__ == "__main__":
    main()
