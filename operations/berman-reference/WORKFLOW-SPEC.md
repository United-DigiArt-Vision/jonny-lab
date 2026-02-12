# OpenClaw Power-User System — Workflow Specification

**Source:** Matthew Berman "OpenClaw is NUTS" (YouTube, Feb 2026)
**Version:** 1.0 — 2026-02-12

---

## Table of Contents

1. [Workflow Index](#1-workflow-index)
2. [Workflow Details](#2-workflow-details)
   - [WF-01 CRM Daily Ingestion](#wf-01-crm-daily-ingestion)
   - [WF-02 Meeting Prep](#wf-02-meeting-prep)
   - [WF-03 Knowledge Base Ingestion](#wf-03-knowledge-base-ingestion)
   - [WF-04 Knowledge Base Query](#wf-04-knowledge-base-query)
   - [WF-05 Video Idea Pipeline](#wf-05-video-idea-pipeline)
   - [WF-06 X/Twitter Tiered Research](#wf-06-xtwitter-tiered-research)
   - [WF-07 YouTube Analytics Collection](#wf-07-youtube-analytics-collection)
   - [WF-08 Business Meta-Analysis (Council)](#wf-08-business-meta-analysis-council)
   - [WF-09 HubSpot NL Operations](#wf-09-hubspot-nl-operations)
   - [WF-10 Content Humanization](#wf-10-content-humanization)
   - [WF-11 Image Generation](#wf-11-image-generation)
   - [WF-12 Video Generation](#wf-12-video-generation)
   - [WF-13 Task Extraction (Meetings)](#wf-13-task-extraction-meetings)
   - [WF-14 Task Management (Manual)](#wf-14-task-management-manual)
   - [WF-15 Usage & Cost Tracking](#wf-15-usage--cost-tracking)
   - [WF-16 Code Repo Sync](#wf-16-code-repo-sync)
   - [WF-17 Database Backup](#wf-17-database-backup)
   - [WF-18 Memory Weekly Synthesis](#wf-18-memory-weekly-synthesis)
   - [WF-19 Markdown Maintenance](#wf-19-markdown-maintenance)
   - [WF-20 Platform Health Checks](#wf-20-platform-health-checks)
3. [Workflow Interconnections](#3-workflow-interconnections)
4. [Scheduling Matrix](#4-scheduling-matrix)
5. [Cost Profile Summary](#5-cost-profile-summary)

---

## 1. Workflow Index

| ID | Name | Category | Trigger | Schedule |
|----|------|----------|---------|----------|
| WF-01 | CRM Daily Ingestion | Data | Cron | Daily |
| WF-02 | Meeting Prep | Intelligence | Cron | Daily (morning) |
| WF-03 | KB Ingestion | Data | Manual (Telegram) | On demand |
| WF-04 | KB Query | Intelligence | Manual (Telegram) | On demand |
| WF-05 | Video Idea Pipeline | Content | Manual (Telegram/Slack) | On demand |
| WF-06 | X/Twitter Research | Research | Called by other WFs | On demand |
| WF-07 | YouTube Analytics | Data | Cron | Daily |
| WF-08 | Business Meta-Analysis | Intelligence | Cron | Daily (night) |
| WF-09 | HubSpot NL Ops | CRM | Manual | On demand |
| WF-10 | Content Humanization | Quality | Always active | Continuous |
| WF-11 | Image Generation | Creative | Manual (Telegram) | On demand |
| WF-12 | Video Generation | Creative | Manual (Telegram) | On demand |
| WF-13 | Task Extraction (Meetings) | Productivity | Event (Fathom transcript) | On meeting end |
| WF-14 | Task Management (Manual) | Productivity | Manual | On demand |
| WF-15 | Usage & Cost Tracking | Operations | Passive + Manual query | Continuous |
| WF-16 | Code Repo Sync | Infrastructure | Cron | Hourly |
| WF-17 | Database Backup | Infrastructure | Cron | Daily |
| WF-18 | Memory Weekly Synthesis | Memory | Cron | Weekly |
| WF-19 | Markdown Maintenance | Quality | Cron | Daily |
| WF-20 | Platform Health Checks | Operations | Cron | Daily |

---

## 2. Workflow Details

### WF-01 CRM Daily Ingestion

**Category:** Data Collection
**Trigger:** Daily cron job
**Dependencies:** Google Workspace API (Gmail + Calendar)

**Steps:**
1. Download all new emails from Gmail via Google Workspace (`gog`)
2. Download today's calendar events
3. Extract people from email senders and calendar participants
4. **Stage 1 Filter (Hard Rules):** Remove noreply@, role-based inboxes, newsletters
5. **Stage 2 Filter (LLM):** Classify remaining contacts using Gemini 2.5 Flash — role, relevance, quality
6. Deduplicate: match by email, then by name+company combo
7. Merge into existing contact records
8. AI-classify role and context (Gemini 2.5 Flash)
9. Update interaction timeline and Last Touch timestamp
10. Compute contact score (+5/exchange, +15 CEO/Founder, +25 email+calendar)
11. Generate embeddings (gemini-embedding-001) for semantic indexing
12. Store/update in CRM SQLite database
13. Send summary of new/updated contacts to Telegram

**Input:** Gmail inbox, Google Calendar
**Processing:** 2-stage filter → dedup → classify → score → embed
**Output:** Updated CRM database, Telegram notification

**Error Handling:**
- Gmail API failure → retry with backoff
- Classification ambiguity → store with low confidence, flag for review
- Duplicate detection miss → periodic dedup sweep (weekly housekeeping)

**Cost Profile:**
- Gemini 2.5 Flash: ~$0.01-0.05/day (classification)
- gemini-embedding-001: free
- Google Workspace API: included in subscription

---

### WF-02 Meeting Prep

**Category:** Intelligence
**Trigger:** Daily cron (morning)
**Dependencies:** WF-01 (CRM data), Google Calendar

**Steps:**
1. Read today's calendar
2. Filter: remove events with no external attendees or internal-only meetings
3. For each qualifying meeting:
   a. Identify attendee(s)
   b. Query CRM for contact record
   c. Retrieve last conversation/interaction
   d. Pull meeting agenda/description
   e. Generate prep brief
4. Deliver all briefs to Telegram (Meeting Prep topic)

**Input:** Calendar events, CRM database
**Processing:** Filter → CRM lookup → brief generation
**Output:** Meeting prep briefs in Telegram

**Error Handling:** No CRM match → note "unknown contact, consider adding after meeting"

**Cost Profile:** Minimal (LLM generation only for brief text)

---

### WF-03 Knowledge Base Ingestion

**Category:** Data Collection
**Trigger:** Manual — user drops URL or file in Telegram KB topic
**Dependencies:** None (standalone)

**Steps:**
1. Receive URL or file in Telegram
2. Detect source type (article, PDF, tweet, video)
3. Extract content via fallback chain:
   a. Readability parser
   b. Firecrawl API
   c. Headless browser
   d. Raw HTTP
4. Validate content quality:
   - Min 20 chars
   - Min 15% lines >80 chars
   - No error page signals
5. Normalize text
6. Deduplicate: URL normalization + SHA-256 content hash
7. Chunk: 800 chars, 200 overlap, min 100 chars, sentence boundaries
8. Generate embeddings (gemini-embedding-001)
9. Store chunks + metadata in KB SQLite
10. Post summary to Slack team channel
11. Confirm to user in Telegram

**Input:** URL or file
**Processing:** Extract → validate → chunk → embed → store
**Output:** Stored KB entry, Slack notification, Telegram confirmation

**Error Handling:**
- All extraction methods fail → notify user, request manual paste
- Content too short → reject with reason
- Duplicate detected → notify, skip storage

**Cost Profile:**
- Firecrawl: ~$0.01/page (if fallback triggered)
- Embeddings: free
- LLM (summary): ~$0.01

---

### WF-04 Knowledge Base Query

**Category:** Intelligence
**Trigger:** Manual — user asks question in Telegram KB topic
**Dependencies:** WF-03 (stored KB data)

**Steps:**
1. Receive user question
2. Generate query embedding (gemini-embedding-001)
3. Cosine similarity search against KB chunks
4. Retrieve top-K candidate chunks
5. Feed candidates + question to LLM
6. Generate answer with source citations
7. Return to user

**Input:** Natural language question
**Processing:** Embed → search → LLM synthesis
**Output:** Answer with sources

**Error Handling:** No relevant results → "No matching articles found. Try different keywords or add more sources."

**Cost Profile:** Embeddings free + LLM answer generation

---

### WF-05 Video Idea Pipeline

**Category:** Content Creation
**Trigger:** Manual — Telegram link drop or Slack @mention
**Dependencies:** WF-03/04 (KB), WF-06 (X Research), Asana API

**Steps:**
1. Receive idea trigger (link or topic description)
2. Parse video topic/intent
3. **Parallel research:**
   a. Search X/Twitter via WF-06 (Tiered Research)
   b. Search web via Brave Search
   c. Query Knowledge Base for related articles
4. Generate video pitch(es)
5. Deduplicate against existing pitches:
   - 70% semantic similarity (embedding)
   - 30% keyword overlap (title 30%, summary 20%, tags 20%)
   - Threshold: >40% → reject as duplicate
6. Build hooks and outline
7. Link all source references
8. Create Asana task with full brief
9. Send confirmation to originating channel (Telegram or Slack)

**Input:** Topic/link
**Processing:** Research → pitch → dedup → outline → task creation
**Output:** Asana task, confirmation message

**Error Handling:**
- Duplicate detected → notify "Similar pitch already exists: [link]"
- X/Twitter research fails all tiers → proceed with web-only research
- Asana API down → store locally, retry later

**Cost Profile:**
- X/Twitter: $0-0.15 depending on tier
- Brave Search: per-query pricing
- LLM (Opus): ~$0.10-0.30 per pipeline run

---

### WF-06 X/Twitter Tiered Research

**Category:** Research
**Trigger:** Called by WF-05, WF-08, or ad-hoc queries
**Dependencies:** None (standalone service)

**Steps:**
1. Receive research question
2. Decompose into 2-4 focused sub-queries
3. For each sub-query, try tiers in order:
   - **Tier 1 — FxTwitter** (`api.fxtwitter.com`): free, single tweet lookup only
   - **Tier 2 — TwitterAPI.io** (`api.twitterapi.io`): $0.15/1k, search+profiles+threads
   - **Tier 3 — X API v2** (`api.x.com/2/`): $0.005/tweet, full API, 350ms rate limit
   - **Tier 4 — Grok x-search** (`api.x.ai/v1/responses`, model `grok-4-1-fast-reasoning`): fallback
4. Aggregate results across sub-queries
5. Filter: remove retweets, suppress low-quality
6. Deduplicate results
7. Expand threads for high-engagement tweets
8. Rank by engagement (likes + retweets + replies, weighted)
9. Synthesize output:
   - 3-5 key narratives
   - 5-10 notable posts
   - Sentiment summary
   - Contrarian takes

**Input:** Research question (text)
**Processing:** Decompose → tiered fetch → filter → rank → synthesize
**Output:** Structured research report

**Error Handling:** Each tier failure cascades to next. All tiers fail → return partial results with warning.

**Cost Profile:** $0 (FxTwitter only) to ~$1+ (if reaching X API v2 for large queries)

---

### WF-07 YouTube Analytics Collection

**Category:** Data Collection
**Trigger:** Daily cron
**Dependencies:** YouTube Data API v3

**Steps:**
1. Fetch own channel statistics via YouTube API
2. Fetch per-video metrics (views, likes, comments)
3. Snapshot all data to SQLite (timestamped)
4. Compute derived metrics (7-day MA, views-per-video trend)
5. Scan competitor channels: upload cadence, view momentum
6. Generate dark-theme PNG charts (matplotlib)
7. Store charts
8. Feed insights to WF-08 (Business Meta-Analysis)

**Input:** YouTube API data
**Processing:** Fetch → store → compute → chart → feed downstream
**Output:** SQLite snapshots, PNG charts, signals for WF-08

**Error Handling:** API quota exceeded → retry next hour. Partial data → store what's available.

**Cost Profile:** YouTube API: free tier usually sufficient

---

### WF-08 Business Meta-Analysis (Council)

**Category:** Intelligence
**Trigger:** Daily cron (night, during low-usage hours)
**Dependencies:** WF-01 (CRM), WF-07 (YouTube), WF-06 (X data), Fathom, HubSpot, Asana, Slack, Gmail, Cron Log

**Steps:**
1. **Signal Collection** from 10 sources:
   - YouTube Metrics (WF-07)
   - CRM Health (WF-01)
   - Cron Reliability (Cron Log DB)
   - Social Growth (X/Twitter)
   - Slack Activity
   - Email Themes (Gmail)
   - Asana Backlog
   - X/Twitter Trends (WF-06)
   - Fathom Meetings
   - HubSpot Pipeline
2. Normalize all signals to standard format: `{source, signal_name, value, confidence, direction, category}`
3. **Compact** to top 200 signals by confidence score
4. **Phase 1 — LeadAnalyst** (Opus 4.6): Generate initial draft analysis
5. **Phase 2 — Parallel Review** by 4 specialists:
   - GrowthStrategist
   - RevenueGuardian
   - SkepticalOperator
   - TeamDynamicsArchitect
6. **Phase 3 — CouncilModerator** (Opus 4.6): Reconcile disagreements, synthesize consensus
7. **Phase 4 — Priority Scoring:**
   ```
   Priority = (impact × 0.40) + (confidence × 0.35) + ((100 - effort) × 0.25)
   ```
8. Persist full council trace to database (draft + reviews + consensus + scores)
9. Deliver digest to Telegram (Business Analysis topic)

**Input:** 10 data sources
**Processing:** Collect → normalize → compact → 4-phase council → score → persist
**Output:** Prioritized business briefing, audit trail in DB

**Error Handling:**
- Source unavailable → proceed with available sources, note gaps
- Council disagreement unresolvable → Moderator flags as "contested" with both positions
- Hard constraint: never recommend "publish now"

**Cost Profile:** Highest cost workflow. Multiple Opus 4.6 calls. ~$1-5/run. Scheduled at night to avoid peak usage.

---

### WF-09 HubSpot NL Operations

**Category:** CRM
**Trigger:** Manual (natural language request)
**Dependencies:** HubSpot API

**Steps:**
1. Receive NL request (e.g., "Show me all open deals over $5k")
2. Classify intent: Lookup / Create / Update / List / Associate
3. Map to HubSpot endpoint + object type
4. Validate payload — check required fields, request missing ones
5. Execute HubSpot API call
6. Return normalized, human-readable summary

**Input:** Natural language request
**Processing:** Classify → map → validate → execute → format
**Output:** Human-readable result

**Error Handling:** Missing fields → ask user. API error → report with details.

**Cost Profile:** HubSpot API (subscription-based), minimal LLM cost for classification

---

### WF-10 Content Humanization

**Category:** Quality Assurance
**Trigger:** Always active on all text output
**Dependencies:** None

**Steps:**
1. Receive draft text
2. Scan for 7 AI-writing patterns (overuse words, tone inflation, generic phrasing, repetitive structures, excessive hedging, too-clean lists, identical paragraph lengths)
3. Mark problematic spans
4. Rewrite: apply contractions, vary sentence length, add rhythm, remove filler
5. If channel-specific output → apply channel tuning (X: punchy, LinkedIn: professional, Blog: longer, Email: brief)
6. Return humanized draft

**Input:** Any text output
**Processing:** Detect → mark → rewrite → tune
**Output:** Humanized text

**Error Handling:** N/A — always produces output

**Cost Profile:** Included in normal LLM generation (skill-level instruction)

---

### WF-11 Image Generation

**Category:** Creative
**Trigger:** Manual (Telegram Images topic)
**Dependencies:** Nano Banana API

**Steps:**
1. Receive description or existing image + edit instructions
2. Interpret subject, style, composition
3. Generate 1-3 image variants
4. Present to user
5. If not satisfied → receive change description → regenerate (loop)
6. Final asset → use for thumbnails, presentations, social media

**Input:** Text description or image + instructions
**Processing:** Interpret → generate → iterate
**Output:** Final image asset

**Cost Profile:** Nano Banana API per-generation pricing

---

### WF-12 Video Generation

**Category:** Creative
**Trigger:** Manual (Telegram Video topic)
**Dependencies:** VO API

**Steps:** Similar to WF-11 but for video content.

**Cost Profile:** VO API per-generation pricing

---

### WF-13 Task Extraction (Meetings)

**Category:** Productivity
**Trigger:** Meeting ends → Fathom transcript available
**Dependencies:** Fathom API, WF-01 (CRM), Todoist API

**Steps:**
1. Receive Fathom meeting transcript
2. Send to Gemini 2.5 Flash for extraction:
   - User's action items (with deadlines)
   - Attendee's action items
3. Cross-reference mentioned people against CRM (WF-01)
4. Enrich tasks with company/context info
5. Present numbered task list for review
6. User approves / edits (adjust priorities, dates, wording)
7. Create approved tasks in Todoist
8. Send confirmation

**Input:** Fathom transcript
**Processing:** Extract → CRM lookup → present → approve → create
**Output:** Todoist tasks, confirmation

**Error Handling:** CRM miss → create task without enrichment, flag for later. Todoist API down → queue locally.

**Cost Profile:** Gemini 2.5 Flash: ~$0.01/transcript. Todoist API: free.

---

### WF-14 Task Management (Manual)

**Category:** Productivity
**Trigger:** Manual ("Add task to follow up with X by Friday")
**Dependencies:** WF-01 (CRM), Todoist API

**Steps:**
1. Parse natural language task description
2. Extract: action, owner, deadline
3. Cross-reference people with CRM
4. Present for confirmation
5. Create in Todoist on approval

**Input:** Natural language task request
**Output:** Todoist task

---

### WF-15 Usage & Cost Tracking

**Category:** Operations
**Trigger:** Passive (every API call) + Manual queries
**Dependencies:** All other workflows (logging source)

**Steps (Passive):**
1. Intercept every AI/API call
2. Log: provider, model, token count, task type, cost, timestamp
3. Store in Usage SQLite database

**Steps (Query):**
1. Receive query ("How much this week?", "30-day trend")
2. Query usage database
3. Generate: cost breakdown, trends, routing suggestions
4. Return analysis

**Alerts:**
- >25% spend by single workflow → optimization candidate flag
- Frontier model used for simple task → routing suggestion
- Repeated identical queries → caching suggestion

**Cost Profile:** Zero additional cost (logging only)

---

### WF-16 Code Repo Sync

**Category:** Infrastructure
**Trigger:** Hourly cron
**Dependencies:** GitHub

**Steps:**
1. Git add all code + markdown changes
2. Commit with auto-generated message
3. Push to GitHub

**Cost Profile:** Free (GitHub)

---

### WF-17 Database Backup

**Category:** Infrastructure
**Trigger:** Daily cron
**Dependencies:** Google Drive API

**Steps:**
1. Package all databases (CRM, KB, Pitches, Analytics, Council, Cron Log, Usage)
2. Create timestamped archive with manifest
3. Upload to Google Drive
4. Apply retention policy (auto-prune old backups)

**Cost Profile:** Google Drive storage (subscription)

---

### WF-18 Memory Weekly Synthesis

**Category:** Memory
**Trigger:** Weekly cron
**Dependencies:** Daily notes files

**Steps:**
1. Read all daily notes from the past week
2. Distill patterns, preferences, recurring themes
3. Update long-term memory file
4. Update `.learnings/` directory with corrective patterns from mistakes

**Cost Profile:** LLM synthesis: ~$0.10-0.30

---

### WF-19 Markdown Maintenance

**Category:** Quality
**Trigger:** Daily cron
**Dependencies:** Local copies of OpenClaw best practices + Opus 4.6 prompting guide

**Steps:**
1. Load locally-stored OpenClaw best practices (downloaded from openclaw.com)
2. Load locally-stored Anthropic Opus 4.6 prompting guide
3. Cross-reference all workspace markdown files against both guides
4. Auto-update/clean files to align with best practices
5. Log changes

**Cost Profile:** LLM analysis of markdown files: ~$0.10-0.50

---

### WF-20 Platform Health Checks

**Category:** Operations
**Trigger:** Daily cron
**Dependencies:** All external service APIs

**Steps:**
1. Verify connectivity to all external services (Telegram, Slack, Google, Asana, Todoist, HubSpot, YouTube, X, Fathom, GitHub, Brave, Firecrawl)
2. Check API key validity
3. Verify database integrity
4. Report any issues to Telegram

---

## 3. Workflow Interconnections

```
                    ┌─────────────────────────────────┐
                    │    SIGNAL SOURCES (Data Layer)    │
                    └─────────┬───────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
   ┌─────────┐         ┌──────────┐          ┌──────────┐
   │ WF-01   │         │ WF-07    │          │ WF-06    │
   │ CRM     │         │ YouTube  │          │ X/Twitter│
   │ Ingest  │         │ Analytics│          │ Research │
   └────┬────┘         └────┬─────┘          └────┬─────┘
        │                   │                     │
        ├───────┐           │                     │
        ▼       ▼           ▼                     ▼
   ┌────────┐ ┌────────────────────────────────────────┐
   │ WF-02  │ │            WF-08                        │
   │Meeting │ │    Business Meta-Analysis (Council)     │
   │ Prep   │ │  ← also receives: Slack, Email, Asana, │
   └────────┘ │    Fathom, HubSpot, Cron Log            │
              └──────────────┬─────────────────────────┘
                             │
                             ▼
                      Telegram Digest
                      
   ┌─────────┐     ┌─────────┐     ┌─────────┐
   │ WF-03   │────▶│ WF-04   │     │ WF-05   │
   │ KB      │     │ KB      │◀────│ Video   │
   │ Ingest  │     │ Query   │     │ Pipeline│
   └────┬────┘     └─────────┘     └────┬────┘
        │                               │
        ▼                               ▼
   Slack Post                      Asana Task
   
   ┌─────────┐     ┌─────────┐
   │ WF-13   │────▶│ WF-14   │──▶ Todoist
   │ Meeting │     │ Manual  │
   │ Tasks   │     │ Tasks   │
   └────┬────┘     └─────────┘
        │
        ▼
   WF-01 (CRM cross-ref)
   
   ┌─────────┐     ┌─────────┐     ┌─────────┐
   │ WF-10   │     │ WF-15   │     │ WF-19   │
   │Humanizer│     │ Cost    │     │Markdown │
   │(global) │     │Tracker  │     │Maint.   │
   └─────────┘     └─────────┘     └─────────┘
   Applied to        Monitors        Maintains
   ALL outputs       ALL workflows   ALL markdown
```

### Key Data Flows

| From | To | Data |
|------|----|------|
| WF-01 CRM | WF-02 Meeting Prep | Contact records, interaction history |
| WF-01 CRM | WF-08 Council | CRM health signals |
| WF-01 CRM | WF-13/14 Tasks | Contact enrichment for mentioned people |
| WF-03 KB Ingest | WF-04 KB Query | Stored chunks + embeddings |
| WF-03 KB Ingest | WF-05 Video Pipeline | Relevant articles |
| WF-03 KB Ingest | Slack | Auto-posted summaries |
| WF-06 X Research | WF-05 Video Pipeline | Twitter discourse |
| WF-06 X Research | WF-08 Council | Social signals |
| WF-07 YouTube | WF-08 Council | Metrics signals |
| WF-08 Council | Telegram | Daily business briefing |
| WF-13 Tasks | Todoist | Approved action items |
| WF-15 Cost Tracker | All WFs | Logging every API call |
| WF-16 Repo Sync | GitHub | Code + markdown |
| WF-17 DB Backup | Google Drive | All databases |

---

## 4. Scheduling Matrix

| Time | Workflows |
|------|-----------|
| **Every hour** | WF-16 Code Repo Sync |
| **Every hour** | CRM change check, signal scouting |
| **Daily (morning)** | WF-02 Meeting Prep |
| **Daily** | WF-01 CRM Ingestion |
| **Daily** | WF-07 YouTube Analytics |
| **Daily** | WF-17 Database Backup |
| **Daily** | WF-19 Markdown Maintenance |
| **Daily** | WF-20 Platform Health Checks |
| **Daily (night)** | WF-08 Business Meta-Analysis |
| **Weekly** | WF-18 Memory Synthesis |
| **Weekly** | Housekeeping (cleanup, pruning, audits) |
| **Continuous** | WF-10 Humanizer (on every output) |
| **Continuous** | WF-15 Cost Tracker (on every API call) |
| **On demand** | WF-03/04 KB, WF-05 Video, WF-06 X Research, WF-09 HubSpot, WF-11/12 Image/Video, WF-13/14 Tasks |

---

## 5. Cost Profile Summary

| Workflow | Primary Cost Driver | Estimated Cost |
|----------|-------------------|----------------|
| WF-01 CRM | Gemini Flash classification | ~$0.01-0.05/day |
| WF-02 Meeting Prep | LLM brief generation | ~$0.01-0.05/day |
| WF-03 KB Ingest | Firecrawl (fallback), LLM summary | ~$0.01/article |
| WF-05 Video Pipeline | Opus + X Research | ~$0.10-0.50/run |
| WF-06 X Research | Tiered: $0 to ~$1+ per query | Variable |
| WF-07 YouTube | YouTube API (free tier) | ~$0 |
| WF-08 Council | Multiple Opus 4.6 calls | ~$1-5/run |
| WF-09 HubSpot | LLM classification | ~$0.01/query |
| WF-11 Image Gen | Nano Banana API | Per-generation |
| WF-12 Video Gen | VO API | Per-generation |
| WF-13 Task Extract | Gemini Flash | ~$0.01/transcript |
| WF-19 Markdown Maint | LLM analysis | ~$0.10-0.50/day |
| **Total** | | **~$150/month** |

The Business Meta-Analysis (WF-08) is deliberately scheduled at night to use Opus 4.6 capacity during off-peak hours.
