# AI-Ready CLI Wrappers — Service-Paket

> **WorkflowAudit** by United DigiArt Vision
> workflowaudit.uniteddigiart.com
> Deep Blue `#1a365d` · Electric Teal `#0891b2`
> Stand: 2026-02-14

---

## 1. Service-Beschreibung

### Was wir machen

Wir bauen CLI-Schnittstellen für SaaS-Produkte, die keine haben.

**Das Problem:** Die meisten Business-SaaS-Tools (CRMs, ERPs, HR-Systeme, Buchhaltung) bieten nur Web-UIs oder lückenhafte APIs. AI-Agents — ob Claude, GPT, eigene LLM-Pipelines oder Automatisierungsplattformen — brauchen aber programmatische Schnittstellen: stdin/stdout, strukturierten Output (JSON), klare Kommandos. Ohne das bleibt jede AI-Initiative stecken.

**Was wir liefern:**

| Deliverable | Beschreibung |
|---|---|
| **CLI Binary** | Eigenständiges Kommandozeilen-Tool (Go/Rust), installierbar via Homebrew, apt, oder als statisches Binary |
| **Strukturierter Output** | Jeder Befehl liefert JSON, optional human-readable. Maschinenlesbar ab Tag 1 |
| **Auth-Modul** | OAuth2, API-Key, Session-basiert — je nach Ziel-SaaS. Einmal einrichten, danach headless |
| **Agent-Adapter** | Vorkonfigurierte Tool-Definitionen für OpenAI function calling, Anthropic tool_use, LangChain, MCP |
| **Dokumentation** | Man-pages, --help für jeden Befehl, README mit Quickstart |
| **Test-Suite** | Integration-Tests gegen die echte SaaS-API (mit Sandbox/Staging wo verfügbar) |

### Was wir NICHT machen

- Keine eigene SaaS-Plattform bauen
- Keine Daten hosten oder verarbeiten
- Kein AI-Modell trainieren
- Wir bauen die **Brücke**, nicht das Haus auf beiden Seiten

### Technischer Ansatz

```
┌──────────────┐     ┌─────────────────┐     ┌──────────────┐
│  AI Agent     │────▶│  CLI Wrapper     │────▶│  SaaS API /  │
│  (Claude,GPT, │     │  (Go/Rust)       │     │  Web Scraping│
│   Automation) │◀────│  JSON stdout     │◀────│  GraphQL/REST│
└──────────────┘     └─────────────────┘     └──────────────┘
```

**Drei Integrationspfade je nach SaaS:**

1. **API-First** — Offizielle REST/GraphQL-API vorhanden → Wrapper drumrum (schnellster Pfad)
2. **Reverse-Engineering** — Keine öffentliche API, aber interne API-Calls im Web-Client → Abfangen + wrappen
3. **Browser-Automation** — Kein API-Zugang → Playwright/Puppeteer-basiert, headless, mit Retry-Logik

Pfad 1 = 2-4 Wochen. Pfad 2 = 4-6 Wochen. Pfad 3 = 6-10 Wochen.

### Skalierbarkeits-Prinzip

Jeder CLI-Wrapper folgt derselben Architektur:

```
shared/
  ├── auth/          # Wiederverwendbare Auth-Module (OAuth2, SAML, API-Key)
  ├── output/        # JSON-Formatter, Table-Renderer
  ├── agent-adapters/# MCP, OpenAI, LangChain Templates
  └── testing/       # Test-Harness, Mock-Server
wrappers/
  ├── datev-cli/
  ├── personio-cli/
  └── hubspot-cli/
```

Jeder neue Wrapper nutzt 60-70% Shared Code. Wrapper #1 dauert 4 Wochen. Wrapper #5 dauert 2 Wochen.

---

## 2. Zielkunden

### Primäre Branchen

