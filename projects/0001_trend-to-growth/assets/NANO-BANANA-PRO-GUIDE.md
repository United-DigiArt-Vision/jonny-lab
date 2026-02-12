# Nano Banana Pro - Complete Professional Guide

**Quelle:** Google AI Studio / Guillaume Vernade, Gemini Developer Advocate
**Gespeichert:** 2026-02-02
**Status:** MEMORIZED ✅

---

## 🌟 Kernkonzept

Nano Banana Pro ist ein **"Thinking" Model** - es versteht Intent, Physik und Komposition.
**NICHT** mehr "tag soup" (dog, park, 4k, realistic) - sondern **wie ein Creative Director kommunizieren!**

---

## 🏆 THE GOLDEN RULES OF PROMPTING

### Rule 1: Edit, Don't Regenerate
Wenn das Bild zu 80% stimmt → **nicht neu generieren**, sondern anpassen!
```
"That looks great, but adjust the lighting to golden hour sunset and make the headline text neon blue."
```

### Rule 2: Natural Language Communication
Komplette Sätze, proper grammar, vivid descriptions.

❌ **FALSCH:** "Cool car, neon, city, night, 8k"
✅ **RICHTIG:** "A cinematic wide-angle shot of a sleek futuristic sports car racing through rain-slicked Tokyo streets at midnight. Vibrant neon signage reflects off the wet asphalt and the car's polished metallic body."

### Rule 3: Embrace Specificity and Detail
Vage = generisch. Definiere ALLES: Subject, Environment, Lighting, Emotional Tone.

❌ "a woman"
✅ "an elegant elderly woman wearing a vintage Chanel-inspired tweed suit with pearl accessories"

**Material-Beschreibungen:** "matte ceramic finish", "brushed aluminum", "crushed velvet", "weathered parchment paper"

### Rule 4: Provide Context and Purpose
Das Model VERSTEHT Kontext und trifft dann smarte Entscheidungen.
```
"Create an appetizing photograph of an artisan sandwich for a premium Brazilian gourmet cookbook."
```
→ Model inferiert automatisch: Professional food styling, shallow depth of field, studio-quality lighting

---

## 📝 TEXT RENDERING & INFOGRAPHICS

### Best Practices
- **Information Compression:** "compress" oder "synthesize" dense documents
- **Style Direction:** "polished editorial magazine layout", "technical engineering diagram", "casual hand-drawn whiteboard sketch"
- **Text in Quotes:** Exakten Text IMMER in Anführungszeichen!

### Beispiel-Prompts

**Financial Report:**
```
"Generate a clean, contemporary infographic summarizing the key financial highlights from this quarterly earnings report. Include data visualizations for 'Revenue Growth' and 'Net Income', and feature the CEO's key statement in an elegant pull-quote design element."
```

**Educational Whiteboard:**
```
"Illustrate the concept of 'Transformer Neural Network Architecture' as a hand-sketched whiteboard diagram suitable for a graduate-level lecture. Use distinct colored markers for Encoder and Decoder components."
```

---

## 👤 CHARACTER CONSISTENCY (WICHTIG für DenkWende!)

### Best Practices
- **Identity Preservation:** "Maintain the person's facial features exactly as shown in Image 1."
- **Expression Variation:** Emotionen ändern, aber Identität konsistent halten
- **Composite Thumbnails:** Subjects + Graphics + Text in einem Generation Pass

### Viral Thumbnail Prompt Template
```
"Design an attention-grabbing video thumbnail using the person from Image 1.

Face Consistency: Preserve the person's facial features exactly as Image 1, but change their expression to excited and surprised.

Pose: Position the person on the left side, pointing enthusiastically toward the right side of the frame.

Subject: On the right side, place [SUBJECT].

Graphics: Add a bold yellow arrow connecting the person's pointing finger to the [SUBJECT].

Text: Overlay large, pop-style text in the center: '[TEXT]' Use thick white outline with drop shadow.

Background: Softly blurred, bright [SETTING]. High saturation and contrast."
```

### Multi-Character Story (für Video-Serien)
```
"Create an entertaining 10-part visual story featuring these 3 characters on [ADVENTURE]. The narrative should include exciting moments, emotional highs and lows, culminating in a heartwarming finale. Maintain consistent appearance and attire for all characters throughout, while varying expressions, poses, and camera angles."
```

---

## 🔍 GROUNDING WITH GOOGLE SEARCH

Das Model kann **real-time Google Search Daten** nutzen für aktuelle/faktische Informationen!

### Beispiel
```
"Generate an informative infographic showing the optimal times to visit major U.S. National Parks in 2025, based on current travel trends and seasonal considerations."
```

---

## 🎨 ADVANCED EDITING

