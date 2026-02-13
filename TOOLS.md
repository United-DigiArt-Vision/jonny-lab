# TOOLS.md - Local Notes

Skills define *how* tools work. This file is for *your* specifics — the stuff that's unique to your setup.

## Accounts & Zugänge 🔑

> **📍 ZENTRALE DATENBANK:** `secrets/accounts.json`
> 
> Alle Accounts mit Usernames, Passwörtern und Details sind dort strukturiert gespeichert.
> Bei neuen Accounts → sofort dort eintragen!

## Backup System 💾

| Was | Details |
|-----|---------|
| Brain Backup | Täglich 04:00, ~20KB |
| Script | `~/jonny-lab/tools/backup/brain-backup.sh` |
| LaunchAgent | `ai.jonny.brain-backup` |
| Ziel (aktuell) | `~/JonnyBackups/` |
| Ziel (TODO) | Cloud Drive (Dino richtet ein) |

**Manuelles Backup:** `~/jonny-lab/tools/backup/brain-backup.sh`
**Restore:** Backup entpacken → `./restore.sh`

## Projekt-Workflow 🗂️

**Bei neuen Projekten IMMER:**
1. Ordner anlegen in `projects/` mit Format: `XXXX_projektname` (z.B. `0001_nano-banana-pro`)
2. Nächste freie ID aus `projects/README.md` nehmen und dort hochzählen
3. README.md + NOTES.md erstellen (siehe `projects/README.md` für Template)
4. Während der Arbeit: NOTES.md kontinuierlich pflegen
5. Bei Kontext-Verlust: Projekt-Ordner lesen → sofort wieder im Bilde

## GitHub & Development 🐙

### Setup Status
| Komponente | Status | Details |
|------------|--------|---------|
| `git` | ✅ Aktiv | Basis-Versionskontrolle |
| `gh` CLI | ✅ Aktiv | GitHub CLI für erweiterte Features |
| Account | `digit500` | Authentifiziert via Keyring |
| Scopes | Vollständig | `repo`, `workflow`, `gist`, `read:org` |

### Basis-Befehle (git)
```bash
git clone/commit/push/pull    # Standard-Workflow
git status / git log          # Status prüfen
```

### Erweiterte Befehle (gh CLI)
```bash
# Issues & PRs
gh issue list --repo owner/repo
gh issue create --title "Bug" --body "Description"
gh pr create --title "Feature" --body "Description"
gh pr checks 55 --repo owner/repo          # CI Status

# CI/Actions
gh run list --repo owner/repo --limit 10   # Workflow runs
gh run view <run-id> --log-failed          # Fehler-Logs

# Gists (Code-Snippets teilen = Marketing!)
gh gist create script.py --public --desc "Useful tool"
gh gist list

# Search (für Promotion & Research)
gh search repos "ai automation" --sort stars
gh search issues "help wanted" --state open
gh search issues "good first issue" label:"help wanted"

# API (für alles andere)
gh api repos/owner/repo --jq '.stargazers_count'
gh api search/users?q=ai+automation --jq '.items[].login'
```

### Promotion-Strategie
1. **Offene Issues finden** → Helfen → Sichtbarkeit
2. **Gists erstellen** → Nützliche Snippets → Traffic
3. **Trending Repos** → Relevante Projekte finden → Networking
4. **Good First Issues** → In Open Source beitragen → Credibility

### Unsere Repos
| Repo | Zweck | URL |
|------|-------|-----|
| `jonny-lab` | Workspace - Apps, Tools, Experiments | https://github.com/digit500/jonny-lab |

---

## ⚠️ Browser-Regeln (IMMER beachten!)

| Aktion | Danach SOFORT |
|--------|---------------|
| YouTube Transkript geholt | → Tab schließen! (Auto-Play läuft sonst weiter) |

---

## What Goes Here

Things like:
- Camera names and locations
- SSH hosts and aliases  
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras
- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH
- home-server → 192.168.1.100, user: admin

### TTS
- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## 🐦 X/Twitter Tweets lesen — Fallback-Kette (PFLICHT!)

**Bei JEDEM X/Twitter-Link diese Stufen durchgehen bis einer funktioniert. NICHT bei Dino eskalieren bevor ALLE Stufen durch sind!**

