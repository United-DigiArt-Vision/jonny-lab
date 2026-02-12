#!/usr/bin/env python3
"""Lead/Proposal Tracker — SQLite-based. Pure stdlib."""

import argparse
import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timedelta

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'mission-control', 'leads.db')

SCHEMA = """
CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY,
    source TEXT NOT NULL,
    title TEXT NOT NULL,
    company TEXT,
    contact TEXT,
    price TEXT,
    url TEXT UNIQUE,
    notes TEXT,
    status TEXT DEFAULT 'new',
    score INTEGER DEFAULT 50,
    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT DEFAULT (datetime('now'))
);
CREATE TABLE IF NOT EXISTS status_history (
    id INTEGER PRIMARY KEY,
    lead_id INTEGER REFERENCES leads(id) ON DELETE CASCADE,
    old_status TEXT,
    new_status TEXT,
    notes TEXT,
    changed_at TEXT DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_leads_status ON leads(status);
CREATE INDEX IF NOT EXISTS idx_leads_source ON leads(source);
"""

def get_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    return conn

def parse_price(price_str):
    """Extract numeric value from price string like '$1,500' or '$75/hr'."""
    if not price_str:
        return 0
    m = re.search(r'[\d,]+(?:\.\d+)?', price_str.replace(',', ''))
    if not m:
        return 0
    val = float(m.group())
    if '/hr' in price_str.lower():
        val *= 20  # estimate 20hrs
    return val

def calc_score(source, title, price_str, url):
    score = 50
    val = parse_price(price_str)
    if val > 1000: score += 15
    elif val > 500: score += 10
    elif val > 200: score += 5
    if val > 0 and val < 100: score -= 10
    t = (title or '').lower()
    if 'ai' in t.split() or 'automation' in t: score += 10
    if source == 'upwork': score += 10
    if url: score += 5
    if 'volunteer' in t or 'unpaid' in t: score -= 15
    return max(0, min(100, score))

def jaccard(a, b):
    sa = set(a.lower().split())
    sb = set(b.lower().split())
    if not sa or not sb: return 0
    return len(sa & sb) / len(sa | sb)

def add_lead(args):
    db = get_db()
    score = calc_score(args.source, args.title, args.price, args.url)
    # dedup: URL
    if args.url:
        existing = db.execute("SELECT id, title FROM leads WHERE url=?", (args.url,)).fetchone()
        if existing:
            print(f"⚠️  DUPLICATE URL — existing lead #{existing['id']}: {existing['title']}")
            db.close(); return
    # dedup: title similarity
    rows = db.execute("SELECT id, title FROM leads").fetchall()
    for r in rows:
        if jaccard(args.title, r['title']) > 0.6:
            print(f"⚠️  Similar title to lead #{r['id']}: {r['title']} — adding anyway")
    db.execute(
        "INSERT INTO leads (source, title, company, contact, price, url, notes, status, score) VALUES (?,?,?,?,?,?,?,?,?)",
        (args.source, args.title, getattr(args, 'company', None), getattr(args, 'contact', None),
         args.price, args.url, getattr(args, 'notes', None), 'new', score))
    db.commit()
    lid = db.execute("SELECT last_insert_rowid()").fetchone()[0]
    db.execute("INSERT INTO status_history (lead_id, old_status, new_status, notes) VALUES (?, NULL, 'new', 'Created')", (lid,))
    db.commit()
    print(f"✅ Lead #{lid} added — Score: {score} — {args.title}")
    db.close()

def update_lead(args):
    db = get_db()
    row = db.execute("SELECT * FROM leads WHERE id=?", (args.id,)).fetchone()
    if not row:
        print(f"❌ Lead #{args.id} not found"); db.close(); return
    old = row['status']
    db.execute("UPDATE leads SET status=?, updated_at=datetime('now') WHERE id=?", (args.status, args.id))
    db.execute("INSERT INTO status_history (lead_id, old_status, new_status, notes) VALUES (?,?,?,?)",
               (args.id, old, args.status, getattr(args, 'notes', None)))
    db.commit()
    print(f"✅ Lead #{args.id}: {old} → {args.status}")
    # Emit CHAIN_EVENT for feedback loop
    if args.status in ("won", "lost"):
        event = {"event": args.status, "lead_id": args.id, "title": row["title"], "url": row["url"]}
        print(f"CHAIN_EVENT:{json.dumps(event)}")
    db.close()

def list_leads(args):
    db = get_db()
    q = "SELECT * FROM leads WHERE 1=1"
    params = []
    if args.status:
        q += " AND status=?"; params.append(args.status)
    if args.source:
        q += " AND source=?"; params.append(args.source)
    if args.days:
        cutoff = (datetime.now() - timedelta(days=int(args.days))).strftime('%Y-%m-%d')
        q += " AND created_at >= ?"; params.append(cutoff)
    sort = "score DESC" if getattr(args, 'sort', None) == 'score' else "created_at DESC"
    q += f" ORDER BY {sort}"
    rows = db.execute(q, params).fetchall()
    if not rows:
        print("No leads found."); db.close(); return
    print(f"| {'ID':>3} | {'Score':>5} | {'Source':<8} | {'Status':<10} | {'Price':<10} | {'Title':<40} | {'Date':<16} |")
    print(f"|{'-'*5}|{'-'*7}|{'-'*10}|{'-'*12}|{'-'*12}|{'-'*42}|{'-'*18}|")
    for r in rows:
        price = r['price'] or '-'
        print(f"| {r['id']:>3} | {r['score']:>5} | {r['source']:<8} | {r['status']:<10} | {price:<10} | {r['title'][:40]:<40} | {r['created_at']:<16} |")
    print(f"\n{len(rows)} leads total")
    db.close()

