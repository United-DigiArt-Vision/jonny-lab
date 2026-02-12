# Projekt 0001 – Chronologische Notizen

## 2026-02-01

### Initiale Besprechung (ca. 14:58 - 15:42)

**Dino's Idee:**
- YouTube-Channel in Motivational/Personal-Growth-Nische
- Kombiniert mit aktuellen Trends (Wirtschaft, KI, Finanzen, Tech, Krypto, Politik)
- Schnelle Video-Produktion bei Trend-Themen
- Struktur: Was passiert → Falsche Reaktionen → Wie man es nutzt

**Meine Analyse:**
- Starke Idee: Trend-Speed + Evergreen-Growth = guter Hebel
- 3 Risiken identifiziert:
  1. "Zu breit" → klare Identität nötig
  2. "News-Vorlesen" → anti-news Struktur
  3. Quellen/Fehler → Research-Protokoll

**Vereinbart:**
- Sprache: Deutsch
- Trend-Cron: Mo-Fr 07:00, kurze DM
- Faceless, Clean & Modern
- 8-12 Minuten + Shorts

**Production Pipeline besprochen:**
- Bilder: Nano Banana Pro
- VoiceOver: ElevenLabs
- Schnitt: ffmpeg (Ken Burns, Zoom/Pan, Overlays)

**Offene Actions:**
- Brave API Key einrichten (Dino)
- Nano Banana Pro recherchieren (Jonny) → erledigt
- ElevenLabs Infos kommen später
- Brand-Name, Du/Sie, erste 3 Themen noch offen

### Nano Banana Pro Recherche (21:13)

**Was ist Nano Banana Pro?**
- Web-basiertes AI Text-to-Image Tool
- URL: https://nanobanana.pro
- Features:
  - Context-aware Image Generation
  - Character Consistency (wichtig für uns!)
  - Region-Specific Editing
  - Style Reference Blending
  - Iterative Refinement

**Pricing:**
- Basic: $9.90/Monat = 1000 Credits
- Höhere Pläne verfügbar
- Credit Packs als Add-on

**API-Situation:**
- Keine öffentliche API-Dokumentation gefunden
- Scheint primär Web-Interface zu sein
- → Browser-Automation nötig für automatisierten Zugang

**Für Video-Pipeline relevant:**
- ✅ Character Consistency (gleiche Charaktere über Szenen)
- ✅ Style Reference (konsistenter visueller Stil)
- ✅ Studio-Level Output Qualität
- ⚠️ Kein direkter API-Zugang

### Projekt-Struktur eingerichtet (21:06)

- Neue Namenskonvention: `XXXX_projektname` (fortlaufende ID)
- Projekt 0001 angelegt, umbenannt zu `0001_trend-to-growth`
- Standard-Struktur: README.md, NOTES.md, research/, assets/, output/

### Erste Trend-Recherche (21:15)

**Quellen:** Tagesschau Wirtschaft, Handelsblatt Finanzen
(Brave API Key fehlt noch → manuelle Quellen)

**8 Trend-Themen identifiziert:**
1. Fed-Chef Warsh (Trump nominiert, Konfliktpotenzial)
2. Dollar-Absturz & Goldreserven
3. Inflation auf 2,1% (Essen, Restaurant)
4. Bosch: 20.000 Stellen weg
5. KI-Rally: Blase oder Chance?
6. Trump-Zölle 50% auf Flugzeuge
7. Grüner Wasserstoff aus Saudi-Arabien
8. Ver.di Streiks Nahverkehr

**Top 5 für sofortigen Start:**
1. Fed-Chef Warsh (Angst: Geld, Zinsen)
2. Bosch Stellenabbau (Angst: Job, Zukunft)
3. KI-Rally (FOMO vs Fear)
4. Inflation (direkte Betroffenheit)
5. Dollar/Gold (Sicherheit)

→ Vollständige Recherche: `research/trend-recherche-2026-02-01.md`

