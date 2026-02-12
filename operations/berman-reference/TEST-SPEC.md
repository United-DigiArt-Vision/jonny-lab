# OpenClaw Power-User System — Test Specification

**Source:** Matthew Berman "OpenClaw is NUTS" (YouTube, Feb 2026)
**Version:** 1.0 — 2026-02-12

**Usage:** These tests are written generically. Replace `{{PLACEHOLDER}}` values with your specific configuration. Applicable to any OpenClaw system implementing comparable workflows.

---

## Table of Contents

1. [Infrastructure Tests (T-001 – T-012)](#infrastructure)
2. [CRM Tests (T-013 – T-020)](#crm)
3. [Knowledge Base Tests (T-021 – T-028)](#knowledge-base)
4. [Video Idea Pipeline Tests (T-029 – T-035)](#video-idea-pipeline)
5. [X/Twitter Research Tests (T-036 – T-043)](#xtwitter-research)
6. [YouTube Analytics Tests (T-044 – T-049)](#youtube-analytics)
7. [Business Meta-Analysis Tests (T-050 – T-058)](#business-meta-analysis)
8. [HubSpot Tests (T-059 – T-063)](#hubspot)
9. [Humanizer Tests (T-064 – T-070)](#humanizer)
10. [Image/Video Generation Tests (T-071 – T-075)](#imagevideo-generation)
11. [Task Management Tests (T-076 – T-082)](#task-management)
12. [Usage Tracker Tests (T-083 – T-088)](#usage-tracker)
13. [Automation Tests (T-089 – T-095)](#automations)
14. [Backup & Restore Tests (T-096 – T-101)](#backup--restore)
15. [Memory Tests (T-102 – T-108)](#memory)
16. [Cross-Workflow Integration Tests (T-109 – T-115)](#cross-workflow-integration)

---

## Infrastructure

| ID | What | Precondition | Steps | Expected Result | Priority |
|----|------|-------------|-------|-----------------|----------|
| T-001 | Host machine is always-on | Machine configured in clamshell/always-on mode | 1. Close lid. 2. Wait 5 min. 3. SSH into machine. | SSH connection succeeds; OpenClaw gateway responds. | Critical |
| T-002 | SSH access via Tailscale | Tailscale installed on both machines | 1. From remote machine, `ssh {{USER}}@{{TAILSCALE_HOST}}`. | Shell prompt appears within 5s. | Critical |
| T-003 | TeamViewer fallback | TeamViewer installed and running | 1. Connect via TeamViewer from remote device. | Desktop visible, mouse/keyboard functional. | Medium |
| T-004 | OpenClaw gateway running | Gateway installed | 1. `openclaw gateway status`. | Status: running. | Critical |
| T-005 | Gateway survives reboot | Machine reboots | 1. Reboot host. 2. Wait for boot. 3. `openclaw gateway status`. | Gateway auto-starts, status: running. | Critical |
| T-006 | Telegram interface responds | Telegram channel configured | 1. Send "ping" in primary Telegram topic. | OpenClaw responds within 30s. | Critical |
| T-007 | Telegram topics isolation | Multiple topics configured | 1. Send KB query in KB topic. 2. Send task in Task topic. | Each topic processes its domain; no cross-contamination. | High |
| T-008 | Slack interface responds | Slack configured with restricted channels | 1. Tag OpenClaw in allowed channel. | Response within 30s. | High |
| T-009 | Slack ignores unauthorized users | Slack restriction configured | 1. Have non-authorized user tag OpenClaw. | No response. | High |
| T-010 | Session persistence (1-year expiry) | Session expiry set to 1 year | 1. Send message in topic. 2. Wait 25+ hours. 3. Send follow-up referencing earlier message. | Context from prior message is retained. | High |
| T-011 | SQLite WAL mode enabled | Any database created | 1. `PRAGMA journal_mode;` on any DB. | Returns `wal`. | High |
| T-012 | SQLite foreign keys enabled | Any database with relations | 1. `PRAGMA foreign_keys;` on any DB. | Returns `1`. | High |

---

## CRM

| ID | What | Precondition | Steps | Expected Result | Priority |
|----|------|-------------|-------|-----------------|----------|
| T-013 | Daily email ingestion runs | Gmail API configured, cron active | 1. Check cron log after scheduled time. | Ingestion job completed successfully. | Critical |
| T-014 | Contacts extracted from emails | Emails in inbox | 1. Run ingestion. 2. Query CRM for known sender. | Contact record exists with correct name/email. | Critical |
| T-015 | Newsletter/spam filtered out | Emails from noreply@ in inbox | 1. Run ingestion. 2. Query CRM for noreply@ addresses. | No records for filtered addresses. | High |
| T-016 | LLM classification assigns roles | Contacts ingested | 1. Query contact record. | Role field populated (e.g., CEO, Engineer). | Medium |
| T-017 | Dedup: email match | Same sender emails twice | 1. Run ingestion twice. 2. Count records for that email. | Exactly 1 record (merged). | Critical |
| T-018 | Dedup: name+company match | Same person, different email | 1. Ingest email from "Jane Doe, Acme" via two addresses. | Single merged record or flagged for review. | High |
| T-019 | Contact scoring | Contact with multiple interactions | 1. Query contact score. | Score reflects formula (+5/exchange, +15 title, +25 multi-channel). | Medium |
| T-020 | Semantic search on contacts | Contacts with embeddings | 1. Query: "Who do I know at {{COMPANY}}?" | Returns relevant contacts with context. | High |

---

## Knowledge Base

| ID | What | Precondition | Steps | Expected Result | Priority |
|----|------|-------------|-------|-----------------|----------|
| T-021 | URL ingestion | KB topic in Telegram | 1. Drop a URL in KB topic. | Confirmation message with title/summary. | Critical |
| T-022 | Content quality validation | URL pointing to error page | 1. Drop URL returning 403/captcha page. | Rejection message: "Content quality too low." | High |
| T-023 | Dedup: same URL twice | Article already ingested | 1. Drop same URL again. | "Already stored" notification, no duplicate. | High |
| T-024 | Dedup: normalized URL | Same article, different URL params | 1. Drop `article?utm_source=x`. 2. Drop `article` (clean). | Single entry, second attempt detected as duplicate. | Medium |
| T-025 | Chunking correctness | Article ingested | 1. Query DB for chunks of known article. | Chunks ~800 chars, overlapping ~200, split at sentence boundaries. | Medium |
| T-026 | Embedding dimensions | Article ingested | 1. Check vector column dimensions. | 768 dimensions (gemini-embedding-001). | Medium |
| T-027 | Semantic search returns results | Multiple articles stored | 1. Ask "What articles do I have about {{TOPIC}}?" | Returns relevant articles with source citations. | Critical |
| T-028 | Slack auto-post on ingestion | Slack integration active | 1. Drop URL in Telegram KB topic. | Summary posted to Slack team channel. | Medium |

---

## Video Idea Pipeline

| ID | What | Precondition | Steps | Expected Result | Priority |
|----|------|-------------|-------|-----------------|----------|
| T-029 | Idea from Telegram triggers pipeline | Pipeline configured | 1. Drop link in Telegram with "make a video about this." | Pipeline runs, confirmation sent. | Critical |
| T-030 | Idea from Slack triggers pipeline | Slack integration active | 1. Tag OpenClaw in Slack: "video idea: {{TOPIC}}." | Pipeline runs, confirmation in Slack. | High |
| T-031 | Duplicate pitch rejected | Similar pitch already exists (>40%) | 1. Submit idea very similar to existing pitch. | Rejection: "Similar pitch exists: {{ID}}." | High |
| T-032 | Unique pitch accepted | No similar pitches | 1. Submit novel idea. | Pitch stored with status `pitched`. | Critical |
| T-033 | Asana task created | Asana integration active | 1. Submit idea, pipeline completes. | Asana task exists with hooks, outline, sources. | High |
| T-034 | KB context included | Related articles in KB | 1. Submit idea on topic with KB articles. | Pitch references relevant KB articles. | Medium |
| T-035 | Status tracking works | Pitch stored | 1. Update pitch status to `accepted`. 2. Query by status. | Correct status returned. | Medium |

---

## X/Twitter Research

| ID | What | Precondition | Steps | Expected Result | Priority |
|----|------|-------------|-------|-----------------|----------|
| T-036 | Tier 1 (FxTwitter) works | API accessible | 1. Request single tweet by ID. | Tweet data returned, cost = $0. | High |
| T-037 | Tier 2 fallback on Tier 1 failure | FxTwitter unavailable or search needed | 1. Request search query. | Falls to Tier 2 (TwitterAPI.io), results returned. | Critical |
| T-038 | Tier 3 fallback on Tier 2 failure | TwitterAPI.io down | 1. Mock Tier 2 failure. 2. Request search. | Falls to Tier 3 (X API v2). | High |
| T-039 | Tier 4 Grok fallback | All API tiers fail | 1. Mock Tiers 1-3 failure. 2. Request search. | Falls to Tier 4 (Grok x-search). | High |
| T-040 | Query decomposition | Complex research question | 1. Submit multi-faceted question. | Decomposes into 2-4 sub-queries (verify in logs). | Medium |
| T-041 | Dedup in results | Query returning overlapping results | 1. Run search. | No duplicate tweets in output. | Medium |
| T-042 | Engagement ranking | Results with varying engagement | 1. Run search. | Results ordered by engagement score (high to low). | Medium |
| T-043 | Synthesis output structure | Search completed | 1. Check output format. | Contains: key narratives, notable posts, sentiment, contrarian takes. | Medium |

---

## YouTube Analytics

| ID | What | Precondition | Steps | Expected Result | Priority |
|----|------|-------------|-------|-----------------|----------|
| T-044 | Daily collection runs | YouTube API configured, cron active | 1. Check cron log after scheduled time. | Collection job completed. | Critical |
| T-045 | Data persisted to SQLite | Collection ran | 1. Query analytics DB for today's date. | Snapshot row exists with metrics. | Critical |
| T-046 | Derived metrics computed | Multiple days of data | 1. Query for 7-day moving average. | MA values present and mathematically correct. | High |
| T-047 | Competitor data collected | Competitor channels configured | 1. Query competitor table. | Upload cadence and view data present. | Medium |
| T-048 | PNG charts generated | Sufficient data points | 1. Check chart output directory. | Dark-theme PNG files exist, recent timestamp. | Medium |
| T-049 | Data feeds into Council | Analytics ran before Council | 1. Check Council signal input for YouTube signals. | YouTube metrics present in signal set. | High |

---

## Business Meta-Analysis

| ID | What | Precondition | Steps | Expected Result | Priority |
|----|------|-------------|-------|-----------------|----------|
| T-050 | Council runs nightly | Cron configured | 1. Check cron log morning after. | Council job completed successfully. | Critical |
| T-051 | All 10 signal sources collected | All integrations active | 1. Check signal collection log. | Signals from all 10 sources present. | High |
| T-052 | Signal compaction to top 200 | >200 raw signals | 1. Check compacted signal set. | Exactly ≤200 signals, ordered by confidence. | High |
| T-053 | Phase 1 draft generated | Signals compacted | 1. Check council trace DB. | LeadAnalyst draft present. | High |
| T-054 | Phase 2 parallel reviews | Draft generated | 1. Check council trace. | 4 specialist reviews present. | High |
| T-055 | Phase 3 reconciliation | Reviews complete | 1. Check council trace. | Moderator reconciliation present. | High |
| T-056 | Priority scoring correct | Reconciliation done | 1. Verify score = impact×0.4 + confidence×0.35 + (100-effort)×0.25. | Scores match formula for sample items. | Medium |
| T-057 | Digest delivered to Telegram | Council complete | 1. Check Telegram Business Analysis topic. | Briefing message present with priorities. | Critical |
| T-058 | Audit trail persisted | Council complete | 1. Query council trace DB. | Full trace: draft + 4 reviews + consensus + scores. | High |

---

## HubSpot

| ID | What | Precondition | Steps | Expected Result | Priority |
|----|------|-------------|-------|-----------------|----------|
| T-059 | Lookup operation | Deals exist in HubSpot | 1. "Show me deal {{DEAL_NAME}}." | Deal details returned in human-readable format. | High |
| T-060 | List operation | Multiple deals | 1. "List all open deals." | All open deals listed. | High |
| T-061 | Create operation | HubSpot write access | 1. "Create a deal for {{COMPANY}}, ${{AMOUNT}}." | Deal created, confirmation returned. | Medium |
| T-062 | Validation: missing fields | Incomplete request | 1. "Create a deal" (no details). | System asks for required fields. | Medium |
| T-063 | Human-readable output | Any operation | 1. Run any HubSpot query. | No raw JSON in response. | Low |

---

## Humanizer

| ID | What | Precondition | Steps | Expected Result | Priority |
|----|------|-------------|-------|-----------------|----------|
| T-064 | Em-dash removal | Humanizer active | 1. Request text that would typically contain em-dashes. | No em-dashes (—) in output. | High |
| T-065 | "Delve" blocked | Humanizer active | 1. Request exploratory text. | Word "delve" does not appear. | High |
| T-066 | Varied sentence length | Generate 5+ sentence paragraph | 1. Measure sentence lengths. | Standard deviation of sentence length > 3 words. | Medium |
| T-067 | Contractions used | Generate conversational text | 1. Check for contractions. | At least 50% of eligible cases use contractions. | Medium |
| T-068 | No tone inflation | Generate description of mundane topic | 1. Check for "revolutionary", "game-changing", etc. | None of these words for mundane topics. | Medium |
| T-069 | Channel-specific: Twitter | Generate Twitter post | 1. Check length and style. | <280 chars, punchy, no filler. | High |
| T-070 | Channel-specific: Email | Generate email draft | 1. Check style. | Brief, clear, action-oriented. | Medium |

---

## Image/Video Generation

| ID | What | Precondition | Steps | Expected Result | Priority |
|----|------|-------------|-------|-----------------|----------|
| T-071 | Text-to-image works | Image gen API configured | 1. Request "Generate an image of {{DESCRIPTION}}." | Image returned in Telegram. | Critical |
| T-072 | Iterative editing | Image generated | 1. Request change: "Make background darker." | Modified image returned. | High |
| T-073 | Session context retained | Same Telegram topic | 1. Generate image. 2. Say "make it wider." | System remembers what "it" refers to. | Medium |
| T-074 | Video generation works | Video gen API configured | 1. Request video generation. | Video returned in Telegram. | High |
| T-075 | Multiple variants | Request image | 1. "Generate 3 variants." | 3 different images returned. | Medium |

---

## Task Management

| ID | What | Precondition | Steps | Expected Result | Priority |
|----|------|-------------|-------|-----------------|----------|
| T-076 | Meeting transcript → tasks | Fathom integration active | 1. After meeting, check task extraction. | Action items extracted with owners + deadlines. | Critical |
| T-077 | Owner distinction (is_owner) | Tasks extracted | 1. Check extracted tasks. | User tasks and attendee tasks clearly separated. | High |
| T-078 | CRM cross-reference | Contact exists in CRM | 1. Extract task mentioning known contact. | Task enriched with company/context from CRM. | High |
| T-079 | Approval flow | Tasks presented | 1. Review list. 2. Approve items 1, 3. Reject 2. | Only items 1, 3 created in Todoist. | Critical |
| T-080 | Edit before approval | Tasks presented | 1. Edit deadline on item 1. 2. Approve. | Todoist task has edited deadline. | Medium |
| T-081 | Manual task creation | Todoist integration active | 1. "Add task: follow up with {{NAME}} by Friday." | Task created in Todoist with correct deadline. | High |
| T-082 | Confirmation sent | Task created | 1. Create task. | Confirmation message in Telegram. | Medium |

---

## Usage Tracker

| ID | What | Precondition | Steps | Expected Result | Priority |
|----|------|-------------|-------|-----------------|----------|
| T-083 | API calls logged | Tracker active | 1. Make any API call. 2. Query usage DB. | Log entry with provider, model, tokens, cost. | Critical |
| T-084 | Cost breakdown query | Multiple logged calls | 1. "How much did I spend this week?" | Breakdown by provider and task type. | High |
| T-085 | 30-day trend | 30+ days of data | 1. "Show 30-day spending trend." | Trend chart or table returned. | Medium |
| T-086 | >25% spend warning | One workflow dominates | 1. Check for alerts. | Warning: "{{WORKFLOW}} consumes >25% of total spend." | Medium |
| T-087 | Routing suggestion | Expensive model for simple task | 1. Check optimization suggestions. | Suggestion to use cheaper model for flagged tasks. | Low |
| T-088 | Caching suggestion | Repeated identical queries | 1. Make same query 3x. 2. Check suggestions. | "Consider caching: {{QUERY}} called 3x." | Low |

---

## Automations

| ID | What | Precondition | Steps | Expected Result | Priority |
|----|------|-------------|-------|-----------------|----------|
| T-089 | Hourly code sync runs | Cron configured | 1. Check GitHub repo commits. | Commits at ~hourly intervals. | High |
| T-090 | Daily jobs complete | All daily crons active | 1. Check cron log for today. | All daily jobs: status = success. | Critical |
| T-091 | Weekly jobs complete | Weekly crons active | 1. Check cron log for past week. | Weekly jobs ran on schedule. | High |
| T-092 | Job failure → Telegram alert | Cron job fails | 1. Introduce controlled failure. 2. Check Telegram. | Failure notification in cron updates topic. | Critical |
| T-093 | Job success → Telegram notify | Cron job succeeds | 1. Check Telegram after scheduled job. | Success notification with summary. | High |
| T-094 | Log start/end pattern | Any cron job | 1. Query cron log for specific job. | Start entry + end entry with status + summary. | High |
| T-095 | Concurrent job protection | Two jobs scheduled close together | 1. Check lock-file behavior. | Second job waits or is queued (no corruption). | High |

---

## Backup & Restore

| ID | What | Precondition | Steps | Expected Result | Priority |
|----|------|-------------|-------|-----------------|----------|
| T-096 | Code pushed to GitHub | Hourly sync active | 1. Make code change. 2. Wait for sync. 3. Check GitHub. | Change present on GitHub. | Critical |
| T-097 | DB backup to Google Drive | Daily backup cron active | 1. Check Google Drive for today's backup. | Timestamped archive with manifest present. | Critical |
| T-098 | Backup manifest correct | Backup exists | 1. Download backup. 2. Check manifest. | All databases listed, checksums match. | High |
| T-099 | Old backups pruned | Retention policy active, old backups exist | 1. Check Google Drive. | Backups older than retention period removed. | Medium |
| T-100 | Full restore procedure | Backup available | 1. Follow restore doc. 2. Restore all DBs. 3. Verify. | CRM, KB, analytics, cron — all operational. | Critical |
| T-101 | Restore: gateway + jobs verify | Post-restore | 1. `openclaw gateway status`. 2. Trigger test cron. | Gateway running, cron executes successfully. | Critical |

---

## Memory

| ID | What | Precondition | Steps | Expected Result | Priority |
|----|------|-------------|-------|-----------------|----------|
| T-102 | Daily notes created | System active for a day | 1. Check daily notes file for today. | File exists with conversation summaries, tasks, learnings. | High |
| T-103 | Weekly synthesis runs | Week of daily notes | 1. Check long-term memory after weekly cron. | Updated with distilled patterns from the week. | High |
| T-104 | Learnings recorded | Mistake made and corrected | 1. Check `.learnings/` directory. | Corrective pattern documented. | High |
| T-105 | Learning prevents repeat | Known mistake scenario | 1. Trigger scenario matching a recorded learning. | System avoids the mistake (follows corrective pattern). | Medium |
| T-106 | Long-term memory persists | Preferences established | 1. Start new session. 2. Test known preference. | Preference respected from long-term memory. | Critical |
| T-107 | Session context within topic | Topic with history | 1. Reference something from 5 messages ago in same topic. | System recalls and responds correctly. | High |
| T-108 | Memory isolation between topics | Multiple topics | 1. Discuss topic A in topic A channel. 2. In topic B, ask about topic A details. | Topic B does not have topic A's session context. | Medium |

---

## Cross-Workflow Integration

| ID | What | Precondition | Steps | Expected Result | Priority |
|----|------|-------------|-------|-----------------|----------|
| T-109 | KB → Video Pipeline | Article in KB, pipeline active | 1. Submit video idea on topic covered by KB article. | Pipeline references the KB article in pitch. | High |
| T-110 | CRM → Meeting Prep | Contact in CRM, meeting scheduled | 1. Morning cron runs. | Prep brief includes CRM data for attendee. | High |
| T-111 | CRM → Task Extraction | Contact in CRM, meeting transcript available | 1. Extract tasks from meeting mentioning known contact. | Tasks enriched with CRM context (company, role). | High |
| T-112 | YouTube Analytics → Council | Analytics collected, council runs | 1. Check council signals. | YouTube metrics present as signals. | High |
| T-113 | X Research → Video Pipeline | Video idea triggers X search | 1. Submit video idea. 2. Check pitch sources. | X/Twitter discourse included in pitch. | Medium |
| T-114 | Cost Tracker captures Council cost | Council runs | 1. Query cost tracker for council workflow. | Council API costs logged with breakdown by phase. | Medium |
| T-115 | KB Ingest → Slack | Article ingested | 1. Ingest article via Telegram. 2. Check Slack channel. | Summary auto-posted to Slack. | Medium |
