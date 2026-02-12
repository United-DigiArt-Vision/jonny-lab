# Product Requirements Document (PRD)
## City Apps — Poxdorf (Pilot)

| Feld | Wert |
|------|------|
| **Projekt** | City Apps |
| **Pilot** | Gemeinde Poxdorf (Oberfranken) |
| **Autor** | United DigiArt Vision |
| **Version** | 1.0 |
| **Erstellt** | 2026-02-06 |
| **Aktualisiert** | 2026-02-08 |
| **Status** | In Arbeit |

---

## 1. Executive Summary

City Apps ist eine Plattform für moderne Gemeinde-Apps, die die Brücke zwischen der realen und digitalen Welt baut. Wir starten mit der Gemeinde Poxdorf als Pilot und skalieren dann regional und überregional. Die App bietet Bürgern echten Mehrwert (Müllkalender, Veranstaltungen, Flyer Scanner) und wird kostenlos angeboten, um organisch Nutzung aufzubauen und die Gemeinde zur offiziellen Übernahme zu bewegen.

---

## 2. Problemstellung

### Ist-Zustand
- Viele kleine Gemeinden in Deutschland haben keine oder schlechte digitale Angebote
- Informationen sind verstreut (Aushänge, PDFs, Webseiten, schwarze Bretter)
- Bürger verpassen Veranstaltungen, Mülltermine, wichtige Meldungen
- 56% Bürger-Unzufriedenheit mit bestehenden Stadt-Apps (Telekom-Studie)
- OZG-Pflicht: Kommunen MÜSSEN bis 2028 digitale Services anbieten

### Soll-Zustand
- Eine zentrale, benutzerfreundliche App pro Gemeinde
- Alle relevanten Informationen an einem Ort
- Proaktive Benachrichtigungen (Push)
- Bürger können selbst Inhalte beitragen (Flyer Scanner)
- Regionale Vernetzung zwischen Gemeinden

### Lücke
- Bestehende Lösungen (Heimat-Info, etc.) sind generisch, unpersönlich, nicht Premium
- Kein Anbieter bietet Flyer-zu-Event Digitalisierung
- Kein Anbieter bietet adressbasierte Müll-Push-Erinnerungen
- Bestehende Apps bieten kein regionales Netzwerk

---

## 3. Zielgruppen & Personas

### Persona 1: Maria (68, Rentnerin)
- **Technik-Level:** Gering (WhatsApp, gelegentlich Facebook)
- **Bedürfnis:** Mülltermine nicht vergessen, wissen was im Ort los ist
- **Schmerzpunkt:** Muss immer den Papier-Müllkalender suchen
- **Erwartung:** Einfach, übersichtlich, große Schrift
- **Schlüssel-Feature:** Müllkalender mit Push

### Persona 2: Thomas (42, Familienvater)
- **Technik-Level:** Mittel (nutzt Apps täglich)
- **Bedürfnis:** Kinderaktivitäten finden, Gemeinde-News
- **Schmerzpunkt:** Erfährt von Events oft zu spät
- **Erwartung:** Modern, schnell, zuverlässig
- **Schlüssel-Feature:** Veranstaltungskalender mit Push

### Persona 3: Lisa (35, Vereinsvorsitzende)
- **Technik-Level:** Hoch
- **Bedürfnis:** Vereinstermine bewerben, Mitglieder erreichen
- **Schmerzpunkt:** Erstellt Flyer, aber Reichweite ist gering
- **Erwartung:** Einfach Events teilen, Feedback bekommen
- **Schlüssel-Feature:** Flyer Scanner + Event-Sharing

### Persona 4: Bürgermeister Müller (55)
- **Technik-Level:** Mittel
- **Bedürfnis:** Bürger informieren, moderne Gemeinde darstellen
- **Schmerzpunkt:** Kein Budget für teure Lösungen, IT-Abteilung fehlt
- **Erwartung:** Fertige Lösung, wenig Aufwand, gutes Preis-Leistung
- **Schlüssel-Feature:** Admin-Dashboard, Nutzungsstatistiken

