# Mission Control Board — Anforderungen

**Stand:** 2026-02-11
**Typ:** Single-Page Dashboard (HTML + JS, kein Backend)
**Datenquelle:** `data.json` (wird von Balerion aktualisiert) + `logs/activity.jsonl`

---

## Funktionale Anforderungen

### ANF-1: Drachen-Karten (MUSS)
Alle Drachen aus `data.json.dragons` werden als Karten angezeigt.
- Dino + Balerion oben
- Sub-Drachen (Caraxes, Vermithrax, Meleys, Sunfyre) in einer Reihe darunter
- Jede Karte zeigt: Avatar/Bild, Name, Titel, Rolle, Model, Tags
- Wenn ein Drache in `data.json` existiert, MUSS er im Dashboard sichtbar sein

### ANF-2: Drachen-Bilder (MUSS)
Jeder Drache hat ein Profilbild unter `img/[name].png`.
- Bilder werden korrekt geladen und angezeigt
- Bei fehlendem Bild: Fallback (Emoji oder Placeholder)

### ANF-3: Raids/Proposals Anzeige (MUSS)
`data.json.raids` wird als Liste/Tabelle angezeigt.
- Name, Target, Bounty, Status, Demo-Link (wenn vorhanden)
- Status wird visuell unterschieden (submitted, demo_ready, etc.)

### ANF-4: Next Targets Anzeige (SOLL)
`data.json.nextTargets` wird angezeigt mit Name, Emoji, Bounty, Proposals-Anzahl, Note.

### ANF-5: Kriegskasse (MUSS)
`data.json.kriegskasse` zeigt:
- Connects (aktuell / total)
- Einnahmen
- Offene Proposals

### ANF-6: City Apps Status (SOLL)
`data.json.cityApps` zeigt: Status, Pilot-Gemeinde, Features, Demo-Link.

### ANF-7: X Revenue Tab (SOLL)
`data.json.xRevenue` zeigt:
- Account, Plan, Follower (aktuell/Ziel)
- Meilensteine mit done/nicht-done Status
- Strategie-Übersicht
- Revenue Streams

### ANF-8: Activity Feed (MUSS)
`logs/activity.jsonl` wird als chronologischer Feed angezeigt.
- Neueste Einträge oben
- Filtermöglichkeit nach Drache (Balerion, Caraxes, Vermithrax, Meleys, Sunfyre)
- Jeder Eintrag zeigt: Timestamp, Drache, Topic

### ANF-9: Last Update Anzeige (MUSS)
`data.json.lastUpdate` wird als Timestamp angezeigt, damit sichtbar ist wie aktuell die Daten sind.

### ANF-10: Navigation (MUSS)
Tab-Navigation zwischen den verschiedenen Ansichten (Overview, Dragons, Raids, X Revenue, Feed, etc.)

### ANF-11: Blocker-Anzeige (SOLL)
`data.json.blocker` wird als Liste angezeigt — aktuelle Probleme/Blockaden.

---

## Nicht-funktionale Anforderungen

### NFA-1: Responsive Design (SOLL)
Dashboard soll auf Desktop UND Mobile (iPhone) nutzbar sein.

### NFA-2: Keine externen Abhängigkeiten (MUSS)
Nur HTML, CSS, JS. Keine Frameworks, keine CDN-Einbindungen. Alles lokal.

### NFA-3: Dark Theme (MUSS)
Dunkles Farbschema passend zur Drachen-Ästhetik.

### NFA-4: Auto-Reload-fähig (KANN)
Daten könnten per Reload aktualisiert werden (kein WebSocket nötig).

### NFA-5: Cache-Busting (MUSS)
`data.json` und `activity.jsonl` dürfen NICHT gecached werden (meta tags + fetch headers).

---

## Daten-Konsistenz-Regeln

### DK-1: Drachen-Sync (MUSS)
Jeder Drache der in `data.json.dragons` existiert, MUSS:
- Im Dashboard als Karte sichtbar sein
- Im Activity Feed filterbar sein
- In der Org-Chart / Overview erscheinen
- Einen Eintrag in EMOJI_MAP haben

### DK-2: Daten-Vollständigkeit (MUSS)
Alle Felder in `data.json` die befüllt sind, müssen im Dashboard reflektiert werden.
Keine "vergessenen" Felder die zwar in der JSON stehen aber nie angezeigt werden.
