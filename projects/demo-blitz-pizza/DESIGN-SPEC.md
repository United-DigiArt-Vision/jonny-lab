# Design-Spezifikation: Blitz Pizza Heilsbronn

**Erstellt von:** Syrax 🩵 — Die Architektin
**Datum:** 2026-02-13
**Referenz:** PRD.md

---

## 1. Seitenstruktur (Single Page App)

```
┌─────────────────────────────────┐
│  NAVBAR (fixed top)             │
│  Logo + Nav-Links + 🛒 Badge   │
├─────────────────────────────────┤
│  HERO Section                   │
│  Titel, Tagline, CTA-Button    │
├─────────────────────────────────┤
│  INFO Section                   │
│  Öffnungszeiten, Adresse, Tel  │
│  Google Maps Embed (Platzhalter)│
├─────────────────────────────────┤
│  MENU Section                   │
│  Kategorie-Tabs (horizontal    │
│  scrollbar auf Mobile)          │
│  Menükarten-Grid                │
├─────────────────────────────────┤
│  CART Sidebar / Overlay         │
│  Warenkorbinhalt + Summe        │
│  → Checkout Button              │
├─────────────────────────────────┤
│  CHECKOUT Modal                 │
│  Formular + Zahlungsmethode     │
│  → Bestätigung                  │
├─────────────────────────────────┤
│  FOOTER                         │
│  Impressum, Kontakt, Social     │
└─────────────────────────────────┘
```

### Navigation (Smooth Scroll)
- **Desktop:** Horizontal navbar: `Startseite | Speisekarte | Kontakt | 🛒 (Badge mit Anzahl)`
- **Mobile:** Hamburger-Menü (☰) + Sticky Cart-Icon unten rechts

### Section IDs
- `#hero`, `#info`, `#menu`, `#contact`, `#footer`
- Cart: `#cart-sidebar` (Desktop slide-in rechts) / `#cart-overlay` (Mobile fullscreen)
- Checkout: `#checkout-modal` (Modal overlay)
- Bestätigung: `#confirmation-modal`

---

## 2. Farbschema

| Rolle | Farbe | Hex |
|-------|-------|-----|
| Primary (Rot) | Pizzeria-Rot | `#D32F2F` |
| Primary Dark | Dunkelrot | `#B71C1C` |
| Secondary (Gold) | Warm Gold | `#FFB300` |
| Secondary Light | Helles Gold | `#FFD54F` |
| Accent (Orange) | Warmes Orange | `#FF6D00` |
| Background | Fast-Schwarz | `#1A1A2E` |
| Surface | Dunkles Blau-Grau | `#16213E` |
| Card BG | Dunkel-Surface | `#0F3460` |
| Text Primary | Weiß | `#FFFFFF` |
| Text Secondary | Helles Grau | `#B0BEC5` |
| Success | Grün | `#4CAF50` |
| Error | Helles Rot | `#EF5350` |

### Gradient
- Hero-Overlay: `linear-gradient(135deg, #1A1A2E 0%, #16213E 50%, #0F3460 100%)`
- CTA-Buttons: `linear-gradient(135deg, #D32F2F, #FF6D00)`
- Kategorie-Tab aktiv: `#D32F2F` mit `box-shadow: 0 4px 15px rgba(211, 47, 47, 0.4)`

---

## 3. Typografie

| Element | Font | Größe | Gewicht |
|---------|------|-------|---------|
| H1 (Hero) | `'Poppins', sans-serif` | 3.5rem (Desktop) / 2.2rem (Mobile) | 800 |
| H2 (Sections) | `'Poppins', sans-serif` | 2rem / 1.5rem | 700 |
| H3 (Kartentitel) | `'Poppins', sans-serif` | 1.1rem | 600 |
| Body | `'Inter', sans-serif` | 1rem (16px) | 400 |
| Preis | `'Poppins', sans-serif` | 1.2rem | 700 |
| Small/Label | `'Inter', sans-serif` | 0.85rem | 400 |
| Nav | `'Poppins', sans-serif` | 0.95rem | 500 |

**Font-Loading:** Google Fonts CDN (Poppins 600-800, Inter 400-500). Fallback: system sans-serif.

---

## 4. Komponenten

### 4.1 Navbar
- Fixed top, `backdrop-filter: blur(10px)`, `background: rgba(26, 26, 46, 0.9)`
- Logo: "⚡ Der neue Blitz" — ⚡ in `#FFB300`, Text in weiß
- Cart-Icon: 🛒 mit rotem Badge (Anzahl Artikel), pulsiert bei Änderung
- Höhe: 64px (Desktop), 56px (Mobile)

### 4.2 Hero Section
- Höhe: `100vh` (Desktop), `80vh` (Mobile)
- Zentral: Großer Titel "Der neue Blitz ⚡"
- Tagline: "Pizza • Pasta • Burger • Indisch — Lieferung & Abholung"
- CTA-Button: "Jetzt bestellen →" → scrollt zu `#menu`
- Hintergrund: Dark Gradient + dezente animierte 🍕-Emojis (floating)
- Food-Emoji-Ring: große Emojis 🍕🍔🥗🍝🍛 kreisförmig animiert