---

## 4. User Stories

### Müllkalender
| ID | Als... | möchte ich... | damit ich... | Prio |
|----|--------|---------------|--------------|------|
| US-001 | Bürger | meine Adresse eingeben | die richtigen Mülltermine sehe | 🔴 |
| US-002 | Bürger | am Vorabend eine Push-Erinnerung bekommen | keine Tonne vergesse | 🔴 |
| US-003 | Bürger | sehen welche Tonne morgen dran ist | die richtige rausstelle | 🔴 |
| US-004 | Bürger | die Termine in meinen Kalender exportieren | alles an einem Ort habe | 🟡 |
| US-005 | Bürger | meinen Standort per GPS nutzen | nicht tippen muss | 🟡 |

### Veranstaltungen
| ID | Als... | möchte ich... | damit ich... | Prio |
|----|--------|---------------|--------------|------|
| US-010 | Bürger | alle Events in Poxdorf sehen | nichts verpasse | 🔴 |
| US-011 | Bürger | an einem Event "Interessiert" klicken | eine Erinnerung bekomme | 🟡 |
| US-012 | Bürger | Events aus Nachbargemeinden sehen | auch regionale Events finde | 🟡 |
| US-013 | Bürger | Events nach Kategorie filtern | schnell finde was mich interessiert | 🟢 |

### Flyer Scanner
| ID | Als... | möchte ich... | damit ich... | Prio |
|----|--------|---------------|--------------|------|
| US-020 | Bürger | einen Flyer/Poster fotografieren | die Infos automatisch in die App kommen | 🔴 |
| US-021 | Bürger | die erkannten Daten korrigieren können | alles korrekt ist bevor es live geht | 🔴 |
| US-022 | Bürger | sehen was andere gescannt haben | ich neue Events entdecke | 🟡 |
| US-023 | Moderator | eingescannte Events prüfen/freigeben | keine falschen Infos erscheinen | 🔴 |

### Nachrichten
| ID | Als... | möchte ich... | damit ich... | Prio |
|----|--------|---------------|--------------|------|
| US-030 | Bürger | aktuelle Meldungen der Gemeinde sehen | informiert bin | 🔴 |
| US-031 | Bürger | Push bei wichtigen Meldungen bekommen | nichts Wichtiges verpasse | 🟡 |
| US-032 | Admin | News-Artikel verfassen und posten | Bürger informieren kann | 🟡 |

### Kirchliche Veranstaltungen (NEU — Bürgerfeedback 08.02.2026)
| ID | Als... | möchte ich... | damit ich... | Prio |
|----|--------|---------------|--------------|------|
| US-050 | Bürger | Gottesdienst-Zeiten sehen | weiß wann der nächste Gottesdienst ist | 🔴 |
| US-051 | Bürger | Kirchliche Feste und Feiern im Kalender sehen | keine kirchlichen Events verpasse | 🔴 |
| US-052 | Bürger | Push-Erinnerung für kirchliche Events | rechtzeitig daran erinnert werde | 🟡 |
| US-053 | Kirchengemeinde | eigene Events einstellen | die Gemeinde informiert ist | 🟡 |
| US-054 | Bürger | Kontaktdaten der Kirchengemeinde finden | Ansprechpartner erreiche | 🟢 |

### Bushaltestellen / ÖPNV (NEU — Bürgerfeedback 08.02.2026)
| ID | Als... | möchte ich... | damit ich... | Prio |
|----|--------|---------------|--------------|------|
| US-060 | Bürger | alle Bushaltestellen in Poxdorf auf einer Karte sehen | weiß wo ich hinmuss | 🔴 |
| US-061 | Bürger | Abfahrtszeiten und Linien pro Haltestelle sehen | den Bus nicht verpasse | 🔴 |
| US-062 | Bürger | die nächste Haltestelle per GPS finden | schnell den nächsten Bus finde | 🟡 |
| US-063 | Bürger | Verspätungen/Ausfälle per Push erfahren | nicht umsonst warte | 🟢 |
| US-064 | Bürger | Verbindungen in Nachbarorte sehen | weiß wie ich hinkomme | 🟡 |

