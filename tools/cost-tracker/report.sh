#!/bin/bash
# AI Cost Tracker — Shell wrapper for report.py
# Usage: report.sh [--days N] [--model X] [--task-type Y]
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$SCRIPT_DIR/report.py" "$@"
