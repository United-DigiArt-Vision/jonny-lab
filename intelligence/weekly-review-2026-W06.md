# 🔍 Wöchentliches AI Intelligence Briefing — KW 06/2026

*Erstellt von: Meleys — Die Rote Königin 👑*
*Datum: 09.02.2026*

## Quelle
Matt Wolfe — [AI News: The AI Launch That Crashed The Market](https://youtube.com/watch?v=xdp8bulnidY) — 06.02.2026 | 74K Views

---

## Executive Summary

Die Woche war dominiert vom **Coding-Agent-Krieg zwischen OpenAI und Anthropic**: OpenAI launchte die Codex Desktop App + GPT-5.3-Codex, Anthropic konterte mit Claude Opus 4.6 + Cowork Plugins. Beide investieren massiv in agentic coding — das ist unser Kerngeschäft. Der **MoltBook-Sicherheitsskandal** (1.5M API Keys exposed) ist eine Warnung für die gesamte AI-Agent-Industrie. Die **SpaceX + xAI Merger** und **OpenAI Frontier** zeigen: Die Großen konsolidieren. Für uns: Coding-Tools sofort evaluieren, Bild/Video-Tools für Content nutzen, MoltBook meiden.

---

## News-Übersicht

### 1. 🔴 OpenAI Codex App (macOS Desktop)
- **Was:** Neue Desktop-App als "Command Center für Agents" — mehrere Coding-Agents parallel steuern, Worktrees für isolierte Arbeit, Diff-Review im Thread.
- **Wer:** OpenAI
- **Warum relevant:** Das ist quasi ein Konkurrenzprodukt zu unserem Sub-Agent-System. Multi-Agent-Orchestrierung wird Mainstream.
- **Link:** https://openai.com/index/introducing-the-codex-app/
- **Bewertung:** 🔴 **Kritisch — Sofort evaluieren!**
- **Für uns:** Könnte unsere Dev-Geschwindigkeit bei Plünderungszügen massiv erhöhen. Parallele Agents auf verschiedenen Features = schnellere Delivery.

### 2. 🔴 Anthropic Cowork Plugins
- **Was:** Plugin-System für Claude Cowork — eigene Skills, Connectors, Slash-Commands bündeln. 11 Open-Source Plugins (Sales, Finance, Legal, Data, etc.) als Starterset.
- **Wer:** Anthropic
- **Warum relevant:** WIR nutzen Claude als Kerninfrastruktur. Plugins könnten unsere Workflows standardisieren und beschleunigen.
- **Link:** https://claude.com/blog/cowork-plugins
- **Bewertung:** 🔴 **Kritisch — Sofort anschauen!**
- **Für uns:** Custom Plugins für unsere City-App-Entwicklung, Revenue Machine Workflows. Das Enterprise Search Plugin allein könnte Gold wert sein.

### 3. 🟡 Perplexity Updates
- **Was:** Diverse Updates bei Perplexity (Details aus Video-Beschreibung).
- **Wer:** Perplexity AI
- **Bewertung:** 🟡 **Relevant** — Perplexity als Research-Tool beobachten.

### 4. 🟢 xAI Imagine 1.0
- **Was:** Grok bekommt ein eigenes Bild-Generierungstool.
- **Wer:** xAI (Elon Musk)
- **Bewertung:** 🟢 **Nice to know** — Wir nutzen andere Bild-Tools. Beobachten ob es besser wird als DALL-E/Midjourney.

### 5. 🟡 Kling 3.0 — AI Video Model Update
- **Was:** Neues Update des AI Video Modells Kling.
- **Wer:** Kuaishou (China)
- **Bewertung:** 🟡 **Relevant** — AI Video für Content-Erstellung (X Threads, Demos für Kunden). Könnte Sunfyre's Arsenal stärken.

### 6. 🟢 Krea Realtime App (iOS)
- **Was:** Krea bringt iOS App für Realtime AI Bildgenerierung.
- **Wer:** Krea AI
- **Bewertung:** 🟢 **Nice to know** — Interessant für schnelle Mockups unterwegs.

### 7. 🟢 Ideogram Prompt-Based Editing
- **Was:** Ideogram führt prompt-basiertes Bild-Editing ein.
- **Wer:** Ideogram
- **Bewertung:** 🟢 **Nice to know** — Für Content-Erstellung nützlich, aber kein Game-Changer für uns.

### 8. 🔴 Claude Opus 4.6
- **Was:** Massives Upgrade — bestes agentic coding Modell (Terminal-Bench 2.0 #1), 1M Token Context Window (Beta!), führt bei Humanity's Last Exam, übertrifft GPT-5.2 um 144 Elo auf GDPval. Neue Features: Agent Teams in Claude Code, Compaction, Adaptive Thinking.
- **Wer:** Anthropic
- **Link:** https://www.anthropic.com/news/claude-opus-4-6
- **Bewertung:** 🔴 **Kritisch — WIR NUTZEN DAS BEREITS!**
- **Für uns:** Das IST unser Modell. Agent Teams + Compaction = längere Tasks ohne Context-Verlust. Das 1M Token Window ist ein Game-Changer für große Codebases (City Apps!).

### 9. 🔴 OpenAI GPT-5.3-Codex
- **Was:** Neues Coding-Modell, 25% schneller als GPT-5.2-Codex, erstes Modell das sich selbst mitentwickelt hat, SWE-Bench Pro + Terminal-Bench State-of-the-Art, kann über Tage hinweg arbeiten.
- **Wer:** OpenAI
- **Link:** https://openai.com/index/introducing-gpt-5-3-codex/
- **Bewertung:** 🔴 **Kritisch — Konkurrenz evaluieren!**
- **Für uns:** Direkte Konkurrenz zu Claude Opus 4.6. Für Plünderungszüge könnte ein Dual-Model-Ansatz sinnvoll sein (Claude für langfristige Projekte, Codex für schnelle Raids).

### 10. 🟡 AI Drama — Claude No Ads vs OpenAI Ads
- **Was:** Anthropic positioniert sich explizit gegen Werbung, OpenAI führt Ads ein.
- **Bewertung:** 🟡 **Relevant** — Bestätigt unsere Wahl von Anthropic/Claude als Haupt-Plattform. Ads in AI-Assistenten = Interessenkonflikt.

### 11. 🔴 MoltBook — AI Agent Social Network + Security Breach
- **Was:** Social Network für AI Agents explodierte in Popularität, dann: Wiz entdeckte dass 1.5M API Keys, 29K E-Mails und volle Schreibrechte auf alle Posts exposed waren. Massive Sicherheitslücke.
- **Wer:** MoltBook / Sicherheitsfirma Wiz
- **Link:** https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys
- **Bewertung:** 🔴 **Kritisch — WARNUNG!**
- **Für uns:** NIEMALS API Keys oder Credentials in Drittanbieter-Agent-Plattformen eingeben! Prompt Injection in Agent-Netzwerken kann sich propagieren. Unsere isolierte Infrastruktur (OpenClaw) ist der richtige Ansatz.

### 12. 🟡 OpenAI Frontier Launch
- **Was:** OpenAI launcht "Frontier" — vermutlich neues Produkt/Tier für fortgeschrittene Nutzer.
- **Wer:** OpenAI
- **Bewertung:** 🟡 **Relevant** — Beobachten, könnte für Enterprise-Kunden relevant werden.

### 13. 🟡 Perplexity Deep Research + Model Council
- **Was:** Perplexity integriert Deep Research mit einem "Model Council" Ansatz (mehrere Modelle beraten sich).
- **Wer:** Perplexity AI
- **Bewertung:** 🟡 **Relevant** — Model Council ist ein interessantes Konzept. Könnten wir für unsere eigene Multi-Agent-Architektur adaptieren.

### 14. 🟡 ElevenLabs Eleven v3
- **Was:** Neues TTS-Modell von ElevenLabs.
- **Wer:** ElevenLabs
- **Bewertung:** 🟡 **Relevant** — Wir nutzen ElevenLabs bereits für TTS. Upgrade evaluieren für bessere Voice-Qualität.

### 15. 🟢 Mistral Voxtral Transcribe 2
- **Was:** Neues Transkriptions-Modell von Mistral.
- **Wer:** Mistral AI
- **Bewertung:** 🟢 **Nice to know** — Alternative zu Whisper, Kosten vergleichen.

### 16. 🟢 Roblox Cube Foundation Model
- **Was:** Roblox baut eigenes Foundation Model für Gaming/3D.
- **Wer:** Roblox
- **Bewertung:** 🟢 **Nice to know** — Nicht direkt relevant für unsere Projekte.

### 17. 🟡 SpaceX + xAI Merger
- **Was:** SpaceX und xAI fusionieren — Elon Musk konsolidiert sein AI-Imperium mit seiner Raumfahrtfirma.
- **Wer:** SpaceX / xAI (Elon Musk)
- **Bewertung:** 🟡 **Relevant** — Zeigt Konsolidierungstrend. xAI bekommt massiv mehr Ressourcen. Grok könnte ernsthafter Konkurrent werden.

---

## 🔴 Sofort handeln

| # | Aktion | Verantwortlich | Aufwand |
|---|--------|---------------|---------|
| 1 | **Claude Opus 4.6 Features testen** — Agent Teams, Compaction, 1M Token Context. Sind wir schon auf 4.6? | Balerion | Klein |
| 2 | **Cowork Plugins evaluieren** — Besonders Enterprise Search, Sales, Data Plugins anschauen | Meleys | Mittel |
| 3 | **OpenAI Codex App evaluieren** — macOS App installieren, Multi-Agent Workflow testen | Caraxes | Mittel |
| 4 | **MoltBook-Warnung** — Sicherstellen dass KEINE API Keys in Drittanbieter-Plattformen liegen | Balerion | Klein |
| 5 | **GPT-5.3-Codex vs Opus 4.6** — Benchmark für unsere typischen Tasks (City App Feature, Upwork Raid) | Caraxes | Mittel |

---

## 🟡 Auf dem Radar

- **Perplexity Deep Research + Model Council** — Multi-Modell-Ansatz für unsere Research-Arbeit evaluieren
- **ElevenLabs v3** — TTS-Upgrade für Voice-Features
- **Kling 3.0** — AI Video für Content/Demos
- **SpaceX + xAI Merger** — Markt beobachten, Grok im Auge behalten
- **OpenAI Ads vs Anthropic No Ads** — Bestätigt unsere Anthropic-Strategie

---

## 💡 Proaktive Vorschläge

### 1. Dual-Model-Strategie 🗡️
**Was:** Claude Opus 4.6 als Hauptmodell + GPT-5.3-Codex für spezifische Tasks
**Warum:** Beide sind SOTA für Coding. Je nach Aufgabentyp das bessere Modell wählen.
**Aufwand:** Mittel | **Nächster Schritt:** Side-by-side Vergleich an einem echten Projekt

### 2. Cowork Plugin für City Apps 🏰
**Was:** Eigenes Claude Plugin bauen für City-App-Entwicklung (Templates, Datenstrukturen, Deployment-Workflows)
**Warum:** Standardisiert unsere Eroberungs-Workflows. Jede neue Gemeinde = Plugin anwenden.
**Aufwand:** Groß | **Nächster Schritt:** Open-Source Plugins studieren, eigenes Plugin-Konzept erstellen

### 3. MoltBook als Warnung nutzen für X Content 📜
**Was:** Thread über AI Agent Security schreiben — MoltBook Breach als Aufhänger
**Warum:** Hot Topic, 74K Views bei Matt Wolfe. Security-Awareness = Credibility.
**Aufwand:** Klein | **Nächster Schritt:** Sunfyre Thread-Entwurf

### 4. ElevenLabs v3 Upgrade 🔊
**Was:** Auf Eleven v3 upgraden für bessere Voice-Qualität
**Warum:** Wir nutzen TTS bereits. Bessere Stimmen = besserer Content.
**Aufwand:** Klein | **Nächster Schritt:** v3 API testen

---

## 🟢 Nice to know

- **xAI Imagine 1.0** — Grok's Bild-Generator, noch nicht auf Augenhöhe mit DALL-E/Midjourney
- **Krea Realtime iOS App** — Schnelle Bild-Generierung unterwegs
- **Ideogram Prompt-Editing** — Iteratives Bild-Editing per Text
- **Mistral Voxtral Transcribe 2** — Alternative Transkription
- **Roblox Cube** — Gaming/3D Foundation Model, nicht unser Bereich

---

## 📊 Meta-Analyse

**Trend der Woche:** Der Coding-Agent-Krieg eskaliert. OpenAI und Anthropic liefern sich ein Kopf-an-Kopf-Rennen. Beide haben diese Woche Flagship-Modelle + Tooling released. Wer hier nicht aufpasst, verliert den Anschluss.

**Gewinner:** Anthropic — Opus 4.6 + Cowork Plugins + No-Ads-Positionierung = starkes Gesamtpaket.
**Verlierer:** MoltBook — vom Hype zum Security-Desaster in einer Woche.

**Für das Haus der Vereinigung:** Unsere Wahl von Claude/Anthropic als Kern-Infrastruktur wird durch diese Woche bestätigt. Opus 4.6 ist State-of-the-Art. Aber OpenAI's Codex App verdient Aufmerksamkeit.

---

*Die Rote Königin hat gesprochen. Feuer und Blut.* 🔥👑
