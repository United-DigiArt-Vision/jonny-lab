#!/usr/bin/env python3
"""AI Cost Tracker — Report. Generates markdown reports from ai-usage.jsonl."""

import argparse
import json
import os
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE = os.path.dirname(os.path.dirname(SCRIPT_DIR))
LOG_FILE = os.path.join(WORKSPACE, "mission-control", "logs", "ai-usage.jsonl")

WARN_THRESHOLD = 0.25  # 25%
PRICING_FILE = os.path.join(SCRIPT_DIR, "pricing.json")

# Task types considered "simple" — don't need expensive models
SIMPLE_TASKS = {"classification", "scoring", "filtering", "tagging", "routing",
                "extraction", "summarization", "formatting", "validation"}

# Models considered expensive (input price >= $10/1M)
EXPENSIVE_THRESHOLD = 10  # $/1M input tokens


def load_entries(days=None, model=None, task_type=None):
    if not os.path.exists(LOG_FILE):
        return []
    cutoff = None
    if days:
        cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    entries = []
    with open(LOG_FILE) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            e = json.loads(line)
            ts = datetime.fromisoformat(e["timestamp"])
            if cutoff and ts < cutoff:
                continue
            if model and e["model"] != model:
                continue
            if task_type and e["taskType"] != task_type:
                continue
            entries.append(e)
    return entries


def fmt_cost(c):
    return f"${c:.4f}"


def fmt_tokens(t):
    if t >= 1_000_000:
        return f"{t/1_000_000:.1f}M"
    if t >= 1_000:
        return f"{t/1_000:.1f}K"
    return str(t)


def pct(part, total):
    return (part / total * 100) if total else 0


def _build_aggregates(entries):
    """Return (by_model, by_task, by_day, total_cost) dicts."""
    by_model = defaultdict(lambda: {"calls": 0, "tokens": 0, "cost": 0.0})
    by_task = defaultdict(lambda: {"calls": 0, "tokens": 0, "cost": 0.0})
    by_day = defaultdict(lambda: {"calls": 0, "tokens": 0, "cost": 0.0})
    for e in entries:
        for agg, key in [(by_model, e["model"]), (by_task, e["taskType"]), (by_day, e["timestamp"][:10])]:
            d = agg[key]
            d["calls"] += 1
            d["tokens"] += e["tokens"]["total"]
            d["cost"] += e["costEstimate"]
    total_cost = sum(e["costEstimate"] for e in entries)
    return by_model, by_task, by_day, total_cost


def _spend_warnings(by_model, by_task, total_cost):
    """Return list of warning strings for items exceeding WARN_THRESHOLD."""
    if total_cost <= 0:
        return []
    warnings = []
    for name, d in sorted(by_model.items(), key=lambda x: -x[1]["cost"]):
        p = pct(d["cost"], total_cost)
        if p > WARN_THRESHOLD * 100:
            warnings.append(
                f"⚠️ WARNING: Model **{name}** accounts for {p:.1f}% of total spend ({fmt_cost(d['cost'])}). "
                f"Consider using a cheaper model (e.g. Haiku/Flash) for simple tasks to reduce costs."
            )
    for name, d in sorted(by_task.items(), key=lambda x: -x[1]["cost"]):
        p = pct(d["cost"], total_cost)
        if p > WARN_THRESHOLD * 100:
            warnings.append(
                f"⚠️ WARNING: Task type **{name}** accounts for {p:.1f}% of total spend ({fmt_cost(d['cost'])}). "
                f"Consider batching, caching, or using lighter models for this task type."
            )
    return warnings