| Stufe | Methode | Wie | Liest Artikel? |
|-------|---------|-----|----------------|
| 1 | **fxtwitter API** | `web_fetch https://api.fxtwitter.com/{user}/status/{id}` | ✅ Ja (article.content.blocks) |
| 2 | **Syndication API** | `web_fetch https://cdn.syndication.twimg.com/tweet-result?id={id}&token=0` | ✅ Teilweise |
| 3 | **vxtwitter** | `web_fetch https://vxtwitter.com/{user}/status/{id}` | ⚠️ Nur Kurztext |
| 4 | **Nitter Instanzen** | `web_fetch https://nitter.net/{user}/status/{id}` (oder andere Instanzen: nitter.privacydev.net, nitter.poast.org) | ✅ Ja |
| 5 | **Brave Search** | `web_search` mit Tweet-ID oder Zitat aus dem Tweet | ⚠️ Nur Snippet |
| 6 | **Browser Relay** | `browser` → x.com direkt öffnen (Dino's Chrome, eingeloggt) | ✅ Ja |
| 7 | **Grok auf x.com** | Browser → grok.x.ai → Tweet-Link eingeben | ✅ Ja |

**Parsing-Hinweise:**
- fxtwitter: Normaler Tweet → `tweet.text`. X Article (Langform) → `tweet.article.content.blocks[].text`
- Tweet-ID aus URL extrahieren: `https://x.com/{user}/status/{ID}` → ID = Zahl am Ende
- Bei Articles: Blöcke zu Text zusammenbauen mit `\n\n` dazwischen

**REGEL:** Stufe 1 funktioniert fast immer. Erst wenn ALLE 7 Stufen fehlschlagen → Dino fragen.

---

## 🎬 YouTube Transkripte lesen — Fallback-Kette (PFLICHT!)

**Bei JEDEM YouTube-Video diese Stufen durchgehen bis einer funktioniert. NICHT bei Dino eskalieren bevor ALLE Stufen durch sind!**

**Video-ID extrahieren:** `https://www.youtube.com/watch?v={ID}` oder `https://youtu.be/{ID}`

| Stufe | Methode | Wie | Hinweise |
|-------|---------|-----|----------|
| 1 | **summarize --extract** | `summarize "URL" --extract --plain` | Sauberster Output, kein LLM nötig, nutzt YouTube Web-Scraping |
| 2 | **yt-dlp mit OpenClaw-Cookies** | `yt-dlp --cookies-from-browser "chrome:/Users/macmini001/.openclaw/browser/openclaw/user-data/Default" --write-auto-sub --sub-lang en --sub-format json3 --skip-download -o "/tmp/yt-{ID}" "URL"` dann JSON parsen | ⭐ ZUVERLÄSSIGSTE Methode! Umgeht Bot-Detection, auch Auto-Captions |
| 3 | **summarize mit yt-dlp** | `summarize "URL" --extract --youtube yt-dlp --plain` | Erzwingt yt-dlp als Backend |
| 4 | **web_fetch auf Transkript-Services** | `web_fetch https://youtubetranscript.com?v={ID}` | Drittanbieter, nicht immer verfügbar |
| 5 | **Browser Relay** | `browser` → YouTube öffnen → "...mehr" → "Transkript anzeigen" → kopieren → **Tab SOFORT schließen!** | Letzter Ausweg, Dino's Chrome eingeloggt |

**Parsing yt-dlp json3:**
```python
import json
with open('/tmp/yt-{ID}.en.json3') as f:
    data = json.load(f)
text = []
for e in data.get('events', []):
    for s in e.get('segs', []):
        t = s.get('utf8', '').strip()
        if t and t != '\n': text.append(t)
print(' '.join(text))
```

**Sprachen:** `--sub-lang de` für Deutsch, `en` für Englisch. Bei `summarize`: automatische Erkennung.

**REGEL:** Stufe 1 funktioniert in 90% der Fälle. Erst wenn ALLE 5 Stufen fehlschlagen → Dino fragen.
**WICHTIG:** Nach Browser-Methode Tab SOFORT schließen (Auto-Play!)

---

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
