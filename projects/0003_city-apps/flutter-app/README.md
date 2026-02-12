# 🏛️ Poxdorf City App

Die offizielle City App für die Gemeinde Poxdorf – entwickelt von **United DigiArt Vision**.

## 📱 Features

### ✅ Implementiert
- ✨ **Material Design 3** mit modernem UI/UX
- 🌓 **Dark Mode Support** (automatisch basierend auf System-Einstellungen)
- 🎨 **Poxdorf Farbschema** (Primärfarbe: Grün #166534)
- 📍 **Bottom Navigation** mit 5 Tabs:
  - 🏠 **Home**: Übersicht mit Wappen, Müllabfuhr-Infos und Event-Karussell
  - 📅 **Kalender**: Termine und Veranstaltungen
  - 📸 **Scanner**: QR-Code Scanner für Gemeinde-Services
  - 📰 **News**: Aktuelle Nachrichten aus der Gemeinde
  - ☰ **Mehr**: Zusätzliche Infos und Einstellungen

### 🏠 Home Screen
- Poxdorf Wappen + Name im Header
- **Nächste Müllabfuhr Widget** mit Datum und Mülltonnen-Typ
- **Events Karussell** mit automatischem Scroll
- Responsive Design

### 🚧 Coming Soon
- Backend-Anbindung für echte Daten (API)
- QR-Code Scanner Funktionalität
- Push-Benachrichtigungen
- Offline-Support
- Mehrsprachigkeit

---

## 🚀 Setup & Installation

### Voraussetzungen
- Flutter SDK (>=3.0.0)
- Dart SDK (kommt mit Flutter)
- Android Studio / Xcode (für Emulator/Simulator)
- Git

### Installation

1. **Repository klonen** (falls noch nicht geschehen):
   ```bash
   cd /Users/macmini001/.openclaw/workspace/projects/0003_city-apps/flutter-app/
   ```

2. **Dependencies installieren**:
   ```bash
   flutter pub get
   ```

3. **App starten**:
   ```bash
   # iOS Simulator
   flutter run -d ios
   
   # Android Emulator
   flutter run -d android
   
   # Chrome (Web)
   flutter run -d chrome
   ```

4. **Build für Release**:
   ```bash
   # Android APK
   flutter build apk --release
   
   # iOS (benötigt Xcode auf macOS)
   flutter build ios --release
   ```

---

## 📁 Projektstruktur

```
flutter-app/
├── lib/
│   ├── main.dart                 # Entry Point & Navigation
│   └── screens/
│       ├── home_screen.dart      # Home mit Müllabfuhr & Events
│       ├── calendar_screen.dart  # Kalender (Placeholder)
│       ├── scanner_screen.dart   # QR-Scanner (Placeholder)
│       ├── news_screen.dart      # News-Liste
│       └── more_screen.dart      # Mehr-Menü
├── pubspec.yaml                  # Dependencies & Config
└── README.md                     # Diese Datei
```

---

## 🎨 Design System

### Farben
- **Primärfarbe**: Grün `#166534` (Poxdorf Grün)
- **Material Design 3**: Automatische Farbpaletten-Generierung
- **Dark Mode**: Voll unterstützt

### Typografie
- Material Design 3 Standard-Schriftarten
- Responsive Textgrößen

### Icons
- Material Icons (Standard)
- Custom Icons können später hinzugefügt werden

---

## 🔧 Dependencies

| Package | Zweck |
|---------|-------|
| `carousel_slider` | Event-Karussell auf Home-Screen |
| `intl` | Datumsformatierung (Deutsch) |
| `provider` | State Management (bereit für Backend) |
| `material_symbols_icons` | Erweiterte Material Icons |

---

## 📝 Nächste Schritte (TODO)

### Phase 1: Backend Integration
- [ ] API-Client für Gemeinde-Daten implementieren
- [ ] Müllabfuhr-Kalender aus Backend laden
- [ ] Events aus CMS/Backend laden
- [ ] News aus Backend laden

### Phase 2: Features
- [ ] QR-Code Scanner mit Kamera implementieren
- [ ] Push-Benachrichtigungen (Firebase Cloud Messaging)
- [ ] Kalender mit tatsächlichen Terminen
- [ ] Offline-Caching (Hive/SharedPreferences)

### Phase 3: Polish
- [ ] Poxdorf Wappen als Asset hinzufügen
- [ ] Splash Screen mit Gemeinde-Logo
- [ ] App-Icon für iOS/Android
- [ ] Animations & Transitions
- [ ] Barrierefreiheit (Accessibility)

### Phase 4: Deployment
- [ ] Android: Google Play Store
- [ ] iOS: Apple App Store
- [ ] Backend-Server Setup
- [ ] CI/CD Pipeline (GitHub Actions)

---

## 🐛 Testing

```bash
# Unit Tests
flutter test

# Widget Tests
flutter test test/widget_test.dart

# Integration Tests
flutter drive --target=test_driver/app.dart
```

---

## 🤝 Entwicklung

### Code-Style
- Englische Variablen/Funktionen
- Deutsche Kommentare und User-facing Texte
- DartFmt für Formatierung: `flutter format .`
- Linting: `flutter analyze`

### Git Workflow
```bash
git add .
git commit -m "feat: implement feature X"
git push origin main
```

### Branching Strategy
- `main`: Production-ready Code
- `develop`: Development Branch
- `feature/*`: Feature Branches
- `fix/*`: Bugfix Branches

---

## 📄 Lizenz

© 2026 United DigiArt Vision  
Alle Rechte vorbehalten.

---

## 👥 Team

**Lead Engineer**: 🔴 CARAXES (Der Blutdrache)  
**Firma**: United DigiArt Vision  
**Projekt**: City Apps für Gemeinden

---

## 📞 Support

Bei Fragen oder Problemen:
- GitHub Issues: (TODO: Repository Link)
- Email: (TODO: Support Email)
- Dokumentation: (TODO: Docs Link)

---

**Status**: ✅ **Grundgerüst fertiggestellt**  
**Version**: 1.0.0  
**Letzte Aktualisierung**: 07.02.2026