### 4.3 Info Section
- 3-Spalten Grid (Desktop) / Stack (Mobile)
- Karte 1: 📍 Adresse + Maps-Platzhalter (grauer Kasten mit Pin-Icon)
- Karte 2: 🕐 Öffnungszeiten (Tabelle Mo-So)
- Karte 3: 📞 Telefon + Bestell-Link
- Cards mit `border-radius: 16px`, leichter `box-shadow`

### 4.4 Menü-Bereich

#### Kategorie-Tabs
- Horizontal scrollbar (Mobile)
- Pill-Shape Buttons: inaktiv = `#16213E` border, aktiv = `#D32F2F` filled
- Kategorien: Angebote, Pizza, Pasta, Burger, Salate, Fleisch, Indisch, Fingerfood, Desserts, Getränke
- Icons als Prefix: 🎁 🍕 🍝 🍔 🥗 🥩 🍛 🍗 🍰 🥤

#### Menükarte (einzelnes Gericht)
```
┌────────────────────────────┐
│  🍕  (großes Emoji)        │
│  Margherita                │
│  Tomaten, Mozzarella, ...  │
│  ─────────────────────     │
│  5,50 €       [+ Warenkorb]│
└────────────────────────────┘
```
- Card: `background: #16213E`, `border-radius: 12px`
- Emoji: 3rem, zentriert oben
- Name: H3, weiß
- Beschreibung: `#B0BEC5`, max 2 Zeilen (text-overflow: ellipsis)
- Preis: `#FFB300`, fett, links
- Button: `+` Kreis-Button, `#D32F2F`, rechts unten
- Hover: `transform: translateY(-4px)`, `box-shadow` verstärkt

#### Grid-Layout
- Desktop: `grid-template-columns: repeat(auto-fill, minmax(260px, 1fr))`
- Tablet: 2 Spalten
- Mobile: 1 Spalte (volle Breite, kompakteres Layout)

### 4.5 Warenkorb (Cart)

#### Desktop: Slide-in Sidebar
- Rechts, 380px breit, `position: fixed`
- Slide-in Animation von rechts
- Schließen-X oben rechts

#### Mobile: Bottom Sheet / Fullscreen
- Von unten hochgleitend, volle Breite
- Sticky Header + Sticky Footer (Summe + Checkout)

#### Cart-Item
```
🍕 Margherita        5,50 €
   [−]  2  [+]      11,00 €
   [🗑️ Entfernen]
```
- Minus/Plus Buttons: kleine Kreise
- Menge: zwischen den Buttons
- Einzelpreis + Gesamtpreis
- Entfernen: Textlink rot
- Trennlinie zwischen Items

#### Cart-Footer (sticky)
- Zwischensumme
- Liefergebühr: "Kostenlos" (Demo)
- **Gesamt: fett, groß, `#FFB300`**
- "Zur Kasse →" Button (volle Breite, gradient)

### 4.6 Checkout Modal
- Fullscreen-Overlay mit zentriertem Card (max 500px)
- Backdrop: `rgba(0,0,0,0.7)` mit blur

#### Formular-Felder
1. Name (text, required)
2. Straße + Hausnummer (text, required)
3. PLZ + Ort (text, required)
4. Telefon (tel, required)
5. Anmerkungen (textarea, optional)

#### Zahlungsmethoden (visuell)
- 3 große Radio-Cards nebeneinander:
  - 💵 Barzahlung
  - 🅿️ PayPal
  - 💳 Kreditkarte
- Aktiv: Gold-Border (`#FFB300`)

#### Bestellzusammenfassung
- Kompakte Liste aller Items
- Gesamtsumme prominent

#### Submit
- "Bestellung absenden ⚡" Button
- Validation: alle required Felder + mindestens 1 Zahlungsmethode

### 4.7 Bestätigungs-Modal
- Großes ✅ animiert (scale bounce)
- "Vielen Dank für deine Bestellung!"
- Bestellnummer: zufällig generiert (`BLZ-XXXXX`)
- Zusammenfassung: Items, Adresse, Zahlungsmethode, Gesamtbetrag
- "Geschätzte Lieferzeit: 30-45 Min"
- "Neue Bestellung" Button → Reset

---

## 5. Responsive Breakpoints

| Name | Breakpoint | Layout |
|------|-----------|--------|
| Mobile S | < 375px | 1 Spalte, kompakt |
| Mobile | 375px - 767px | 1 Spalte, Standard |
| Tablet | 768px - 1023px | 2 Spalten Menü |
| Desktop | 1024px - 1439px | 3-4 Spalten Menü, Sidebar-Cart |
| Desktop L | ≥ 1440px | max-width Container 1200px, zentriert |

