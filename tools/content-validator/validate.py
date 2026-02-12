#!/usr/bin/env python3
"""Content Quality Validation Module.

Checks whether extracted content is clean data vs error pages, captchas, login walls, etc.

CLI:  python3 validate.py --text "..." [--type article|tweet|note] [--url "..."]
      echo "..." | python3 validate.py --type article
Module: from validate import validate_content
"""

import argparse
import json
import string
import sys


ERROR_SIGNALS = [
    "access denied", "403 forbidden", "captcha", "please enable javascript",
    "cloudflare", "404 not found", "sign in to continue", "blocked",
    "rate limit", "too many requests", "bot detected", "unusual traffic",
]

MIN_LENGTHS = {"article": 500, "tweet": 20, "note": 10}


def validate_content(text: str, content_type: str = "article", url: str = "") -> dict:
    issues = []
    score = 100
    text_lower = text.lower()

    # --- Error Page Detection ---
    hits = [s for s in ERROR_SIGNALS if s in text_lower]
    if len(hits) >= 2:
        score -= 50 * len(hits)
        issues.append(f"Error page detected ({len(hits)} signals: {', '.join(hits)})")

    # --- Min Length ---
    min_len = MIN_LENGTHS.get(content_type, 10)
    if len(text) < min_len:
        score -= 20
        issues.append(f"Too short for {content_type} ({len(text)}<{min_len} chars)")

    # --- Encoding Check ---
    if text:
        non_print = sum(1 for c in text if c not in string.printable and c not in "\n\r\t")
        if non_print / len(text) > 0.05:
            score -= 10
            issues.append(f"Encoding issues ({non_print} non-printable chars, {non_print*100//len(text)}%)")

    lines = text.splitlines()
    non_empty = [l for l in lines if l.strip()]

    # --- Prose Detection (articles only) ---
    if content_type == "article" and non_empty:
        long_lines = sum(1 for l in non_empty if len(l) > 80)
        ratio = long_lines / len(non_empty)
        if ratio < 0.15:
            score -= 30
            issues.append(f"Low prose ratio ({ratio:.0%} lines >80 chars, need ≥15%)")

    # --- Boilerplate Detection ---
    if non_empty and len(text) > 200:
        short = sum(1 for l in non_empty if len(l.strip()) < 30)
        if short / len(non_empty) > 0.5:
            score -= 20
            issues.append("Boilerplate suspected (>50% short lines)")

    # --- Duplicate Content ---
    paragraphs = [p.strip() for p in text.split("\n\n") if len(p.strip()) > 50]
    seen: dict[str, int] = {}
    for p in paragraphs:
        seen[p] = seen.get(p, 0) + 1
    dupes = {p: c for p, c in seen.items() if c >= 3}
    if dupes:
        score -= 5 * len(dupes)
        issues.append(f"Duplicate paragraphs: {len(dupes)}")

    score = max(0, score)
    has_error_page = any("Error page" in i for i in issues)
    has_min_length_fail = any("Too short" in i for i in issues)
    valid = score >= 50 and not has_error_page and not has_min_length_fail

    return {"valid": valid, "score": score, "issues": issues}


def main():
    parser = argparse.ArgumentParser(description="Validate extracted content quality")
    parser.add_argument("--text", default=None)
    parser.add_argument("--type", dest="content_type", default="article", choices=["article", "tweet", "note"])
    parser.add_argument("--url", default="")
    args = parser.parse_args()

    text = args.text if args.text is not None else sys.stdin.read()
    result = validate_content(text, args.content_type, args.url)
    print(json.dumps(result))
    sys.exit(0 if result["valid"] else 1)


if __name__ == "__main__":
    main()
