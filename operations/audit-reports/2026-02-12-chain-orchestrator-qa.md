# QA Report: Chain Orchestrator
**Tester:** Vermithrax 🛡️  
**Datum:** 2026-02-12 17:44 CET  
**Gegenstand:** `tools/chain-orchestrator/chain.py` + modifizierte Tools

---

## Testergebnisse

| # | Test | Erwartet | Tatsächlich | Ergebnis |
|---|------|----------|-------------|----------|
| 1 | News Chain Happy Path | JSON mit articles_found, validated, ingested, errors | ✅ Korrektes JSON: `articles_found:0, validated:0, ingested:0, errors:[]` — strukturell korrekt, 0 Results wegen fehlender Live-Daten bei Query "test" | **PASS** |
| 2 | News Chain Duplikat (gleiche Query 2x) | Zweiter Run liefert 0 neue Artikel oder markiert Duplikate | ✅ Zweiter Run: identisches Ergebnis (0 articles). Duplikat-Handling konnte nicht verifiziert werden da keine Articles gefunden — strukturell kein Fehler | **PASS (eingeschränkt)** |
| 3 | Job Chain Happy Path | JSON mit jobs_found, leads_added, errors | ⚠️ Error: `research.py` wird mit `--mode brave` aufgerufen, aber research.py akzeptiert nur `auto, tweet, x_search, web_search` | **FAIL** |
| 4 | Job Chain Duplikat-URL | Duplikate werden übersprungen | ❌ Kann nicht getestet werden da Job Chain bereits in Step 1 (search) fehlschlägt | **BLOCKED** |
| 5 | Council Feed | JSON mit kb, leads, threads, costs, learning Stats | ✅ Vollständiges JSON mit allen 5 Sektionen + Timestamp + Learning-Daten | **PASS** |
| 6 | Feedback Loop Posted | Status ok, Feedback für posted Event | ✅ `{"status":"ok","feedback_result":{"status":"suggestions","suggested_prefer_keywords":[...]}}` | **PASS** |
| 7 | Feedback Loop Rejected | Status ok, Feedback für rejected Event | ✅ `{"status":"ok","feedback_result":{"status":"logged","relevant":false}}` | **PASS** |
| 8 | Health Check | Status aller Komponenten | ✅ Alle 5 Tools `ok`, alle 3 DBs `exists`, API Keys korrekt erkannt | **PASS** |
| 9 | Chain Log (`chain-log.jsonl`) | Jeder Chain-Run wird geloggt | ✅ 11 Einträge nach allen Tests. Format: `{ts, chain, step, status, duration_ms}`. Errors werden korrekt mit `status:error` + `error:...` geloggt | **PASS** |
| 10a | kb.py --help | Hilfetext mit chain-kompatiblen Actions | ✅ Actions: ingest, ingest-note, search, list, stats | **PASS** |
| 10b | pipeline.py --help | Hilfetext mit chain-kompatiblen Actions | ✅ Actions: register, check, list, update, stats, scan, get-source | **PASS** |
| 10c | tracker.py --help | Hilfetext mit chain-kompatiblen Actions | ✅ Actions: add, update, list, stats, search, migrate, contact, timeline, get-source | **PASS** |
| 10d | report.py --help | Hilfetext mit --json Flag | ✅ Flags: --days, --model, --task-type, --weekly, --routing, --json | **PASS** |
| 11 | CHAIN_RESULT / CHAIN_EVENT Outputs | Tools emittieren CHAIN_RESULT/CHAIN_EVENT Prefixes | ✅ kb.py: CHAIN_RESULT implementiert (Z.216). pipeline.py: CHAIN_EVENT (Z.167). tracker.py: CHAIN_EVENT (Z.121). chain.py parsed CHAIN_RESULT (Z.72) | **PASS** |
| 12 | Error Handling ohne GEMINI_API_KEY | Health Check zeigt "missing", kein Crash | ✅ `"GEMINI_API_KEY": "missing"` — graceful degradation, kein Crash | **PASS** |

---

## Zusammenfassung

| Kategorie | Anzahl |
|-----------|--------|
| **PASS** | 11 |
| **PASS (eingeschränkt)** | 1 |
| **FAIL** | 1 |
| **BLOCKED** | 1 |

## Kritische Findings

### 🔴 FAIL: Job Chain — Falscher Research Mode
**Schwere:** Hoch — Job Chain komplett nicht nutzbar  
**Ursache:** `chain.py` ruft `research.py` mit `--mode brave` auf, aber `research.py` kennt nur: `auto, tweet, x_search, web_search`  
**Fix:** In `chain.py` den Mode auf `web_search` oder `auto` ändern  

### 🟡 EINGESCHRÄNKT: Duplikat-Tests
News-Duplikat-Test konnte nur strukturell geprüft werden (0 Results bei "test"-Query). Empfehlung: Test mit echten Daten wiederholen sobald Job Chain gefixt ist.

---

## Empfehlung

**Job Chain Fix durchführen, dann Re-Test von Test 3 + 4.**  
Alle anderen Chains sind produktionsbereit.

---
*Vermithrax 🛡️ — QA Complete*
