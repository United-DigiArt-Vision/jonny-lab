# Testspezifikation — City Apps

| Feld | Wert |
|------|------|
| **Bezug** | PRD.md (Anforderungen) |
| **Version** | 1.0 |
| **Erstellt** | 2026-02-07 |
| **Status** | Aktiv |

---

## 1. Teststrategie

### Testebenen
| Ebene | Was | Wie | Wann |
|-------|-----|-----|------|
| **E2E / Smoke** | Landingpage funktioniert | Playwright | Nach jedem Deployment |
| **Unit Tests** | Einzelne Funktionen | Flutter Test | Bei jedem Commit |
| **Widget Tests** | UI-Komponenten | Flutter Test | Bei jedem Commit |
| **Integration** | Feature-Flows | Flutter Integration | Vor Release |
| **Visuell** | Design korrekt | Screenshot-Vergleich | Nach Deployment |
| **Performance** | Ladezeiten | Lighthouse | Nach Deployment |
| **Accessibility** | Barrierefreiheit | Lighthouse + axe | Nach Deployment |

### Testprozess
```
Code Push → GitHub Actions → Build → Deploy → Auto-Tests → Ergebnis → Dino informiert
```

---

## 2. Testfälle — Landingpage (Phase 1)

### Bezug: PRD Kapitel 9 (UI/UX) + Kapitel 10 (Akzeptanzkriterien)

| Test-ID | PRD-Ref | Beschreibung | Erwartetes Ergebnis | Prio |
|---------|---------|--------------|---------------------|------|
| T-LP-001 | Allgemein | Seite lädt erfolgreich | HTTP 200, Title korrekt | 🔴 |
| T-LP-002 | Design | Poxdorf-Wappen wird angezeigt | Bild lädt, kein 404 | 🔴 |
| T-LP-003 | Design | Gemeindename "Poxdorf" sichtbar | Text vorhanden | 🔴 |
| T-LP-004 | Design | Kein "Dorf" im Text | "Dorf" kommt nicht isoliert vor | 🔴 |
| T-LP-005 | Allgemein | Keine KI/AI Buzzwords | "KI", "AI", "künstliche Intelligenz" nicht in Feature-Beschreibungen | 🔴 |
| T-LP-006 | Design | Alle 6 Feature-Cards sichtbar | Müll, Events, Scanner, News, Notfall, Kontakte | 🔴 |
| T-LP-007 | Design | Transparenz-Banner vorhanden | "offizielle Poxdorf-App" Text sichtbar | 🔴 |
| T-LP-008 | Design | Vision-Sektion vorhanden | "Unsere Vision" sichtbar | 🟡 |
| T-LP-009 | Design | Regionale Vernetzung sichtbar | Pinzberg, Effeltrich, etc. | 🟡 |
| T-LP-010 | Design | Footer mit United DigiArt Vision | Copyright-Text vorhanden | 🟡 |
| T-LP-011 | Performance | Seite lädt in <3 Sekunden | Lighthouse Performance >80 | 🟡 |
| T-LP-012 | Accessibility | WCAG AA konform | Lighthouse Accessibility >90 | 🟡 |
| T-LP-013 | Responsive | Mobile Ansicht funktioniert | Kein horizontales Scrolling auf 375px | 🟡 |
| T-LP-014 | Links | Alle Navigation-Links funktionieren | Kein 404, Anker existieren | 🟢 |
| T-LP-015 | Design | Keine kaputten Bilder | Alle img-Tags laden erfolgreich | 🔴 |

---

## 3. Testfälle — Flyer Scanner (Phase 1)

### Bezug: PRD F-003, US-020 bis US-023

