# HEARTBEAT.md – Proaktive Aufgaben

**Letzte Aktualisierung:** 2026-02-07

> 📚 **Alle Regeln & Vereinbarungen:** siehe `MEMORY.md`  
> Diese Datei hier ist NUR die Aktions-Checkliste.

---

## ⭐ LEITFRAGE (bei JEDEM Heartbeat!)

> **"Based on everything you know about me, my business, and my goals — what are all the ways you could proactively help me? Don't wait for me to ask."**

**Ziel:** Dino wacht auf und denkt "wow, du hast viel geschafft."

### Session-Kontext nutzen (Steinberger-Prinzip)
> Der Heartbeat ist am wertvollsten wenn er auf den aktuellen Kontext aufbaut.
> - Was wurde zuletzt besprochen? → Follow-up darauf
> - Gibt es offene Fragen/Tasks? → Weiterarbeiten
> - Hat sich seit dem letzten Gespräch etwas geändert? → Proaktiv melden
> - Nicht nur Routine-Checks, sondern echte Weiterarbeit an laufenden Projekten

---

## 🔴 KRITISCH — JEDER HEARTBEAT

### 1. Kommunikation checken
| Was | Wie | Bei Fund |
|-----|-----|----------|
| Reddit Inbox | browser → reddit.com/message/inbox | → Dino DM |
| Reddit Chat | browser → reddit.com/chat | → Dino DM |
| Email | `himalaya envelope list -n 10` | → Dino DM wenn wichtig |

### 1.5 🐉 Mission Control aktualisieren
**Bei JEDEM Heartbeat:** `mission-control/data.json` updaten mit:
- Dragon-Status (wer fliegt/ruht/kämpft)
- Aktive Raids + neue Proposals
- Kriegskasse (Connects, Einnahmen)
- Neue Chronik-Einträge
```bash
# Datei: mission-control/data.json
# Einfach die JSON-Werte aktualisieren, Dashboard liest automatisch
```

### 2. Aktive Opportunities tracken

**⚡ Leads jetzt in SQLite!** Statt Markdown-Tabellen:
```bash
./tools/lead-tracker/tracker.sh --action list
./tools/lead-tracker/tracker.sh --action stats
```
Neue Leads hinzufügen:
```bash
./tools/lead-tracker/tracker.sh --action add --source upwork --title "Job Title" --price "$500" --url "https://..."
```

**GitHub PRs:**
| PR | Repo | Status |
|----|------|--------|
| #3598 | adenhq/hive | ❌ Closed (warte auf Zuweisung) |

---

## 🟡 TÄGLICH — Mindestens 1x pro Tag

### 3. NEUE Jobs suchen (PROAKTIV!)

**Reddit scannen:**
```
r/forhire (sort: new) → [Hiring] Posts
r/hiring (sort: new)
r/freelance_forhire (sort: new)
r/remotejs, r/remotepython
```

**Bei passendem Job:**
1. Kommentar hinterlassen (kurz, professionell)
2. DM senden mit Details
3. In Tabelle oben eintragen
4. → Dino informieren

**Andere Plattformen (TODO - Profile anlegen):**
- [ ] Upwork
- [ ] Toptal
- [ ] Fiverr (für kleine Gigs)
- [ ] LinkedIn Jobs

### 4. Upwork Favoriten reviewen (NEU 2026-02-08)

**Regelmäßig prüfen:**
- Dino's gespeicherte Favoriten auf Upwork durchgehen
- Feedback geben: Passt der Job zu uns? Aufwand? Preis fair?
- Eigene Job-Suche: Neue passende Jobs finden
- Bei gutem Match: Demo-Idee + Pitch vorbereiten

