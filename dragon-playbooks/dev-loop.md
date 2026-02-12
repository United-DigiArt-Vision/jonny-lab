# 🔄 Dragon Dev Loop — Standard-Entwicklungsprozess

**Gilt für ALLES was entwickelt/programmiert wird. KEINE AUSNAHMEN.**

Balerion startet diesen Loop automatisch. Dino muss es NIE erklären.

---

## Der Loop

```
┌─────────────────────────────────────────────┐
│  1. ANFORDERUNGEN (Balerion)                │
│     → PRD / REQUIREMENTS.md erstellen       │
│     → Wenn schon vorhanden: prüfen/updaten  │
├─────────────────────────────────────────────┤
│  2. TESTS ZUERST (Vermithrax 🛡️)           │
│     → Liest Anforderungen                   │
│     → Schreibt Test-Spezifikation           │
│     → Definiert Akzeptanzkriterien          │
├─────────────────────────────────────────────┤
│  3. IMPLEMENTIERUNG (Caraxes 🔴)            │
│     → Bekommt Anforderungen + Test-Spec     │
│     → Implementiert gegen die Tests         │
│     → Liefert Code                          │
├─────────────────────────────────────────────┤
│  4. QA (Vermithrax 🛡️)                     │
│     → Testet Code gegen Anforderungen       │
│     → Erstellt vollständigen QA Report      │
│     → PASS oder FAIL                        │
├─────────────────────────────────────────────┤
│  5. PASS? ──→ JA ──→ Balerion liefert      │
│     │              an Dino mit Protokoll    │
│     │                                       │
│     └──→ NEIN ──→ Zurück zu Schritt 3      │
│              Caraxes fixt die Findings      │
│              Dann wieder Schritt 4          │
│              (Loop bis PASS)                │
├─────────────────────────────────────────────┤
│  6. LIEFERUNG (Balerion → Dino)             │
│     → Volles Protokoll im Chat:             │
│       - Anforderungsdokument (Pfad)         │
│       - Test-Spezifikation (Pfad)           │
│       - Traceability-Matrix                 │
│       - Alle Dateipfade                     │
│       - Freigabe-Entscheidung               │
└─────────────────────────────────────────────┘
```

---

## Wann wird der Loop gestartet?

**AUTOMATISCH bei:**
- Neues Feature / neue Funktion
- Bug-Fix
- UI-Änderung
- Refactoring
- Jede Code-Änderung die an Dino geliefert wird

**NICHT nötig bei:**
- Reine Dokumentations-Änderungen (MEMORY.md, NOTES.md)
- Config-Änderungen (openclaw.json, cron jobs)
- Reine Daten-Updates (data.json Werte aktualisieren)

---

## Rollen im Loop

| Wer | Was | Wann |
|-----|-----|------|
| **Balerion** | Anforderungen erstellen/prüfen, Loop orchestrieren, finale Validation, Lieferung an Dino | Start + Ende |
| **Vermithrax** | Tests definieren, Code prüfen, QA Report, PASS/FAIL | Vor + Nach Implementierung |
| **Caraxes** | Code implementieren, Findings fixen | Mitte |

---

## Regeln

1. **Kein Code ohne Anforderungen.** Keine Implementierung ohne PRD/REQUIREMENTS.
2. **Kein Code ohne Tests.** Vermithrax definiert Tests VOR der Implementierung.
3. **Kein FAIL an Dino.** Nur PASS-Ergebnisse werden geliefert. Loop bis es passt.
4. **Immer Protokoll.** Jede Lieferung an Dino mit vollem QA-Protokoll im Chat.
5. **Balerion entscheidet nicht allein.** Vermithrax hat das letzte Wort bei Qualität.
6. **Der Loop ist Pflicht.** Balerion startet ihn automatisch — Dino muss es nie sagen.

---

## Eskalation

- **Loop dreht sich >3 Mal ohne PASS:** Balerion meldet an Dino mit Analyse was schiefläuft
- **Anforderungen unklar:** Balerion fragt Dino BEVOR der Loop startet
- **Technisch unmöglich:** Balerion meldet an Dino mit Alternativen

---

*Qualität ist kein Feature. Qualität ist der Prozess.* 🛡️🔴🖤
