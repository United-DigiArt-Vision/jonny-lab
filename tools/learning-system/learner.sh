#!/usr/bin/env bash
# Wrapper for learner.py
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$SCRIPT_DIR/learner.py" "$@"