### Mobile-Specific
- Navbar: Hamburger-Menü, 56px Höhe
- Hero: 80vh, kleinere Schrift
- Menü-Tabs: horizontal scroll mit Fade-Edge
- Menükarten: volle Breite, horizontal Layout (Emoji links, Text rechts)
- Cart: Bottom-Sheet statt Sidebar
- Checkout: Fullscreen statt Modal
- Sticky "🛒 Warenkorb (3)" Button unten rechts (FAB-Style)

---

## 6. Animations & Transitions

| Element | Animation | Dauer | Easing |
|---------|-----------|-------|--------|
| Navbar-Scroll | Background opacity 0→0.9 | 300ms | ease |
| Hero-Emojis | Floating/Rotating | 6-10s | infinite linear |
| Menükarte Hover | translateY(-4px) + shadow | 200ms | ease-out |
| Kategorie-Tab Switch | Inhalt fade+slide | 300ms | ease-in-out |
| Cart öffnen | slideInRight / slideUp | 350ms | cubic-bezier(0.4,0,0.2,1) |
| Cart schließen | slideOutRight / slideDown | 250ms | ease-in |
| Cart-Badge Pulse | scale(1.3) + zurück | 300ms | ease |
| Checkout Modal | fadeIn + scaleUp(0.9→1) | 300ms | ease-out |
| Bestätigung ✅ | scale bounce (0→1.2→1) | 500ms | spring |
| Button Hover | brightness(1.1) + scale(1.02) | 150ms | ease |
| Add-to-Cart | Kurzes Fliegen-Emoji zum Cart-Icon | 400ms | ease-in |
| Smooth Scroll | Zu Section | — | `scroll-behavior: smooth` |
| Menü-Filter | Items fade-out → rearrange → fade-in | 300ms | ease |

---

## 7. Datenstruktur (JS-Objekt Schema)

```javascript
const MENU_DATA = {
  categories: [
    {
      id: "angebote",         // String, unique, für Tab-ID
      name: "Angebote & Menüs", // Anzeigename
      icon: "🎁",             // Emoji-Icon für Tab
      items: [
        {
          id: "ang-1",        // String, unique global
          name: "Family Box",
          desc: "2 große Pizzen + 1 Familiensalat + 1,5L Getränk",
          price: 24.90,       // Number, in Euro
          emoji: "🎉",        // Platzhalter-Bild
          tags: ["family", "deal"],  // Optional: für spätere Filter
          popular: true       // Optional: für Highlight
        }
        // ...
      ]
    },
    {
      id: "pizza",
      name: "Pizza",
      icon: "🍕",
      items: [
        {
          id: "piz-1",
          name: "Margherita",
          desc: "Tomatensoße, Mozzarella, Oregano",
          price: 5.50,
          emoji: "🍕",
          tags: ["vegetarisch"],
          popular: true
        }
        // ... ~35 Sorten
      ]
    }
    // ... weitere Kategorien: pasta, burger, salate, fleisch, indisch, fingerfood, desserts, getraenke
  ]
};

// Warenkorb-State
const cart = {
  items: [
    // { menuItemId: "piz-1", quantity: 2 }
  ],
  
  // Methoden
  addItem(id) {},
  removeItem(id) {},
  updateQuantity(id, qty) {},
  getTotal() {},      // Returns Number
  getItemCount() {},  // Returns Number
  clear() {}
};

// Checkout-Daten
const orderData = {
  customer: {
    name: "",           // String, required
    street: "",         // String, required
    zipCity: "",        // String, required
    phone: "",          // String, required
    notes: ""           // String, optional
  },
  payment: "",          // "cash" | "paypal" | "creditcard"
  items: [],            // Kopie von cart.items mit aufgelösten Preisen
  total: 0,             // Number
  orderNumber: "",      // "BLZ-XXXXX"
  timestamp: ""         // ISO-String
};
```

### Preis-Formatierung
- Immer: `price.toFixed(2).replace('.', ',') + ' €'` → "5,50 €"
- Tausender-Trennzeichen nicht nötig (Beträge < 1000€)

### Kategorie-IDs (fest)
`angebote`, `pizza`, `pasta`, `burger`, `salate`, `fleisch`, `indisch`, `fingerfood`, `desserts`, `getraenke`

---

## 8. Datei-Struktur

**Eine einzige HTML-Datei:** `index.html`

```
index.html
├── <style> (eingebettetes CSS, ~500-800 Zeilen)
├── <body>
│   ├── nav#navbar
│   ├── section#hero
│   ├── section#info
│   ├── section#menu
│   ├── aside#cart-sidebar
│   ├── div#checkout-modal
│   ├── div#confirmation-modal
│   └── footer#footer
└── <script> (eingebettetes JS, ~400-600 Zeilen)
    ├── MENU_DATA (Daten-Objekt)
    ├── Cart-Logik
    ├── Rendering-Funktionen
    ├── Event-Handler
    └── Navigation/Scroll
```

---

*Syrax 🩵 — Bauplan steht. Caraxes kann schmieden.*
