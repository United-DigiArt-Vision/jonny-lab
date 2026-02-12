# 🏛️ Projekt: City Apps für Gemeinden

**Projekt-ID**: 0003  
**Kunde**: Gemeinde Poxdorf  
**Firma**: United DigiArt Vision  
**Lead Engineer**: 🔴 CARAXES (Der Blutdrache)  
**Erstellt**: 07.02.2026  
**Status**: ✅ Flutter-Grundgerüst fertiggestellt

---

## 📁 Projektstruktur

```
projects/0003_city-apps/
├── flutter-app/              # Flutter Mobile App
│   ├── lib/
│   │   ├── main.dart        # Entry Point + Navigation
│   │   └── screens/
│   │       ├── home_screen.dart      # 🏠 Home (Müllabfuhr + Events)
│   │       ├── calendar_screen.dart  # 📅 Kalender
│   │       ├── scanner_screen.dart   # 📸 QR-Scanner
│   │       ├── news_screen.dart      # 📰 News
│   │       └── more_screen.dart      # ☰ Mehr
│   ├── test/
│   │   └── widget_test.dart # Widget Tests
│   ├── pubspec.yaml         # Dependencies
│   ├── README.md            # Vollständige Doku
│   ├── NOTES.md             # Dev-Notes + TODOs
│   ├── QUICKSTART.md        # Schnellstart-Guide
│   └── .gitignore           # Git-Ignore
└── PROJEKT-OVERVIEW.md      # Diese Datei
```

---

## 🎯 Projekt-Ziele

### Vision
Eine **White-Label City App Plattform** für Gemeinden in Deutschland.