### Semantic Instructions (kein manuelles Masking!)
```
"Remove all tourists from the background of this landmark photo. Fill the empty spaces with contextually appropriate textures."
```

### Localization/Adaption
```
"Adapt this London bus stop advertisement concept for a Tokyo setting. Translate the tagline into natural Japanese, transform the background into bustling Shibuya intersection at night."
```

### Seasonal/Lighting Transformation
```
"Transform this summer scene into deep winter. Preserve the exact architectural details, but add realistic snow accumulation. Shift the lighting to evoke a cold, overcast late afternoon."
```

---

## 🔄 DIMENSIONAL TRANSLATION (2D ↔ 3D)

### Floor Plan to Interior Design
```
"Based on this uploaded 2D floor plan, generate a professional interior design presentation board.

Layout: Create a collage featuring one large hero image at the top (wide-angle perspective of the main living area), with three smaller images below.

Style: Apply a Modern Minimalist aesthetic with warm oak wood flooring and soft off-white walls.

Quality: Photorealistic rendering with soft, natural window lighting."
```

### Meme to 3D
```
"Transform the classic 'This is Fine' dog meme into a photorealistic 3D render. Maintain the exact original composition, but render the dog as a plush toy with realistic fabric texture."
```

---

## 📐 HIGH-RESOLUTION & TEXTURES

### Best Practices
- **Explicit Resolution:** Request "2K" or "4K" when needed
- **Texture Descriptions:** Include imperfections, surface variations, material properties

### 4K Prompt Example
```
"Harness native high-fidelity output to create a breathtaking, atmospheric environment of a mossy forest floor after rainfall. Render complex dappled lighting effects and delicate organic textures, ensuring pixel-perfect clarity suitable for 4K desktop wallpaper."
```

---

## 🧠 THINKING & REASONING MODE

Das Model generiert **intermediate conceptual images** (nicht berechnet) bevor es das finale Bild erstellt.

### Analytical Reasoning
```
"Analyze this photograph of a finished room and generate a 'before' image showing what this space likely looked like during construction—exposed framing, unfinished drywall, visible electrical rough-ins."
```

---

## 🎬 ONE-SHOT STORYBOARDING

### Luxury Brand Campaign (9-Part)
```
"Create a captivating 9-part visual narrative featuring [CHARACTERS] in [SCENARIO].

Story Arc: Include emotional peaks and valleys throughout, culminating in an elegant closing shot.

Consistency Requirements: Identities, facial features, and attire must remain absolutely consistent throughout all 9 images.

Visual Variety: Vary camera angles, distances, and expressions across the sequence.

Format: Generate images one at a time. Maintain 16:9 landscape aspect ratio."
```

---

## 📏 STRUCTURAL CONTROL & LAYOUT

### Sketch to Final
```
"Create a polished advertisement for [product] following the exact composition and element placement shown in this rough sketch. Maintain indicated proportions while elevating to professional quality."
```

### Sprite Sheet for Animation
```
"Create a sprite sheet showing a character performing a backflip, arranged in a 3x3 grid. Each cell should represent one frame of the animation sequence in chronological order."
```

---

## 🎯 DenkWende-Spezifische Anwendung

### Unser Character Prompt (LOCKED)
```
Simple minimalist businessman character with round white head (minimal facial features - just dots for eyes and simple line mouth), blue rectangular body suit with orange tie, stick-like arms and legs
```

### Video-Szenen Prompt Template
```
"Flat 2D illustration. [CHARACTER_DESC]. [SCENE_DESCRIPTION]. Isometric style, dark blue background (#1a365d), clean vector art, no gradients, limited color palette (blue, orange, white, [ADDITIONAL_COLORS]). Finance explainer video style. 16:9."
```

### Viral Thumbnail für DenkWende
```
"Design an attention-grabbing YouTube thumbnail.

Character: [DENKWENDE_CHARACTER] with [EXPRESSION] expression.

Layout: Character on left, [SUBJECT] on right.

Text: Bold text '[HEADLINE]' - thick white outline, drop shadow.

Graphics: [ARROW/ICONS] connecting elements.

Background: Dark blue (#1a365d), high contrast.

Style: Flat 2D, clean vector, eye-catching for YouTube. 16:9."
```

---

## ✅ QUICK REFERENCE CHECKLIST

Vor jedem Prompt prüfen:

- [ ] Natural Language (keine Tags)
- [ ] Spezifisch (Subject, Environment, Lighting, Mood)
- [ ] Kontext/Zweck angegeben
- [ ] Text in "Anführungszeichen"
- [ ] Character Description konsistent
- [ ] Resolution angegeben wenn nötig (1K/2K/4K)
- [ ] Aspect Ratio (16:9 für YouTube)