def report(entries):
    if not entries:
        print("No data found.")
        return

    total_calls = len(entries)
    total_tokens = sum(e["tokens"]["total"] for e in entries)
    total_cost = sum(e["costEstimate"] for e in entries)

    print("## 📊 AI Usage Report\n")
    print(f"**Total Calls:** {total_calls} | **Total Tokens:** {fmt_tokens(total_tokens)} | **Total Cost:** {fmt_cost(total_cost)}\n")

    by_model, by_task, by_day, _ = _build_aggregates(entries)

    print("### By Model\n")
    print("| Model | Calls | Tokens | Cost |")
    print("|-------|------:|-------:|-----:|")
    for name, d in sorted(by_model.items(), key=lambda x: -x[1]["cost"]):
        print(f"| {name} | {d['calls']} | {fmt_tokens(d['tokens'])} | {fmt_cost(d['cost'])} |")
    print()

    print("### By Task Type\n")
    print("| Task Type | Calls | Tokens | Cost |")
    print("|-----------|------:|-------:|-----:|")
    for name, d in sorted(by_task.items(), key=lambda x: -x[1]["cost"]):
        print(f"| {name} | {d['calls']} | {fmt_tokens(d['tokens'])} | {fmt_cost(d['cost'])} |")
    print()

    print("### By Day (recent)\n")
    print("| Date | Calls | Tokens | Cost |")
    print("|------|------:|-------:|-----:|")
    for day in sorted(by_day.keys(), reverse=True)[:10]:
        d = by_day[day]
        print(f"| {day} | {d['calls']} | {fmt_tokens(d['tokens'])} | {fmt_cost(d['cost'])} |")
    print()

    # Spend warnings
    warnings = _spend_warnings(by_model, by_task, total_cost)
    if warnings:
        print("### 🚨 Spend Warnings\n")
        for w in warnings:
            print(w)
        print()


def _load_pricing():
    """Load pricing data from pricing.json."""
    if not os.path.exists(PRICING_FILE):
        return {}
    with open(PRICING_FILE) as f:
        return json.load(f)


def _find_cheapest_capable(pricing):
    """Return (model_name, input_price, output_price) of cheapest model."""
    best = None
    for model, p in pricing.items():
        if best is None or p["input"] < best[1]:
            best = (model, p["input"], p["output"])
    return best


def routing_suggestions(entries=None, days=None):
    """Analyze workflows and suggest cheaper model routing."""
    if entries is None:
        entries = load_entries(days=days)
    if not entries:
        print("## 💡 Routing Suggestions\n")
        print("No data available for routing analysis.\n")
        return ""

    pricing = _load_pricing()
    cheapest = _find_cheapest_capable(pricing)

    # Group by (taskType, model)
    workflows = defaultdict(lambda: {"calls": 0, "cost": 0.0, "input_tokens": 0, "output_tokens": 0})
    for e in entries:
        key = (e.get("taskType", "unknown"), e.get("model", "unknown"))
        w = workflows[key]
        w["calls"] += 1
        w["cost"] += e["costEstimate"]
        w["input_tokens"] += e["tokens"].get("input", 0)
        w["output_tokens"] += e["tokens"].get("output", 0)

    # Determine time span for weekly projection
    if entries:
        timestamps = [datetime.fromisoformat(e["timestamp"]) for e in entries]
        span_days = max((max(timestamps) - min(timestamps)).total_seconds() / 86400, 1)
    else:
        span_days = 7

    suggestions = []
    for (task_type, model), w in workflows.items():
        model_pricing = pricing.get(model)
        if not model_pricing:
            continue
        # Only suggest if model is expensive
        if model_pricing["input"] < EXPENSIVE_THRESHOLD:
            continue
        # Only suggest if task is simple
        if task_type.lower() not in SIMPLE_TASKS:
            continue
        if not cheapest or cheapest[0] == model:
            continue

        # Calculate savings
        avg_input = w["input_tokens"] / w["calls"]
        avg_output = w["output_tokens"] / w["calls"]
        current_cost_per_call = (avg_input * model_pricing["input"] + avg_output * model_pricing["output"]) / 1_000_000
        cheap_cost_per_call = (avg_input * cheapest[1] + avg_output * cheapest[2]) / 1_000_000
        saving_per_call = current_cost_per_call - cheap_cost_per_call

        calls_per_week = w["calls"] / span_days * 7
        weekly_saving = saving_per_call * calls_per_week

        if weekly_saving < 0.001:
            continue

        suggestions.append({
            "task_type": task_type,
            "model": model,
            "model_pricing": model_pricing,
            "suggested_model": cheapest[0],
            "suggested_pricing": {"input": cheapest[1], "output": cheapest[2]},
            "calls": w["calls"],
            "calls_per_week": calls_per_week,
            "weekly_saving": weekly_saving,
            "reason": f"Simple {task_type} task, doesn't need {model.split('-')[0].capitalize()}",
        })

    suggestions.sort(key=lambda x: -x["weekly_saving"])

    lines = ["## 💡 Routing Suggestions\n"]
    if not suggestions:
        lines.append("No routing optimizations found. All workflows look efficient! ✅\n")
    else:
        for i, s in enumerate(suggestions, 1):
            lines.append(f"### {i}. {s['task_type']} — Potential savings: ${s['weekly_saving']:.2f}/week")
            lines.append(f"   Currently: {s['model']} (${s['model_pricing']['input']}/{s['model_pricing']['output']} per 1M)")
            lines.append(f"   Suggested: {s['suggested_model']} (${s['suggested_pricing']['input']}/{s['suggested_pricing']['output']} per 1M)")
            lines.append(f"   Reason: {s['reason']}")
            lines.append(f"   Calls/week: {s['calls_per_week']:.0f}")
            lines.append("")

    output = "\n".join(lines)
    print(output)
    return output


