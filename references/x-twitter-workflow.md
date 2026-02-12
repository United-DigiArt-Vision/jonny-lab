# X/Twitter Thread & Reply-Jack Workflow

## Thread schreiben
1. Say: "Ich lese jetzt das Template..."
2. Read `projects/0002_revenue-machine/x-thread-template.md`
3. Follow checklist
4. Save content in `x-threads/` before posting

## After each thread
1. What went well? What was difficult?
2. New learnings → MEMORY.md
3. Improve template if needed

## Reply-Jack rules
1. Write substance — own opinion, analysis, context
2. Every reply must contain the current thread link
3. Before sending: is `https://x.com/DaBrusi/status/...` in the text?
4. Build in naturally — short human comment + opinion, then link directly after (same or next line, no blank line)
5. This triggers X preview cards → better optics + click rate

Bad: "Full breakdown here: [link]" (smells like ads)
Good: "When the person building safety guardrails walks away... that's the real story. [link]"

## Preflight
Before every thread, write preflight log entry:
```json
{ "date": "...", "manual": "x-threads.md", "action": "...", "confirmed": true }
```
→ File: `operations/preflight-log.json`
