# ffmpeg Video-Pipeline – Trend to Growth

**Zweck:** Automatisiertes Zusammenbauen von Videos aus Bildern + VoiceOver

---

## Übersicht

```
Bilder (Nano Banana)
       ↓
Ken Burns Animation (ffmpeg)
       ↓
+ VoiceOver (ElevenLabs)
       ↓
+ Text-Overlays
       ↓
+ Musik/SFX (optional)
       ↓
= Fertiges Video (1080p/4K)
```

---

## 1. Bilder vorbereiten

**Input-Format:**
- JPG oder PNG
- Mindestens 1920x1080 (besser: 2560x1440 oder höher für Ken Burns)
- 16:9 Seitenverhältnis
- Benannt: `01_hook.png`, `02_problem.png`, etc.

**Ordnerstruktur pro Video:**
```
output/video-XXX-thema/
├── SKRIPT.md
├── images/
│   ├── 01_hook.png
│   ├── 02_intro.png
│   └── ...
├── audio/
│   ├── voiceover.mp3
│   └── music.mp3 (optional)
├── temp/
│   └── (Zwischendateien)
└── final/
    ├── video-XXX-full.mp4
    └── shorts/
        ├── short-01.mp4
        └── ...
```

---

## 2. Ken Burns Effekt (Zoom/Pan)

**Grundlegendes Kommando:**

```bash
# Langsamer Zoom In (5% über 8 Sekunden)
ffmpeg -loop 1 -i image.png -vf "scale=8000:-1,zoompan=z='min(zoom+0.0005,1.25)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=200:s=1920x1080:fps=25" -t 8 -c:v libx264 -pix_fmt yuv420p output.mp4

# Langsamer Zoom Out
ffmpeg -loop 1 -i image.png -vf "scale=8000:-1,zoompan=z='if(lte(zoom,1.0),1.25,max(1.001,zoom-0.0005))':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=200:s=1920x1080:fps=25" -t 8 -c:v libx264 -pix_fmt yuv420p output.mp4

# Langsamer Pan (links nach rechts)
ffmpeg -loop 1 -i image.png -vf "scale=8000:-1,zoompan=z='1.25':x='if(lte(on,1),0,min(x+2,iw-iw/zoom))':y='ih/2-(ih/zoom/2)':d=200:s=1920x1080:fps=25" -t 8 -c:v libx264 -pix_fmt yuv420p output.mp4
```

**Parameter erklärt:**
- `d=200`: Dauer in Frames (200 Frames bei 25fps = 8 Sekunden)
- `z`: Zoom-Faktor (1.0 = 100%, 1.25 = 125%)
- `s=1920x1080`: Output-Auflösung
- `fps=25`: Framerate

---

## 3. Clips zusammenfügen

**Methode: Concat Demuxer**

1. Erstelle `concat.txt`:
```
file 'clip01.mp4'
file 'clip02.mp4'
file 'clip03.mp4'
```

2. Zusammenfügen:
```bash
ffmpeg -f concat -safe 0 -i concat.txt -c copy output.mp4
```

---

## 4. Audio hinzufügen

**VoiceOver unter Video:**
```bash
ffmpeg -i video.mp4 -i voiceover.mp3 -c:v copy -c:a aac -map 0:v -map 1:a -shortest output.mp4
```

**Mit Hintergrundmusik (leise):**
```bash
ffmpeg -i video.mp4 -i voiceover.mp3 -i music.mp3 \
  -filter_complex "[1:a]volume=1.0[vo];[2:a]volume=0.15[bg];[vo][bg]amix=inputs=2:duration=first" \
  -c:v copy -c:a aac output.mp4
```

---

## 5. Text-Overlays

**Einfacher Text:**
```bash
ffmpeg -i video.mp4 -vf "drawtext=text='KAPITEL 1':fontfile=/path/to/font.ttf:fontsize=48:fontcolor=white:x=(w-text_w)/2:y=h-100:enable='between(t,0,3)'" -c:a copy output.mp4
```

**Mit Box/Hintergrund:**
```bash
ffmpeg -i video.mp4 -vf "drawtext=text='KAPITEL 1':fontfile=/path/to/font.ttf:fontsize=48:fontcolor=white:box=1:boxcolor=black@0.7:boxborderw=10:x=(w-text_w)/2:y=h-100:enable='between(t,0,3)'" -c:a copy output.mp4
```