def weekly_report():
    """Generate a weekly summary comparing this week vs last week."""
    now = datetime.now(timezone.utc)
    # This week = last 7 days, prev week = 7-14 days ago
    this_week = load_entries(days=7)
    all_14 = load_entries(days=14)
    # Split: prev_week = entries older than 7 days within 14-day window
    cutoff_this = now - timedelta(days=7)
    prev_week = [e for e in all_14 if datetime.fromisoformat(e["timestamp"]) < cutoff_this]

    if not this_week:
        print("No data for this week.")
        return

    by_model, by_task, by_day, total_cost = _build_aggregates(this_week)

    print("## 📊 Weekly Cost Summary\n")
    print(f"**Period:** {(now - timedelta(days=7)).strftime('%Y-%m-%d')} → {now.strftime('%Y-%m-%d')}\n")
    print(f"**Total Cost:** {fmt_cost(total_cost)} | **Total Calls:** {len(this_week)} | **Total Tokens:** {fmt_tokens(sum(e['tokens']['total'] for e in this_week))}\n")

    # Expensive day
    if by_day:
        top_day = max(by_day.items(), key=lambda x: x[1]["cost"])
        print(f"**💰 Most Expensive Day:** {top_day[0]} — {fmt_cost(top_day[1]['cost'])}")

    # Expensive model
    if by_model:
        top_model = max(by_model.items(), key=lambda x: x[1]["cost"])
        print(f"**🤖 Most Expensive Model:** {top_model[0]} — {fmt_cost(top_model[1]['cost'])}")

    # Expensive task
    if by_task:
        top_task = max(by_task.items(), key=lambda x: x[1]["cost"])
        print(f"**🏷️ Most Expensive Task Type:** {top_task[0]} — {fmt_cost(top_task[1]['cost'])}")

    # Trend vs previous week
    prev_cost = sum(e["costEstimate"] for e in prev_week)
    if prev_cost > 0:
        change = (total_cost - prev_cost) / prev_cost * 100
        if change > 10:
            trend = f"📈 Rising (+{change:.0f}%)"
        elif change < -10:
            trend = f"📉 Falling ({change:.0f}%)"
        else:
            trend = f"➡️ Stable ({change:+.0f}%)"
        print(f"**📊 Trend vs Last Week:** {trend} (prev: {fmt_cost(prev_cost)})")
    else:
        print("**📊 Trend:** No previous week data for comparison.")

    print()

    # Spend warnings for this week too
    warnings = _spend_warnings(by_model, by_task, total_cost)
    if warnings:
        print("### 🚨 Spend Warnings\n")
        for w in warnings:
            print(w)
        print()

    # Append routing suggestions to weekly report
    routing_suggestions(entries=this_week)


