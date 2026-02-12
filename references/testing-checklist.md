# Testing Checklist (PRD → Implement → Test)

## 1. PRD first (before coding)
- What exactly to build/change?
- Data flow?
- Acceptance criteria?
- Document PRD in project folder or inline

## 2. Implement
- Build only what the PRD says
- New requirements → update PRD first, then implement

## 3. Test (every time)
- [ ] Functional: does it do what the PRD says?
- [ ] Data consistency: are all displayed values correct? (not just "it loads")
- [ ] Completeness: all fields/areas correctly populated?
- [ ] Edge cases: missing data? empty lists?
- [ ] Visual: screenshot or browser check
- [ ] Cross-check: displayed data matches source?

## 4. Completion report
```
📋 ABSCHLUSSBERICHT
─────────────────
PRD: [requirement]
IMPLEMENTIERT: [what was built/changed, which files]
GETESTET:
  ✅/❌ Funktionstest
  ✅/❌ Daten-Konsistenz
  ✅/❌ Vollständigkeit
  ✅/❌ Visuell geprüft
  ✅/❌ Cross-Check
FLIGHT LOG: [takeoff + landing logged?]
ERGEBNIS: Bereit zur Abnahme
```

Only deliver to Dino when everything passes. Never use Dino as your tester.