### Notfall & Kontakte
| ID | Als... | möchte ich... | damit ich... | Prio |
|----|--------|---------------|--------------|------|
| US-040 | Bürger | wichtige Nummern schnell finden | im Notfall sofort anrufen kann | 🔴 |
| US-041 | Bürger | Kontakte auch offline sehen | auch ohne Internet Hilfe finde | 🔴 |
| US-042 | Bürger | Rathaus-Öffnungszeiten sehen | nicht vor verschlossener Tür stehe | 🟡 |

---

## 5. Funktionale Anforderungen

### F-001: Müllkalender
- **Eingabe:** Adresse (GPS oder manuell mit Autocomplete)
- **Verarbeitung:** Adresse → Abfuhrgebiet → Termine laden
- **Ausgabe:** Kalenderansicht mit farbcodierten Mülltypen
- **Push:** Vorabend-Erinnerung (konfigurierbar: 18:00, 19:00, 20:00)
- **Export:** ICS-Datei für externen Kalender
- **Mülltypen:** Restmüll, Papier, Gelbe Tonne, Bio, Grünschnitt, Sperrmüll, Glas
- **Datenquelle:** Awido API / Regio IT / CSV-Import

### F-002: Veranstaltungskalender
- **Ansichten:** Liste, Kalender (Monat/Woche), Karte
- **Filter:** Kategorie, Datum, Entfernung
- **Kategorien:** Fest, Konzert, Markt, Sport, Kirche, Verein, Kinder, Senioren, Kultur, Sonstiges
- **Aktion:** "Interessiert" markieren → Push-Erinnerung 1h vorher
- **Regional:** Events aus konfigurierbarem Radius (5km, 10km, 20km)
- **Sharing:** Event per WhatsApp/SMS teilen

### F-003: Flyer Scanner
- **Eingabe:** Foto aus Kamera oder Galerie
- **Verarbeitung:** 
  1. Texterkennung auf Bild
  2. Strukturierte Daten extrahieren (Name, Datum, Uhrzeit, Ort, Beschreibung)
  3. Kategorie vorschlagen
- **Review:** Nutzer bestätigt/korrigiert erkannte Daten
- **Moderation:** Event geht in Warteschlange → Moderator gibt frei
- **Duplikat:** Warnung wenn ähnliches Event bereits existiert
- **Output:** Neuer Eintrag in Veranstaltungskalender + News-Feed

### F-004: Nachrichten
- **Typen:** Offiziell, Verein, Baustelle/Sperrung, Warnung, Allgemein
- **Ansicht:** Chronologischer Feed mit Bildern
- **Push:** Konfigurierbar pro Typ (z.B. nur Warnungen)
- **Admin:** CMS-ähnliche Eingabemaske (Web-Dashboard)

### F-005: Notfallinformationen
- **Inhalte:** Ärzte, Apotheken (Notdienst), Feuerwehr, Polizei, Krankenhaus
- **Offline:** Komplett ohne Internet verfügbar
- **Aktion:** Direktes Anrufen per Tap
- **Aktualisierung:** Bei Internetverbindung automatisch synchronisieren

### F-006: Gemeindekontakte
- **Inhalte:** Rathaus, Vereine, Kirchen, Schulen, Kindergärten
- **Details:** Name, Adresse, Telefon, Email, Öffnungszeiten
- **Aktion:** Anrufen, E-Mail, Navigation (Maps öffnen)
- **Kategorien:** Verwaltung, Vereine, Bildung, Gesundheit, Freizeit

