# Projekte

Dieser Ordner enthält alle Projekte mit persistenter Dokumentation.

## Ordner-Namenskonvention

```
XXXX_projektname
```

**Beispiel:** `0001_nano-banana-pro`
- `0001` = Fortlaufende Projekt-ID (4-stellig)
- `nano-banana-pro` = Kurze, prägnante Projekt-Kennzeichnung

**Nächste freie ID:** 0004

## Aktive Projekte

| ID | Name | Beschreibung |
|----|------|--------------|
| 0001 | nano-banana-pro | Gemini Image Generation |
| 0002 | revenue-machine | Umsatz-Generierung, WorkflowAudit |
| 0003 | city-apps | Stadt-Apps für deutsche Kommunen |

## Standard-Projektstruktur

Jedes Projekt enthält mindestens:

```
XXXX_projektname/
├── README.md           # Projektübersicht, Ziele, Status
├── NOTES.md            # Chronologische Gesprächsnotizen & Entscheidungen
├── research/           # Recherche-Ergebnisse, Links, Quellen
├── assets/             # Dateien, Bilder, Dokumente
└── output/             # Ergebnisse, Deliverables
```

## README.md Template (pro Projekt)

```markdown
# [Projektname]

**Projekt-ID:** XXXX
**Erstellt:** YYYY-MM-DD

## Ziel
Was wollen wir erreichen?

## Status
🟡 In Arbeit / 🟢 Abgeschlossen / 🔴 Pausiert

## Kontext
Warum dieses Projekt? Hintergrund.

## Nächste Schritte
- [ ] ...

## Entscheidungen
| Datum | Entscheidung | Begründung |
|-------|--------------|------------|
| ... | ... | ... |
```

## Workflow

1. **Neues Projekt starten:** Dino sagt "neues Projekt" → Jonny vergibt nächste ID
2. **Während der Arbeit:** NOTES.md wird kontinuierlich aktualisiert
3. **Bei Entscheidungen:** README.md wird gepflegt
4. **Recherche:** Ergebnisse landen in `research/`
5. **Projekt referenzieren:** "Wir arbeiten an Projekt 0001"
6. **Context-Recovery:** Bei Kontext-Verlust → README.md + NOTES.md lesen

So geht kein Wissen mehr verloren! 🦁
