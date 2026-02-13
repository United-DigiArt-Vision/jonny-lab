# PRD: Blitz Pizza Heilsbronn — Demo Website

**Zweck:** System-Test unseres Dragon Dev Loop. KEINE echte Kundenarbeit.
**Ziel:** Vollständige, moderne Pizzeria-Website als Single-Page-App (HTML/CSS/JS).

## Geschäftsdaten

| Feld | Wert |
|------|------|
| Name | Der neue Blitz |
| Ort | Nürnberger Straße 2, 91560 Heilsbronn |
| Typ | Pizza-Lieferservice + Abholung |
| Küche | Pizza, Pasta, Burger, Salate, Indisch, Fleischgerichte, Fingerfood |
| Bestellplattform | der-neue-blitz.de (aktuell via Lieferando-artiges System) |

## Anforderungen

### ANF-1: Moderne Landing Page
- Hero-Bereich mit appetitlichem Design
- Öffnungszeiten
- Adresse + Google Maps Einbettung (Platzhalter OK)
- Kontakt (Telefon)
- Responsive Design (Mobile-First!)

### ANF-2: Vollständige Speisekarte
Kategorien (alle aus der echten Karte):
- **Angebote/Menüs** (Family, Party, Single)
- **Pizza** (~35 Sorten, Ø30cm, Preise 5,50€ - 8,00€)
- **Pasta** (~13 Sorten, 8,50€ - 10,00€)
- **Burger & Burger-Menüs** (~15 Optionen, 6,00€ - 14,50€)
- **Salate** (~11 Sorten, 6,00€ - 9,50€)
- **Fleischgerichte** (Schnitzel, Gyros, Cordon Bleu)
- **Indische Gerichte** (~12 Gerichte, Curry, Tikka, etc.)
- **Fingerfood & Beilagen** (Wings, Nuggets, Pommes, etc.)
- **Desserts** (Tiramisu, Viennetta)
- **Getränke** (Cola, Fanta, Säfte, etc.)

Jedes Gericht mit: Name, Beschreibung, Preis (€).
Filter/Tabs nach Kategorie.

### ANF-3: Warenkorb-System
- Gerichte in den Warenkorb legen (+ / - Buttons)
- Warenkorb-Übersicht mit Summe
- Mengenänderung und Entfernen möglich

### ANF-4: Bestell-/Zahlungs-Simulation
- Checkout-Flow (Name, Adresse, Telefon)
- Zahlungsmethoden-Auswahl (visuell): Barzahlung, PayPal, Kreditkarte
- "Bestellung absenden" Button (zeigt Bestätigungs-Modal, keine echte Zahlung)
- Bestellbestätigung mit Zusammenfassung

### ANF-5: Design & UX
- Farbschema: Warme Farben (Rot/Orange/Gold — Pizzeria-typisch)
- Appetitliche Food-Emojis als Platzhalter für Bilder (🍕🍔🥗🍝🍛)
- Smooth Scroll Navigation
- Dark Mode optional
- Animations/Transitions für poliertes Gefühl
- Branding: "Der neue Blitz" mit Blitz-⚡-Element

### ANF-6: Technische Anforderungen
- Single HTML File (mit eingebettetem CSS + JS)
- Pure HTML/CSS/JS — kein Framework, kein npm
- Alle Daten als JS-Objekt im File (keine externe DB)
- Funktioniert offline
- Performant (kein Lag bei 100+ Menüeinträgen)

## Speisekarte-Daten

Komplette Daten sind verfügbar — Caraxes soll sie von der echten Website holen:
https://www.der-neue-blitz.de/

## Akzeptanzkriterien
1. Seite lädt ohne Fehler
2. Alle Kategorien sichtbar und filterbar
3. Mindestens 80 Gerichte korrekt dargestellt mit Preisen
4. Warenkorb funktioniert (hinzufügen, entfernen, Summe)
5. Checkout-Flow komplett durchklickbar
6. Mobile-responsive (iPhone-Größe)
7. Visuell ansprechend (kein "Bootstrap-Standard-Look")
8. Keine JS-Fehler in der Console
