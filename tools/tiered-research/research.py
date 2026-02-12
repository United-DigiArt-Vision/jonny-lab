#!/usr/bin/env python3
"""
Tiered Social Media Research System
====================================
Tier 1 (Free):    FxTwitter API — single tweet lookups
Tier 2 (Cheap):   Grok API (xAI) — X/Twitter search + real-time intelligence
Tier 3 (Standard): Brave Search — general web research (returns instruction for caller)

Cascade: cheapest first, fallback on error.
All stdlib — no pip.
"""

import json
import hashlib
import os
import re
import subprocess
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
CACHE_DIR = SCRIPT_DIR / "cache"
CACHE_DIR.mkdir(exist_ok=True)

LOG_DIR = Path(__file__).resolve().parent.parent.parent / "mission-control" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
USAGE_LOG = LOG_DIR / "research-usage.jsonl"

CACHE_TTL = 3600  # 1 hour

# Cost estimates (USD) per call
COST_ESTIMATES = {
    "tier1_fxtwitter": 0.0,
    "tier2_grok": 0.003,   # ~3k tokens × $1/M input rough estimate
    "tier3_brave": 0.005,
}

# ---------------------------------------------------------------------------
# Cache
# ---------------------------------------------------------------------------

def _cache_key(query: str, tier: str) -> str:
    return hashlib.sha256(f"{query}|{tier}".encode()).hexdigest()


def cache_get(query: str, tier: str):
    key = _cache_key(query, tier)
    path = CACHE_DIR / f"{key}.json"
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text())
        if time.time() - data.get("ts", 0) > CACHE_TTL:
            path.unlink(missing_ok=True)
            return None
        return data["result"]
    except Exception:
        return None


def cache_set(query: str, tier: str, result):
    key = _cache_key(query, tier)
    path = CACHE_DIR / f"{key}.json"
    path.write_text(json.dumps({"ts": time.time(), "result": result}, ensure_ascii=False, default=str))

# ---------------------------------------------------------------------------
# Usage logging
# ---------------------------------------------------------------------------