def report_json(entries):
    """Output report as JSON."""
    if not entries:
        print(json.dumps({"total_calls": 0, "total_tokens": 0, "total_cost": 0}))
        return
    by_model, by_task, by_day, total_cost = _build_aggregates(entries)
    data = {
        "total_calls": len(entries),
        "total_tokens": sum(e["tokens"]["total"] for e in entries),
        "total_cost": round(total_cost, 4),
        "by_model": {k: {"calls": v["calls"], "tokens": v["tokens"], "cost": round(v["cost"], 4)} for k, v in by_model.items()},
        "by_task": {k: {"calls": v["calls"], "tokens": v["tokens"], "cost": round(v["cost"], 4)} for k, v in by_task.items()},
        "by_day": {k: {"calls": v["calls"], "tokens": v["tokens"], "cost": round(v["cost"], 4)} for k, v in by_day.items()},
        "warnings": _spend_warnings(by_model, by_task, total_cost),
    }
    print(json.dumps(data, indent=2))


def weekly_report_json():
    """Output weekly report as JSON."""
    now = datetime.now(timezone.utc)
    this_week = load_entries(days=7)
    all_14 = load_entries(days=14)
    cutoff_this = now - timedelta(days=7)
    prev_week = [e for e in all_14 if datetime.fromisoformat(e["timestamp"]) < cutoff_this]

    if not this_week:
        print(json.dumps({"total_cost": 0, "total_calls": 0, "trend": "no_data"}))
        return

    by_model, by_task, by_day, total_cost = _build_aggregates(this_week)
    prev_cost = sum(e["costEstimate"] for e in prev_week)

    if prev_cost > 0:
        change = (total_cost - prev_cost) / prev_cost * 100
        if change > 10:
            trend = "rising"
        elif change < -10:
            trend = "falling"
        else:
            trend = "stable"
    else:
        trend = "no_previous_data"

    data = {
        "period_start": (now - timedelta(days=7)).strftime('%Y-%m-%d'),
        "period_end": now.strftime('%Y-%m-%d'),
        "total_cost": round(total_cost, 4),
        "total_calls": len(this_week),
        "total_tokens": sum(e["tokens"]["total"] for e in this_week),
        "prev_week_cost": round(prev_cost, 4),
        "trend": trend,
        "by_model": {k: {"calls": v["calls"], "tokens": v["tokens"], "cost": round(v["cost"], 4)} for k, v in by_model.items()},
        "by_task": {k: {"calls": v["calls"], "tokens": v["tokens"], "cost": round(v["cost"], 4)} for k, v in by_task.items()},
        "warnings": _spend_warnings(by_model, by_task, total_cost),
    }
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="AI Cost Tracking Report")
    p.add_argument("--days", type=int, help="Filter last N days")
    p.add_argument("--model", help="Filter by model")
    p.add_argument("--task-type", help="Filter by task type")
    p.add_argument("--weekly", action="store_true", help="Show weekly summary with trend analysis")
    p.add_argument("--routing", action="store_true", help="Show model routing suggestions to reduce costs")
    p.add_argument("--json", action="store_true", dest="json_output", help="Output as JSON (machine-readable)")
    args = p.parse_args()

    if args.routing:
        routing_suggestions(days=args.days)
    elif args.weekly:
        if args.json_output:
            weekly_report_json()
        else:
            weekly_report()
    else:
        entries = load_entries(days=args.days, model=args.model, task_type=args.task_type)
        if args.json_output:
            report_json(entries)
        else:
            report(entries)
