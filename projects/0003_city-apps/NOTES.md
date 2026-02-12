# City Apps - Laufende Notizen

---

## 2026-02-08 — Erstes Bürgergespräch Poxdorf ⭐

**Teilnehmerin:** Gut vernetzte Bürgerin, lebt ganzes Leben in Poxdorf, stark kirchlich verbunden.

**Kernerkenntnisse:**

1. **"In wessen Auftrag machst du das?"**
   - Bürger erwarten offiziellen Rahmen/Auftraggeber
   - Zeigt: Legitimität ist wichtig für Akzeptanz
   - Gute Antwort vorbereiten für künftige Gespräche

2. **Feature-Wünsche:**
   - ⛪ Kirchliche Veranstaltungen (Gottesdienste, Feste)
   - 🚌 Bushaltestellen / ÖPNV-Info (Fahrpläne, Abdeckung)

3. **"Rede mit den Politikern"**
   - Bestätigt: Gemeinde-Kontakt wird früher oder später nötig
   - Unsere Strategie bleibt: erst Bottom-Up, dann Politik

4. **Testerin gewonnen!** ✅

**Dokumentiert in:** `poxdorf/gespraech-ergebnis-08-02-2026.md`

**Aktionen:**
- [x] Zwei neue Features in Landingpage eingebaut
- [x] PRD aktualisiert (User Stories, Funktionale Anforderungen, Datenmodell, API)
- [x] FEATURES.md erweitert
- [ ] Demo auf GitHub Pages deployen
- [ ] VGN-API Recherche für ÖPNV-Daten

---

## 2026-02-07 — Killer-Feature: Flyer-zu-Event

### Die Idee (Dino)

> "Wenn Flyer gemacht werden oder Poster für eine Veranstaltung — diese sollte einfach per Bild digitalisiert werden können und alle Informationen in die City App direkt eingetragen werden können."

### So funktioniert es:
1. Bürger sieht Flyer/Poster im Ort
2. Fotografiert es mit der App
3. AI extrahiert automatisch:
   - Veranstaltungsname
   - Datum & Uhrzeit
   - Ort
   - Beschreibung
   - Kontakt
4. Event erscheint automatisch in:
   - Kalender
   - News
   - (evtl. mit "Interessiert" Button)

### Warum das ein Gamechanger ist:
- **Jeder Bürger wird Digitalisierungs-Agent** für seine Gemeinde
- **Minimaler Aufwand** — nur ein Foto
- **Social Network Effekt** — Leute teilen, was in ihrer Gemeinde passiert
- **Keine manuelle Datenpflege** für die Kommune nötig
- **Unique Feature** — das hat Heimat-Info NICHT!

### Technische Umsetzung (TODO):
- [ ] Vision API (Google Cloud Vision / OpenAI GPT-4V)
- [ ] Strukturierte Daten-Extraktion
- [ ] Review-Workflow (Moderator bestätigt bevor live)
- [ ] Duplikat-Erkennung

### Zur größeren Vision:
Dieses Feature ist Teil unserer strategischen Vision "Real-World-Digitalisierung" (siehe MEMORY.md).

### Warum wir Facebook schlagen (Dino, 07.02):
- ❌ Facebook: Kein Flyer → Event Feature
- ❌ Facebook: Komplett unübersichtlich geworden
- ❌ Facebook: Keine Push-Erinnerungen für lokale Events
- ❌ Facebook: Schwacher regionaler Fokus
- ✅ Wir: Flyer fotografieren → automatisch Event
- ✅ Wir: Push-Reminder wenn Event startet
- ✅ Wir: Regionales Netzwerk wo Leute sich KENNEN (nicht nur online)
- ✅ Wir: Übersichtlich, fokussiert auf die Gemeinde

---

## 2026-02-06 — Projekt-Start

### Ursprung der Idee (Dino, 06:20 Uhr)

