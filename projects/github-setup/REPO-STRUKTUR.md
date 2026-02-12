# GitHub Organization – Repo-Struktur

**Vorbereitet:** 2026-02-02
**Status:** Bereit für Ausführung (wartet auf `gh auth login`)

---

## Organization Name

Vorschlag: `denkwende-dev` oder `dino-ventures`

---

## Repos die ich anlegen werde:

### 1. `denkwende-channel`
Alles rund um den YouTube-Kanal.

```
denkwende-channel/
├── README.md
├── scripts/                 # Video-Skripte
│   ├── 001-ki-rally/
│   └── 002-bosch/
├── assets/                  # Bilder, Audio, Vorlagen
├── templates/               # Skript-Templates
├── tools/                   # Automation-Scripts
│   ├── video-pipeline.sh
│   └── shorts-generator.sh
└── docs/
    ├── STYLE-GUIDE.md
    └── WORKFLOW.md
```

### 2. `tools-internal`
Interne Tools und Automation.

```
tools-internal/
├── README.md
├── trend-radar/            # Trend-Recherche Tools
├── video-tools/            # ffmpeg Wrapper, etc.
└── utilities/              # Allgemeine Helfer
```

### 3. Zukünftige Repos (bei Bedarf)
- `denkwende-website` – Falls Website kommt
- `app-[name]` – Für jede App die wir bauen
- `experiment-[name]` – Für Prototypen

---

## Branching-Strategie

```
main        → Stable, produktionsreif
dev         → Aktive Entwicklung  
feature/*   → Einzelne Features
hotfix/*    → Dringende Fixes
```

---

## Workflow

1. **Ich arbeite** auf `dev` oder `feature/xyz`
2. **Ich erstelle PR** → `main`
3. **Dino reviewt** auf GitHub
4. **Dino merged** wenn OK
5. **Auto-Deploy** via Vercel (wenn eingerichtet)

---

## Commit-Konvention

```
feat: Neues Feature
fix: Bug-Fix
docs: Dokumentation
refactor: Code-Verbesserung
chore: Maintenance
```

Beispiele:
- `feat: Video 001 Skript hinzugefügt`
- `fix: ffmpeg Audio-Sync korrigiert`
- `docs: Style-Guide aktualisiert`

---

## Nach Auth – Sofort ausführen:

```bash
# 1. Org erstellen (macht Dino auf github.com)

# 2. Erstes Repo anlegen
gh repo create [ORG]/denkwende-channel --private --description "DenkWende YouTube Channel"

# 3. Lokales Projekt verbinden
cd ~/workspace/projects/0001_trend-to-growth
git init
git remote add origin https://github.com/[ORG]/denkwende-channel.git

# 4. Initial commit
git add .
git commit -m "feat: Initial project setup"
git push -u origin main
```

---

## Checkliste für heute Abend

- [ ] `gh auth login`
- [ ] Organization auf github.com erstellen
- [ ] Mir den Org-Namen sagen
- [ ] Ich führe Rest aus

---

*Ready to execute* 🦁
