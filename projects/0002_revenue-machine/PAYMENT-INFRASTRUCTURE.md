# Payment & Business Infrastructure

## 🎯 Was wir brauchen

1. **Geld empfangen** – Wie zahlen Kunden?
2. **Rechnungen ausstellen** – Professionell & rechtskonform
3. **Steuern** – Alles korrekt für's Finanzamt
4. **Buchhaltung** – Überblick behalten

---

## 1. Payment Processing

### Option A: Lemonsqueezy (EMPFOHLEN für Start)
**Was:** Merchant of Record – sie handeln als Verkäufer
**Vorteile:**
- Übernimmt EU-VAT komplett
- Du brauchst keine eigene USt-IdNr
- Einfaches Setup
- Checkout-Pages inklusive
- Auszahlung auf dein Konto

**Kosten:** 5% + €0.50 pro Transaktion
**Bei €299 Service:** ~€15.45 Gebühr → €283.55 für dich

**Perfekt für:** Schnell starten ohne Bürokratie

### Option B: Stripe
**Was:** Payment Processor
**Vorteile:**
- Professionell
- Günstigere Gebühren (1.4% + €0.25 EU)
- Mehr Kontrolle

**Nachteile:**
- Du bist Verkäufer (VAT-Pflichten)
- Braucht Gewerbeanmeldung
- Mehr Setup

**Bei €299 Service:** ~€4.44 Gebühr → €294.56 für dich

### Option C: PayPal
**Was:** Einfachste Option
**Vorteile:**
- Jeder kennt es
- Sofort einsatzbereit

**Nachteile:**
- Teuer (2.49% + €0.35)
- Nicht so professionell
- Käuferschutz-Risiko

---

## 2. Rechnungen (Deutschland)

### Pflichtangaben auf deutschen Rechnungen:
- Vollständiger Name & Adresse (Verkäufer)
- Vollständiger Name & Adresse (Käufer)
- Steuernummer ODER USt-IdNr
- Rechnungsdatum
- Fortlaufende Rechnungsnummer
- Menge & Art der Leistung
- Zeitpunkt der Leistung
- Nettobetrag
- Steuersatz & Steuerbetrag (oder Kleinunternehmer-Hinweis)
- Bruttobetrag

### Kleinunternehmerregelung (§19 UStG)
**Wenn Umsatz < €22.000/Jahr:**
- Keine Umsatzsteuer ausweisen
- Hinweis auf Rechnung: "Gemäß §19 UStG wird keine Umsatzsteuer berechnet."
- Einfachere Buchhaltung

### Tools für Rechnungen:
1. **Lexoffice** – €7.90/Monat, sehr gut für DE
2. **SevDesk** – Ab €8.90/Monat
3. **Debitoor/SumUp** – Ab €7/Monat
4. **Wave** – Kostenlos (aber nicht DE-optimiert)

---

## 3. Business Setup (Deutschland)

### Brauchst du:
- [ ] **Gewerbeanmeldung** – Beim Gewerbeamt, ~€20-30
- [ ] **Steuernummer** – Kommt automatisch nach Gewerbeanmeldung
- [ ] **Geschäftskonto** – Empfohlen (nicht Pflicht bei Einzelunternehmen)

### Kleinunternehmer vs. Regelbesteuerung:
| | Kleinunternehmer | Regelbesteuerung |
|---|---|---|
| Umsatzgrenze | < €22.000/Jahr | Keine |
| USt ausweisen | Nein | Ja (19%) |
| Vorsteuer abziehen | Nein | Ja |
| Aufwand | Gering | Höher |

**Empfehlung:** Start als Kleinunternehmer, später wechseln

---

## 4. Empfohlenes Setup (Schnellstart)

### Sofort (heute):
1. **Lemonsqueezy Account** erstellen
2. **Produkt anlegen** (AI-Workflow-Audit €299)
3. **Checkout-Link** auf Landing Page einbauen

### Diese Woche:
4. **Gewerbeanmeldung** (falls nicht vorhanden)
5. **Lexoffice Testaccount** für Rechnungen

### Später:
6. Zu Stripe wechseln wenn Volumen steigt
7. Steuerberater konsultieren

---

## 5. Action Items

- [ ] Lemonsqueezy Account erstellen
- [ ] Produkt konfigurieren
- [ ] Checkout auf Landing Page verlinken
- [ ] Erste Test-Transaktion
- [ ] Gewerbeanmeldung klären (Dino)

---

## Fragen an Dino

1. Hast du bereits ein Gewerbe angemeldet?
2. Hast du eine Steuernummer?
3. Welches Bankkonto für Einnahmen?
4. Sollen wir mit Lemonsqueezy starten (einfach) oder direkt Stripe (günstiger)?
