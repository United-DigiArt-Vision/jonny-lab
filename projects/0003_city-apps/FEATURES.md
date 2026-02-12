# City Apps — Feature-Set

## 🎯 Basis-Paket (Kern-Features)

| Feature | Beschreibung | Priorität |
|---------|--------------|-----------|
| **Müllkalender** | Interaktiver Kalender mit allen Abfuhrterminen | 🔴 KRITISCH |
| **Push-Erinnerungen** | "Morgen wird Gelbe Tonne abgeholt" (Vorabend) | 🔴 KRITISCH |
| **Adress-basiert** | Automatische Termine basierend auf Straße | 🔴 KRITISCH |

### 🗑️ Müllkalender — Technische Details

**User-Flow (2 Optionen):**

**Option A: Standortfreigabe (empfohlen)**
1. App fragt: "Standort freigeben?"
2. GPS → Reverse Geocoding → Adresse automatisch
3. Termine sofort da — KEIN Tippen nötig!

**Option B: Manuelle Eingabe**
1. User tippt Adresse (Autocomplete)
2. App ermittelt Abfuhrgebiet
3. Termine werden angezeigt

**Danach:**
- Push-Erinnerung am Vorabend
- Adresse in Settings änderbar

**Datenquellen (Priorität):**
1. **Awido API** — Viele Landkreise nutzen dieses System
2. **Regio IT** — Weiterer großer Anbieter
3. **ICS/iCal Export** — Viele Städte bieten das an
4. **CSV/Excel** — Stadt liefert Daten, wir importieren
5. **PDF Digitalisierung** — Letzte Option, aufwändig

**Bekannte Anbieter mit API:**
- Awido (CubeFour GmbH)
- Regio IT
- MyMüll
- MüllMax
- Abfall+ 

**Datenstruktur:**
```
Stadt → Straße → Hausnummernbereich → Abfuhrgebiet → Termine
```

**Beispiel Erlangen:**
```json
{
  "street": "Hauptstraße",
  "range": "1-50",
  "district": "Bezirk-Mitte-A",
  "schedule": {
    "restmuell": ["Mo", "every_2_weeks"],
    "gelbe_tonne": ["Mi", "every_2_weeks"],
    "papier": ["Fr", "every_4_weeks"],
    "bio": ["Mo", "weekly"]
  }
}
```
| **News-Feed** | Aktuelle Meldungen der Stadt | 🟡 WICHTIG |
| **Veranstaltungen** | Lokale Events mit Kalender-Integration | 🟡 WICHTIG |
| **Kontakt** | Wichtige Telefonnummern & Öffnungszeiten | 🟡 WICHTIG |
| **Kirchliche Events** | Gottesdienste, Feste, Kirchengemeinde-Infos | 🟡 WICHTIG |
| **Bushaltestellen/ÖPNV** | Haltestellen-Karte, Fahrpläne, nächster Bus | 🟡 WICHTIG |
| **Mängelmelder** | Bürger melden Probleme (Schlagloch, etc.) | 🟢 NICE |

---

## 💎 Premium-Module (Add-ons)

| Modul | Beschreibung | Zielgruppe |
|-------|--------------|------------|
| **ÖPNV-Integration** | Echtzeit Abfahrten, Routenplaner | Städte mit Bus/Bahn |
| **Parkplatz-Finder** | Freie Parkplätze in Echtzeit | Städte mit Sensoren |
| **Bürgerportal** | Termine buchen, Anträge stellen | Digitale Kommunen |
| **Kindergarten-Modul** | Anmeldung, Warteliste, Infos | Familien-Fokus |
| **Tourismus** | Sehenswürdigkeiten, Touren, Audio-Guides | Touristische Orte |
| **Vereins-Portal** | Lokale Vereine präsentieren sich | Gemeinschafts-Fokus |
| **Baustellen-Info** | Aktuelle Sperrungen & Umleitungen | Pendler |
| **Notfall-Modul** | Warndurchsagen, Sirenen-Erklärung | Alle |

---

## 📱 Design-Prinzipien (Dubai-Level)

### 1. Premium Look
- Sanfte Farbverläufe (keine flachen Farben)
- Großzügige Abstände
- Subtle Schatten für Tiefe
- Hochwertige Icons (SF Symbols / Material)

### 2. Intuitive UX
- Max 3 Taps zu jedem Feature
- Personalisierter Home-Screen
- Intelligente Defaults
- Haptic Feedback

### 3. Accessibility
- VoiceOver / TalkBack Support
- Dynamische Schriftgrößen
- Hoher Kontrast Option
- Einhändige Bedienung

### 4. Performance
- < 2 Sekunden App-Start
- Offline-Grundfunktionen
- Effiziente Batterienutzung
- < 50 MB App-Größe

---

## 🛠️ Technische Architektur

