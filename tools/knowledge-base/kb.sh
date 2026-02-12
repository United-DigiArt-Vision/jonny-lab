#!/bin/bash
# Knowledge Base Shell Wrapper
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$SCRIPT_DIR/kb.py" "$@"