---

## 6. Progress Bar

**Animierte Progress Bar am unteren Rand:**
```bash
ffmpeg -i video.mp4 -vf "drawbox=x=0:y=ih-10:w='(iw*t/TOTAL_DURATION)':h=10:color=#00D4FF:t=fill" -c:a copy output.mp4
```

Ersetze `TOTAL_DURATION` mit der Gesamtlänge in Sekunden.

---

## 7. Shorts erstellen (9:16)

**Crop für Vertikal:**
```bash
ffmpeg -i video.mp4 -vf "crop=ih*9/16:ih" -c:a copy vertical.mp4
```

**Mit Zoom auf Zentrum:**
```bash
ffmpeg -i video.mp4 -vf "scale=-1:1920,crop=1080:1920" -c:a copy vertical.mp4
```

---

## 8. Untertitel (SRT)

**SRT-Datei einbrennen:**
```bash
ffmpeg -i video.mp4 -vf "subtitles=subtitles.srt:force_style='FontName=Inter,FontSize=24,PrimaryColour=&HFFFFFF,OutlineColour=&H000000,Outline=2'" -c:a copy output.mp4
```

---

## 9. Kompletter Workflow (Beispiel-Script)

```bash
#!/bin/bash

VIDEO_DIR="output/video-001-ki-blase"
IMAGES_DIR="$VIDEO_DIR/images"
AUDIO_DIR="$VIDEO_DIR/audio"
TEMP_DIR="$VIDEO_DIR/temp"
FINAL_DIR="$VIDEO_DIR/final"

mkdir -p "$TEMP_DIR" "$FINAL_DIR"

# 1. Ken Burns für jedes Bild (8 Sekunden pro Bild)
for img in "$IMAGES_DIR"/*.png; do
    name=$(basename "$img" .png)
    ffmpeg -loop 1 -i "$img" \
        -vf "scale=8000:-1,zoompan=z='min(zoom+0.0005,1.25)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=200:s=1920x1080:fps=25" \
        -t 8 -c:v libx264 -pix_fmt yuv420p \
        "$TEMP_DIR/${name}.mp4"
done

# 2. Concat-Liste erstellen
ls "$TEMP_DIR"/*.mp4 | sed "s/^/file '/" | sed "s/$/'/" > "$TEMP_DIR/concat.txt"

# 3. Zusammenfügen
ffmpeg -f concat -safe 0 -i "$TEMP_DIR/concat.txt" -c copy "$TEMP_DIR/video_raw.mp4"

# 4. Audio hinzufügen
ffmpeg -i "$TEMP_DIR/video_raw.mp4" -i "$AUDIO_DIR/voiceover.mp3" \
    -c:v copy -c:a aac -map 0:v -map 1:a -shortest \
    "$FINAL_DIR/video-001-full.mp4"

echo "Done! Output: $FINAL_DIR/video-001-full.mp4"
```

---

## 10. Qualitäts-Einstellungen

**Für YouTube (empfohlen):**
```
-c:v libx264 -preset slow -crf 18 -c:a aac -b:a 192k
```

**Für schnelles Preview:**
```
-c:v libx264 -preset ultrafast -crf 28 -c:a aac -b:a 128k
```

**Für 4K:**
```
-vf "scale=3840:2160" -c:v libx264 -preset slow -crf 18
```

---

## Farben (Hex zu ffmpeg)

| Farbe | Hex | ffmpeg Format |
|-------|-----|---------------|
| Electric Blue | #00D4FF | 0x00D4FF |
| Warning Orange | #FF6B35 | 0xFF6B35 |
| Pure White | #FFFFFF | white |
| Deep Black | #0D0D0D | 0x0D0D0D |

---

## Fonts

Für macOS Inter-Font Pfad:
```
/System/Library/Fonts/Supplemental/Inter-Regular.otf
```

Oder installieren via Homebrew:
```bash
brew install --cask font-inter
```

---

## Troubleshooting

**Fehler: "height not divisible by 2"**
→ Lösung: `-vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2"`

**Audio/Video out of sync**
→ Lösung: Beide neu encoden statt copy: `-c:v libx264 -c:a aac`

**Ken Burns ruckelt**
→ Lösung: Höhere Source-Auflösung verwenden (min. 4K für smooth 1080p Ken Burns)
