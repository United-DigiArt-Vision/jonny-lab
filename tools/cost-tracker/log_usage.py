#!/usr/bin/env python3
"""AI Cost Tracker — Logger. Logs a single API call to ai-usage.jsonl."""

import json
import os
import sys
from datetime import datetime, timezone

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PRICING_FILE = os.path.join(SCRIPT_DIR, "pricing.json")
WORKSPACE = os.path.dirname(os.path.dirname(SCRIPT_DIR))
LOG_FILE = os.path.join(WORKSPACE, "mission-control", "logs", "ai-usage.jsonl")


def load_pricing():
    with open(PRICING_FILE) as f:
        return json.load(f)


def calc_cost(model, input_tokens, output_tokens, pricing):
    p = pricing.get(model)
    if not p:
        return 0.0
    return (input_tokens * p["input"] + output_tokens * p["output"]) / 1_000_000


def log_usage(model, input_tokens, output_tokens, task_type, description):
    pricing = load_pricing()
    cost = calc_cost(model, input_tokens, output_tokens, pricing)
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model": model,
        "tokens": {
            "input": input_tokens,
            "output": output_tokens,
            "total": input_tokens + output_tokens,
        },
        "taskType": task_type,
        "description": description,
        "costEstimate": round(cost, 6),
    }
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
    print(f"✅ Logged: {model} | {input_tokens+output_tokens} tokens | ${cost:.6f}")
    return entry


if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Usage: log_usage.py <model> <input_tokens> <output_tokens> <task_type> <description>")
        sys.exit(1)
    log_usage(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], " ".join(sys.argv[5:]))