### Phase 1: Poxdorf (Pilot) ✅
- ✅ Flutter-Grundgerüst mit Material Design 3
- ✅ 5 Haupt-Bereiche (Home, Kalender, Scanner, News, Mehr)
- ✅ Dark Mode Support
- ✅ Poxdorf Branding (Grün #166534)
- 🚧 Backend-Integration (TODO)
- 🚧 QR-Scanner Funktionalität (TODO)

### Phase 2: Skalierung
- 📱 White-Label Lösung für beliebige Gemeinden
- 🗄️ Multi-Tenant Backend
- 🎨 Anpassbares Branding pro Gemeinde
- 📊 Analytics & Insights

### Phase 3: Smart City Features
- 🚗 Parkplatz-Auslastung
- 🌡️ Lokale Wetterdaten
- 🚌 ÖPNV-Integration
- 💡 Transparenz (Haushalt, Energie)

---

## 🛠️ Tech Stack

### Mobile App
- **Framework**: Flutter (Dart)
- **UI**: Material Design 3
- **State Management**: Provider (vorbereitet)
- **Dependencies**:
  - `carousel_slider` - Event-Karussell
  - `intl` - Deutsche Datumsformatierung
  - `provider` - State Management
  - `material_symbols_icons` - Extended Icons

### Backend (TODO)
- **Option A**: Node.js + Express + MongoDB
- **Option B**: Firebase (Firestore + Cloud Functions)
- **Option C**: Supabase (PostgreSQL + REST API)

### Infrastruktur (TODO)
- **Hosting**: AWS / Google Cloud / Vercel
- **CDN**: Cloudflare
- **CI/CD**: GitHub Actions
- **Monitoring**: Sentry / Firebase Crashlytics

---

## 📊 Features-Übersicht

### ✅ Implementiert

| Feature | Status | Screen |
|---------|--------|--------|
| Bottom Navigation (5 Tabs) | ✅ | Alle |
| Material Design 3 | ✅ | Alle |
| Dark Mode | ✅ | Alle |
| Poxdorf Branding | ✅ | Alle |
| Müllabfuhr Widget | ✅ | Home |
| Event-Karussell | ✅ | Home |
| News-Liste | ✅ | News |
| Mehr-Menü | ✅ | Mehr |
| Widget Tests | ✅ | test/ |

### 🚧 In Entwicklung

| Feature | Priorität | Aufwand |
|---------|-----------|---------|
| Backend-API | 🔴 Hoch | 2-3 Tage |
| Echte Daten-Integration | 🔴 Hoch | 1-2 Tage |
| QR-Scanner | 🟡 Mittel | 1 Tag |
| Push-Benachrichtigungen | 🟡 Mittel | 1-2 Tage |
| Wappen-Asset | 🟢 Niedrig | 2 Stunden |
| App-Icons | 🟢 Niedrig | 1 Stunde |
| Detailseiten (Event/News) | 🟡 Mittel | 1-2 Tage |

### 💡 Geplant (Backlog)

- Offline-Caching
- Mehrsprachigkeit (Deutsch/Englisch)
- Barrierefreiheit-Optimierung
- Foto-Upload (Mängelmeldungen)
- Bürger-Forum
- Online-Formulare
- Termin-Buchung Rathaus
- Gamification

---

## 🎨 Design-System

### Farben
| Element | Light Mode | Dark Mode |
|---------|------------|-----------|
| Primary | `#166534` (Poxdorf Grün) | `#166534` |
| Background | System | System |
| Surface | System | System |
| Error | System | System |

### Typografie
- **Headlines**: Bold, größer
- **Body**: Regular, lesbar
- **Labels**: Klein, sekundär

### Spacing
- **Grid**: 8px Basis
- **Padding**: 16px Standard
- **Margins**: 16px zwischen Cards

---

## 📈 Nächste Schritte

### Sprint 1: Backend Foundation (1 Woche)
1. Backend-Framework wählen und aufsetzen
2. API-Endpoints definieren:
   - `GET /api/waste-collection` → Müllabfuhr
   - `GET /api/events` → Veranstaltungen
   - `GET /api/news` → Nachrichten
3. Flutter API-Client implementieren
4. Provider/State Management einrichten

### Sprint 2: Core Features (1 Woche)
5. QR-Scanner implementieren
6. Push-Notifications Setup (FCM)
7. Wappen + App-Icons hinzufügen
8. Detailseiten für Events/News

### Sprint 3: Testing & Polish (3-5 Tage)
9. Unit + Widget Tests erweitern
10. Integration Tests
11. UI/UX Polish
12. Performance-Optimierung

### Sprint 4: Launch Prep (3-5 Tage)
13. App Store Listings (Google Play + Apple)
14. Beta-Testing mit Gemeinde
15. Feedback einarbeiten
16. Production Release

---

## 🚀 Launch-Checkliste

### App
- [ ] Backend deployed & stabil
- [ ] Echte Gemeinde-Daten integriert
- [ ] Push-Notifications funktional
- [ ] QR-Scanner funktional
- [ ] App-Icons & Splash Screen
- [ ] Tests erfolgreich (>80% Coverage)
- [ ] Performance optimiert (FPS >60)

### Stores
- [ ] Google Play Store Account
- [ ] Apple Developer Account
- [ ] Screenshots erstellt (alle Devices)
- [ ] Store-Beschreibung (DE/EN)
- [ ] Privacy Policy
- [ ] Terms of Service

### Marketing
- [ ] Landing Page
- [ ] Social Media Posts
- [ ] Pressemitteilung Gemeinde
- [ ] Flyer für Bürger

---

## 📞 Kontakt & Support

**Entwickler**: CARAXES (Lead Engineer)  
**Firma**: United DigiArt Vision  
**Projekt-Channel**: TBD  
**Docs**: `/projects/0003_city-apps/`

---

## 📝 Changelog

### [1.0.0] - 07.02.2026 - GRUNDGERÜST
**Added:**
- ✅ Flutter-Projektstruktur komplett
- ✅ Alle 5 Screens (Home, Kalender, Scanner, News, Mehr)
- ✅ Material Design 3 + Dark Mode
- ✅ Event-Karussell mit Auto-Play
- ✅ Müllabfuhr-Widget mit Beispieldaten
- ✅ News-Liste mit Kategorien
- ✅ Umfangreiche Dokumentation (README, NOTES, QUICKSTART)
- ✅ Widget Tests

**Status**: ✅ READY FOR BACKEND INTEGRATION

---

**🔴 CARAXES** — Der Blutdrache hat gesprochen! 🐉
