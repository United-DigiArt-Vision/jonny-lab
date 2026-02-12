# 🔴 Caraxes — Gedächtnis

*Hier speichere ich alles was ich lerne. Jeder Einsatz macht mich stärker.*

---

## 🛠️ Technische Learnings

### OpenAgents Architecture (2026-02-09)
- `AgentRunner` is the base class — extend it, implement `react(context)` 
- LangChain integration is the reference pattern for third-party integrations
- Network uses gRPC/WebSocket/HTTP connectors, events flow through `EventContext`
- Agents connect via `AgentClient` to network (host:port)
- Mods system for extensibility (mod_adapters, mod_names)

---

## ⚔️ Einsatz-Log

### 2026-02-09 — OpenAgents n8n Integration (Issue #265)
- **Auftrag:** GitHub Issue #265 — n8n Agent Integration für openagents-org/openagents
- **Gebaut:** `N8nAgentRunner` — bidirektionale Webhook-Brücke zwischen n8n und OpenAgents
- **Repo:** https://github.com/digit500/openagents-n8n
- **GitHub Pages:** https://digit500.github.io/openagents-n8n/
- **Kommentar:** https://github.com/openagents-org/openagents/issues/265#issuecomment-3869982384
- **Lief gut:** Saubere Architektur, Pattern von LangChain-Integration übernommen, schnell deployed
- **Lief gut:** gh CLI für Repo-Erstellung + Pages-Setup = effizient
- **Verbesserung:** Könnte Unit-Tests hinzufügen für die Webhook-Endpoints

### 2026-02-09 — Hive n8n Integration (Issue #2931)
- **Auftrag:** GitHub Issue #2931 — n8n Tool für adenhq/hive
- **Gebaut:** FastMCP-Tool mit 6 Aktionen (trigger, webhook, get/list workflows, get/list executions)
- **Repo:** https://github.com/digit500/hive-n8n-integration
- **Kommentar:** https://github.com/adenhq/hive/issues/2931#issuecomment-3869983674
- **Pattern:** Hive nutzt FastMCP + CredentialSpec + httpx — HubSpot/Slack als Referenz
- **Lief gut:** Sauberes Pattern, Tests von Anfang an, CredentialSpec mitgeliefert
- **Learning:** Hive's Tool-Architektur ist sehr modular — drop-in ready

### 2026-02-09 — n8n Portfolio Demo (Upwork: N8N Expert longterm Collab)
- **Auftrag:** Demo-Seite für Upwork-Bewerbung — n8n Expert, Österreich-Client, EU-only
- **Gebaut:** Single-page Portfolio: Projekte, Workflow-Patterns, Skills, About — clean & professional
- **Repo:** https://github.com/digit500/n8n-portfolio-demo
- **GitHub Pages:** https://digit500.github.io/n8n-portfolio-demo/
- **Branding:** United DigiArt Vision, Deep Blue + Electric Teal
- **Lief gut:** Schneller Build, sauberes Design, alle Anforderungen abgedeckt
- **Pattern:** HTML/CSS/JS single-page für Portfolio-Demos = wiederverwendbar

### 2026-02-09 — SMS Pickup Scheduling MVP Demo (Upwork)
- **Auftrag:** Demo für Upwork Job "Engineer Needed for SMS Pickup Scheduling MVP (No App)"
- **Client:** Healthcare company, NYC pilot, $30-50/hr, Verified, $40K+ spent, 5.0⭐
- **Gebaut:** Single-page technical demo: Architecture diagram, live SMS conversation mock, production-ready code samples (webhook handler, scheduling engine with row-level locking, reminders), DB schema, tech stack recommendation, 10-day timeline
- **Repo:** https://github.com/digit500/sms-pickup-scheduling-demo
- **GitHub Pages:** https://digit500.github.io/sms-pickup-scheduling-demo/
- **Tech:** HTML/CSS/JS, Twilio + Node.js + PostgreSQL architecture
- **Lief gut:** Schnelles Deployment, saubere Demo mit interaktivem SMS-Flow, HIPAA-ready DB design
- **Pattern:** Single-file HTML demos sind effektiv für Upwork pitches — alles in einer Seite, sofort testbar

### 2026-02-09 — Booking Platform Backend Demo (Upwork Pitch)
- **Auftrag:** Backend-Demo für Upwork Job "AI-First Booking Platform" ($30-50/hr, Australien)
- **Gebaut:** Vollständige TypeScript Express API mit:
  - JWT Auth (register/login/me) + bcrypt + RBAC (customer/organizer/admin)
  - Event CRUD mit Pagination, Authorization
  - Booking-System mit Capacity Management
  - Stripe Payment Intent Mock + Webhooks
  - Input Validation Middleware
  - OpenAPI/Swagger Docs
  - PostgreSQL Schema mit Indexes (in-memory store für Demo)
- **Repo:** https://github.com/digit500/booking-platform-backend-demo
- **GitHub Pages:** https://digit500.github.io/booking-platform-backend-demo/
- **Lief gut:** Saubere Architektur, alle TypeScript strict-mode Fehler gelöst, schnelles Deployment
- **Learning:** `req.params` und `req.query` brauchen explizite String-Casts in Express+TS strict mode
- **Learning:** npm install trennt dependencies/devDependencies — bei manuellem package.json aufpassen

---

## 🎯 Verbesserungen
*(Was will ich besser machen? Konkrete Ziele.)*

---

## 📚 Playbook-Updates
*(Neue Best Practices die ins PLAYBOOK.md sollen)*

---