> "Viele Städte und Dörfer hier in Deutschland haben eine ziemlich schlechte App. Gegebenenfalls gar keine App. Meine Idee ist, dass wir für sie Apps entwickeln und verkaufen. Städte Apps sind wichtig und für die Stadt geben ein gutes Bild her."

**Dino's Anforderungen:**
- Müllabfuhr Kalender mit Push-Nachricht Funktion
- Premium-Look wie Dubai
- Nativ (nicht WebView)
- Kein $99/Jahr Apple Developer Fee am Anfang

### Technologie-Entscheidung

**Frage:** "Wenn wir mit Flutter entwickeln, sind das dann native Apps?"

**Antwort:** Ja! Flutter kompiliert zu nativem ARM-Code. Kein WebView, keine Webseite-in-App. Performance wie native, aber eine Codebase für iOS + Android.

### Lösung für Developer Account Problem

Stadt/Gemeinde hat ihren eigenen Apple Developer Account → wir entwickeln, sie publishen unter ihrem Namen.
- Professioneller (App gehört der Stadt)
- Kein Risiko für uns
- $99 zahlt die Stadt (oder wir investieren später)

### Recherche abgeschlossen

**DubaiNow analysiert:**
- 320+ Services von 50+ Behörden
- EINE App für ALLES
- Premium UX/UI
- Goldstandard für Stadt-Apps weltweit

**Deutsche Konkurrenz identifiziert:**
| Anbieter | Modell | Stärke | Schwäche |
|----------|--------|--------|----------|
| Citykey (Telekom) | White-Label | Brand, Standard | Teuer?, wenig flexibel |
| VillageApp | Budget | <€1/Einwohner | Basic Features |
| Smart Village App | Open Source | Flexibel | Braucht Dev-Know-how |

**Marktlücke erkannt:**
- Deutsche Apps sehen "funktional" aus, nicht "wow"
- Premium-Design fehlt
- Wir können Dubai-Level bieten

### Dateien erstellt

- `README.md` — Projektübersicht ✅
- `NOTES.md` — Diese Datei ✅
- `research/market-analysis.md` — Detaillierte Marktanalyse ✅

---

## 🚨 DARF NICHT VERGESSEN WERDEN

*Höchste Priorität — bei jeder Session prüfen!*

- [ ] **Premium-Design wie Dubai** — das ist der USP, nicht vergessen!
- [ ] **Müllkalender + Push** — Kern-Feature, muss perfekt sein
- [ ] **Flutter = Nativ** — keine Kompromisse bei Performance

---

## Offene Fragen (nach Priorität)

**P0 - Muss vor MVP geklärt sein:**
- [ ] Backend-Lösung? (Firebase vs Supabase vs Custom)
- [ ] Welche Features sind "must have" vs "nice to have"?

**P1 - Wichtig für Go-to-Market:**
- [ ] Wie Kommunen ansprechen? (Kaltakquise? Messen? Netzwerk?)
- [ ] Preismodell finalisieren

**P2 - Später klären:**
- [ ] Skalierung bei vielen Kunden
- [ ] White-Label vs Custom pro Stadt

---

## Nächste Session: TODOs

1. ~~**UI/UX Mockups**~~ ✅ DONE (2026-02-06)
2. ~~**Feature-Matrix**~~ ✅ DONE (2026-02-06)
3. **Pitch-Deck** — PowerPoint/PDF für Kommunen
4. **Prototyp** — Flutter App mit Müllkalender-Feature

---

## 2026-02-06 — Mockups & Features erstellt (09:54 Uhr)

### UI Mockups fertig:
- `mockups/home-screen.html` — Home-Screen mit Premium-Design
- `mockups/waste-calendar.html` — Müllkalender mit Push-Erinnerung

### Feature-Set definiert:
- `FEATURES.md` — Basis-Paket, Premium-Module, Preismodell

### Design-Highlights:
- Deep Blue (#1a365d) + Electric Teal (#0891b2)
- Sanfte Farbverläufe
- Großzügige Abstände
- Premium-Schatten
- Dubai-inspiriert aber für deutsche Nutzer

---
