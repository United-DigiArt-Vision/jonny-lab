#!/usr/bin/env python3
"""Learning System for Research Tools - Self-improving content filter."""

import argparse
import json
import os
import sys
import tempfile
from datetime import datetime, timezone
from urllib.parse import urlparse

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(SCRIPT_DIR, "config.json")
LOG_PATH = os.path.join(SCRIPT_DIR, "learning-log.jsonl")


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)


def save_config(cfg):
    cfg["updated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    fd, tmp = tempfile.mkstemp(dir=SCRIPT_DIR, suffix=".json")
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(cfg, f, indent=2, ensure_ascii=False)
            f.write("\n")
        os.replace(tmp, CONFIG_PATH)
    except:
        os.unlink(tmp)
        raise


def log_entry(entry):
    entry["timestamp"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def extract_domain(url):
    if not url:
        return None
    try:
        d = urlparse(url).hostname or ""
        return d.removeprefix("www.")
    except:
        return None


def score_content(cfg, title="", url="", text=""):
    signals = []
    score = 50
    domain = extract_domain(url)
    combined = ((title or "") + " " + (text or "")).lower()

    # Skip domain check
    if domain and any(domain == d or domain.endswith("." + d) for d in cfg["skip_domains"]):
        signals.append(f"-30 skip_domain:{domain}")
        return {"score": 0, "signals": signals, "action": "skip"}

    # Prefer domain
    if domain and any(domain == d or domain.endswith("." + d) for d in cfg["prefer_domains"]):
        score += 15
        signals.append(f"+15 prefer_domain:{domain}")

    # Prefer keywords (max +40)
    kw_bonus = 0
    for kw in cfg["prefer_keywords"]:
        if kw.lower() in combined and kw_bonus < 40:
            score += 10
            kw_bonus += 10
            signals.append(f"+10 keyword:{kw}")

    # Skip keywords (max -30)
    kw_penalty = 0
    for kw in cfg["skip_keywords"]:
        if kw.lower() in combined and kw_penalty < 30:
            score -= 10
            kw_penalty += 10
            signals.append(f"-10 keyword:{kw}")

    score = max(0, min(100, score))
    action = "skip" if score < cfg["min_quality_score"] else "keep"
    return {"score": score, "signals": signals, "action": action}


def do_score(args):
    cfg = load_config()
    result = score_content(cfg, args.title or "", args.url or "", args.text or "")
    print(json.dumps(result, indent=2))


def do_learn(args):
    cfg = load_config()
    key_map = {
        "skip_domain": "skip_domains",
        "skip_keyword": "skip_keywords",
        "prefer_keyword": "prefer_keywords",
        "prefer_domain": "prefer_domains",
    }
    key = key_map[args.type]
    val = args.value.lower() if "domain" in args.type else args.value
    if val not in cfg[key]:
        cfg[key].append(val)
        save_config(cfg)
        log_entry({"action": "learn", "type": args.type, "value": val, "reason": args.reason or ""})
        print(json.dumps({"status": "added", "type": args.type, "value": val}))
    else:
        print(json.dumps({"status": "exists", "type": args.type, "value": val}))


def do_feedback(args):
    cfg = load_config()
    relevant = args.relevant.lower() == "true"
    domain = extract_domain(args.url)
    entry = {"action": "feedback", "url": args.url, "relevant": relevant, "domain": domain, "reason": args.reason or ""}
    log_entry(entry)

    if not relevant and domain:
        # Count irrelevant feedback for this domain
        count = 0
        if os.path.exists(LOG_PATH):
            with open(LOG_PATH) as f:
                for line in f:
                    try:
                        e = json.loads(line)
                        if e.get("action") == "feedback" and not e.get("relevant") and e.get("domain") == domain:
                            count += 1
                    except:
                        pass
        if count >= 3 and domain not in cfg["skip_domains"]:
            cfg["skip_domains"].append(domain)
            save_config(cfg)
            log_entry({"action": "auto_learn", "type": "skip_domain", "value": domain, "reason": f"{count} irrelevant results"})
            print(json.dumps({"status": "auto_skipped", "domain": domain, "irrelevant_count": count}))
            return
    elif relevant and args.title:
        # Suggest keywords from title
        stopwords = {"the","a","an","is","are","was","were","of","in","to","for","and","on","with","at","by","from","it","its","this","that","as","or"}
        words = [w for w in args.title.split() if len(w) > 2 and w.lower() not in stopwords]
        existing = {k.lower() for k in cfg["prefer_keywords"]}
        suggestions = [w for w in words if w.lower() not in existing][:5]
        if suggestions:
            print(json.dumps({"status": "suggestions", "suggested_prefer_keywords": suggestions}))
            return

    print(json.dumps({"status": "logged", "relevant": relevant}))


def do_stats(args):
    cfg = load_config()
    stats = {
        "skip_domains": len(cfg["skip_domains"]),
        "skip_keywords": len(cfg["skip_keywords"]),
        "prefer_domains": len(cfg["prefer_domains"]),
        "prefer_keywords": len(cfg["prefer_keywords"]),
        "min_quality_score": cfg["min_quality_score"],
        "updated_at": cfg["updated_at"],
    }

    # Recent learnings and domain frequency
    recent = []
    domain_freq = {}
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH) as f:
            for line in f:
                try:
                    e = json.loads(line)
                    recent.append(e)
                    if e.get("action") == "feedback" and not e.get("relevant") and e.get("domain"):
                        domain_freq[e["domain"]] = domain_freq.get(e["domain"], 0) + 1
                except:
                    pass

    stats["recent_learnings"] = recent[-10:]
    stats["top_skip_domains"] = sorted(domain_freq.items(), key=lambda x: -x[1])[:5]
    print(json.dumps(stats, indent=2))


def do_bulk_score(args):
    cfg = load_config()
    results = []
    with open(args.file) as f:
        for line in f:
            try:
                article = json.loads(line)
                r = score_content(cfg, article.get("title", ""), article.get("url", ""), article.get("text", ""))
                r["title"] = article.get("title", "")
                r["url"] = article.get("url", "")
                results.append(r)
            except:
                pass
    results.sort(key=lambda x: -x["score"])
    print(json.dumps(results, indent=2))


def main():
    p = argparse.ArgumentParser(description="Learning System for Research Tools")
    p.add_argument("--action", required=True, choices=["score", "learn", "feedback", "stats", "bulk-score"])
    p.add_argument("--title", default="")
    p.add_argument("--url", default="")
    p.add_argument("--text", default="")
    p.add_argument("--type", choices=["skip_domain", "skip_keyword", "prefer_keyword", "prefer_domain"])
    p.add_argument("--value", default="")
    p.add_argument("--reason", default="")
    p.add_argument("--relevant", default="")
    p.add_argument("--file", default="")

    args = p.parse_args()

    actions = {
        "score": do_score,
        "learn": do_learn,
        "feedback": do_feedback,
        "stats": do_stats,
        "bulk-score": do_bulk_score,
    }
    actions[args.action](args)


if __name__ == "__main__":
    main()