**Zugang:** Chrome Extension Browser Relay (Dino's eingeloggter Chrome)

### 5. City Apps vorantreiben

**Aktuelle Prio:** VG Gosberg (Pinzberg, Kunreuth, Wiesenthau)

| Aufgabe | Status |
|---------|--------|
| Gemeinden-Liste Bayern < 20k Einwohner | ⏳ TODO |
| Kontaktdaten sammeln (Email, Tel) | ⏳ TODO |
| Demo-App Prototyp bauen | ⏳ TODO |
| Pitch-Deck vorbereiten | ⏳ TODO |
| Anschreiben-Template | ⏳ TODO |

**Recherche:**
- Welche Gemeinden haben KEINE App?
- Welche nutzen Heimat-Info? (= Upgrade-Potenzial)
- Fördermittel-Programme finden

### 5. AI/Tech News — Viral Content

**X/Twitter scannen (Bird CLI, @DaBrusi Account):**
```bash
bird search "AI OR artificial intelligence OR GPT OR LLM OR robotics OR quantum computing breaking" --plain --no-emoji --chrome-profile-dir "/Users/macmini001/.openclaw/browser/openclaw/user-data/Default"
```
- ⚠️ NUR LESEN! Kein tweet, reply, follow, unfollow!
- Max 2-3x pro Tag, nicht jede Stunde
- Suche BREIT: AI, Innovation, Technologie, Startups, Robotik, Quantum

**Weitere Quellen:**
- OpenAI Blog/Twitter
- Anthropic News
- Google DeepMind
- YouTube: @OpenAI, @AnthropicAI, @GoogleDeepMind

**Bei Breaking News:**
1. `summarize "URL" --transcript`
2. Thread schreiben (10-15 Teile, EN, Format beachten!)
3. In `x-threads/` speichern
4. → Dino zum Review schicken
5. Posten auf @DaBrusi

**X Account Status:**
- @DaBrusi → ✅ Aktiv (Dino's Account)
- @JonnyDigiArt → ❌ Gesperrt (Appeal läuft)

---

## 🔵 NACH JEDER INTERAKTION — Lernen & Wachsen

### 5.5 Was habe ich gelernt? (IMMER FRAGEN!)

**Über Dino:**
- Neue Präferenz? Neue Arbeitsweise? → MEMORY.md

**Über mich selbst:**
- Was habe ich gut gemacht? Was schlecht?
- Wie kann ich effizienter werden?
- Welche Fehler nicht wiederholen?

**Über das Business:**
- Neue Markt-Erkenntnisse?
- Was funktioniert? Was nicht?
- Neue Chancen entdeckt?

**Über die Welt:**
- Neue Tools/Technologien?
- Trends die relevant sind?
- Best Practices gelernt?

**→ Alles Relevante in MEMORY.md dokumentieren!**

**Ziel:** Jeden Tag besser, effizienter, hilfreicher werden. Mehr Geld verdienen. Erfolgreicher sein.

---

## 🟢 WÖCHENTLICH

### 6. Sales-Vorbereitung

- [ ] Konkurrenz-Analyse updaten (Preise, Features)
- [ ] Case Studies / Testimonials sammeln
- [ ] Demo-Material aktualisieren
- [ ] Neue Einnahmequellen brainstormen

### 7. Tools & Automation

- [ ] Was mache ich wiederholt? → Automatisieren
- [ ] Welche Tools würden Zeit sparen? → Bauen
- [ ] Dokumentation aktuell? → Updaten

### 8. Memory Maintenance

- [ ] `memory/YYYY-MM-DD.md` Dateien reviewen
- [ ] Wichtiges nach MEMORY.md übertragen
- [ ] Veraltetes aus MEMORY.md entfernen

---

## 📋 AKTIVE PROJEKTE

| Prio | ID | Projekt | Fokus |
|------|----|---------|-------|
| 🔥 | 0003 | City Apps | Erster Kunde! Demo + Outreach |
| ⏸️ | 0002 | Revenue Machine | Pause |
| ⏸️ | 0001 | DenkWende | Geparkt |

**OBERSTES ZIEL:** So schnell wie möglich Geld verdienen!

---

## 📊 TAGES-LOG

*Was habe ich heute gemacht? (für Dino's Überblick)*

**2026-02-07:**
- [ ] Reddit gescannt
- [ ] X neue Jobs gefunden / beworben
- [ ] City Apps: ...
- [ ] Content: ...
- [ ] Sonstiges: ...

---

## 🧠 AUTOMATISIERUNGEN

| Was | Wann | Model | Status |
|-----|------|-------|--------|
| Nightly Dragon Council | 02:00 | Opus | ✅ Cron (mit Priority Score Formel) |
| Daily Markdown Cross-Reference | 03:00 | Sonnet | ✅ Cron (NEU!) |
| Daily Learning Sweep | 07:30 | Opus | ✅ Cron |
| Security Audit | 08:00 | Opus | ✅ Cron |
| Platform Health Check | 08:30 | Sonnet | ✅ Cron (NEU!) |
| Meleys News Patrol | 09,13,18,22 | Opus | ✅ Cron (4x/Tag) |
| Reddit Job Scanner | 10,16 | Opus | ✅ Cron (2x/Tag) |
| GitHub Opportunities | Mo+Do 09:00 | Opus | ✅ Cron |
| Weekly Skills Discovery | Mo 10:00 | Opus | ✅ Cron |
| Weekly AI Review | So 20:00 | Opus | ✅ Cron |
| Hourly Git Sync | Jede Stunde | Sonnet | ✅ Cron (NEU!) |
| Blogwatcher | 25 Feeds | — | ✅ Aktiv |

**Neue Crons (12.02.2026):** Hourly Git Sync, Platform Health Check, Markdown Cross-Reference
**Security-Quellen im Blogwatcher:** OpenClaw-Releases, Cisco-AI-Security, CrowdStrike-Blog

---

## 💡 IDEEN-BACKLOG

*Ideen für später:*

- Dashboard für Opportunity-Tracking
- Auto-Scraper für Job-Boards
- City Apps: Interaktive Demo-Seite
- (wird gefüllt)

---

## 📝 REGELN

1. **Proaktiv handeln** – nicht warten bis Dino fragt
2. **Jeden Tag Fortschritt** – immer etwas voranbringen
3. **Kommunikation nie verpassen** – Reddit/Email IMMER checken
4. **Bei Antworten SOFORT melden** – Zeit ist Geld
5. **Dokumentieren** – Tages-Log führen
6. **Nichts live pushen** – Dino reviewt alles

---

## ⚠️ BEI PROBLEMEN

- OpenAI Quota erschöpft → Dino sofort informieren
- Tool funktioniert nicht → Workaround finden, dokumentieren
- Unsicher ob handeln → Im Zweifel handeln, Dino informieren