### F-008: Kirchliche Veranstaltungen (NEU — Bürgerfeedback 08.02.2026)
- **Quelle:** Kirchengemeinde selbst oder Flyer Scanner
- **Inhalte:** Gottesdienst-Zeiten (regelmäßig), Feste, Feiern, Konzerte, Basare
- **Kategorien:** Gottesdienst, Kirchenfest, Konzert, Gemeindeabend, Sonstiges
- **Kalender:** Eigener Filter "Kirche" im Veranstaltungskalender
- **Push:** Erinnerung vor Gottesdiensten/Events (konfigurierbar)
- **Kontakt:** Pfarrbüro-Kontaktdaten (Telefon, Email, Öffnungszeiten)
- **Datenquelle:** Manuell (Kirchengemeinde) oder Flyer Scanner
- **Hinweis:** In kleinen Gemeinden ist die Kirche DER Veranstaltungs-Hub — hohe Priorität!

### F-009: Bushaltestellen / ÖPNV (NEU — Bürgerfeedback 08.02.2026)
- **Kartenansicht:** Alle Bushaltestellen in Poxdorf und Umgebung auf Karte
- **Haltestellendetails:** Name, Linien, Abfahrtszeiten, Richtungen
- **Nächste Haltestelle:** GPS-basiert die nächste Haltestelle finden
- **Fahrplan:** Statischer Fahrplan pro Haltestelle (PDF oder strukturiert)
- **Echtzeit (optional v2):** Live-Abfahrtszeiten via VGN/DELFI API
- **Verbindungssuche (optional v2):** Von A nach B mit Umsteigemöglichkeiten
- **Datenquelle:** VGN (Verkehrsverbund Großraum Nürnberg) — Poxdorf liegt im VGN-Gebiet
- **Offline:** Statische Fahrpläne auch ohne Internet verfügbar
- **Hinweis:** Direkte Bürgernachfrage — Haltestellen-Abdeckung ist Thema in ländlichen Gebieten

### F-007: Regionales Netzwerk
- **Cross-Community:** Events/News aus verbundenen Gemeinden anzeigen
- **Konfigurierbar:** Nutzer wählt welche Nachbargemeinden sichtbar
- **Kennzeichnung:** Klare Markierung aus welcher Gemeinde der Inhalt stammt
- **Einheitliche Datenstruktur:** Alle Gemeinden nutzen identisches Schema

---

## 6. Nicht-funktionale Anforderungen

### Performance
| Anforderung | Zielwert |
|-------------|----------|
| App-Start (Cold) | < 2 Sekunden |
| Seitennavigation | < 500ms |
| Push-Zustellung | < 30 Sekunden |
| API-Antwortzeit | < 200ms (p95) |
| App-Größe | < 50 MB |

### Verfügbarkeit
| Anforderung | Zielwert |
|-------------|----------|
| Uptime Backend | 99.5% |
| Offline-Funktionalität | Notfallinfos, Kontakte, zuletzt geladene Daten |
| Datensynchronisierung | Automatisch bei Internetverbindung |

### Sicherheit
| Anforderung | Detail |
|-------------|--------|
| Datenschutz | DSGVO-konform |
| Datenübertragung | TLS 1.3 (HTTPS) |
| Authentifizierung | Optional (für Flyer Scanner Pflicht) |
| Standortdaten | Nur lokal verarbeitet, nicht gespeichert |
| Personenbezogene Daten | Minimal: nur Adresse für Müllkalender |

### Accessibility
| Anforderung | Detail |
|-------------|--------|
| Screen Reader | VoiceOver (iOS) + TalkBack (Android) |
| Schriftgröße | Dynamisch (System-Einstellung) |
| Kontrast | WCAG AA (4.5:1 minimum) |
| Bedienung | Einhändig möglich |
| Sprache | Deutsch (weitere Sprachen later) |

### Design
| Anforderung | Detail |
|-------------|--------|
| Design-Level | Premium ("Dubai-Level") |
| Personalisierung | Gemeinde-Wappen, Name, Farben pro Gemeinde |
| Dark Mode | Unterstützt |
| Responsive | Optimiert für iPhone SE bis iPad |
| Konsistenz | Material Design 3 / Cupertino Guidelines |

---

## 7. Datenmodell