def log_usage(tier: str, query: str, cached: bool):
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "tier": tier,
        "query": query[:200],
        "cost_estimate": 0.0 if cached else COST_ESTIMATES.get(tier, 0),
        "cached": cached,
    }
    with open(USAGE_LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")

# ---------------------------------------------------------------------------
# Tier 1 — FxTwitter (free, single tweet lookup)
# ---------------------------------------------------------------------------

def _extract_tweet_info(query: str):
    """Extract (screen_name, tweet_id) from URL or raw ID. screen_name may be None."""
    query = query.strip()
    # Direct ID
    if query.isdigit():
        return None, query
    # URL patterns: twitter.com/USER/status/ID or x.com/USER/status/ID
    parts = query.rstrip("/").split("/")
    for i, p in enumerate(parts):
        if p == "status" and i + 1 < len(parts):
            tid = parts[i + 1].split("?")[0]
            screen_name = parts[i - 1] if i > 0 else None
            if tid.isdigit():
                return screen_name, tid
    return None, None


def _extract_tweet_id(query: str):
    """Compat wrapper — returns just the ID."""
    _, tid = _extract_tweet_info(query)
    return tid


def tier1_fxtwitter(tweet_id: str, screen_name: str = None) -> dict:
    """Fetch a single tweet via FxTwitter API (free, no auth)."""
    user = screen_name or "i"
    url = f"https://api.fxtwitter.com/{user}/status/{tweet_id}"
    req = urllib.request.Request(url, headers={"User-Agent": "TieredResearch/1.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode())

# ---------------------------------------------------------------------------
# Tier 2 — Grok API (xAI)
# ---------------------------------------------------------------------------

def tier2_grok(query: str, search_type: str = "x_search") -> dict:
    """Query Grok API with search sources (x, web, or both)."""
    api_key = os.environ.get("XAI_API_KEY")
    if not api_key:
        raise EnvironmentError("XAI_API_KEY not set")

    sources = []
    if search_type in ("x_search", "both"):
        sources.append("x")
    if search_type in ("web_search", "both"):
        sources.append("web")
    if not sources:
        sources = ["x"]

    payload = json.dumps({
        "model": "grok-4-1-fast-non-reasoning",
        "messages": [
            {"role": "system", "content": "You are a research assistant. Return factual, concise results. Include sources/links where possible."},
            {"role": "user", "content": query},
        ],
        "search": {"mode": "auto", "sources": sources},
        "temperature": 0,
    }).encode()

    result = subprocess.run(
        ["curl", "-s", "-X", "POST", "https://api.x.ai/v1/chat/completions",
         "-H", f"Authorization: Bearer {api_key}",
         "-H", "Content-Type: application/json",
         "-d", payload.decode(),
         "--max-time", "30"],
        capture_output=True, text=True, timeout=35,
    )
    if result.returncode != 0:
        raise RuntimeError(f"curl failed: {result.stderr}")
    return json.loads(result.stdout)

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def lookup_tweet(query: str) -> dict:
    """Look up a single tweet. Tier 1 → Tier 2 cascade."""
    screen_name, tweet_id = _extract_tweet_info(query)
    if not tweet_id:
        return search_x(query)

    # Tier 1
    cached = cache_get(tweet_id, "tier1_fxtwitter")
    if cached:
        log_usage("tier1_fxtwitter", tweet_id, True)
        return {"tier": "tier1_fxtwitter", "cached": True, "data": cached}

    try:
        result = tier1_fxtwitter(tweet_id, screen_name)
        if result.get("code") == 200:
            cache_set(tweet_id, "tier1_fxtwitter", result)
            log_usage("tier1_fxtwitter", tweet_id, False)
            return {"tier": "tier1_fxtwitter", "cached": False, "data": result}
        raise ValueError(f"FxTwitter returned code {result.get('code')}")
    except Exception:
        pass  # fallback to Tier 2

    # Tier 2 fallback
    return search_x(f"tweet {tweet_id}")


def search_x(query: str) -> dict:
    """Search X/Twitter via Grok. Tier 2."""
    cached = cache_get(query, "tier2_grok")
    if cached:
        log_usage("tier2_grok", query, True)
        return {"tier": "tier2_grok", "cached": True, "data": cached}

    try:
        result = tier2_grok(query, "x_search")
        cache_set(query, "tier2_grok", result)
        log_usage("tier2_grok", query, False)
        return {"tier": "tier2_grok", "cached": False, "data": result}
    except Exception as e:
        return {"tier": "tier2_grok", "error": str(e)}


def search_web(query: str) -> dict:
    """Web search. Tier 2 (Grok web_search) → Tier 3 (Brave, caller-handled)."""
    cached = cache_get(query, "tier2_grok_web")
    if cached:
        log_usage("tier2_grok", query, True)
        return {"tier": "tier2_grok_web", "cached": True, "data": cached}

    try:
        result = tier2_grok(query, "web_search")
        cache_set(query, "tier2_grok_web", result)
        log_usage("tier2_grok", query, False)
        return {"tier": "tier2_grok_web", "cached": False, "data": result}
    except Exception:
        # Tier 3 — Brave Search (caller must handle via their own web_search tool)
        log_usage("tier3_brave", query, False)
        return {
            "tier": "tier3_brave",
            "cached": False,
            "data": None,
            "action_required": "Use Brave web_search tool with this query",
            "query": query,
        }


# ---------------------------------------------------------------------------
# Query Decomposition
# ---------------------------------------------------------------------------

def _is_complex_query(query: str) -> bool:
    """A query is complex if it has >3 words or contains AND/OR."""
    words = query.strip().split()
    if len(words) > 3:
        return True
    upper = query.upper()
    return " AND " in upper or " OR " in upper


def _decompose_query(query: str) -> list:
    """Split a complex query into 2-4 focused sub-queries."""
    # If explicit AND/OR, split on those
    upper = query.upper()
    if " AND " in upper or " OR " in upper:
        parts = re.split(r'\s+(?:AND|OR)\s+', query, flags=re.IGNORECASE)
        return [p.strip() for p in parts if p.strip()][:4]

    # Otherwise: extract key noun phrases / chunks
    words = query.strip().split()
    sub_queries = []
    # Full query always included as first
    sub_queries.append(query)
    # Try meaningful splits: first half, second half, key terms
    mid = len(words) // 2
    if mid >= 2:
        sub_queries.append(" ".join(words[:mid]))
        sub_queries.append(" ".join(words[mid:]))
    # Last 3 words as a focused sub-query
    if len(words) > 4:
        sub_queries.append(" ".join(words[-3:]))
    return sub_queries[:4]


def _merge_results(results: list) -> dict:
    """Merge multiple research results, deduplicating by content hash."""
    if not results:
        return {"error": "No results"}
    if len(results) == 1:
        return results[0]

    seen_content = set()
    merged_choices = []
    base = results[0].copy()

    for r in results:
        data = r.get("data") or {}
        if "choices" in data:
            for choice in data["choices"]:
                content = choice.get("message", {}).get("content", "")
                h = hashlib.md5(content.encode()).hexdigest()
                if h not in seen_content and content:
                    seen_content.add(h)
                    merged_choices.append(choice)

    if merged_choices:
        base.setdefault("data", {})["choices"] = merged_choices
        base["sub_queries_used"] = len(results)
    return base


# ---------------------------------------------------------------------------
# Engagement Ranking
# ---------------------------------------------------------------------------

def _compute_engagement(item: dict) -> int:
    """Compute engagement score from available metrics."""
    likes = int(item.get("likes", 0) or 0)
    retweets = int(item.get("retweets", 0) or 0)
    replies = int(item.get("replies", 0) or 0)
    return likes + retweets + replies


def _add_engagement_scores(result: dict) -> dict:
    """Add engagement_score to result data where metrics are available."""
    data = result.get("data") or {}

    # FxTwitter single tweet
    if "tweet" in data:
        t = data["tweet"]
        t["engagement_score"] = _compute_engagement(t)

    # Grok responses: parse search_results if present
    if "search_results" in data:
        for sr in data.get("search_results", []):
            for res in sr.get("results", []):
                res["engagement_score"] = _compute_engagement(res)
            # Sort by engagement
            sr["results"] = sorted(
                sr.get("results", []),
                key=lambda x: x.get("engagement_score", 0),
                reverse=True,
            )

    result["data"] = data
    return result


def research(query: str, mode: str = "auto") -> dict:
    """
    Main entry point.
    mode: auto | tweet | x_search | web_search
    """
    if mode == "tweet" or (mode == "auto" and _extract_tweet_id(query)):
        return _add_engagement_scores(lookup_tweet(query))
    elif mode == "x_search":
        return _run_with_decomposition(query, search_x, mode)
    elif mode == "web_search":
        return _add_engagement_scores(search_web(query))
    elif mode == "auto":
        result = _run_with_decomposition(query, search_x, mode)
        if "error" in result:
            return _add_engagement_scores(search_web(query))
        return result
    else:
        return {"error": f"Unknown mode: {mode}"}


def _run_with_decomposition(query: str, search_fn, mode: str) -> dict:
    """Run search with query decomposition if query is complex."""
    if _is_complex_query(query):
        sub_queries = _decompose_query(query)
        results = []
        for sq in sub_queries:
            r = search_fn(sq)
            if "error" not in r:
                results.append(r)
        if not results:
            # All failed, return last error
            return search_fn(query)
        merged = _merge_results(results)
        merged["decomposed"] = True
        merged["sub_queries"] = sub_queries
        return _add_engagement_scores(merged)
    else:
        return _add_engagement_scores(search_fn(query))

# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Tiered Social Media Research")
    parser.add_argument("query", help="Query string or tweet URL/ID")
    parser.add_argument("--mode", choices=["auto", "tweet", "x_search", "web_search"], default="auto")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    result = research(args.query, args.mode)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
    else:
        tier = result.get("tier", "?")
        cached = result.get("cached", False)
        decomposed = result.get("decomposed", False)
        print(f"[{tier}] {'(cached) ' if cached else ''}{'(decomposed) ' if decomposed else ''}")
        if decomposed:
            print(f"  Sub-queries: {result.get('sub_queries', [])}")
        if result.get("action_required"):
            print(f"→ {result['action_required']}")
            print(f"  Query: {result['query']}")
        elif "error" in result:
            print(f"Error: {result['error']}")
        else:
            data = result.get("data", {})
            # Pretty-print Grok response
            if "choices" in data:
                msg = data["choices"][0].get("message", {}).get("content", "")
                print(msg)
            # Pretty-print FxTwitter
            elif "tweet" in data:
                t = data["tweet"]
                print(f"@{t.get('author', {}).get('screen_name', '?')}: {t.get('text', '')}")
                print(f"♥ {t.get('likes', 0)}  🔁 {t.get('retweets', 0)}  💬 {t.get('replies', 0)}  📊 engagement: {t.get('engagement_score', 0)}")
            else:
                print(json.dumps(data, indent=2, ensure_ascii=False, default=str)[:2000])


if __name__ == "__main__":
    main()