def stats(args):
    db = get_db()
    days_filter = ""
    params = []
    if args.days:
        cutoff = (datetime.now() - timedelta(days=int(args.days))).strftime('%Y-%m-%d')
        days_filter = " WHERE created_at >= ?"; params.append(cutoff)
    total = db.execute(f"SELECT COUNT(*) c FROM leads{days_filter}", params).fetchone()['c']
    applied = db.execute(f"SELECT COUNT(*) c FROM leads WHERE status IN ('applied','responded','interview','won','lost'){' AND created_at >= ?' if args.days else ''}", params).fetchone()['c']
    won = db.execute(f"SELECT COUNT(*) c FROM leads WHERE status='won'{' AND created_at >= ?' if args.days else ''}", params).fetchone()['c']
    print(f"📊 Lead Stats{f' (last {args.days} days)' if args.days else ''}")
    print(f"   Total: {total} | Applied: {applied} | Won: {won}")
    print(f"   Win Rate: {won/applied*100:.1f}%" if applied else "   Win Rate: N/A")
    # by source
    sources = db.execute(f"SELECT source, COUNT(*) c FROM leads{days_filter} GROUP BY source", params).fetchall()
    print("   By Source: " + ", ".join(f"{s['source']}: {s['c']}" for s in sources))
    # revenue
    won_rows = db.execute(f"SELECT price FROM leads WHERE status='won'{' AND created_at >= ?' if args.days else ''}", params).fetchall()
    rev = sum(parse_price(r['price']) for r in won_rows)
    print(f"   Revenue (Won): ${rev:,.0f}")
    # avg response time
    resp = db.execute("""SELECT AVG(julianday(sh.changed_at) - julianday(l.created_at)) avg_days
        FROM status_history sh JOIN leads l ON sh.lead_id=l.id
        WHERE sh.new_status='responded'""").fetchone()
    if resp['avg_days']:
        print(f"   Avg Response Time: {resp['avg_days']:.1f} days")
    db.close()

def search(args):
    db = get_db()
    q = f"%{args.query}%"
    rows = db.execute("SELECT * FROM leads WHERE title LIKE ? OR company LIKE ? OR notes LIKE ? ORDER BY score DESC", (q,q,q)).fetchall()
    if not rows:
        print("No results."); db.close(); return
    for r in rows:
        print(f"  #{r['id']} [{r['score']}] {r['source']}/{r['status']} — {r['title']} ({r['price'] or 'no price'})")
    db.close()

