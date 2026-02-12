#!/usr/bin/env bash
# Thread Pipeline wrapper
DIR="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$DIR/pipeline.py" "$@"
