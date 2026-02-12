#!/usr/bin/env python3
"""Chain Orchestrator — Central orchestrator for all Dragon Fleet chains.

CLI:
  python3 chain.py --chain news --query "AI automation"
  python3 chain.py --chain jobs --query "freelance AI developer" --source reddit
  python3 chain.py --chain council
  python3 chain.py --chain feedback --event posted --thread-id 5
  python3 chain.py --chain feedback --event won --lead-id 12 --reason "Great fit"
  python3 chain.py --chain health
"""

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent.parent
TOOLS = WORKSPACE / "tools"
CHAIN_LOG = WORKSPACE / "mission-control" / "chain-log.jsonl"

# Tool paths
RESEARCH_PY = TOOLS / "tiered-research" / "research.py"
VALIDATE_PY = TOOLS / "content-validator" / "validate.py"
LEARNER_PY = TOOLS / "learning-system" / "learner.py"
KB_PY = TOOLS / "knowledge-base" / "kb.py"
PIPELINE_PY = TOOLS / "thread-pipeline" / "pipeline.py"
TRACKER_PY = TOOLS / "lead-tracker" / "tracker.py"
REPORT_PY = TOOLS / "cost-tracker" / "report.py"

MIN_QUALITY_SCORE = 70  # maps to ≥7 on 1-10 scale


# ── Helpers ──────────────────────────────────────────────────────────

def run_tool(tool_path: str, args: list, timeout: int = 30) -> tuple:
    """Run a tool as subprocess. Returns (returncode, stdout, stderr)."""
    cmd = ["python3", str(tool_path)] + [str(a) for a in args]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout,
                           cwd=str(WORKSPACE))
        return r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "TIMEOUT"
    except Exception as e:
        return -2, "", str(e)


