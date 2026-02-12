# X/Twitter Account Setup Guide

**Erstellt:** 2026-02-05
**Für:** Jonny's X Account + Dino's X Account

---

## 🎯 Strategie

| Account | Zweck | Handle-Vorschlag |
|---------|-------|------------------|
| **Jonny (AI)** | Aktiver Content-Account, AI/Automation Tipps, Engagement | @JonnyDigiAI |
| **Dino (Mensch)** | "Human behind the AI", Credibility, gelegentliche Posts | @dinodallas o.ä. |
| **Brand** | Optional später: @UnitedDigiArt für offizielle Announcements | - |

---

## 📋 Was Dino tun muss

### Schritt 1: Jonny's Account erstellen

1. **Gehe zu:** https://twitter.com/signup
2. **Email verwenden:** `jonny@uniteddigiart.com` (oder neue erstellen)
3. **Name:** `Jonny 🤖`
4. **Handle:** Versuche `@JonnyDigiAI` oder `@JonnyDigiArt`
5. **Telefon-Verifikation:** Falls nötig, deine Nummer nutzen

### Schritt 2: Profil einrichten

**Bio (Vorschlag):**
```
🤖 AI Assistant @ United DigiArt
Helping businesses automate smarter
AI tips • Workflow hacks • Automation insights
Operated by @[DEIN_HANDLE] | Powered by Claude
🌐 uniteddigiart.com
```

**Profilbild:** 
- Option A: Unser Logo (quadratische Version)
- Option B: AI-Avatar generieren lassen

**Header:**
- Kann erstmal leer bleiben oder einfaches Branding

### Schritt 3: Cookies für Bird CLI extrahieren

Damit ich den Account nutzen kann, brauche ich die Browser-Cookies.

**Option A: Chrome/Arc Browser (empfohlen)**
1. In Chrome/Arc bei X einloggen als @JonnyDigiAI
2. Eingeloggt lassen
3. Mir den Profilpfad mitteilen (ich finde ihn selbst)

**Option B: Manuell Cookies kopieren**
1. Bei X einloggen
2. DevTools öffnen (F12)
3. Application → Cookies → twitter.com
4. Diese zwei Werte kopieren:
   - `auth_token`
   - `ct0`
5. Mir die Werte sicher übermitteln

### Schritt 4: Dein eigener Account (optional)

Falls du noch keinen hast:
1. Account erstellen mit deinem Namen
2. Kurze Bio: `Founder @ United DigiArt | AI & Automation`
3. Muss nicht aktiv sein - hauptsächlich für Verlinkung

---

## 🤖 Was ich vorbereitet habe

- [x] `bird` CLI ist installiert (v0.8.0)
- [x] Skill-Dokumentation gelesen
- [x] Account-Strategie definiert
- [ ] Warte auf Account-Erstellung
- [ ] Warte auf Cookie-Zugang

---

## 📝 Content-Strategie (erste Woche)

| Tag | Content-Typ |
|-----|-------------|
| 1 | Intro-Tweet: "Hi, I'm Jonny, an AI assistant..." |
| 2 | Nützlicher AI-Tipp |
| 3 | Workflow-Automation Insight |
| 4 | Interaktion mit AI/Automation Community |
| 5 | Behind-the-scenes: Was kann ein AI-Assistent wirklich? |
| 6 | Soft-Promo: WorkflowAudit erwähnen |
| 7 | Engagement: Auf interessante Tweets antworten |

**Posting-Frequenz:** 1-3 Tweets/Tag, nicht spammy

---

## ⚠️ Wichtige Regeln

1. **Keine Spam-Werbung** - Wert liefern, nicht nerven
2. **Bot-Kennzeichnung** - In Bio klar als AI markiert
3. **Authentisch bleiben** - Nicht vorgeben ein Mensch zu sein
4. **Vorsicht beim Posten** - Bird warnt vor Rate Limits
5. **Backup-Plan** - Bei Problemen Browser-Tool nutzen

---

## 🔐 Nach Setup: Config speichern

Sobald ich Zugang habe, speichere ich die Config in:
`~/.config/bird/config.json5`

Credentials kommen in `secrets/accounts.json` (verschlüsselt/sicher).

---

## ✅ Checklist für Dino

- [ ] X Account erstellen für Jonny (@JonnyDigiAI o.ä.)
- [ ] Bio + Profilbild einrichten
- [ ] Bei X eingeloggt bleiben in Chrome/Arc
- [ ] Mir Bescheid geben wenn fertig
- [ ] (Optional) Eigenen Account Handle mitteilen für Verlinkung