| Branche | Warum | Typische Tools ohne CLI |
|---|---|---|
| **Steuerberatung / Buchhaltung** | Hoher Automatisierungsdruck, viele repetitive Aufgaben, DATEV-Ökosystem | DATEV, Lexoffice, sevDesk |
| **HR / Recruiting** | Fachkräftemangel erzwingt Effizienz, viele manuelle Prozesse | Personio, Workday, BambooHR |
| **Agenturen (Marketing/Digital)** | Viele Tools, kleine Teams, hoher Zeitdruck | Asana, Monday, Canva, HubSpot |
| **E-Commerce** | Multichannel-Chaos, Daten in 10 Systemen | Shopify (teilw.), JTL, Billbee |
| **Fertigung / Industrie** | ERP-Systeme aus den 90ern, keine API-Kultur | SAP (teilw.), Sage, proAlpha |

### Firmengrößen

| Segment | Mitarbeiter | Budget | Kaufmotivation |
|---|---|---|---|
| **KMU (Sweet Spot)** | 50-500 | 15-50k€ pro Wrapper | Können keine eigene Integration bauen, AI-Budget vorhanden aber ROI unklar |
| **Mittelstand** | 500-5.000 | 50-150k€ | Haben IT-Abteilung, aber die ist ausgelastet. Externe Spezialisten für Nischenthemen |
| **Enterprise** | 5.000+ | 100-500k€+ | Compliance, Sicherheit, Support-SLAs. Kaufen Pakete, nicht Stunden |

### Buyer Personas

**1. "Der CTO, der AI will aber nicht kann"**
- 35-50 Jahre, technisch versiert
- Hat AI-Budget freigegeben, Team probiert ChatGPT/Copilot
- Scheitert an: "Unser CRM hat keine API die der Agent nutzen kann"
- Kauft: Konkretes Ergebnis in 4 Wochen, nicht Beratung

**2. "Die Geschäftsführerin, die ROI braucht"**
- 40-55 Jahre, betriebswirtschaftlich
- Hört überall "AI" aber sieht keine Ergebnisse
- Scheitert an: Berater liefern Slides, keine lauffähige Software
- Kauft: Bewiesene Zeitersparnis, Amortisation in <6 Monaten

**3. "Der IT-Leiter, der entlasten will"**
- 30-45 Jahre, operativ überlastet
- Sein Team macht 40% manuelle Datenübertragung zwischen Systemen
- Scheitert an: Kein Budget für Vollzeit-Entwickler, SaaS-Anbieter reagiert nicht
- Kauft: Fertige Lösung die sein Team sofort nutzen kann

---

## 3. Pricing-Modell

### Pakete

| | **Starter** | **Pro** | **Enterprise** |
|---|---|---|---|
| **Preis** | 9.500 € | 24.500 € | ab 65.000 € |
| **Scope** | 1 SaaS-Tool, bis 10 Befehle | 1 SaaS-Tool, bis 30 Befehle + Agent-Adapter | Multi-Tool-Integration, Custom Workflows |
| **Integrationspfad** | Nur API-First | API-First oder Reverse-Engineering | Alle Pfade inkl. Browser-Automation |
| **Agent-Adapter** | Keiner (nur CLI) | 1 Adapter (OpenAI ODER MCP ODER LangChain) | Alle Adapter + Custom |
| **Lieferzeit** | 2-3 Wochen | 4-6 Wochen | 8-12 Wochen |
| **Support** | 30 Tage Bugfix | 90 Tage Bugfix + Updates | 12 Monate SLA (48h Response) |
| **Wartung** | — | Optional: 500€/Monat | Inkludiert (12 Monate) |
| **Source Code** | Nein (Binary) | Ja (Repo-Zugang) | Ja + Transfer of Ownership möglich |

### Add-Ons

| Add-On | Preis |
|---|---|
| Weiterer Agent-Adapter | 2.500 € |
| Browser-Automation-Upgrade (Pfad 3) | 8.000 € |
| Wartungsvertrag (12 Monate, monatl.) | 500-1.500 €/Monat je nach Komplexität |
| Onboarding-Workshop (halber Tag) | 1.800 € |
| Zusätzliche 10 Befehle | 4.000 € |

### US-Preise

Faktor 1.3x auf alle EUR-Preise (in USD). Starter $12,500 / Pro $32,000 / Enterprise ab $85,000.

### Warum diese Preise funktionieren

