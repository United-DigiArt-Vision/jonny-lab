# United DigiArt Website – Spezifikationen

**Letzte Aktualisierung:** 2026-02-05

---

## Übersicht

| Eigenschaft | Wert |
|-------------|------|
| **URL** | https://uniteddigiart.com |
| **Repo** | `~/uniteddigiart-main` |
| **Framework** | Next.js 16 |
| **Hosting** | Vercel |
| **Styling** | Tailwind CSS |

---

## Anforderungen

### Mehrsprachigkeit (implementiert 2026-02-05)

**Regel:** ALLE Seiten müssen die ausgewählte Sprache respektieren.

| Anforderung | Status |
|-------------|--------|
| Sprachschalter in Navigation (EN/DE) | ✅ |
| Homepage übersetzt | ✅ |
| Workflow-Audit Seite übersetzt | ✅ |
| About Seite übersetzt | ⏳ TODO |
| Contact Seite übersetzt | ⏳ TODO |
| Impressum übersetzt | ⏳ TODO |

**Technische Umsetzung:**
- `LanguageContext` für globalen Sprachstatus
- `translations.ts` enthält alle Übersetzungen (EN + DE)
- Jede Seite nutzt `useLanguage()` Hook
- Default-Sprache: Englisch

**Struktur in translations.ts:**
```typescript
translations.en.seitenname.key
translations.de.seitenname.key
```

### Design

| Eigenschaft | Wert |
|-------------|------|
| **Hintergrund** | Dunkles Theme (slate-900 bis slate-800) |
| **Primärfarbe** | Teal (#0891b2) |
| **Akzent** | Teal-400 für Highlights |
| **Font** | System UI |

### Seiten

| Route | Beschreibung | Status |
|-------|--------------|--------|
| `/` | Homepage mit Service-Übersicht | ✅ Live |
| `/services/workflow-audit` | Workflow-Audit Detailseite | ✅ Live |
| `/about` | Über uns | ✅ Live |
| `/contact` | Kontakt | ✅ Live |
| `/impressum` | Rechtliches (Pflicht) | ✅ Live |

---

## Workflow-Audit Service

| Eigenschaft | EN | DE |
|-------------|----|----|
| **Preis** | $149 | 149€ |
| **Lieferzeit** | 48-72 hours | 48-72 Stunden |
| **Payment** | PayPal | PayPal |

**PayPal Link:** `https://www.paypal.com/ncp/payment/UFKF67L5SLXVS`

**Verkaufsargumente:**
- ✓ Keine Calls, keine Meetings
- ✓ 100% Automatisiert
- ✓ Detaillierter PDF-Report
- ✓ ROI-Schätzungen
- ✓ Tool-Empfehlungen
- ✓ Umsetzungs-Roadmap

---

## Deployment

**Befehl:**
```bash
cd ~/uniteddigiart-main && npx vercel --prod --yes
```

**Nach Änderungen:**
1. Code ändern
2. Lokal testen (optional): `npm run dev`
3. Deployen mit obigem Befehl
4. Vercel baut automatisch und deployed auf uniteddigiart.com

---

## Entscheidungen & Regeln

| Datum | Entscheidung |
|-------|--------------|
| 2026-02-05 | Default-Sprache ist Englisch (internationaler Markt) |
| 2026-02-05 | Sprachschalter muss ALLE Seiten beeinflussen |
| 2026-02-05 | Neue Seiten MÜSSEN `useLanguage()` nutzen |
| 2026-02-05 | Übersetzungen immer in `translations.ts` hinzufügen |

---

## TODO

- [ ] About-Seite übersetzen
- [ ] Contact-Seite übersetzen
- [ ] Impressum übersetzen
- [ ] Meta-Tags/SEO für beide Sprachen
- [ ] Analytics einbinden
