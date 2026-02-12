#!/bin/bash
# AI Cost Tracker — Shell wrapper for log_usage.py
# Usage: log-usage.sh <model> <input_tokens> <output_tokens> <task_type> <description...>
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$SCRIPT_DIR/log_usage.py" "$@"
