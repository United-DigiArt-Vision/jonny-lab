# Upwork Proposals — 14.02.2026

## 1. 🥇 Autotrader.co.uk Scraper ($10 Fixed)

**Job:** Python/selenium/playwright/puppeteer Scraper
**Client:** UK, Payment verified, 5.0 Rating, $400+ spent
**URL:** /jobs/Python-selenium-playwright-puppeteer-Scraper_~022022537512707034894/

---

**PROPOSAL:**

Hi — this is a straightforward Playwright job. I've built similar automotive scrapers before and can have this done within 24 hours.

**My approach:**
- Playwright (Python) with headless Chromium — handles the dynamic "below market average" badge that only loads after clicking into each listing
- Pagination → click each car → extract pricing badge + details → aggregate into JSON/CSV
- Polite scraping built in: 2-5s random delays, rotating user-agents, retry logic for failed requests

**Deliverable:**
- Clean Python script (Playwright)
- CSV/JSON output with: make, model, year, price, market comparison, mileage, dealer, URL
- Runs locally, easy to re-run for weekly fresh scans
- README with setup instructions (pip install, one command to run)

**Tech stack:** Python 3.12, Playwright, pandas for data export

Happy to do a quick test run on 1-2 pages before full delivery so you can validate the output format.

I also saw the mention of follow-on app automation work — very much in my wheelhouse (Playwright + API integration is what I do daily).

Can deliver within 24h of starting.

---

## 2. 🥈 HLTV CS:GO Data Scrape ($30 Fixed)

**Job:** Scrap all the Games data from HLTV
**Client:** India, Payment verified, 5.0 Rating, $400+ spent
**URL:** /jobs/Scrap-all-the-Games-data-from-HLTV_~022022481617481710174/

---

**PROPOSAL:**

Hey — CS player here (well, viewer these days), so I know the HLTV data structure well. This is a clean scraping job and I'd enjoy doing it.

**What I'll scrape:**
- **Players:** name, team, country, rating 2.0, maps played, K/D, headshot %
- **Teams:** name, ranking, country, roster, world ranking history
- **Matches:** date, event, team1 vs team2, map scores, map picks/bans
- **Events:** name, dates, prize pool, location, participating teams

**Storage approach (my recommendation):**
- SQLite database with normalized tables (players, teams, matches, events, maps)
- Relationships: player ↔ team (with date ranges for roster changes), match ↔ event, match ↔ maps
- Also export to CSV/JSON for quick analysis
- This structure lets you easily query things like "all matches where s1mple played on Inferno"

**Tech:** Python + BeautifulSoup/Playwright (HLTV uses Cloudflare, so Playwright with stealth for some pages), pandas, SQLite

**Why this structure matters for phase 2:** If you're building analytics/predictions on top, normalized SQL is the right foundation — much easier to query than flat files.

Estimated delivery: 3-4 days (HLTV has a lot of historical data, want to be thorough + respectful with request rates).

---

## 3. 🥉 University Course Scraper ($75 Fixed)

**Job:** Scrape information from a website (Indiana University courses)
**Client:** US, Payment verified, 5.0 Rating, $4K+ spent
**URL:** /jobs/Scrape-information-from-website_~022022303825344837087/

---

**PROPOSAL:**

Hi — I took a look at the IU course search portal (sisjee.iu.edu). It's a JavaScript-rendered SPA, so standard HTTP requests won't work — this needs browser automation.

**My approach:**
1. **Playwright** (Python) to load the search page and interact with the dynamic form
2. Iterate through all semesters available in the dropdown
3. For each semester: paginate through all courses, extracting:
   - Semester (e.g., "Fall 2025")
   - Course code (e.g., "CHEM-A 315")
   - Course title
   - Class number
   - Instructor name
   - Enrolled students (from the "X of Y seats" display)
   - Credit hours
4. Export to clean CSV with proper column headers

**Technical details:**
- The "open seats" field shows "X of Y" — I'll capture the denominator (total enrolled) as requested
- Handles pagination automatically (no manual semester selection needed)
- Respectful rate limiting (1-2s between page loads)
- Error handling + retry logic for timeouts
- Deduplication check

**Deliverable:**
- Python script (well-commented, easy to re-run)
- CSV file with all courses across all available semesters
- README with setup + usage instructions

**Timeline:** 48 hours from start. I'll send a sample of the first 50 rows within a few hours so you can verify the format before I run the full scrape.

---

## 4. 🎖️ BONUS: AI-Assisted Developer ($15/hr, ongoing)

**Job:** AI-Assisted Developer — Scripts, Scrapers & Automation (Part-Time)
**Client:** Singapore, Payment verified, 4.9 Rating, $10K+ spent
**URL:** /jobs/Assisted-Developer-Scripts-Scrapers-Automation-Part-Time_~022022337711276816592/

---

**PROPOSAL:**

Hi — this role describes exactly what I do every day. I build and maintain automation scripts, scrapers, API integrations, and scheduled jobs — all with AI tools as part of my workflow.

**My daily toolkit:**
- **Scraping:** Playwright, Puppeteer, BeautifulSoup, Scrapy — pick the right tool for the job (headless browser for JS-heavy sites, lightweight HTTP for static)
- **APIs:** REST/GraphQL integration, OAuth flows, webhook handling, rate limit management
- **Automation:** Cron jobs, Docker containers, CI/CD pipelines, monitoring/alerting
- **AI-assisted development:** I use Claude and GPT daily for code generation, debugging, and architecture decisions — not as a crutch, but as a multiplier. I understand what the AI generates and can debug/optimize it.
- **Languages:** Python (primary), JavaScript/Node.js, Bash

**What makes me a good fit:**
- I genuinely enjoy small, independent automation tasks — it's what I do for my own projects too
- Strong foundational understanding of HTTP, networking, Docker, databases (Postgres, SQLite, MongoDB), cron
- I ship fast but maintainable — proper error handling, logging, documentation
- Timezone: CET (Europe), but flexible and async-friendly

**Recent examples:**
- Built a multi-source news aggregation pipeline (25+ RSS feeds, web scraping, API calls, SQLite storage, automated analysis)
- Automated data extraction from dynamic web apps using Playwright with retry logic and proxy rotation
- Created CLI tools for SaaS products that lacked API access

Happy to start with a small test task to demonstrate my speed and quality.

---
