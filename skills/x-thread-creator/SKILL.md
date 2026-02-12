---
name: x-thread-creator
description: >
  Create X/Twitter threads for breaking news and tech announcements on @DaBrusi.
  Use when: writing a Twitter/X thread, breaking news thread, tech announcement thread,
  or when user says "schreib einen Thread", "X thread", "tweet this", "post this on X".
  Don't use when: replying to a single tweet, writing a DM, or posting on other platforms.
  Output: Copy-paste-ready thread parts saved to x-threads/ folder.
---

# X Thread Creator

Write breaking news threads for @DaBrusi. Output = copy-paste-ready parts in `x-threads/`.

## Workflow

1. **DEDUPE CHECK FIRST!** Run before writing anything:
   ```bash
   python3 tools/thread-pipeline/pipeline.py --action check --title "YOUR TITLE" --tags "tag1,tag2"
   ```
   If score >0.4 → STOP, inform that a similar thread exists
2. Read the source material (article, announcement, video transcript)
3. Extract concrete numbers, benchmarks, dates, comparisons
4. Write 8-15 parts following the template below
5. Save to `x-threads/YYYY-MM-DD-topic.md`
6. Register in pipeline:
   ```bash
   python3 tools/thread-pipeline/pipeline.py --action register --file "x-threads/YYYY-MM-DD-topic.md" --title "TITLE" --tags "tags"
   ```
7. Deliver to Dino for review

## Template

See `references/thread-template.md` for the full format, numbering rules, and checklist.

## Rules

- **Language:** English
- **Account:** @DaBrusi (NEVER @JonnyDigiArt)
- **One topic per thread** — never mix announcements
- **Concrete numbers always** — %, scores, $, benchmarks WITH context
- **CTA in the middle** (after part 4-6), unnumbered
- **Every content part numbered** `X/Y` at the start
- **Threshold:** 8/10 quality minimum
- **Dino posts manually** — just deliver copy-paste-ready parts
- **Explain jargon** — readers are not all technical