| Test-ID | PRD-Ref | Beschreibung | Erwartetes Ergebnis | Prio |
|---------|---------|--------------|---------------------|------|
| T-FS-001 | F-003 | Script startet ohne Fehler | Exit Code 0 bei --help | 🔴 |
| T-FS-002 | US-020 | Erkennt Veranstaltungsname | "event_name" nicht null | 🔴 |
| T-FS-003 | US-020 | Erkennt Datum | "date" im Format YYYY-MM-DD | 🔴 |
| T-FS-004 | US-020 | Erkennt Ort | "location" nicht null | 🟡 |
| T-FS-005 | US-020 | Erkennt Kategorie | Gültige Kategorie aus Liste | 🟡 |
| T-FS-006 | F-003 | Output ist valides JSON | JSON parse erfolgreich | 🔴 |
| T-FS-007 | US-020 | Erkennung >80% bei Standard-Flyern | Mindestens 4/5 Felder korrekt | 🟡 |

---

## 4. Testfälle — Flutter App (Phase 2, TODO)

### Bezug: PRD F-001 bis F-007

| Test-ID | PRD-Ref | Beschreibung | Erwartetes Ergebnis | Prio |
|---------|---------|--------------|---------------------|------|
| T-APP-001 | Allgemein | App startet | Splash Screen → Home in <2s | 🔴 |
| T-APP-002 | F-001 | Adresseingabe funktioniert | Autocomplete zeigt Vorschläge | 🔴 |
| T-APP-003 | F-001 | Mülltermine laden | Kalender zeigt Termine nach Adresseingabe | 🔴 |
| T-APP-004 | F-001 | Push-Erinnerung wird registriert | Notification scheduled | 🔴 |
| T-APP-005 | F-002 | Events werden angezeigt | Mindestens 1 Event in Liste | 🔴 |
| T-APP-006 | F-003 | Kamera öffnet sich | Permission-Dialog → Kamera-View | 🔴 |
| T-APP-007 | F-004 | News-Feed lädt | Mindestens 1 News-Artikel | 🔴 |
| T-APP-008 | F-005 | Notfall-Kontakte offline | Daten verfügbar im Airplane Mode | 🔴 |
| T-APP-009 | F-006 | Rathaus-Kontakt sichtbar | Name, Telefon, Öffnungszeiten | 🔴 |
| T-APP-010 | F-007 | Regionale Events sichtbar | Events aus Nachbargemeinde angezeigt | 🟡 |
| T-APP-011 | NF-Perf | App-Größe <50MB | APK/IPA Größenprüfung | 🟡 |
| T-APP-012 | NF-A11y | VoiceOver navigierbar | Alle Elemente haben Labels | 🟡 |

---

## 5. Automatisierter Testprozess

### Ablauf nach Deployment:
```
1. git push → GitHub Actions triggered
2. Build & Deploy auf GitHub Pages
3. Warten bis Deployment live (30s)
4. Playwright E2E Tests ausführen
5. Lighthouse Audit ausführen
6. Ergebnisse sammeln
7. Report erstellen
8. Dino via Discord informieren (✅ oder ❌)
```

### Bei Fehler:
- ❌ Test fehlgeschlagen → Dino sofort informieren mit Details
- ⚠️ Warning (Performance/A11y unter Schwelle) → In Report aufnehmen

### Reporting-Format:
```
🧪 Test-Report: Poxdorf Landingpage
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ T-LP-001: Seite lädt (200 OK)
✅ T-LP-002: Wappen sichtbar
✅ T-LP-003: "Poxdorf" gefunden
❌ T-LP-004: "Dorf" gefunden in Zeile 42
...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ergebnis: 14/15 bestanden (93%)
Performance: 92/100
Accessibility: 95/100
```

---

## 6. Test-Infrastruktur

| Tool | Zweck | Phase |
|------|-------|-------|
| **Playwright** | E2E Browser-Tests | Phase 1 (jetzt) |
| **Lighthouse CI** | Performance + A11y | Phase 1 (jetzt) |
| **GitHub Actions** | CI/CD Pipeline | Phase 1 (jetzt) |
| **Flutter Test** | Unit + Widget Tests | Phase 2 |
| **Flutter Integration** | E2E App Tests | Phase 2 |
| **Firebase Test Lab** | Device Testing | Phase 3 |

---

*Wird fortlaufend erweitert wenn neue Features/Anforderungen dazukommen.*
