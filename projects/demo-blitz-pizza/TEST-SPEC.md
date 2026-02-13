# Test-Spezifikation: Blitz Pizza Heilsbronn

**Erstellt von:** Syrax 🩵 — Die Architektin
**Datum:** 2026-02-13
**Referenz:** PRD.md, DESIGN-SPEC.md
**Ausführung durch:** Vermithrax 🛡️

---

## Testumgebung

- **Browser:** OpenClaw Browser (Chromium)
- **Methode:** `browser` Tool — navigate, snapshot, screenshot, act
- **Datei:** `projects/demo-blitz-pizza/index.html` (file:// oder localhost)
- **Viewports:** Desktop (1280×800), Mobile (375×812)

## Konventionen

- **PASS** = Erwartung erfüllt
- **FAIL** = Erwartung nicht erfüllt → Details + Screenshot
- Bei FAIL: Screenshot speichern als `projects/demo-blitz-pizza/test-results/FAIL-{TEST-ID}.png`
- Ergebnis-Report: `projects/demo-blitz-pizza/TEST-REPORT.md`

---

## ANF-1: Moderne Landing Page

| Test-ID | Was | Wie | Erwartetes Ergebnis | Traceability |
|---------|-----|-----|---------------------|-------------|
| T-1.1 | Seite lädt fehlerfrei | `browser navigate` zu index.html, dann `browser console` prüfen | Keine JS-Fehler in Console | ANF-1, AK-1, AK-8 |
| T-1.2 | Hero sichtbar | `browser screenshot` Desktop-Viewport | Hero-Section mit "Der neue Blitz", Tagline, CTA-Button sichtbar. Visuell: dunkler Hintergrund, warme Farben, kein Bootstrap-Look | ANF-1, ANF-5, AK-7 |
| T-1.3 | Öffnungszeiten sichtbar | `browser snapshot` → nach "Öffnungszeiten" suchen | Öffnungszeiten-Bereich mit Tagen und Uhrzeiten vorhanden | ANF-1 |
| T-1.4 | Adresse + Maps | `browser snapshot` → nach "Nürnberger Straße 2" suchen | Adresse korrekt angezeigt, Maps-Platzhalter vorhanden | ANF-1 |
| T-1.5 | Kontakt/Telefon | `browser snapshot` → nach Telefonnummer suchen | Telefonnummer sichtbar und klickbar (tel: Link) | ANF-1 |
| T-1.6 | Navbar vorhanden | `browser snapshot` → nav-Element prüfen | Navbar mit Logo "Der neue Blitz" + ⚡ + Nav-Links + Cart-Icon | ANF-1, ANF-5 |
| T-1.7 | Smooth Scroll | `browser act` → auf "Speisekarte" Nav-Link klicken | Seite scrollt smooth zum Menü-Bereich (kein harter Jump) | ANF-5 |
| T-1.8 | Mobile Hero | Viewport auf 375×812 setzen, `browser screenshot` | Hero responsiv, Text lesbar, kein Overflow, CTA-Button sichtbar | ANF-1, AK-6 |

---

## ANF-2: Vollständige Speisekarte

| Test-ID | Was | Wie | Erwartetes Ergebnis | Traceability |
|---------|-----|-----|---------------------|-------------|
| T-2.1 | Alle Kategorien vorhanden | `browser snapshot` im Menü-Bereich → Tabs zählen | Mindestens 10 Kategorie-Tabs: Angebote, Pizza, Pasta, Burger, Salate, Fleisch, Indisch, Fingerfood, Desserts, Getränke | ANF-2, AK-2 |
| T-2.2 | Kategorie-Filter funktioniert | Auf "Pizza"-Tab klicken → `browser snapshot` | Nur Pizza-Gerichte werden angezeigt, andere Kategorien ausgeblendet | ANF-2, AK-2 |
| T-2.3 | Mindestens 80 Gerichte | `browser act evaluate` → `document.querySelectorAll('[data-item-id]').length` oder JS: Gesamtanzahl Items in MENU_DATA zählen | Rückgabewert ≥ 80 | ANF-2, AK-3 |
| T-2.4 | Gericht hat Name+Beschreibung+Preis | `browser snapshot` bei einem Pizza-Eintrag | Jede Karte zeigt: Name, Beschreibungtext, Preis in "X,XX €" Format | ANF-2, AK-3 |
| T-2.5 | Preise korrekt formatiert | `browser act evaluate` → Stichprobe: 5 zufällige Preise prüfen | Preise im Format "X,XX €", keine NaN, keine 0,00 € | ANF-2 |
| T-2.6 | Pizza-Sortiment | `browser act` → Pizza-Tab klicken, `browser snapshot` | ~35 Pizza-Sorten sichtbar, Preise zwischen 5,50€ und 8,00€ | ANF-2 |
| T-2.7 | Visuelles: Menükarten-Design | `browser screenshot` Desktop, Menü-Bereich | Cards mit Emoji, dunklem Hintergrund, Gold-Preisen, rotem +-Button. Kein generischer Look. | ANF-2, ANF-5, AK-7 |
| T-2.8 | Mobile Menü-Tabs | Viewport 375×812, `browser screenshot` Menü-Bereich | Tabs horizontal scrollbar, kein Overflow, kein Umbruch | ANF-2, AK-6 |

---

## ANF-3: Warenkorb-System

| Test-ID | Was | Wie | Erwartetes Ergebnis | Traceability |
|---------|-----|-----|---------------------|-------------|
| T-3.1 | Artikel hinzufügen | `browser act` → "+"-Button bei Margherita klicken | Cart-Badge zeigt "1", Cart enthält Margherita | ANF-3, AK-4 |
| T-3.2 | Mehrere Artikel | "+"-Button bei 3 verschiedenen Gerichten klicken | Cart-Badge zeigt "3", alle 3 Gerichte im Warenkorb | ANF-3, AK-4 |
| T-3.3 | Menge erhöhen | Im Warenkorb: "+"-Button bei einem Artikel klicken | Menge steigt auf 2, Zwischensumme und Gesamtsumme passen sich an | ANF-3, AK-4 |
| T-3.4 | Menge verringern | Im Warenkorb: "−"-Button klicken (Menge war 2) | Menge sinkt auf 1, Summe passt sich an | ANF-3, AK-4 |
| T-3.5 | Artikel entfernen | "−"-Button klicken bei Menge 1 ODER Entfernen-Button | Artikel verschwindet aus Warenkorb, Badge aktualisiert | ANF-3, AK-4 |
| T-3.6 | Summenberechnung | 2× Margherita (5,50€) + 1× Pasta (8,50€) hinzufügen | Gesamtsumme = 19,50 € (korrekt berechnet) | ANF-3, AK-4 |
| T-3.7 | Leerer Warenkorb | Cart öffnen ohne Artikel | Meldung "Dein Warenkorb ist leer" oder ähnlich, kein Checkout-Button | ANF-3 |
| T-3.8 | Cart-Badge Animation | Artikel hinzufügen, `browser screenshot` sofort | Badge pulsiert/animiert bei Änderung | ANF-3, ANF-5 |
| T-3.9 | Visuelles: Cart-Design | `browser screenshot` mit gefülltem Warenkorb | Sidebar/Overlay korrekt dargestellt, Preise lesbar, Buttons erkennbar | ANF-3, ANF-5, AK-7 |
| T-3.10 | Mobile Cart | Viewport 375×812, Cart öffnen, `browser screenshot` | Cart als Bottom-Sheet oder Fullscreen, nicht als schmale Sidebar | ANF-3, AK-6 |

---

## ANF-4: Bestell-/Zahlungs-Simulation

| Test-ID | Was | Wie | Erwartetes Ergebnis | Traceability |
|---------|-----|-----|---------------------|-------------|
| T-4.1 | Checkout öffnen | Artikel im Cart → "Zur Kasse" klicken | Checkout-Modal/Form erscheint mit Feldern: Name, Straße, PLZ/Ort, Telefon | ANF-4, AK-5 |
| T-4.2 | Formular-Validierung | Ohne Felder auszufüllen "Bestellen" klicken | Validierungsfehler, Bestellung wird NICHT abgeschickt | ANF-4 |
| T-4.3 | Zahlungsmethoden sichtbar | `browser screenshot` Checkout-Bereich | 3 Optionen sichtbar: Barzahlung, PayPal, Kreditkarte | ANF-4 |
| T-4.4 | Zahlungsmethode wählen | Auf "PayPal" klicken | PayPal-Option visuell als ausgewählt markiert (Gold-Border o.ä.) | ANF-4 |
| T-4.5 | Kompletter Checkout-Flow | Alle Felder ausfüllen + Zahlungsmethode wählen + "Bestellen" klicken | Bestätigungs-Modal erscheint mit ✅, Bestellnummer (BLZ-XXXXX), Zusammenfassung | ANF-4, AK-5 |
| T-4.6 | Bestätigungsdetails | `browser snapshot` des Bestätigungs-Modals | Enthält: Bestellnummer, bestellte Artikel, Adresse, Zahlungsmethode, Gesamtbetrag | ANF-4 |
| T-4.7 | Neue Bestellung | Im Bestätigungs-Modal "Neue Bestellung" klicken | Cart wird geleert, zurück zur Startseite/Menü | ANF-4 |
| T-4.8 | Visuelles: Checkout-Design | `browser screenshot` ausgefülltes Checkout-Formular | Formular sauber gestylt, Zahlungs-Cards visuell ansprechend, kein Standard-HTML-Look | ANF-4, ANF-5, AK-7 |

### Checkout End-to-End Test (E2E)

**T-4.E2E:** Kompletter Durchlauf:
1. Zur Speisekarte navigieren
2. 2× Pizza Margherita hinzufügen
3. 1× Pasta Carbonara hinzufügen
4. Cart öffnen → Summe prüfen
5. "Zur Kasse" klicken
6. Formular ausfüllen: Name="Max Mustermann", Straße="Teststraße 1", PLZ="91560 Heilsbronn", Tel="0911-123456"
7. Zahlungsmethode: Barzahlung
8. "Bestellung absenden" klicken
9. Bestätigung prüfen: Bestellnummer, korrekte Artikel, korrekter Betrag
10. "Neue Bestellung" → Cart ist leer

**Erwartetes Ergebnis:** Alle Schritte durchlaufen ohne Fehler, korrekte Daten in Bestätigung.

---

## ANF-5: Design & UX

| Test-ID | Was | Wie | Erwartetes Ergebnis | Traceability |
|---------|-----|-----|---------------------|-------------|
| T-5.1 | Farbschema | `browser screenshot` fullpage Desktop | Warme Farben (Rot/Orange/Gold auf dunklem Hintergrund), konsistent | ANF-5, AK-7 |
| T-5.2 | Kein Bootstrap-Look | Visueller Vergleich `browser screenshot` | Eigenes Design erkennbar: Custom Cards, Gradient-Buttons, kein Standard-Framework-Look | ANF-5, AK-7 |
| T-5.3 | Food-Emojis | `browser snapshot` Menükarten | Jede Karte hat ein passendes Emoji als Platzhalter | ANF-5 |
| T-5.4 | Branding ⚡ | `browser snapshot` → nach "⚡" oder "Blitz" suchen | Blitz-Element im Logo/Branding vorhanden | ANF-5 |
| T-5.5 | Animationen vorhanden | Menükarte hovern, Cart öffnen → visuell prüfen | Hover-Effekte auf Cards, Slide-Animation bei Cart, Smooth transitions | ANF-5 |
| T-5.6 | Fullpage Screenshot Desktop | `browser screenshot fullPage=true` bei 1280px | Gesamtseite visuell kohärent, keine gebrochenen Layouts, keine leeren Bereiche | ANF-5, AK-7 |
| T-5.7 | Fullpage Screenshot Mobile | Viewport 375×812, `browser screenshot fullPage=true` | Mobile Layout vollständig, keine horizontalen Scrollbars, Text lesbar | ANF-5, AK-6, AK-7 |

---

## ANF-6: Technische Anforderungen

| Test-ID | Was | Wie | Erwartetes Ergebnis | Traceability |
|---------|-----|-----|---------------------|-------------|
| T-6.1 | Single HTML File | `ls projects/demo-blitz-pizza/index.html` + `wc -l` | Genau 1 HTML-Datei, CSS+JS eingebettet | ANF-6 |
| T-6.2 | Kein Framework | `grep -i "react\|angular\|vue\|bootstrap\|tailwind\|jquery" index.html` | Keine Treffer — pure HTML/CSS/JS | ANF-6 |
| T-6.3 | Daten als JS-Objekt | `grep "MENU_DATA\|menuData\|categories" index.html` | Menü-Daten als JS-Objekt/Array im File definiert | ANF-6 |
| T-6.4 | Keine Console-Fehler | `browser console` nach komplettem Durchlauf (alle Tabs klicken, Cart nutzen, Checkout) | 0 Errors, 0 unhandled exceptions | ANF-6, AK-8 |
| T-6.5 | Performance: 100+ Items | `browser act evaluate` → Rendering-Zeit messen: `performance.now()` vor/nach Menü-Render | Render-Zeit < 500ms für komplettes Menü | ANF-6, AK-3 |
| T-6.6 | Performance: Scroll-Lag | Bei sichtbarem Menü (alle Items) schnell scrollen | Kein spürbarer Lag, flüssiges Scrolling | ANF-6 |
| T-6.7 | Offline-fähig | Seite laden, Netzwerk trennen (kann simuliert werden), Interaktion testen | Seite funktioniert komplett ohne Netzwerk (außer Google Fonts Fallback) | ANF-6 |

---

## Zusammenfassung: Test-Matrix

| ANF | Tests | Visuell | Funktional | Mobile | Performance |
|-----|-------|---------|------------|--------|-------------|
| ANF-1 | T-1.1 – T-1.8 | T-1.2, T-1.8 | T-1.1, T-1.7 | T-1.8 | — |
| ANF-2 | T-2.1 – T-2.8 | T-2.7, T-2.8 | T-2.2, T-2.3, T-2.5 | T-2.8 | — |
| ANF-3 | T-3.1 – T-3.10 | T-3.8, T-3.9, T-3.10 | T-3.1–T-3.7 | T-3.10 | — |
| ANF-4 | T-4.1 – T-4.8, T-4.E2E | T-4.3, T-4.8 | T-4.1–T-4.7, T-4.E2E | — | — |
| ANF-5 | T-5.1 – T-5.7 | T-5.1–T-5.7 | — | T-5.7 | — |
| ANF-6 | T-6.1 – T-6.7 | — | T-6.1–T-6.4 | — | T-6.5, T-6.6 |

**Gesamt:** 47 Tests (8+8+10+9+7+7 = 49 inkl. E2E)
**Visuell:** 15 Tests mit Pflicht-Screenshot
**Funktional:** 25 Tests
**Mobile:** 5 Tests
**Performance:** 2 Tests

---

## Anweisungen an Vermithrax 🛡️

1. **Starte** den OpenClaw Browser, navigiere zu `file:///Users/macmini001/.openclaw/workspace/projects/demo-blitz-pizza/index.html`
2. **Führe Tests in Reihenfolge aus** (T-1.1 zuerst — wenn Seite nicht lädt, alles FAIL)
3. **Screenshots speichern** bei JEDEM visuellen Test unter `projects/demo-blitz-pizza/test-results/`
4. **Bei Viewport-Wechsel:** Browser-Größe explizit setzen (375×812 für Mobile, 1280×800 für Desktop)
5. **Console-Check:** Nach JEDEM funktionalen Test `browser console` prüfen
6. **E2E-Test am Ende:** T-4.E2E als finaler Integrationstest
7. **Report erstellen:** `projects/demo-blitz-pizza/TEST-REPORT.md` mit Ergebnis pro Test-ID

---

*Syrax 🩵 — Tests definiert. Vermithrax kann prüfen.*