### Gemeinde
```json
{
  "id": "poxdorf-oberfranken",
  "name": "Poxdorf",
  "state": "Bayern",
  "district": "Forchheim",
  "population": 800,
  "area_km2": 5.2,
  "zip": "91099",
  "wappen_url": "assets/wappen/poxdorf.png",
  "primary_color": "#166534",
  "coordinates": { "lat": 49.67, "lng": 11.07 },
  "neighbors": ["pinzberg", "effeltrich", "kunreuth", "wiesenthau"],
  "created_at": "2026-02-07T00:00:00Z"
}
```

### Event
```json
{
  "id": "evt_abc123",
  "gemeinde_id": "poxdorf-oberfranken",
  "title": "Sommerfest Poxdorf",
  "description": "Großes Sommerfest mit Live-Musik und Essen.",
  "category": "fest",  // fest|konzert|markt|sport|kirche|verein|kinder|senioren|kultur|oepnv|sonstiges
  "date_start": "2026-07-15T14:00:00+02:00",
  "date_end": "2026-07-15T22:00:00+02:00",
  "location": {
    "name": "Hauptplatz Poxdorf",
    "address": "Hauptstraße 1, 91099 Poxdorf",
    "coordinates": { "lat": 49.67, "lng": 11.07 }
  },
  "organizer": "Gemeinde Poxdorf",
  "contact": "info@poxdorf.de",
  "price": "Eintritt frei",
  "source": "flyer_scan",
  "source_image_url": "uploads/flyer_abc123.jpg",
  "status": "approved",
  "created_by": "user_xyz",
  "approved_by": "moderator_001",
  "created_at": "2026-07-01T10:00:00Z"
}
```

### Mülltermin
```json
{
  "id": "muell_001",
  "gemeinde_id": "poxdorf-oberfranken",
  "district": "Bezirk-A",
  "waste_type": "restmuell",
  "date": "2026-03-15",
  "streets": ["Hauptstraße 1-50", "Kirchweg"],
  "created_at": "2026-01-01T00:00:00Z"
}
```

### News
```json
{
  "id": "news_001",
  "gemeinde_id": "poxdorf-oberfranken",
  "title": "Straßensperrung Kirchweg",
  "body": "Der Kirchweg ist vom 15.-20. März wegen Bauarbeiten gesperrt.",
  "type": "baustelle",
  "image_url": "uploads/news_001.jpg",
  "push_sent": true,
  "published_at": "2026-03-10T08:00:00Z",
  "created_by": "admin_001"
}
```

### Kontakt
```json
{
  "id": "contact_001",
  "gemeinde_id": "poxdorf-oberfranken",
  "name": "Rathaus Poxdorf",
  "category": "verwaltung",
  "address": "Hauptstraße 1, 91099 Poxdorf",
  "phone": "+49 9191 12345",
  "email": "info@poxdorf.de",
  "hours": {
    "mo": "08:00-12:00",
    "di": "08:00-12:00, 14:00-16:00",
    "mi": "08:00-12:00",
    "do": "08:00-12:00, 14:00-18:00",
    "fr": "08:00-12:00"
  },
  "coordinates": { "lat": 49.67, "lng": 11.07 }
}
```

### Bushaltestelle (NEU — 08.02.2026)
```json
{
  "id": "stop_001",
  "gemeinde_id": "poxdorf-oberfranken",
  "name": "Poxdorf Ortsmitte",
  "coordinates": { "lat": 49.67, "lng": 11.07 },
  "lines": [
    {
      "line": "222",
      "direction": "Forchheim Bahnhof",
      "operator": "VGN",
      "schedule": [
        { "time": "06:45", "days": "Mo-Fr" },
        { "time": "07:15", "days": "Mo-Fr" },
        { "time": "12:30", "days": "Mo-Sa" }
      ]
    }
  ],
  "facilities": ["shelter", "bench"],
  "accessible": false
}
```

---

## 8. API-Spezifikation (Überblick)

### REST API Endpunkte