- Ein Entwickler kostet 80-120k€/Jahr. Unsere Lösung spart mind. 0.5 FTE → Amortisation in 2-5 Monaten
- Vergleichbare Custom-Integration vom IT-Dienstleister: 40-80k€ für ähnlichen Scope, aber ohne Agent-Adapter
- Beratungshäuser (McKinsey Digital, Accenture) verkaufen "AI Readiness Assessments" für 50-150k€ — und liefern PowerPoints

---

## 4. Pitch-Deck Outline (10 Slides)

### Slide 1 — Problem
**"Ihre AI-Agents sind blind."**
AI kann nur arbeiten, wenn sie Zugriff auf Ihre Tools hat. 73% der Business-Software hat keine programmatische Schnittstelle. Ihre AI-Investition bringt 0 ROI, solange Agenten nicht lesen, schreiben und handeln können.

### Slide 2 — Markt
**"40% aller AI-Projekte scheitern bis 2027 — nicht an der AI, sondern an fehlenden Schnittstellen."**
Gartner-Prognose. Der Engpass ist nicht das Modell. Der Engpass ist der Zugang zu den Daten und Aktionen in bestehenden Systemen.

### Slide 3 — Lösung
**"Wir bauen die CLI, die Ihr SaaS-Anbieter nicht liefert."**
Kommandozeilen-Tools für jede Business-Software. JSON-Output. Agent-ready. In 2-6 Wochen, nicht 6 Monaten.

### Slide 4 — Wie es funktioniert
**"API da? 2 Wochen. Keine API? Wir finden einen Weg."**
Drei Integrationspfade. Architektur-Diagramm. Shared-Code-Prinzip für Skalierung.

### Slide 5 — Demo / Case Study
**"Vorher: 4h manuelle Dateneingabe. Nachher: 1 Befehl."**
Live-Demo: CLI-Befehl → AI-Agent nutzt CLI → Ergebnis in Sekunden. (gogcli als Referenz-Architektur zeigen.)

### Slide 6 — Für wen
**"Jedes Unternehmen mit >3 SaaS-Tools und dem Wunsch nach Automatisierung."**
Steuerberater, HR-Abteilungen, Agenturen, E-Commerce, Industrie. 50-5.000 Mitarbeiter.

### Slide 7 — Pricing
**"Ab 9.500€. ROI in unter 6 Monaten."**
3 Pakete. Transparent. Kein Berater-Tagessatz-Spiel.

### Slide 8 — Differenzierung
**"Wir sind keine Berater. Wir liefern lauffähige Software."**
Kein Assessment, keine Strategie-Slides. Binary das läuft. Tests die grün sind. Doku die man lesen kann.

### Slide 9 — Team & Track Record
**"Gebaut von Leuten, die AI-Agents jeden Tag selbst nutzen."**
United DigiArt Vision. Wir nutzen diese CLIs intern — sie entstehen aus echtem Bedarf, nicht aus Theorie.

### Slide 10 — Call to Action
**"Welches Tool bremst Ihre AI-Strategie aus? Nennen Sie es uns."**
Kostenlose Machbarkeitsanalyse (30 Min Call). In 48h wissen Sie: geht es, was kostet es, wann ist es fertig.

---

## 5. Konkurrenz-Analyse

### Direkte Wettbewerber

| Wettbewerber | Was sie machen | Stärke | Schwäche |
|---|---|---|---|
| **Merge.dev** | Unified API für HR, ATS, CRM, Accounting | Breite Abdeckung, gehostet | Nur API, keine CLI. Kein Agent-Adapter. Subscription-Modell (teuer langfristig). Abhängigkeit. |
| **Rutter** | Unified API für Commerce/Accounting | E-Commerce-Fokus | Nur API, US-zentrisch, keine EU-Tools (DATEV etc.) |
| **Apideck** | Unified API Plattform | 300+ Integrationen | Generisch, kein Agent-Fokus, keine CLI |
| **Individuelle Freelancer** | Custom API-Integration | Günstig | Kein Standard, keine Wartung, kein Agent-Adapter, kein Shared-Code |
| **SaaS-Anbieter selbst** | Offizielle APIs (wenn vorhanden) | Autorität | Langsam, unvollständig, kein CLI, kein Agent-Fokus |

### Indirekte Wettbewerber