```
┌─────────────────────────────────────────────┐
│                FLUTTER APP                   │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐       │
│  │   iOS   │ │ Android │ │   Web   │       │
│  └────┬────┘ └────┬────┘ └────┬────┘       │
│       └──────────┼──────────┘              │
│                  │                          │
│         ┌───────┴───────┐                  │
│         │  Shared Code  │                  │
│         └───────────────┘                  │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│              BACKEND (Firebase/Supabase)     │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐       │
│  │   Auth  │ │Firestore│ │  Push   │       │
│  └─────────┘ └─────────┘ └─────────┘       │
└─────────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│              ADMIN DASHBOARD                 │
│  (Stadt-Mitarbeiter pflegen Inhalte)        │
│  - News posten                              │
│  - Events verwalten                         │
│  - Mängelmelder bearbeiten                  │
│  - Statistiken einsehen                     │
└─────────────────────────────────────────────┘
```

---

## 💰 Preismodell (Vorschlag)

| Paket | Einwohner | Setup | Monatlich |
|-------|-----------|-------|-----------|
| **Starter** | < 5.000 | €2.900 | €149/Mo |
| **Standard** | 5.000-20.000 | €4.900 | €299/Mo |
| **Premium** | 20.000-50.000 | €7.900 | €499/Mo |
| **Enterprise** | > 50.000 | Auf Anfrage | Auf Anfrage |

**Inkludiert:**
- App für iOS + Android
- Admin-Dashboard
- Hosting & Wartung
- Updates & Support
- Push-Notifications

**Add-on Module:** +€50-200/Mo pro Modul

---

## 📊 Wettbewerbsvergleich

| Feature | Wir | Citykey | VillageApp |
|---------|-----|---------|------------|
| Premium-Design | ✅ Dubai-Level | ⚠️ Funktional | ❌ Basic |
| Müllkalender + Push | ✅ | ✅ | ✅ |
| Native Performance | ✅ Flutter | ⚠️ Hybrid | ❌ WebView |
| Individuelle Anpassung | ✅ | ❌ | ⚠️ |
| Preis (kleine Stadt) | €149/Mo | ~€300/Mo? | €0.90/Einw. |
| Setup-Zeit | 2-4 Wochen | 4-8 Wochen | 2-4 Wochen |

**Unser USP:** Premium-Design zum fairen Preis. Dubai-Level UX für deutsche Kleinstädte.

---

## ✅ MVP Definition (Version 1.0)

**Must Have:**
- [ ] Home-Screen mit Stadt-Branding
- [ ] Müllkalender mit Adress-Suche
- [ ] Push-Erinnerungen (Vorabend)
- [ ] News-Feed
- [ ] Kontakt-Seite
- [ ] Settings (Push an/aus, Adresse)

**Nice to Have (v1.1):**
- [ ] Veranstaltungskalender
- [ ] Mängelmelder
- [ ] Dark Mode

**Später (v2.0):**
- [ ] ÖPNV-Integration
- [ ] Bürgerportal
- [ ] Admin-Dashboard (Web)

---

---

## ⛪ Kirchliche Veranstaltungen (NEU — Bürgerfeedback 08.02.2026)

**Hintergrund:** Aus Bürgergespräch in Poxdorf. Kirche ist DER Veranstaltungs-Hub in kleinen Gemeinden.

**Features:**
- Gottesdienst-Zeiten (wöchentlich wiederkehrend)
- Kirchliche Feste & Feiern (Erntedank, Weihnachten, Ostern, etc.)
- Kirchenkonzerte, Basare, Gemeindeabende
- Push-Erinnerung vor Events
- Kontaktdaten Pfarrbüro
- Eigener Filter "Kirche" im Veranstaltungskalender

**Datenquellen:**
1. Kirchengemeinde pflegt selbst (Admin-Zugang)
2. Flyer Scanner (Bürger fotografieren Aushänge)
3. Website der Kirchengemeinde (Scraping/Import)

**Synergien:**
- Fließt in den allgemeinen Veranstaltungskalender ein
- Flyer Scanner funktioniert auch für kirchliche Flyer
- Push-System wird mitgenutzt

---

## 🚌 Bushaltestellen / ÖPNV (NEU — Bürgerfeedback 08.02.2026)

**Hintergrund:** Aus Bürgergespräch in Poxdorf. ÖPNV-Abdeckung ist Thema in ländlichen Gebieten.

**MVP Features:**
- Karte mit allen Bushaltestellen in Poxdorf
- Pro Haltestelle: Name, Linien, Abfahrtszeiten
- Nächste Haltestelle per GPS finden
- Statische Fahrpläne (offline verfügbar)

**V2 Features:**
- Echtzeit-Abfahrten (VGN API)
- Verbindungssuche (A → B)
- Verspätungs-Push
- Anschluss-Verbindungen

**Datenquellen:**
- VGN (Verkehrsverbund Großraum Nürnberg) — Poxdorf liegt im VGN-Gebiet
- DELFI (Deutschlandweite Fahrplanauskunft) — als Fallback
- OpenStreetMap — Haltestellenpositionen
- Statische Fahrplan-PDFs als Basis

**Technisch:**
- Haltestellenpositionen aus OSM oder manuell
- Fahrplandaten: GTFS-Format (VGN bietet das an)
- Kartenansicht: Leaflet/MapBox

---

*Letzte Aktualisierung: 2026-02-08*