def migrate_seed(db):
    """Seed initial leads from the markdown tables."""
    seeds = [
        ('upwork', 'Swimming Handicap (Australien)', None, None, '$1,500', None, None, 'applied', '2025-02-08'),
        ('upwork', 'Zahnarztpraxis Dashboard (DE)', None, None, '$75/hr', None, None, 'applied', '2025-02-08'),
        ('upwork', 'AI Marketing Agent (USA)', None, None, '$50/hr', None, None, 'applied', '2025-02-08'),
        ('reddit', 'Victory Talent Web Dev', None, 'Dawn151515', None, None, None, 'applied', '2025-02-06'),
        ('reddit', 'r/hiring Software Dev', None, None, None, None, None, 'applied', '2025-02-06'),
        ('reddit', 'MANGO VA Position', None, None, None, None, None, 'applied', '2025-02-06'),
        ('reddit', '[For Hire] Fullstack + AI', None, None, None, None, None, 'applied', '2025-02-05'),
    ]
    for s in seeds:
        source, title, company, contact, price, url, notes, status, date = s
        score = calc_score(source, title, price, url)
        existing = db.execute("SELECT id FROM leads WHERE title=? AND source=?", (title, source)).fetchone()
        if existing:
            continue
        db.execute("INSERT INTO leads (source,title,company,contact,price,url,notes,status,score,created_at,updated_at) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                   (source, title, company, contact, price, url, notes, status, score, date, date))
        lid = db.execute("SELECT last_insert_rowid()").fetchone()[0]
        db.execute("INSERT INTO status_history (lead_id, old_status, new_status, notes, changed_at) VALUES (?, NULL, ?, 'Migrated from HEARTBEAT.md', ?)",
                   (lid, status, date))
    db.commit()

def add_contact(args):
    """Add a contact event to lead timeline (CRM feature)."""
    db = get_db()
    row = db.execute("SELECT * FROM leads WHERE id=?", (args.id,)).fetchone()
    if not row:
        print(f"❌ Lead #{args.id} not found"); db.close(); return
    # Ensure contact_history table exists
    db.execute('''CREATE TABLE IF NOT EXISTS contact_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lead_id INTEGER REFERENCES leads(id),
        type TEXT NOT NULL,
        summary TEXT,
        timestamp TEXT DEFAULT (datetime('now'))
    )''')
    ctype = args.contact_type or 'note'
    db.execute("INSERT INTO contact_history (lead_id, type, summary) VALUES (?,?,?)",
               (args.id, ctype, args.notes))
    db.execute("UPDATE leads SET last_contact=datetime('now'), updated_at=datetime('now') WHERE id=?", (args.id,))
    if args.email:
        db.execute("UPDATE leads SET email=? WHERE id=?", (args.email, args.id))
    db.commit()
    print(f"✅ Contact event added to lead #{args.id}: [{ctype}] {args.notes or ''}")
    db.close()

def timeline(args):
    """Show contact timeline for a lead."""
    db = get_db()
    db.execute('''CREATE TABLE IF NOT EXISTS contact_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lead_id INTEGER REFERENCES leads(id),
        type TEXT NOT NULL,
        summary TEXT,
        timestamp TEXT DEFAULT (datetime('now'))
    )''')
    row = db.execute("SELECT * FROM leads WHERE id=?", (args.id,)).fetchone()
    if not row:
        print(f"❌ Lead #{args.id} not found"); db.close(); return
    print(f"📋 Timeline for Lead #{args.id}: {row['title']}")
    print(f"   Source: {row['source']} | Status: {row['status']} | Score: {row['score']}")
    if row['email']:
        print(f"   Email: {row['email']}")
    if row['contact']:
        print(f"   Contact: {row['contact']}")
    print()
    # Status history
    sh = db.execute("SELECT * FROM status_history WHERE lead_id=? ORDER BY changed_at", (args.id,)).fetchall()
    ch = db.execute("SELECT * FROM contact_history WHERE lead_id=? ORDER BY timestamp", (args.id,)).fetchall()
    # Merge and sort
    events = []
    for s in sh:
        events.append((s['changed_at'], 'status', f"{s['old_status'] or 'new'} → {s['new_status']}" + (f" ({s['notes']})" if s['notes'] else '')))
    for c in ch:
        events.append((c['timestamp'], c['type'], c['summary'] or ''))
    events.sort(key=lambda x: x[0])
    if not events:
        print("   No events yet.")
    for ts, etype, desc in events:
        icon = {'status': '🔄', 'email_sent': '📤', 'email_received': '📥', 'proposal': '📝', 'call': '📞', 'meeting': '🤝', 'note': '📌'}.get(etype, '•')
        print(f"   {ts} {icon} [{etype}] {desc}")
    db.close()

def get_lead_source(args):
    """Lookup lead by ID for feedback chain."""
    db = get_db()
    row = db.execute("SELECT id, title, url, source, status FROM leads WHERE id=?", (args.id,)).fetchone()
    if not row:
        print(f"ERROR: Lead #{args.id} not found", file=sys.stderr)
        db.close(); return
    result = {"id": row["id"], "title": row["title"], "url": row["url"], "source": row["source"], "status": row["status"]}
    print(json.dumps(result, indent=2))
    db.close()


def main():
    p = argparse.ArgumentParser(description='Lead Tracker')
    p.add_argument('--action', required=True, choices=['add','update','list','stats','search','migrate','contact','timeline','get-source'])
    p.add_argument('--source', choices=['upwork','reddit','email','other'])
    p.add_argument('--title')
    p.add_argument('--company')
    p.add_argument('--contact')
    p.add_argument('--price')
    p.add_argument('--url')
    p.add_argument('--notes')
    p.add_argument('--id', type=int)
    p.add_argument('--status')
    p.add_argument('--days', type=int)
    p.add_argument('--sort', choices=['score','date'])
    p.add_argument('--query')
    p.add_argument('--email')
    p.add_argument('--contact-type', dest='contact_type', choices=['email_sent','email_received','proposal','call','meeting','note'])
    args = p.parse_args()

    if args.action == 'add':
        if not args.source or not args.title:
            print("❌ --source and --title required"); sys.exit(1)
        add_lead(args)
    elif args.action == 'update':
        if not args.id or not args.status:
            print("❌ --id and --status required"); sys.exit(1)
        update_lead(args)
    elif args.action == 'list':
        list_leads(args)
    elif args.action == 'stats':
        stats(args)
    elif args.action == 'search':
        if not args.query:
            print("❌ --query required"); sys.exit(1)
        search(args)
    elif args.action == 'contact':
        if not args.id:
            print("❌ --id required"); sys.exit(1)
        add_contact(args)
    elif args.action == 'timeline':
        if not args.id:
            print("❌ --id required"); sys.exit(1)
        timeline(args)
    elif args.action == 'get-source':
        if not args.id:
            print("❌ --id required"); sys.exit(1)
        get_lead_source(args)
    elif args.action == 'migrate':
        db = get_db()
        migrate_seed(db)
        print("✅ Migration complete")
        db.close()

if __name__ == '__main__':
    main()
