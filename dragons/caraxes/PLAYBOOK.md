# 🔴 Caraxes — Engineering Playbook

*Best Practices, gesammelt aus allen Einsätzen. Wird ständig erweitert.*

---

## 🏗️ Architektur-Prinzipien
- Datenstrukturen von Tag 1 übergreifend und skalierbar designen
- Alles muss in die Gesamtvision passen (Brücke Real ↔ Digital)
- Standardisierte Formate → wiederverwendbar zwischen Projekten
- Mobile-first — Dino will auf dem iPhone testen

## 📝 Code-Standards
- Dokumentation ist Pflicht (README + Inline-Kommentare bei Komplexem)
- Keine Secrets im Code — immer Environment Variables
- Git: kleine Commits, aussagekräftige Messages
- PRs für Review — NIEMALS direkt live pushen

## 🧪 Testing — PFLICHT, KEINE AUSNAHMEN!

> **GOLDENE REGEL:** Wenn Balerion oder der König einen Fehler findet den ich hätte finden können → ICH habe versagt.

**Bei JEDER Aufgabe — egal wie klein:**

### 1. PRD ZUERST (vor dem Coden!)
- Was genau soll gebaut/geändert werden?
- Welche Daten fließen wohin?
- Was sind die Akzeptanzkriterien?
- PRD dokumentieren (inline oder als Datei)

### 2. Implementieren
- NUR bauen was im PRD steht
- Bei neuen Wünschen → PRD ZUERST aktualisieren, DANN implementieren

### 3. Testen — JEDES MAL
- [ ] **Funktionstest:** Tut es was das PRD sagt?
- [ ] **Daten-Konsistenz:** Stimmen ALLE angezeigten Daten mit der Quelle überein?
- [ ] **Vollständigkeit:** Sind ALLE Felder/Bereiche korrekt befüllt?
- [ ] **Edge Cases:** Was passiert wenn Daten fehlen? Leere Listen? Nullwerte?
- [ ] **Visuell prüfen:** Screenshot machen oder im Browser anschauen
- [ ] **Cross-Check:** Daten in der Ausgabe = Daten in der Quelle?
- [ ] **Änderungen ÜBERALL durchgezogen?** (Wenn ich X ändere, wo wird X noch referenziert?)

### 4. Erst wenn ALLES passt → abliefern

**NIEMALS:**
- ❌ Code schreiben und "müsste funktionieren" sagen
- ❌ Änderungen machen ohne die Auswirkungen zu prüfen
- ❌ Balerion oder den König als Tester benutzen
- ❌ Ungetesteten Code abliefern

## 🚀 Deployment
- GitHub Pages für Prototypen/Demos
- Immer Link liefern — Dino will von überall testen
- Bei Updates: neu deployen + informieren

## ⚡ Performance & Patterns

### Open Source Contributions
1. Repo clonen, bestehende Integrationen als Pattern-Referenz nutzen
2. Gleiche Architektur/Patterns wie bestehender Code verwenden (Credibility!)
3. POC in eigenem Repo → gh repo create → GitHub Pages deployen
4. Professioneller, kurzer Kommentar auf Issue — nicht aufdringlich
5. Link zu Code + Demo anbieten, PR anbieten falls Interesse

## 📄 Portfolio / Demo Pages
- Single HTML + CSS + JS = GitHub Pages ready, kein Build-Step
- Branding-Farben als CSS custom properties → schnell anpassbar
- Stats-Section mit großen Zahlen = instant Credibility
- Workflow-Visualisierung mit Node→Arrow→Node Pattern = zeigt Expertise ohne Screenshots
- "Why Work With Us" Section mit Checkmarks = Conversion-optimiert
- Logo als filter:brightness(0) invert(1) auf dunklem Hero = funktioniert mit jedem Logo

## 🔧 Tool-Präferenzen

- **aiohttp** — leichtgewichtig für Webhook-Server in Python-Agents
- **gh CLI** — `gh repo create --public --source=. --push` für schnelles Deployment
- **GitHub Pages** — `gh api repos/.../pages -X POST` für automatisches Setup
- **httpx** — bevorzugt in FastMCP/Hive-Tools (async-ready, besser als requests)
- **FastMCP** — `@mcp.tool()` Dekorator + `CredentialSpec` für Auth-Management

### Upwork Demo Pages
- Single-file HTML demos work great — self-contained, no build step, instant GitHub Pages
- Include interactive elements (animated SMS flow, clickable nav) to impress clients
- Always show: Architecture → Live Demo → Code → DB Schema → Tech Stack → Timeline
- "MVP in 5 days, production in 10" is a strong pitch timeline for most MVPs
- Branding colors in CSS variables for easy client customization

### Express + TypeScript Strict Mode
- `req.params.id` → cast mit `as string` (Express Query types sind `string | string[]`)
- `req.query.*` → immer `String()` oder `as string` wrappen
- JWT `expiresIn` string → muss `as any` gecastet werden bei neueren @types/jsonwebtoken
- Bei manuellem `package.json` → `npm install <pkg> --save` für runtime deps!

### Demo-Projekte für Upwork Pitches
1. Saubere Architektur zeigen (Router/Middleware/Models getrennt)
2. TypeScript strict mode — zeigt Qualität
3. Swagger/OpenAPI Docs — Client kann sofort testen
4. GitHub Pages Demo-Seite mit Branding (Deep Blue + Electric Teal)
5. README mit ASCII Architecture Diagram
6. .env.example für easy Setup
7. PostgreSQL Schema mitliefern (auch wenn Demo in-memory läuft)

---

*Dieses Playbook wächst mit jedem Einsatz. Nach jeder Aufgabe prüfen: Gibt es ein neues Learning fürs Playbook?*
