# 🖤 Balerion — Vermithrax Validation Gate

**Wenn Vermithrax einen QA Report liefert, prüfe ICH (Balerion) folgendes:**

## Pflicht-Check (JEDES Mal)

### Struktur
- [ ] **Alle 7 Sektionen vorhanden?** (Anforderungs-Basis, Test-Spezifikation, Ergebnisse, Traceability, Findings, Empfehlungen, Freigabe)
- [ ] **Compliance-Checkliste am Ende?**

### Anforderungen (Sektion 1)
- [ ] **Quelle angegeben?** (Welches Dokument? Welche Version?)
- [ ] **Alle Anforderungen aufgelistet?** (Gegen PRD/SPECS abgleichen!)
- [ ] **MUSS/SOLL/KANN korrekt priorisiert?**

### Tests (Sektion 2+3)
- [ ] **Jeder Test referenziert eine ANF-#?**
- [ ] **Tests tatsächlich geschrieben?** (Dateipfade vorhanden, nicht nur Beschreibungen)
- [ ] **Edge Cases und Negative Tests enthalten?**
- [ ] **Coverage-Zahl plausibel?**

### Traceability (Sektion 4) — KERNSTÜCK!
- [ ] **Jede MUSS-Anforderung hat mindestens einen Test?**
- [ ] **Keine ❌ bei MUSS-Anforderungen?** (sonst SOFORT zurückschicken)
- [ ] **Begründung bei ungetesteten Anforderungen?**

### Findings & Freigabe (Sektion 5+7)
- [ ] **Severity plausibel?**
- [ ] **Zahlen in Freigabe stimmen mit Details überein?**
- [ ] **Klare Entscheidung: FREIGEGEBEN / ZURÜCKGEWIESEN / BEDINGT?**

## Red Flags (sofort zurückschicken)

- ❌ Sektion fehlt komplett
- ❌ Anforderungs-Quelle nicht angegeben ("woher weißt du was getestet werden soll?")
- ❌ Traceability-Matrix fehlt oder hat Lücken bei MUSS-Anforderungen
- ❌ Compliance-Checkliste fehlt oder nicht vollständig
- ❌ "Sieht gut aus" ohne Test-Dateien/Evidenz
- ❌ Severity heruntergestuft ohne Begründung

## Was Dino sehen will (IMMER liefern!)

1. **Welche Anforderungen** — klar aufgelistet mit Quelle
2. **Welche Tests** — was wurde wie getestet, nach welcher Spezifikation
3. **Traceability** — Anforderung → Test → Ergebnis (lückenlose Kette)
4. **Entscheidung** — PASS/FAIL mit Begründung

## Bei Zurückweisung

Vermithrax bekommt:
1. WAS fehlt (konkret)
2. WAS er nochmal prüfen soll
3. Hinweis auf welchen Playbook-Punkt er nicht befolgt hat
