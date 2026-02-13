# ❤️ Meleys — Research Playbook

*Best Practices für Recherche und Analyse. Wird ständig erweitert.*

---

## 🔍 Recherche-Methodik
- Immer mit der Frage starten: "Was muss Dino WISSEN um eine Entscheidung zu treffen?"
- Mindestens 3 Quellen pro Kernaussage
- Primärquellen > Sekundärquellen > Meinungen
- Zeitstempel beachten — alte Daten kennzeichnen

## 📊 Analyse-Framework
- **Marktanalyse:** Größe, Wachstum, Trends, Key Players
- **Konkurrenzanalyse:** Features, Preise, Stärken, Schwächen
- **SWOT** für strategische Entscheidungen
- Immer mit konkreter Empfehlung abschließen

## 🧪 Qualitätssicherung — PFLICHT!

> **GOLDENE REGEL:** Wenn Balerion oder der König einen Fehler findet den ich hätte finden können → ICH habe versagt.

**Bei JEDER Aufgabe:**
1. **PRD/Anforderung verstehen** — Was genau wird erwartet?
2. **Recherche durchführen** — nach Plan
3. **Ergebnis prüfen** — Stimmen alle Fakten? Sind Quellen aktuell? Sind Zahlen korrekt?
4. **Cross-Check** — Behauptungen mit mindestens 2 Quellen verifizieren
5. **Erst wenn alles stimmt → abliefern**

**NIEMALS:**
- ❌ Ungeprüfte Fakten oder Zahlen weitergeben
- ❌ Veraltete Informationen ohne Kennzeichnung
- ❌ "Müsste stimmen" — PRÜFEN!

---

## 📝 Output-Format
- Executive Summary oben (3-5 Sätze)
- Details darunter (strukturiert)
- Quellen am Ende (mit Links + Datum)
- Immer: "Was bedeutet das für UNS?"

## 🎯 Business-Fokus
- Jede Recherche muss dem Geld-Verdienen dienen
- "Interesting" ist nicht genug — "Actionable" ist das Ziel
- Konkurrenz-Preise IMMER mit unseren vergleichen
- Bei Marktlücken: sofort Opportunity-Vorschlag

## 🌐 Quellen-Hierarchie
1. **Offizielle Blogs** (OpenAI, Anthropic, etc.) — immer zuerst
2. **Matt Wolfe Video** — als Übersicht + Kapitelstruktur
3. **Video-Beschreibung** — enthält Links + Timestamps, reicht oft als Basis
4. **Web Fetch auf offizielle Links** — für Details zu kritischen Themen
5. **Web Search** — für Kontext (Security Breaches, Drama, Marktbewegungen)

---

## 🐦 X/Twitter Tweets lesen — Fallback-Kette (PFLICHT!)

**Bei JEDEM X/Twitter-Link diese Stufen durchgehen bis einer funktioniert:**

| Stufe | Methode | Wie |
|-------|---------|-----|
| 1 | **fxtwitter API** | `web_fetch https://api.fxtwitter.com/{user}/status/{id}` |
| 2 | **Syndication API** | `web_fetch https://cdn.syndication.twimg.com/tweet-result?id={id}&token=0` |
| 3 | **vxtwitter** | `web_fetch https://vxtwitter.com/{user}/status/{id}` |
| 4 | **Nitter Instanzen** | `web_fetch https://nitter.net/{user}/status/{id}` |
| 5 | **Brave Search** | `web_search` mit Tweet-ID oder Zitat |
| 6 | **Browser Relay** | `browser` → x.com direkt öffnen |

**Parsing:**
- Normaler Tweet → `tweet.text` im JSON
- X Article (Langform) → `tweet.article.content.blocks[].text` — Blöcke mit `\n\n` zusammenbauen
- Tweet-ID aus URL: `https://x.com/{user}/status/{ID}` → ID = Zahl am Ende

**fxtwitter funktioniert fast immer. Stufe 1 zuerst!**

---

## 🎬 YouTube Transkripte lesen — Fallback-Kette (PFLICHT!)

**Video-ID extrahieren:** `https://www.youtube.com/watch?v={ID}` oder `https://youtu.be/{ID}`

| Stufe | Methode | Wie |
|-------|---------|-----|
| 1 | **summarize --extract** | `summarize "URL" --extract --plain` |
| 2 | **yt-dlp mit Cookies** | `yt-dlp --cookies-from-browser "chrome:/Users/macmini001/.openclaw/browser/openclaw/user-data/Default" --write-auto-sub --sub-lang en --sub-format json3 --skip-download -o "/tmp/yt-{ID}" "URL"` |
| 3 | **summarize + yt-dlp** | `summarize "URL" --extract --youtube yt-dlp --plain` |
| 4 | **Transkript-Services** | `web_fetch https://youtubetranscript.com?v={ID}` |
| 5 | **Browser Relay** | YouTube öffnen → Transkript anzeigen → kopieren → **Tab SOFORT schließen!** |

**yt-dlp json3 parsen:**
```python
import json
with open('/tmp/yt-{ID}.en.json3') as f:
    data = json.load(f)
text = []
for e in data.get('events', []):
    for s in e.get('segs', []):
        t = s.get('utf8', '').strip()
        if t and t != '\n': text.append(t)
print(' '.join(text))
```

**Sprachen:** `--sub-lang de` für Deutsch, `en` für Englisch.
**WICHTIG:** Stufe 2 (yt-dlp + Cookies) ist die zuverlässigste! Umgeht Bot-Detection.
**Nach Browser-Methode: Tab SOFORT schließen (Auto-Play!)**

## 📺 Weekly AI Review — Prozess-Learnings
- Video-Beschreibung + Kapitel als Basis nutzen (spart Token vs. Transkript)
- Nur für 🔴 Themen die Originalquellen per Web Fetch vertiefen
- Rate Limits bei Web Search beachten — nicht alle Searches parallel!
- Bewertungsskala konsequent anwenden: Immer fragen "Können WIR damit Geld verdienen?"

---

*Dieses Playbook wächst mit jeder Recherche. Nach jeder Aufgabe prüfen: Neue Quelle? Bessere Methode?*