| Wettbewerber | Abgrenzung |
|---|---|
| **Zapier / Make / n8n** | Low-Code-Automatisierung. GUI-basiert, nicht agent-ready. Wir liefern die Ebene darunter. |
| **MuleSoft / Boomi** | Enterprise-iPaaS. 6-stellige Lizenzen, 6-monatige Implementierung. Wir sind schneller und günstiger. |
| **RPA (UiPath, Automation Anywhere)** | Desktop-Automation, fragil, teuer. Wir wrappen APIs statt UIs zu klicken. |

### Unsere Differenzierung

1. **CLI-first, nicht API-first** — Wir liefern ein Binary das man ausführen kann, nicht eine API die man selbst einbinden muss
2. **Agent-Adapter inklusive** — MCP, OpenAI function calling, LangChain out-of-the-box. Kein Wettbewerber hat das
3. **EU/DACH-Fokus** — DATEV, Personio, sevDesk, Lexoffice — Tools die Merge.dev nicht kennt
4. **Kein Abo** — Einmalzahlung + optionale Wartung. Keine monatliche API-Gebühr pro Request
5. **Ownership** — Kunde bekommt Source Code (Pro/Enterprise). Keine Vendor-Abhängigkeit

---

## 6. Go-to-Market — Erste 3 Schritte

### Schritt 1: Referenz-Wrapper bauen + Open Source (Woche 1-4)

**Was:** Einen CLI-Wrapper für ein populäres deutsches SaaS-Tool bauen (Empfehlung: **Lexoffice** oder **sevDesk** — Buchhaltung, großer Pain, viele KMUs).

**Warum:** Beweis dass wir es können. Open-Source auf GitHub → Sichtbarkeit in der Developer-Community. Peter Steinberger's gogcli zeigt: sowas geht viral.

**Wie:**
- Wrapper bauen (Lexoffice hat eine API → Pfad 1 → 2-3 Wochen)
- Open Source auf GitHub, MIT-Lizenz
- README mit Agent-Beispielen (Claude nutzt lexoffice-cli um Rechnungen zu erstellen)
- Post auf X/Twitter, Hacker News, r/selfhosted, deutsche Tech-Slack-Communities
- **Ziel:** 500+ GitHub Stars, 3 Inbound-Anfragen

### Schritt 2: Content + Outbound an Steuerberater-Netzwerk (Woche 3-6)

**Was:** Gezieltes Outbound an Steuerberatungskanzleien und deren IT-Dienstleister.

**Warum:** Steuerberater sind perfekte Early Adopter: regulierter Markt, hoher Leidensdruck, DATEV-Monopol, Budget vorhanden.

**Wie:**
- LinkedIn-Artikel: "Warum DATEV Ihre AI-Strategie blockiert — und was Sie dagegen tun können"
- 50 persönliche LinkedIn-Messages an CTOs/IT-Leiter von Top-200-Kanzleien
- Webinar (45 Min): "AI-Agents in der Steuerkanzlei — Live-Demo"
- Landing Page: workflowaudit.uniteddigiart.com/cli-wrappers
- **Ziel:** 5 Discovery Calls, 2 Angebote

### Schritt 3: Erster zahlender Kunde + Case Study (Woche 5-10)

**Was:** Ersten Wrapper als bezahltes Projekt umsetzen, Case Study daraus machen.

**Warum:** Nichts verkauft besser als ein konkretes Ergebnis mit echten Zahlen.

**Wie:**
- Erstem Kunden 30% Rabatt für Case-Study-Recht
- Saubere Dokumentation: Vorher/Nachher, Zeitersparnis, Kosten
- Case Study auf Website, LinkedIn, in jedem Pitch
- **Ziel:** 1 bezahlter Abschluss (min. 15k€), 1 publizierbare Case Study

---

## 7. Beispiel-Projekte

### Projekt 1: DATEV CLI

