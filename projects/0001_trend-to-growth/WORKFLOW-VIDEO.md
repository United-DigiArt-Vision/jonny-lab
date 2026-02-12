# DenkWende Video-Produktions-Workflow

**Stand:** 2026-02-02
**Learnings aus:** Video 001 (KI-Blase) Testproduktion

---

## 🎯 Übersicht

Ein DenkWende-Video besteht aus:
1. **Skript** (Hook → Problem → Perspektive → Schritte → Framework → CTA)
2. **Bilder** (Nano Banana Pro, 1 pro Abschnitt)
3. **Audio** (ElevenLabs, Dino's geklonte Stimme)
4. **Video** (ffmpeg, Ken-Burns-Effekt)

---

## 📝 Phase 1: Skript

### Struktur (8-12 Minuten)
```
1. HOOK (0:00-0:30)
   - Provokante These
   - "95% machen X falsch"
   
2. INTRO (0:30-1:00)
   - Was kommt im Video
   - 3 Punkte ankündigen
   
3. KONTEXT (1:00-2:30)
   - Was passiert gerade?
   - Fakten, Zahlen
   
4. PROBLEM (2:30-4:00)
   - Falsche Reaktionen zeigen
   - Panik vs FOMO
   
5. PERSPEKTIVWECHSEL (4:00-5:30)
   - Die richtige Frage
   - Mindset-Shift
   
6. SCHRITTE (5:30-8:00)
   - 3 konkrete Actionables
   - Mit Beispielen
   
7. FRAMEWORK (8:00-9:00)
   - Einfache Merkregel
   - "Der X-Test"
   
8. CTA (9:00-9:30)
   - Like, Abo, Kommentar
   - Konkrete Frage stellen
```

### Ton & Sprache
- Direkt, du-Form
- Keine Füllwörter ("eigentlich", "quasi")
- Klare Aussagen, keine Hedge-Sprache
- Beispiele mit konkreten Zahlen

---

## 🎨 Phase 2: Bilder (Nano Banana Pro)

### Setup
```bash
export GEMINI_API_KEY="..."
nano-banana-pro generate --prompt "..." --out image.png
```

### Style-Vorgaben
- **Stil:** Digitale Editorial-Illustration
- **Farben:** Kräftige, satte Töne (kein Pastell)
- **Komposition:** Zentrale Figur/Objekt, klarer Fokus
- **Text:** KEINEN Text in Bildern (wird per Overlay hinzugefügt)
- **Auflösung:** Mindestens 1920x1080, besser größer

### Prompt-Pattern
```
Create a [STYLE] illustration showing [SUBJECT].
[MOOD/ATMOSPHERE]. [COMPOSITION DETAILS].
No text, no watermarks. High quality, professional.
```

### Anzahl Bilder
- 1 Bild pro Skript-Abschnitt
- Typisch: 8-12 Bilder pro Video
- Lieber zu viele als zu wenige

---

## 🔊 Phase 3: Audio (ElevenLabs)

### Setup
```bash
export ELEVENLABS_API_KEY="..."
```

### Voice ID
- Dino's geklonte Stimme: `0yq6Q8iERSIPFQbwEZmE`

### Generierung
```bash
# Für lange Texte in Chunks aufteilen (<5000 Zeichen)
sag speak -v "0yq6Q8iERSIPFQbwEZmE" \
  --model-id "eleven_flash_v2_5" \
  -f script-part1.txt \
  -o part1.mp3

# Chunks zusammenfügen
ffmpeg -f concat -safe 0 -i concat.txt -c copy full-voiceover.mp3
```

### ⚠️ WICHTIG
- Audio nur EINMAL generieren
- Bei Video-Iterationen: Audio wiederverwenden!
- ElevenLabs-Tokens sparen

---

## 🎬 Phase 4: Video (ffmpeg)

### Methode: Einzelne Clips → Concat

**Schritt 1: Bild → Clip (mit Ken-Burns)**
```bash
ffmpeg -y -loop 1 -i image.png \
  -c:v libx264 -t [SEKUNDEN] -pix_fmt yuv420p \
  -vf "scale=1920:1080:force_original_aspect_ratio=decrease,\
       pad=1920:1080:(ow-iw)/2:(oh-ih)/2,\
       zoompan=z='min(zoom+0.0008,1.2)':d=[FRAMES]:s=1920x1080:fps=25" \
  clip.mp4
```

**Schritt 2: Clips zusammenfügen**
```bash
# concat.txt erstellen
echo "file 'clip01.mp4'" > concat.txt
echo "file 'clip02.mp4'" >> concat.txt
# ...

ffmpeg -f concat -safe 0 -i concat.txt -c copy video-only.mp4
```

**Schritt 3: Audio hinzufügen**
```bash
ffmpeg -y -i video-only.mp4 -i audio.mp3 \
  -c:v copy -c:a aac -b:a 192k -shortest \
  final-video.mp4
```

### Timing-Berechnung
- 25 fps = 25 Frames pro Sekunde
- Für X Sekunden: d = X * 25 Frames

### ⚠️ NICHT TUN
- Alle Bilder in einem komplexen ffmpeg-Befehl (Bug-anfällig)
- Ken-Burns mit zu schnellem Zoom (0.001+ ist zu viel)

---

## 📤 Phase 5: Export & Komprimierung

### Volle Qualität (für YouTube)
- Format: MP4, H.264
- Auflösung: 1920x1080
- Audio: AAC, 192kbps

### Preview für Discord (<16MB)
```bash
ffmpeg -y -i full-video.mp4 \
  -c:v libx264 -preset fast -crf 32 \
  -c:a aac -b:a 96k \
  -vf "scale=854:480" \
  preview.mp4
```

---

## 📁 Ordnerstruktur

```
projects/0001_trend-to-growth/
├── NOTES.md
├── WORKFLOW-VIDEO.md (diese Datei)
├── assets/
│   ├── DENKWENDE-STYLE.md
│   └── NANO-BANANA-PRO-GUIDE.md
└── output/
    └── video-001-ki-blase/
        ├── SKRIPT.md
        ├── images-v2/
        │   ├── 01-hook.png
        │   ├── 02-tech-giants.png
        │   └── ...
        ├── audio/
        │   ├── chunk01.mp3
        │   ├── chunk02.mp3
        │   └── full-voiceover.mp3
        ├── clips/
        │   ├── 01.mp4
        │   ├── 02.mp4
        │   └── ...
        └── final/
            ├── denkwende-001-ki-blase-v2.mp4 (full)
            └── denkwende-001-v2-preview.mp4 (Discord)
```

---

## ✅ Checkliste

- [ ] Skript geschrieben (Hook → CTA)
- [ ] Skript in Abschnitte aufgeteilt
- [ ] Bild-Prompts für jeden Abschnitt
- [ ] Bilder generiert (Nano Banana Pro)
- [ ] Bilder überprüft (keine Text, gute Qualität)
- [ ] Audio generiert (ElevenLabs)
- [ ] Audio-Länge geprüft
- [ ] Timing für Bilder berechnet
- [ ] Video-Clips erstellt
- [ ] Clips zusammengefügt
- [ ] Audio hinzugefügt
- [ ] Preview komprimiert
- [ ] Zur Review an Dino

---

## 🔄 Iteration

Bei Änderungen:
1. **Nur Skript?** → Neues Audio + Video
2. **Nur Bilder?** → Neues Video (Audio wiederverwenden!)
3. **Nur Timing?** → Neues Video (Audio wiederverwenden!)
4. **Audio-Fehler?** → Nur betroffenen Chunk neu generieren