| Methode | Endpunkt | Beschreibung |
|---------|----------|--------------|
| GET | /api/v1/gemeinden/{id} | Gemeinde-Details |
| GET | /api/v1/gemeinden/{id}/events | Events einer Gemeinde |
| POST | /api/v1/gemeinden/{id}/events | Neues Event erstellen |
| GET | /api/v1/gemeinden/{id}/muell?street={s} | Mülltermine für Adresse |
| GET | /api/v1/gemeinden/{id}/news | Nachrichten |
| GET | /api/v1/gemeinden/{id}/kontakte | Kontakte |
| POST | /api/v1/flyer/scan | Flyer-Bild analysieren |
| GET | /api/v1/events/regional?lat={}&lng={}&radius={} | Regionale Events |
| GET | /api/v1/gemeinden/{id}/events?category=kirche | Kirchliche Events |
| GET | /api/v1/gemeinden/{id}/haltestellen | Bushaltestellen |
| GET | /api/v1/haltestellen/{id}/abfahrten | Abfahrtszeiten einer Haltestelle |
| GET | /api/v1/haltestellen/nearby?lat={}&lng={} | Nächste Haltestellen (GPS) |

### Authentifizierung
- **Lesen:** Öffentlich (kein Auth nötig)
- **Schreiben:** Bearer Token (registrierte User)
- **Admin:** Separater Admin-Token

---

## 9. UI/UX Anforderungen

### Navigation (Bottom Tab Bar)
1. 🏠 **Home** — Übersicht (nächster Mülltermin, nächste Events, letzte News)
2. 📅 **Kalender** — Veranstaltungen + Müll
3. 📸 **Scanner** — Flyer fotografieren (zentraler prominenter Button)
4. 📰 **News** — Nachrichten-Feed
5. ☰ **Mehr** — Kontakte, Notfall, Einstellungen

### Home-Screen
- Gemeinde-Wappen + Name oben
- "Nächste Müllabfuhr" Widget (farbcodiert)
- "Nächste Events" Karussell
- "Aktuelle News" Top-3