### Vorbereitungen abgeschlossen (21:21)

**Entscheidungen:**
- Du-Ansprache: ✅ bestätigt
- Ziel: Viral, Engagement, Reichweite, Monetarisierung
- Erstes Video-Thema: KI-Rally (höchstes Viral-Potenzial)

**Erstellt:**
1. ✅ Style Guide (`assets/STYLE-GUIDE.md`)
   - Farben: Deep Black + Electric Blue + Warning Orange
   - Stil: Clean & Modern, cinematic
   - Tonalität: Direkt, Anti-Mainstream, fundiert

2. ✅ Skript-Template (`assets/SKRIPT-TEMPLATE.md`)
   - Standardstruktur für alle Videos
   - Timing-Vorgaben
   - Hook-Formeln, CTA-Formeln

3. ✅ Erstes Skript: Video 001 KI-Blase (`output/video-001-ki-blase/SKRIPT.md`)
   - Vollständiges ~10 Min Skript
   - 11 Bild-Prompts für Nano Banana
   - 4 Short-Konzepte
   - Titel & Thumbnail Konzepte

4. ✅ ffmpeg Pipeline (`assets/FFMPEG-PIPELINE.md`)
   - Ken Burns Effekte
   - Audio-Mixing
   - Shorts-Erstellung
   - Workflow-Script

**Offene Punkte:**
- [x] ~~Channel-Name~~ → **DenkWende** ✓
- [ ] Nano Banana Pro Account
- [ ] ElevenLabs API Key
- [ ] Brave API Key

### Channel-Name bestätigt (21:30)
- Name: **DenkWende**
- Kanban erstellt: `KANBAN.md`
- Alle bisherigen Aktivitäten dokumentiert

---

## 2026-02-02

### Video 001 Produktion (22:00-23:00)

**Durchgeführt:**
1. ✅ 11 Bilder generiert mit Nano Banana Pro
2. ✅ Audio generiert mit ElevenLabs (Dino's Stimme)
3. ✅ Video v1 gerendert (hatte Bug: nur 1 Bild geloopt)
4. ✅ Video v2 gerendert mit Fix (alle 11 Bilder korrekt)

**Technische Learnings:**
- ffmpeg concat mit komplexem Filter = Bug-anfällig
- Besser: Einzelne Clips pro Bild → dann concat
- ElevenLabs hat 5000 Zeichen-Limit pro Request → chunken
- Audio einmal generieren, bei Iterationen wiederverwenden!

**Dateien:**
- Bilder: `output/video-001-ki-blase/images-v2/`
- Audio: `output/video-001-ki-blase/audio/full-voiceover.mp3`
- Video: `output/video-001-ki-blase/final/denkwende-001-ki-blase-v2.mp4`

### Dino's Feedback (23:01)

**Feedback:**
- Video hatte nur 1 Bild (Bug) → gefixt in v2
- Das ist eine **Testphase** → Workflow definieren, nicht Content produzieren
- Erst wenn Qualität stimmt → echtes Video zu aktuellem Thema

**Wichtige Anweisung:**
- Audio nicht neu generieren bei Iterationen (ElevenLabs-Tokens sparen!)

### Nacht-Session (23:05+)

**Erstellt:**
1. ✅ `WORKFLOW-VIDEO.md` - Kompletter Video-Produktions-Guide
2. ✅ `output/video-002-wachstumsmotoren/SKRIPT-OUTLINE.md` - Outline für Video 002
3. ✅ `IDEAS-AUTOMATION.md` - Ideen für Tools & Automatisierungen
4. ✅ `CONTENT-IDEAS.md` - 13+ Content-Ideen mit Prioritäten

**Zur Review für Dino (morgen früh):**
- [ ] Video 001 v2 (Preview auf Discord geschickt)
- [ ] Video 002 Skript-Outline
- [ ] Content-Ideen-Liste
- [ ] Automatisierungs-Ideen
