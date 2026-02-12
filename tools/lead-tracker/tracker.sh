#!/bin/bash
# Lead Tracker Shell Wrapper
DIR="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$DIR/tracker.py" "$@"