### Farbschema (pro Gemeinde konfigurierbar)
- **Poxdorf:** Grün (#166534) — angelehnt an Natur/Ländlich
- **Mülltypen:** Festgelegt (Restmüll=Grau, Papier=Blau, Gelbe Tonne=Gelb, Bio=Braun)

---

## 10. Akzeptanzkriterien

### MVP Release (v1.0)
- [ ] Bürger kann Adresse eingeben und Mülltermine sehen
- [ ] Push-Erinnerung kommt am Vorabend (±5 Min Genauigkeit)
- [ ] Veranstaltungskalender zeigt mindestens 5 Test-Events
- [ ] Flyer Scanner erkennt Datum + Titel in >80% der Fälle
- [ ] Nachrichten-Feed lädt in <2 Sekunden
- [ ] Notfall-Kontakte sind offline verfügbar
- [ ] App startet in <2 Sekunden
- [ ] Funktioniert auf iOS 16+ und Android 10+
- [ ] DSGVO-konform (Datenschutzerklärung vorhanden)
- [ ] Poxdorf-Wappen und Name korrekt dargestellt

### Regionales Netzwerk (v1.1)
- [ ] Bürger in Poxdorf sieht Events aus Pinzberg
- [ ] Filter "Nur Poxdorf" / "Auch Umgebung" funktioniert
- [ ] Herkunftsgemeinde ist bei jedem Event sichtbar

---

## 11. Abhängigkeiten & Risiken

### Abhängigkeiten
| Abhängigkeit | Status | Risiko |
|--------------|--------|--------|
| Müll-Datenquelle (Awido/CSV) | ⏳ Noch nicht geklärt | 🟡 Mittel |
| Apple Developer Account | ⏳ Noch nicht vorhanden | 🟡 Mittel |
| Google Play Account | ⏳ Noch nicht vorhanden | 🟢 Niedrig |
| Firebase/Supabase Setup | ⏳ Noch nicht eingerichtet | 🟢 Niedrig |
| Gemeinde-Kooperation | ⏳ Brief noch nicht gesendet | 🟡 Mittel |

### Risiken
| Risiko | Wahrscheinlichkeit | Impact | Mitigation |
|--------|---------------------|--------|------------|
| Gemeinde lehnt Kooperation ab | Mittel | Mittel | Bottom-Up Strategie (Nutzung zuerst) |
| Müll-Daten nicht verfügbar | Niedrig | Hoch | Alternative Quellen (PDF, manuell) |
| Geringe Nutzerakzeptanz | Niedrig | Hoch | Premium-Design, echten Mehrwert bieten |
| Konkurrenz kopiert Features | Mittel | Niedrig | Schnell sein, Netzwerkeffekt aufbauen |
| Datenschutz-Bedenken | Niedrig | Hoch | DSGVO-konform, minimal Daten |

---

## 12. Meilensteine & Timeline

| Meilenstein | Ziel-Datum | Status |
|-------------|-----------|--------|
| Landingpage live | 2026-02-07 | ✅ Erledigt |
| Flyer Scanner Prototyp | 2026-02-07 | ✅ Erledigt |
| PRD fertiggestellt | 2026-02-07 | ✅ Erledigt |
| Flutter Grundgerüst | 2026-02-14 | ⏳ |
| Müll-Datenquelle geklärt | 2026-02-14 | ⏳ |
| MVP (v1.0) intern testbar | 2026-03-01 | ⏳ |
| Brief an Bürgermeister | 2026-03-01 | ⏳ |
| App Store / Play Store | 2026-03-15 | ⏳ |
| Erste Nutzerzahlen | 2026-04-01 | ⏳ |
| Zweite Gemeinde | 2026-04-15 | ⏳ |

---

## 13. Erfolgsmetriken

| Metrik | Ziel (3 Monate) | Ziel (12 Monate) |
|--------|------------------|-------------------|
| Downloads | 100 | 500 |
| Aktive Nutzer (MAU) | 50 | 300 |
| Gescannte Flyer | 20 | 200 |
| Events im Kalender | 30 | 300 |
| Push-Zustellrate | >95% | >95% |
| App-Bewertung | >4.0 ⭐ | >4.5 ⭐ |
| Gemeinden angeschlossen | 1 | 5 |
| Fläche Deutschland (%) | 0.001% | 0.01% |
| Monatlicher Umsatz | €0 (kostenlos) | €295+ |

---

## 14. Offene Fragen

- [ ] Welche Müll-Datenquelle für Poxdorf? (Awido? CSV von Gemeinde?)
- [ ] Apple Developer Account — wer zahlt? (Gemeinde vs. wir)
- [ ] Soll es ein Web-Admin-Dashboard von Anfang an geben?
- [ ] Moderations-Workflow: Wer genehmigt gescannte Flyer?
- [ ] Sollen Nutzer sich registrieren müssen?
- [ ] Welche Push-Infrastruktur? (Firebase Cloud Messaging?)
- [ ] VGN-API Zugang für Echtzeitdaten? (oder erstmal statische Fahrpläne?)
- [ ] Welche Bushaltestellen gibt es genau in Poxdorf? (Bürgerin hat aufgezählt)
- [ ] Kontakt zur Kirchengemeinde Poxdorf für Veranstaltungsdaten?
- [ ] Gottesdienst-Zeiten: regelmäßig genug für automatischen Kalender?

---

## Anhänge

- **FEATURES.md** — Detaillierte Feature-Beschreibungen
- **STRATEGY.md** — Verkaufs- & Go-to-Market-Strategie  
- **NOTES.md** — Chronologische Besprechungsnotizen
- **research/** — Markt- & Wettbewerbsanalyse
- **poxdorf/** — Landingpage (live: digit500.github.io/poxdorf-app)
- **prototypes/flyer-to-event/** — Flyer Scanner Prototyp

---

*Dieses PRD wird fortlaufend aktualisiert. Jede Änderung wird mit Datum vermerkt.*