| | |
|---|---|
| **Tool** | DATEV (Buchhaltung, Steuern, Lohnabrechnung) |
| **Pain** | Kein moderner API-Zugang, nur DATEV-eigene Schnittstellen (DATEVconnect), proprietäre Formate |
| **Integrationspfad** | Pfad 2 (Reverse-Engineering DATEVconnect) + teilw. Pfad 3 |
| **Scope** | Belege hochladen, Buchungen lesen, Mandanten-Stammdaten, Export als CSV/JSON |
| **Geschätzter Aufwand** | 6-8 Wochen, 2 Entwickler |
| **Preis** | 45.000 - 65.000 € (Enterprise) |
| **Marktpotenzial** | 40.000+ Steuerberater-Kanzleien in DE. Wenn 0.5% kaufen = 200 Kunden × 50k = 10M€ |

### Projekt 2: Personio CLI

| | |
|---|---|
| **Tool** | Personio (HR-Management, Gehaltsabrechnung) |
| **Pain** | API existiert, aber unvollständig. Keine Bulk-Ops, kein CLI, Agent-Integration fehlt |
| **Integrationspfad** | Pfad 1 (API) + Pfad 2 für fehlende Endpunkte |
| **Scope** | Mitarbeiter CRUD, Abwesenheiten, Dokumente, Gehaltsabrechnungen lesen, Onboarding-Workflows |
| **Geschätzter Aufwand** | 4-5 Wochen, 1-2 Entwickler |
| **Preis** | 24.500 € (Pro) |
| **Marktpotenzial** | Personio hat 14.000+ Kunden. 1% = 140 × 25k = 3.5M€ |

### Projekt 3: Canva CLI

| | |
|---|---|
| **Tool** | Canva (Design, Marketing-Assets) |
| **Pain** | Canva Connect API ist neu und begrenzt. Kein CLI. Agenturen wollen: "Erstelle 50 Social Posts aus Template X" |
| **Integrationspfad** | Pfad 1 (Connect API) + Pfad 2 |
| **Scope** | Designs erstellen aus Template, Texte/Bilder ersetzen, Export als PNG/PDF, Brand Kit lesen |
| **Geschätzter Aufwand** | 3-4 Wochen |
| **Preis** | 18.000 € (Pro mit Extras) |
| **Marktpotenzial** | Jede Agentur mit >5 Mitarbeitern. Tausende in DACH. |

### Projekt 4: JTL-Wawi CLI

| | |
|---|---|
| **Tool** | JTL-Wawi (E-Commerce ERP, Warenwirtschaft) |
| **Pain** | Windows-only Desktop-Software, SQL-Datenbank-Zugang aber kein CLI, keine REST-API |
| **Integrationspfad** | Pfad 2 (direkte DB-Queries wrappen) + Pfad 3 für UI-Aktionen |
| **Scope** | Artikel CRUD, Bestellungen, Lagerbestand, Versandlabels, Marketplace-Sync-Status |
| **Geschätzter Aufwand** | 6-8 Wochen |
| **Preis** | 45.000 € (Enterprise) |
| **Marktpotenzial** | 20.000+ JTL-Nutzer in DACH, viele mit Multi-Channel-Bedarf |

### Projekt 5: HubSpot CLI (DACH-Edition)

| | |
|---|---|
| **Tool** | HubSpot (CRM, Marketing) |
| **Pain** | API existiert und ist gut, aber kein offizielles CLI. Agent-Integration fehlt. DSGVO-Konfiguration komplex |
| **Integrationspfad** | Pfad 1 (REST API, gut dokumentiert) |
| **Scope** | Contacts/Companies/Deals CRUD, Pipeline-Reports, E-Mail-Sequences triggern, DSGVO-konforme Exports |
| **Geschätzter Aufwand** | 2-3 Wochen |
| **Preis** | 9.500 € (Starter) bis 24.500 € (Pro mit Agent-Adapter) |
| **Marktpotenzial** | HubSpot hat 228.000+ Kunden. Auch kleine Adoption = großer Markt |

### Zusammenfassung Beispielprojekte

| Projekt | Pfad | Wochen | Preis | Marge (geschätzt) |
|---|---|---|---|---|
| DATEV CLI | 2+3 | 6-8 | 55.000 € | ~60% |
| Personio CLI | 1+2 | 4-5 | 24.500 € | ~65% |
| Canva CLI | 1+2 | 3-4 | 18.000 € | ~70% |
| JTL-Wawi CLI | 2+3 | 6-8 | 45.000 € | ~55% |
| HubSpot CLI | 1 | 2-3 | 15.000 € | ~75% |

