# 📝 Poxdorf City App - Development Notes

## Projekt-Übersicht
**Firma**: United DigiArt Vision  
**Lead Engineer**: 🔴 CARAXES  
**Projekt-ID**: 0003  
**Status**: ✅ Grundgerüst fertiggestellt  
**Erstellt**: 07.02.2026

---

## ✅ Was wurde implementiert

### Kern-Features
- ✨ **Flutter-Projektstruktur** komplett aufgesetzt
- 🎨 **Material Design 3** mit Poxdorf Grün (#166534)
- 🌓 **Dark Mode** voll funktionsfähig (automatisch)
- 📱 **Bottom Navigation** mit 5 Tabs (Material Design 3 NavigationBar)

### Screens im Detail

#### 1. Home Screen 🏠
- **Header**: Poxdorf Wappen (Placeholder) + Name
- **Müllabfuhr Widget**: 
  - Nächstes Datum mit Countdown
  - Mülltonnen-Typen als farbige Chips
  - Primärfarben-Container mit Schatten
- **Events Karussell**:
  - Auto-Play alle 5 Sekunden
  - 3 Beispiel-Events (Gemeinderatssitzung, Sommerfest, Sperrmüll)
  - Datum, Ort, Icon pro Event
  - Gradient-Cards mit Schatten

#### 2. Kalender Screen 📅
- Placeholder mit Icon
- Call-to-Action Button "Termin hinzufügen"
- Bereit für Kalender-Integration

#### 3. Scanner Screen 📸
- QR-Code Frame (visuell)
- Button "Scanner starten" (zeigt Snackbar)
- Bereit für Kamera-Integration

#### 4. News Screen 📰
- Liste mit 3 Beispiel-News-Artikeln
- Kategorien (Infrastruktur, Politik, Veranstaltungen)
- Datum-Anzeige ("Heute", "Gestern", "Vor X Tagen")
- "Weiterlesen" Button pro Artikel
- Suchbutton in AppBar (noch nicht funktional)

#### 5. Mehr Screen ☰
- Gemeinde-Info Header mit Wappen (Gradient)
- Menü-Sektionen:
  - **Informationen**: Über Poxdorf, Rathaus, Gemeinderat
  - **Services**: Formulare, Notrufnummern, Parkplätze
  - **App**: Benachrichtigungen, Einstellungen, Hilfe, Über
- Footer mit Copyright (United DigiArt Vision)

---

## 🎨 Design-Entscheidungen

### Farbschema
- **Primärfarbe**: `#166534` (Poxdorf Grün)
- **Material 3 ColorScheme**: Automatisch generiert aus Primärfarbe
- **Dark Mode**: Separate ColorScheme mit gleichem Seed
- **Schatten**: Subtile Schatten (opacity 0.05-0.1)

### Typografie
- Material Design 3 Standard-Schriftgrößen
- Bold für Überschriften
- Opacity für deaktivierte/sekundäre Texte

### Spacing
- 8px-Grid-System (8, 12, 16, 24, 32px)
- Padding: meist 16px horizontal
- Margins: Cards 16px bottom

### Components
- **NavigationBar** (Material 3) statt BottomNavigationBar
- **FilledButton** für Primary Actions
- **Cards** mit Outline statt Elevation
- **IndexedStack** für Tab-Persistenz

---

## 📦 Dependencies gewählt

| Package | Version | Warum? |
|---------|---------|--------|
| `carousel_slider` | ^4.2.1 | Bestes Event-Karussell mit Auto-Play |
| `intl` | ^0.19.0 | Deutsche Datumsformatierung |
| `provider` | ^6.1.1 | Standard State Management (bereit für Backend) |
| `material_symbols_icons` | ^4.2785.1 | Erweiterte Material Icons |
| `flutter_lints` | ^3.0.0 | Code-Qualität sicherstellen |

---

## 🚧 Offene Punkte & TODOs

### Kritisch (vor Launch)
- [ ] **Backend-API** aufsetzen (REST oder GraphQL)
- [ ] **Echte Daten** laden (Müllabfuhr-Kalender, Events, News)
- [ ] **QR-Scanner** implementieren (package: `mobile_scanner`)
- [ ] **Push-Benachrichtigungen** (Firebase Cloud Messaging)
- [ ] **Poxdorf Wappen** als Asset hinzufügen (SVG oder PNG)
- [ ] **App-Icon** erstellen (Android + iOS)
- [ ] **Splash Screen** mit Gemeinde-Branding

### Nice-to-Have
- [ ] **Offline-Caching** (Hive oder Isar)
- [ ] **Deutsche Lokalisierung** für `intl` package konfigurieren
- [ ] **Detailseiten** für Events und News
- [ ] **Suchfunktion** in News implementieren
- [ ] **Filter** für Kalender (Kategorien)
- [ ] **Favoritensystem** für Events/News
- [ ] **Teilen-Funktion** für News (Share API)
- [ ] **Barrierefreiheit** testen (Screen Reader)

### Backend-Requirements
- [ ] **Endpoints definieren**:
  - `GET /waste-collection` → Müllabfuhr-Termine
  - `GET /events` → Veranstaltungen
  - `GET /news` → Nachrichten
  - `GET /info/council` → Gemeinderats-Infos
  - `POST /qr-scan` → QR-Code verarbeiten
- [ ] **Authentifizierung?** (Optional für personalisierte Features)
- [ ] **Push-Token Management** für Benachrichtigungen

---

## 🐛 Bekannte Probleme

### Keine (bisher)
- App läuft stabil im aktuellen Zustand
- Alle Placeholder-Screens funktionieren

### Potenzielle Issues
- **Deutsche Datumsformatierung** könnte ohne Locale-Init fehlschlagen  
  → Lösung: `Intl.defaultLocale = 'de_DE';` in `main()` setzen
- **IndexedStack** kann Performance-Probleme bei vielen Screens haben  
  → Aktuell kein Problem (nur 5 einfache Screens)

---

## 📚 Learnings & Erkenntnisse

### Was gut lief
✅ **Material Design 3** ist perfekt für moderne Apps  
✅ **IndexedStack** erhält Screen-State beim Tab-Wechsel  
✅ **ColorScheme.fromSeed** macht Dark Mode super einfach  
✅ **Modulare Screen-Struktur** ist wartungsfreundlich

### Was zu beachten ist
⚠️ **Beispieldaten** müssen durch echte API ersetzt werden  
⚠️ **Deutsche Texte** überall einheitlich verwenden  
⚠️ **Performance** bei vielen News-Artikeln → Pagination nötig

### Architektur-Entscheidungen
- **Screens in separaten Dateien** → Übersichtlich
- **Private Widgets** (`_Widget`) → Nicht global nutzbar, nur im Screen
- **Placeholder-Daten in Widgets** → Später durch State Management ersetzen
- **Keine komplexe State-Logic** → Kommt mit Backend-Integration

---

## 🔄 Nächste Session-Tasks

### Priorität 1
1. **Backend-API aufsetzen** (Node.js/Express oder Firebase)
2. **API-Client in Flutter** implementieren (package: `dio` oder `http`)
3. **Provider/State Management** für API-Daten einrichten

### Priorität 2
4. **QR-Scanner** implementieren (`mobile_scanner` package)
5. **Wappen-Asset** hinzufügen und in Home/More einbinden
6. **App-Icons** generieren (package: `flutter_launcher_icons`)

### Priorität 3
7. **Detailseiten** für Events und News
8. **Push-Notifications** Setup (FCM)
9. **Testing** (Unit + Widget Tests)

---

## 💡 Ideen für Erweiterungen

### Community-Features
- 🗣️ **Bürger-Forum** für Diskussionen
- 📸 **Foto-Upload** für Mängelmeldungen ("Schlagloch melden")
- ⭐ **Bewertungssystem** für Gemeinde-Services
- 🏆 **Gamification** (Punkte für Teilnahme an Events)

### Smart-City-Features
- 🚗 **Parkplatz-Auslastung** in Echtzeit
- 🌡️ **Wetter-Integration** lokal für Poxdorf
- 🚌 **ÖPNV-Anbindung** (wenn vorhanden)
- 💡 **Energieverbrauch** der Gemeinde (Transparenz)

### Verwaltungs-Features
- 📝 **Online-Formulare** direkt in der App ausfüllen
- 🗓️ **Termin-Buchung** beim Rathaus
- 💬 **Chat mit Verwaltung** (Support)
- 📊 **Haushalt-Transparenz** (Wo fließt das Geld hin?)

---

## 🎯 Vision

**Langfristiges Ziel**: Die Poxdorf City App soll DER digitale Hub für alle Bürger werden.  
Nicht nur Infos konsumieren, sondern aktiv teilnehmen und die Gemeinde mitgestalten.

**Skalierbarkeit**: Diese Grundstruktur kann für ALLE Gemeinden genutzt werden (White-Label-Lösung).  
→ **Projekt "City Apps für Gemeinden"** als Produkt von United DigiArt Vision!

---

**📍 Status**: Grundgerüst steht. Ready für Backend-Integration! 🚀