def log_chain_event(chain: str, step: str, status: str, details: dict = None):
    """Append to mission-control/chain-log.jsonl"""
    CHAIN_LOG.parent.mkdir(parents=True, exist_ok=True)
    entry = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "chain": chain,
        "step": step,
        "status": status,
    }
    if details:
        entry.update(details)
    with open(CHAIN_LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")


def parse_json_output(stdout: str) -> dict:
    """Try to parse JSON from stdout. Handles CHAIN_RESULT: prefix too."""
    for line in stdout.strip().splitlines():
        line = line.strip()
        if line.startswith("CHAIN_RESULT:"):
            line = line[len("CHAIN_RESULT:"):]
        try:
            return json.loads(line)
        except (json.JSONDecodeError, ValueError):
            continue
    # Try parsing the whole thing
    try:
        return json.loads(stdout)
    except (json.JSONDecodeError, ValueError):
        return {}


def extract_articles(stdout: str) -> list:
    """Extract articles from research.py JSON output."""
    try:
        data = json.loads(stdout)
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            return data.get("articles", data.get("results", []))
    except (json.JSONDecodeError, ValueError):
        pass
    return []


def extract_jobs(stdout: str) -> list:
    """Extract jobs from search results."""
    try:
        data = json.loads(stdout)
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            return data.get("results", data.get("jobs", []))
    except (json.JSONDecodeError, ValueError):
        pass
    return []


# ── Chains ───────────────────────────────────────────────────────────

def news_discovery_chain(query: str, tags: str = "") -> dict:
    """News Discovery Chain: research → validate → score → KB → dedupe → register."""
    result = {
        "articles_found": 0,
        "validated": 0,
        "scored_above_threshold": 0,
        "ingested": 0,
        "thread_suggestions": [],
        "errors": [],
    }

    # Step 1: Research
    t0 = time.time()
    rc, out, err = run_tool(RESEARCH_PY, [query, "--mode", "x_search", "--json"], timeout=60)
    duration = int((time.time() - t0) * 1000)
    if rc != 0:
        # Retry once
        log_chain_event("news", "research", "retry", {"error": err[:200], "duration_ms": duration})
        time.sleep(2)
        rc, out, err = run_tool(RESEARCH_PY, [query, "--mode", "x_search", "--json"], timeout=60)
        if rc != 0:
            log_chain_event("news", "research", "error", {"error": err[:200]})
            result["errors"].append(f"research failed: {err[:200]}")
            return result
    log_chain_event("news", "research", "ok", {"duration_ms": duration})

    articles = extract_articles(out)
    result["articles_found"] = len(articles)

    for article in articles:
        title = article.get("title", "")
        url = article.get("url", "")
        text = article.get("text", article.get("content", article.get("snippet", "")))
        article_tags = tags or ",".join(article.get("tags", []))

        # Step 2: Validate
        t0 = time.time()
        rc, out, err = run_tool(VALIDATE_PY, ["--text", text[:5000], "--type", "article"], timeout=15)
        duration = int((time.time() - t0) * 1000)
        if rc != 0:
            log_chain_event("news", "validate", "skip", {"article": title[:60], "error": err[:200], "duration_ms": duration})
            continue
        validation = parse_json_output(out)
        if not validation.get("valid", True):
            log_chain_event("news", "validate", "rejected", {"article": title[:60], "issues": validation.get("issues", []), "duration_ms": duration})
            continue
        result["validated"] += 1
        log_chain_event("news", "validate", "ok", {"article": title[:60], "duration_ms": duration})

        # Step 3: Score
        t0 = time.time()
        rc, out, err = run_tool(LEARNER_PY, ["--action", "score", "--title", title, "--url", url, "--text", text[:3000]], timeout=15)
        duration = int((time.time() - t0) * 1000)
        score = 50  # default
        if rc == 0:
            score_data = parse_json_output(out)
            score = score_data.get("score", 50)
            log_chain_event("news", "score", "ok", {"article": title[:60], "score": score, "duration_ms": duration})
        else:
            log_chain_event("news", "score", "error", {"article": title[:60], "error": err[:200], "duration_ms": duration})
            # Use default score=50

        if score < MIN_QUALITY_SCORE:
            log_chain_event("news", "score", "below_threshold", {"article": title[:60], "score": score})
            continue
        result["scored_above_threshold"] += 1

        # Step 4: KB Ingest
        t0 = time.time()
        kb_args = ["--action", "ingest", "--url", url, "--title", title]
        if article_tags:
            kb_args += ["--tags", article_tags]
        rc, out, err = run_tool(KB_PY, kb_args, timeout=60)
        duration = int((time.time() - t0) * 1000)
        if "DUPLICATE" in out:
            log_chain_event("news", "kb_ingest", "duplicate", {"article": title[:60], "duration_ms": duration})
            continue
        if rc != 0 and "GEMINI_API_KEY" in err:
            log_chain_event("news", "kb_ingest", "error", {"article": title[:60], "error": "GEMINI_API_KEY not set", "duration_ms": duration})
            result["errors"].append(f"KB ingest failed for '{title[:40]}': API key missing")
            # Continue anyway — still do dedupe check
        elif rc != 0:
            log_chain_event("news", "kb_ingest", "error", {"article": title[:60], "error": err[:200], "duration_ms": duration})
            result["errors"].append(f"KB ingest failed for '{title[:40]}': {err[:100]}")
        else:
            result["ingested"] += 1
            log_chain_event("news", "kb_ingest", "ok", {"article": title[:60], "duration_ms": duration})

        # Step 5: Dedupe
        t0 = time.time()
        rc, out, err = run_tool(PIPELINE_PY, ["--action", "check", "--title", title, "--tags", article_tags], timeout=15)
        duration = int((time.time() - t0) * 1000)
        if rc == 0:
            dedupe = parse_json_output(out)
            if dedupe.get("is_duplicate", False):
                log_chain_event("news", "dedupe", "duplicate", {"article": title[:60], "matches": dedupe.get("matches", []), "duration_ms": duration})
                continue
            log_chain_event("news", "dedupe", "ok", {"article": title[:60], "duration_ms": duration})
        else:
            # Fail open: register anyway
            log_chain_event("news", "dedupe", "error", {"article": title[:60], "error": err[:200], "duration_ms": duration})

        # Step 6: This article is a suggestion
        result["thread_suggestions"].append({
            "title": title,
            "url": url,
            "score": score,
        })

    return result


def job_hunting_chain(query: str, source: str = "reddit") -> dict:
    """Job Hunting Chain: search → score → add lead → contact log."""
    result = {
        "jobs_found": 0,
        "passed_filter": 0,
        "leads_added": [],
        "duplicates_skipped": 0,
        "errors": [],
    }

    # Step 1: We don't call web_search from CLI — this chain expects
    # pre-fetched results or uses research.py
    t0 = time.time()
    rc, out, err = run_tool(RESEARCH_PY, [query, "--mode", "web_search", "--json"], timeout=60)
    duration = int((time.time() - t0) * 1000)
    if rc != 0:
        log_chain_event("jobs", "search", "error", {"error": err[:200], "duration_ms": duration})
        result["errors"].append(f"search failed: {err[:200]}")
        return result
    log_chain_event("jobs", "search", "ok", {"duration_ms": duration})

    jobs = extract_jobs(out)
    result["jobs_found"] = len(jobs)

    for job in jobs:
        title = job.get("title", "")
        url = job.get("url", "")
        text = job.get("text", job.get("content", job.get("snippet", "")))
        price = job.get("price", "")

        # Step 2: Score
        t0 = time.time()
        rc, out, err = run_tool(LEARNER_PY, ["--action", "score", "--title", title, "--url", url, "--text", text[:2000]], timeout=15)
        duration = int((time.time() - t0) * 1000)
        if rc == 0:
            score_data = parse_json_output(out)
            action = score_data.get("action", "review")
            if action == "skip":
                log_chain_event("jobs", "score", "skip", {"job": title[:60], "duration_ms": duration})
                continue
            log_chain_event("jobs", "score", "ok", {"job": title[:60], "score": score_data.get("score", 50), "duration_ms": duration})
        else:
            log_chain_event("jobs", "score", "error", {"job": title[:60], "error": err[:200], "duration_ms": duration})
            # Continue with default

        result["passed_filter"] += 1

        # Step 3: Add lead
        t0 = time.time()
        lead_args = ["--action", "add", "--source", source, "--title", title]
        if url:
            lead_args += ["--url", url]
        if price:
            lead_args += ["--price", price]
        rc, out, err = run_tool(TRACKER_PY, lead_args, timeout=15)
        duration = int((time.time() - t0) * 1000)

        if "DUPLICATE" in out.upper():
            result["duplicates_skipped"] += 1
            log_chain_event("jobs", "add_lead", "duplicate", {"job": title[:60], "duration_ms": duration})
            continue
        if rc != 0:
            # Retry once
            rc, out, err = run_tool(TRACKER_PY, lead_args, timeout=15)
            if rc != 0:
                log_chain_event("jobs", "add_lead", "error", {"job": title[:60], "error": err[:200], "duration_ms": duration})
                result["errors"].append(f"add lead failed: {title[:40]}")
                continue

        # Extract lead ID from output like "✅ Lead #42 added"
        lead_id = None
        import re
        m = re.search(r'Lead #(\d+)', out)
        if m:
            lead_id = int(m.group(1))
            result["leads_added"].append(lead_id)

        log_chain_event("jobs", "add_lead", "ok", {"job": title[:60], "lead_id": lead_id, "duration_ms": duration})

        # Step 4: Auto-log discovery
        if lead_id:
            rc, out, err = run_tool(TRACKER_PY, [
                "--action", "contact", "--id", str(lead_id),
                "--contact-type", "note", "--notes", f"Auto-discovered via {source} search"
            ], timeout=10)
            log_chain_event("jobs", "contact_log", "ok" if rc == 0 else "error", {"lead_id": lead_id})

    return result


def council_feed() -> dict:
    """Collect all system signals for Dragon Council."""
    feed = {"timestamp": datetime.now(timezone.utc).isoformat()}

    # KB stats
    rc, out, err = run_tool(KB_PY, ["--action", "stats"], timeout=10)
    if rc == 0:
        feed["kb"] = out.strip()
    else:
        feed["kb"] = f"ERROR: {err[:100]}"
    log_chain_event("council", "kb_stats", "ok" if rc == 0 else "error")

    # Lead stats
    rc, out, err = run_tool(TRACKER_PY, ["--action", "stats"], timeout=10)
    if rc == 0:
        feed["leads"] = out.strip()
    else:
        feed["leads"] = f"ERROR: {err[:100]}"
    log_chain_event("council", "lead_stats", "ok" if rc == 0 else "error")

    # Thread stats
    rc, out, err = run_tool(PIPELINE_PY, ["--action", "stats"], timeout=10)
    if rc == 0:
        feed["threads"] = out.strip()
    else:
        feed["threads"] = f"ERROR: {err[:100]}"
    log_chain_event("council", "thread_stats", "ok" if rc == 0 else "error")

    # Cost report (weekly, json)
    rc, out, err = run_tool(REPORT_PY, ["--weekly", "--json"], timeout=10)
    if rc == 0:
        feed["costs"] = out.strip()
    else:
        feed["costs"] = f"ERROR: {err[:100]}"
    log_chain_event("council", "cost_stats", "ok" if rc == 0 else "error")

    # Learning stats
    rc, out, err = run_tool(LEARNER_PY, ["--action", "stats"], timeout=10)
    if rc == 0:
        feed["learning"] = out.strip()
    else:
        feed["learning"] = f"ERROR: {err[:100]}"
    log_chain_event("council", "learning_stats", "ok" if rc == 0 else "error")

    return feed


def feedback_chain(event: str, thread_id: int = None, lead_id: int = None, reason: str = "") -> dict:
    """Feedback loop: look up source, call learner feedback."""
    result = {"status": "ok", "feedback_result": {}}

    relevant = event in ("posted", "won")
    relevant_str = "true" if relevant else "false"

    title = ""
    url = ""

    if thread_id is not None:
        # Look up thread source
        rc, out, err = run_tool(PIPELINE_PY, ["--action", "get-source", "--id", str(thread_id)], timeout=10)
        if rc == 0:
            data = parse_json_output(out)
            title = data.get("title", "")
            url = data.get("source_url", "") or ""
        else:
            log_chain_event("feedback", "lookup_thread", "error", {"thread_id": thread_id, "error": err[:200]})
            result["status"] = "partial"

    elif lead_id is not None:
        # Look up lead source
        rc, out, err = run_tool(TRACKER_PY, ["--action", "get-source", "--id", str(lead_id)], timeout=10)
        if rc == 0:
            data = parse_json_output(out)
            title = data.get("title", "")
            url = data.get("url", "") or ""
        else:
            log_chain_event("feedback", "lookup_lead", "error", {"lead_id": lead_id, "error": err[:200]})
            result["status"] = "partial"

    # Call learner feedback
    fb_args = ["--action", "feedback", "--relevant", relevant_str]
    if title:
        fb_args += ["--title", title]
    if url:
        fb_args += ["--url", url]
    if reason:
        fb_args += ["--reason", reason]

    rc, out, err = run_tool(LEARNER_PY, fb_args, timeout=15)
    if rc == 0:
        result["feedback_result"] = parse_json_output(out) or {"output": out.strip()}
        log_chain_event("feedback", "learner", "ok", {"event": event, "relevant": relevant})
    else:
        result["status"] = "error"
        result["feedback_result"] = {"error": err[:200]}
        log_chain_event("feedback", "learner", "error", {"event": event, "error": err[:200]})

    return result


def chain_health() -> dict:
    """Quick health check all chain dependencies."""
    health = {}
    checks = [
        ("kb", KB_PY, ["--action", "stats"]),
        ("leads", TRACKER_PY, ["--action", "stats"]),
        ("threads", PIPELINE_PY, ["--action", "stats"]),
        ("learner", LEARNER_PY, ["--action", "stats"]),
        ("report", REPORT_PY, ["--days", "1"]),
    ]
    for name, tool, args in checks:
        rc, out, err = run_tool(tool, args, timeout=5)
        health[name] = "ok" if rc == 0 else f"error: {err[:100]}"

    # Check DB files
    for name, path in [
        ("knowledge.db", WORKSPACE / "mission-control" / "knowledge.db"),
        ("leads.db", WORKSPACE / "mission-control" / "leads.db"),
        ("threads.db", WORKSPACE / "mission-control" / "threads.db"),
    ]:
        health[f"db_{name}"] = "exists" if path.exists() else "missing"

    # Check API keys
    health["GEMINI_API_KEY"] = "set" if os.environ.get("GEMINI_API_KEY") else "missing"
    health["XAI_API_KEY"] = "set" if os.environ.get("XAI_API_KEY") else "missing"

    return health


# ── Main ─────────────────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser(description="Chain Orchestrator — Dragon Fleet")
    p.add_argument("--chain", required=True,
                   choices=["news", "jobs", "council", "feedback", "health"],
                   help="Which chain to run")
    p.add_argument("--query", help="Search query (news/jobs chains)")
    p.add_argument("--tags", default="", help="Comma-separated tags (news chain)")
    p.add_argument("--source", default="reddit", help="Lead source (jobs chain)")
    p.add_argument("--event", choices=["posted", "rejected", "won", "lost"],
                   help="Feedback event type")
    p.add_argument("--thread-id", type=int, help="Thread ID (feedback chain)")
    p.add_argument("--lead-id", type=int, help="Lead ID (feedback chain)")
    p.add_argument("--reason", default="", help="Reason for feedback")
    args = p.parse_args()

    if args.chain == "news":
        if not args.query:
            print("ERROR: --query required for news chain", file=sys.stderr)
            sys.exit(1)
        result = news_discovery_chain(args.query, args.tags)
        print(json.dumps(result, indent=2))

    elif args.chain == "jobs":
        if not args.query:
            print("ERROR: --query required for jobs chain", file=sys.stderr)
            sys.exit(1)
        result = job_hunting_chain(args.query, args.source)
        print(json.dumps(result, indent=2))

    elif args.chain == "council":
        result = council_feed()
        print(json.dumps(result, indent=2))

    elif args.chain == "feedback":
        if not args.event:
            print("ERROR: --event required for feedback chain", file=sys.stderr)
            sys.exit(1)
        if not args.thread_id and not args.lead_id:
            print("ERROR: --thread-id or --lead-id required", file=sys.stderr)
            sys.exit(1)
        result = feedback_chain(args.event, args.thread_id, args.lead_id, args.reason)
        print(json.dumps(result, indent=2))

    elif args.chain == "health":
        result = chain_health()
        print(json.dumps(result, indent=2))
        # Exit code: 1 if any error
        if any("error" in str(v) for v in result.values()):
            sys.exit(1)


if __name__ == "__main__":
    main()
