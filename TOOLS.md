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

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
