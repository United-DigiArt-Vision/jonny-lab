#!/bin/bash
# Grok Live Search — News Scanner
# Uses xAI Responses API with x_search + web_search tools
# Usage: grok-news-search.sh [query] [hours_back]

QUERY="${1:-breaking AI technology science innovation news}"
HOURS_BACK="${2:-3}"
TODAY=$(date -u +%Y-%m-%d)

curl -s --max-time 120 https://api.x.ai/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $XAI_API_KEY" \
  -d "$(cat <<EOF
{
  "model": "grok-4-1-fast-non-reasoning",
  "input": [{"role": "user", "content": "Search X and the web for the most important breaking news about: ${QUERY}. Only include news from the last ${HOURS_BACK} hours. For each story provide: headline, source, URL, approximate time published, and a virality score (1-10). Output as JSON array. If nothing breaking found, return empty array []."}],
  "tools": [
    {"type": "web_search"},
    {"type": "x_search", "from_date": "${TODAY}", "to_date": "${TODAY}"}
  ]
}
EOF
)"