---

## 8. ROI-Rechnung für Kunden

### Szenario: Mittelständisches Unternehmen, 200 MA

**Ist-Zustand (ohne CLI Wrapper):**

| Aufgabe | Zeitaufwand/Woche | Wer | Kosten/Monat |
|---|---|---|---|
| Manuelle Datenübertragung CRM → Buchhaltung | 8h | Sachbearbeiter (55€/h) | 1.760 € |
| HR-Reports aus Personio exportieren + aufbereiten | 4h | HR-Manager (65€/h) | 1.040 € |
| Rechnungen aus Buchhaltung ins DMS übertragen | 6h | Buchhaltung (50€/h) | 1.200 € |
| Social-Media-Assets manuell in Canva erstellen | 10h | Marketing (60€/h) | 2.400 € |
| **Gesamt** | **28h/Woche** | | **6.400 €/Monat** |

Jährlich: **76.800 € für manuelle Datenarbeit.**

**Soll-Zustand (mit CLI Wrappers + AI Agent):**

| Aufgabe | Zeitaufwand/Woche | Änderung |
|---|---|---|
| CRM → Buchhaltung Sync | 0.5h (Agent-Überwachung) | -94% |
| HR-Reports | 0.5h (Agent-Überwachung) | -88% |
| Rechnungen → DMS | 0.5h (Spot-Checks) | -92% |
| Social-Media-Assets | 3h (Briefing + Review) | -70% |
| **Gesamt** | **4.5h/Woche** | **-84%** |

Neue Kosten: **~1.100 €/Monat**

### ROI-Rechnung

```
Ersparnis pro Jahr:           76.800 - 13.200 = 63.600 €
Investition (2× Pro-Wrapper):                   49.000 €
Wartung (12 Monate, 2 Tools):                   12.000 €
──────────────────────────────────────────────────────────
Gesamtinvestition:                               61.000 €
──────────────────────────────────────────────────────────
ROI Jahr 1:              63.600 - 61.000 =        2.600 € (positiv ab Monat 11)
ROI Jahr 2:              63.600 - 12.000 =       51.600 € (nur Wartung)
ROI Jahr 3:              63.600 - 12.000 =       51.600 €
──────────────────────────────────────────────────────────
ROI über 3 Jahre:                               105.800 €
Return:                                            273%
```

### Die Killer-Folie für den Pitch

> **Investition: 61.000 €**
> **Return über 3 Jahre: 167.000 €**
> **Amortisation: 11 Monate**
> **Ab Jahr 2: 51.600 € Ersparnis pro Jahr — jedes Jahr.**

### Nicht-monetäre Vorteile (die den Deal oft entscheiden)

- **Fehlerreduktion:** Manuelle Übertragung = 2-5% Fehlerquote. CLI = 0%
- **Geschwindigkeit:** Was vorher Stunden dauert, läuft in Sekunden
- **Skalierbarkeit:** 10× mehr Vorgänge ohne mehr Personal
- **Mitarbeiterzufriedenheit:** Niemand will 8h/Woche Copy-Paste machen
- **AI-Readiness:** Grundlage für weitere AI-Projekte — nächster Wrapper wird günstiger (Shared Code)

---

## Anhang: Checkliste für Machbarkeitsanalyse (30 Min Discovery Call)

1. Welches SaaS-Tool soll gewrapped werden?
2. Hat es eine öffentliche API? (Wir prüfen vorab)
3. Welche 5 Aktionen sind am wichtigsten?
4. Wie viele Stunden/Woche werden aktuell manuell aufgewendet?
5. Wird bereits ein AI-Agent/Automatisierungstool genutzt?
6. Wer ist der technische Ansprechpartner?
7. Budget-Range?
8. Zeitdruck? (ASAP vs. nächstes Quartal)

→ Innerhalb von 48h: Machbarkeitsbewertung + Angebot mit Festpreis.

---

*Erstellt von Syrax 🩵 — Design & Architecture Lead, Drachenfamilie*
*WorkflowAudit by United DigiArt Vision*
