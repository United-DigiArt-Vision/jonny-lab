# ⚡ Quickstart Guide - Poxdorf City App

Schnellstart für Entwickler die sofort loslegen wollen.

## 🚀 In 3 Schritten zur laufenden App

### 1️⃣ Dependencies installieren
```bash
cd /Users/macmini001/.openclaw/workspace/projects/0003_city-apps/flutter-app/
flutter pub get
```

### 2️⃣ App starten
```bash
# iOS Simulator (macOS)
flutter run -d ios

# Android Emulator
flutter run -d android

# Chrome (Web - für schnelles Testing)
flutter run -d chrome

# Oder: Device auswählen
flutter devices
flutter run -d <device-id>
```

### 3️⃣ Hot Reload nutzen
- **`r`** drücken → Hot Reload (schnell, behält State)
- **`R`** drücken → Hot Restart (neu laden)
- **`q`** drücken → Beenden

---

## 🎯 Was du sofort sehen solltest

### Home Screen
- ✅ Poxdorf Header mit Wappen (Placeholder)
- ✅ Müllabfuhr-Widget mit nächstem Termin
- ✅ Event-Karussell mit 3 Events (auto-scroll)

### Bottom Navigation
- ✅ 5 Tabs funktionieren
- ✅ Dark Mode funktioniert (System-Einstellung)
- ✅ Material Design 3 Look & Feel

---

## 🧪 Tests laufen lassen

```bash
# Alle Tests
flutter test

# Mit Coverage
flutter test --coverage

# Einzelner Test
flutter test test/widget_test.dart
```

---

## 📱 Build für Device

### Android
```bash
# Debug APK
flutter build apk --debug

# Release APK (signiert)
flutter build apk --release

# App Bundle (für Play Store)
flutter build appbundle --release
```

### iOS
```bash
# Debug
flutter build ios --debug

# Release (benötigt Apple Developer Account)
flutter build ios --release
```

---

## 🐛 Probleme?

### Flutter nicht gefunden
```bash
# Flutter installieren
https://docs.flutter.dev/get-started/install

# Flutter zu PATH hinzufügen
export PATH="$PATH:`pwd`/flutter/bin"
```

### Dependencies Error
```bash
# Cache clearen
flutter clean
flutter pub get
```

### Emulator startet nicht
```bash
# Android Emulators auflisten
flutter emulators

# Emulator starten
flutter emulators --launch <emulator-id>
```

### iOS Simulator (macOS only)
```bash
# Simulator öffnen
open -a Simulator
```

---

## 💡 Entwickler-Tipps

### Hot Reload funktioniert nicht?
- Nur UI-Änderungen werden hot-reloaded
- Bei State/Logic-Änderungen → Hot Restart (`R`)
- Bei Dependency-Änderungen → App neu starten

### Performance verbessern
```bash
# Release-Mode für bessere Performance
flutter run --release
```

### Debug-Tools
```bash
# Flutter DevTools starten
flutter pub global activate devtools
flutter pub global run devtools
```

### VS Code Extensions
- Flutter (Dart-Code.flutter)
- Dart (Dart-Code.dart-code)
- Flutter Widget Snippets

### Android Studio Plugins
- Flutter
- Dart

---

## 📂 Wichtige Dateien

| Datei | Zweck |
|-------|-------|
| `lib/main.dart` | Entry Point, Navigation |
| `lib/screens/home_screen.dart` | Home mit Müllabfuhr + Events |
| `pubspec.yaml` | Dependencies + Config |
| `analysis_options.yaml` | Linting-Regeln |
| `README.md` | Vollständige Doku |
| `NOTES.md` | Dev-Notes + TODOs |

---

## 🎨 Design anpassen

### Farbe ändern
In `lib/main.dart`:
```dart
seedColor: const Color(0xFF166534), // <-- Hier ändern
```

### Dark Mode deaktivieren
In `lib/main.dart`:
```dart
themeMode: ThemeMode.light, // statt .system
```

### Icons ändern
In jeweiligen `_screen.dart` Dateien.

---

## 🚀 Ready to Code!

Die App läuft? Perfekt! 

**Nächste Schritte:**
1. Schau dir `NOTES.md` für TODOs an
2. Backend-API anbinden
3. Echte Daten laden
4. Features erweitern

**Happy Coding! 🔴🐉**
