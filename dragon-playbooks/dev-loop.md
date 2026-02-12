# 🔄 Dragon Dev Loop — Standard-Entwicklungsprozess

Gilt für alles was entwickelt/programmiert wird. Balerion startet den Loop automatisch.

---

## Der Loop

```
┌─────────────────────────────────────────────┐
│  1. ANFORDERUNGEN (Balerion)                │
│     → PRD / REQUIREMENTS.md erstellen       │
│     → Wenn schon vorhanden: prüfen/updaten  │
├─────────────────────────────────────────────┤
│  2. DESIGN + TESTS (Syrax 🩵)              │
│     → Liest Anforderungen                   │
│     → Schreibt Design-Spec + Workflow-Spec  │
│     → Schreibt Test-Spezifikation           │
│     → Definiert Akzeptanzkriterien          │
│     (Syrax kennt das Design am besten →     │
│      weiß was getestet werden muss)         │
├─────────────────────────────────────────────┤
│  3. IMPLEMENTIERUNG (Caraxes 🔴)            │
│     → Bekommt Design-Spec + Test-Spec       │
│     → Implementiert gegen die Specs         │
│     → Liefert Code                          │
├─────────────────────────────────────────────┤
│  4. QA-AUSFÜHRUNG (Vermithrax 🛡️)          │
│     → Führt Syrax' Tests aus (schreibt      │
│       keine eigenen — verhindert Betrug)    │
│     → Erstellt QA Report: PASS oder FAIL    │
├─────────────────────────────────────────────┤
│  5. PASS? ──→ JA ──→ Balerion liefert      │
│     │              an Dino mit Protokoll    │
│     └──→ NEIN ──→ Zurück zu Schritt 3      │
│              (Loop bis PASS, max 3x)        │
├─────────────────────────────────────────────┤
│  6. LIEFERUNG (Balerion → Dino)             │
│     → Volles Protokoll im Chat:             │
│       - Design-Spec (Pfad)                  │
│       - Test-Spezifikation (Pfad)           │
│       - Traceability-Matrix                 │
│       - Alle Dateipfade                     │
│       - Freigabe-Entscheidung               │
└─────────────────────────────────────────────┘
```

---

## Wann wird der Loop gestartet?

**Automatisch bei:** Feature, Bug-Fix, UI-Änderung, Refactoring, jede Code-Änderung für Dino.

**Nicht nötig bei:** Reine Dokumentation, Config-Änderungen, Daten-Updates.

---

## Rollen im Loop

| Wer | Was | Wann |
|-----|-----|------|
| Balerion 🖤 | Anforderungen, Orchestrierung, finale Validation, Lieferung | Start + Ende |
| Syrax 🩵 | Design-Spec + Test-Spec (beides!) | Nach Anforderungen |
| Caraxes 🔴 | Implementierung gegen beide Specs, Findings fixen | Mitte |
| Vermithrax 🛡️ | Führt Syrax' Tests aus, meldet PASS/FAIL | Nach Code |

**Separation of Concerns:** Syrax schreibt Design UND Tests (sie kennt die Anforderungen am besten). Vermithrax führt die Tests nur AUS — er schreibt keine eigenen, damit er sich nicht selbst bescheißen kann. Caraxes baut nur, testet nicht.

---

## Regeln

1. Kein Code ohne Anforderungen und Design-Spec.
2. Syrax schreibt Design-Spec UND Test-Spec. Niemand sonst.
3. Vermithrax führt Tests nur AUS. Schreibt keine eigenen Tests.
4. Kein FAIL an Dino. Loop bis PASS.
5. Jede Lieferung mit vollem QA-Protokoll.
6. Der Loop ist Pflicht — Balerion startet ihn automatisch.

---

## Eskalation

- Loop >3x ohne PASS → Balerion meldet an Dino mit Analyse
- Anforderungen unklar → Balerion fragt Dino bevor der Loop startet
- Technisch unmöglich → Balerion meldet mit Alternativen

---

*Syrax entwirft und definiert die Prüfung. Caraxes baut. Vermithrax führt die Prüfung aus. Balerion liefert.* 🩵🔴🛡️🖤
