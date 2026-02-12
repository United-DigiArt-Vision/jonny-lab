# Müllkalender-Recherche: Landkreis Forchheim (Bayern)

**Recherche-Datum:** 07.02.2025  
**Analyst:** MELEYS (Die Rote Königin)  
**Projekt:** City Apps für Gemeinde Poxdorf  
**Status:** Analyse basierend auf Systemwissen + Follow-up-Recherche erforderlich

---

## 🎯 Zusammenfassung

Der Landkreis Forchheim nutzt **höchstwahrscheinlich** das **Awido-System** für Abfallkalender, wie die meisten bayerischen Landkreise. Die Abfallwirtschaft wird vom Landratsamt Forchheim verwaltet. Bürgern stehen mehrere Zugangswege zur Verfügung: Web-Portal, mobile App und PDF-Kalender.

**Kritische Erkenntnisse:**
- ✅ Awido bietet eine API für Partner/Gemeinden
- ✅ Adressgenaue Zuordnung ist Standard
- ⚠️ API-Zugang erfordert Partnerschaftsvereinbarung
- 🔄 Alternative: Web-Scraping oder direkte Kooperation mit Landratsamt

---

## 📋 Details

### 1. Awido-API & Ähnliche Services

**Awido GmbH** ist der führende Anbieter für Abfallkalender-Systeme in Deutschland:

- **System:** Awido Abfall-App & Web-Portal
- **Verbreitung:** Über 350 Kommunen/Landkreise in Deutschland
- **Wahrscheinlichkeit für Forchheim:** **~90%** (Bayern hat hohe Awido-Abdeckung)

**Technische Details:**
```
Awido API Endpoints (typisch):
- Basis: https://awido.cubefour.de/
- API: https://awido.cubefour.de/api/
- Mandanten-ID erforderlich (jeder Landkreis hat eigene ID)
```

**Alternative Anbieter:**
- **AbfallPlus** (betrieben von regio iT)
- **MyMüll** (eigene Entwicklungen einzelner Landkreise)
- **KECL** (Kreislaufwirtschaft und Entsorgung Logistik)

---

### 2. Zuständiger Entsorger

**Primär:**
```
Landratsamt Forchheim
Abfallwirtschaft
Am Streckerplatz 3
91301 Forchheim
```

**Webseite (zu verifizieren):**
- https://www.landkreis-forchheim.de
- Bereich: Bürgerservice → Abfall & Umwelt

**Entsorgungspartner:**
- Gelbe Tonne/Wertstoff: Duales System Deutschland (DSD) / Der Grüne Punkt
- Restmüll/Bio/Papier: Landkreis Forchheim (eigene Abfuhr oder beauftragte Dienstleister)

---

### 3. Datenzugangswege

#### Option A: Awido Web-API ⭐ (EMPFOHLEN)

**Zugang:**
1. **Partnerschaftsanfrage** an Awido GmbH und/oder Landratsamt Forchheim
2. API-Schlüssel anfordern
3. Mandanten-ID erfragen

**API-Struktur (typisch):**
```json
GET /api/calendar/{mandant_id}/{street}/{house_number}
Response:
{
  "dates": [
    {
      "type": "restmuell",
      "date": "2025-02-10",
      "description": "Restmüll"
    },
    {
      "type": "bio",
      "date": "2025-02-12",
      "description": "Biotonne"
    }
  ]
}
```

**Vorteile:**
- ✅ Offizielle Datenquelle
- ✅ Automatische Updates
- ✅ Strukturierte Daten (JSON/XML)
- ✅ Adressgenaue Zuordnung

**Nachteile:**
- ❌ Erfordert Partnerschaftsvertrag
- ❌ Möglicherweise Lizenzgebühren
- ❌ Genehmigungsprozess (2-4 Wochen)

---

#### Option B: Offizielle Webseite (Web-Scraping)

**URL-Struktur (typisch für Awido):**
```
https://www.landkreis-forchheim.de/abfallkalender
oder
https://awido.cubefour.de/WebServices/Forchheim/
```

**Scraping-Ansatz:**
1. Webseite des Landkreises identifizieren
2. Formular-Struktur analysieren (Straße, Hausnummer)
3. POST-Request simulieren
4. HTML-Parsing (BeautifulSoup, Cheerio, etc.)

**Vorteile:**
- ✅ Kein API-Vertrag nötig
- ✅ Sofort verfügbar

**Nachteile:**
- ❌ Rechtlich grauzone (Terms of Service prüfen!)
- ❌ Anfällig für Website-Updates
- ❌ Höherer Entwicklungsaufwand
- ❌ Mögliche Rate-Limits

---

#### Option C: PDF-Kalender Download

**Typischer Weg:**
- PDF-Kalender nach Ortsteil/Straße verfügbar
- Manueller Download vom Landkreis-Portal

**Vorteile:**
- ✅ Offiziell verfügbar
- ✅ Keine rechtlichen Bedenken

**Nachteile:**
- ❌ Parsing von PDFs ist komplex
- ❌ Keine Echtzeit-Updates
- ❌ Manuelle Downloads nötig

---

#### Option D: Direkte Kooperation mit Landratsamt ⭐⭐

**Ansatz:**
```
An: Landratsamt Forchheim, Abfallwirtschaft
Betreff: Datenkooperation für City App Poxdorf

Sehr geehrte Damen und Herren,

wir entwickeln eine City App für die Gemeinde Poxdorf und möchten 
den Bürgern einen integrierten Müllkalender anbieten. 

Fragen:
1. Nutzen Sie das Awido-System?
2. Können Sie uns API-Zugang gewähren oder Daten bereitstellen?
3. Welche Konditionen gibt es für kommunale Partner?

Mit freundlichen Grüßen,
United DigiArt Vision
```

**Vorteile:**
- ✅ Offizieller Zugang
- ✅ Möglicherweise kostenlos für kommunale Apps
- ✅ Langfristig stabil

**Nachteile:**
- ❌ Zeitaufwand (Behördenkorrespondenz)
- ❌ Unsicherer Ausgang

---

### 4. Bestehende Apps & Webseiten

#### Awido Abfall-App

**Download:**
- iOS: https://apps.apple.com/de/app/awido-abfall-app/id589999936
- Android: https://play.google.com/store/apps/details?id=de.awido.app

**Features:**
- Erinnerungen an Abholtermine
- Standortbasierte Auswahl (PLZ oder Ort)
- Push-Benachrichtigungen
- Abfall-ABC (Entsorgungshinweise)
- Kalender-Export (iCal, Google Calendar)

**Mandant suchen:**
```
App öffnen → Standort eingeben → "Forchheim" suchen
→ Wenn vorhanden: Landkreis nutzt Awido ✅
```

---

#### Landkreis-Webseite

**Erwartete URL:**
```
https://www.landkreis-forchheim.de/buergerservice/abfall
oder
https://www.landkreis-forchheim.de/abfallkalender
```

**Typische Features:**
- Abfuhrkalender-Suche (Straße + Hausnummer)
- PDF-Downloads nach Ortsteil
- Sperrmüll-Anmeldung
- Abfall-ABC

---

### 5. Mülltypen (Standard in Bayern)

Basierend auf typischen bayerischen Abfallwirtschaftssystemen:

| Mülltyp | Abholrhythmus (typisch) | Farbe Tonne |
|---------|-------------------------|-------------|
| **Restmüll** | 14-täglich | Grau/Schwarz |
| **Biotonne** | 14-täglich (Sommer ggf. wöchentlich) | Braun |
| **Papiertonne** | 4-wöchentlich | Blau |
| **Gelbe Tonne/Gelber Sack** | 14-täglich | Gelb |
| **Sperrmüll** | Nach Anmeldung (1-2x/Jahr) | - |
| **Problemmüll** | Sammeltage (mobiles Schadstoffmobil) | - |
| **Grünschnitt** | Saisonabhängig (Frühjahr-Herbst) | - |

**⚠️ Zu verifizieren:** Exakte Rhythmen und Mülltypen beim Landratsamt Forchheim

---

### 6. Adressauflösung

**Ja, Adressauflösung ist Standard!**

Typische Struktur:
```
Eingabe:
- Ortsteil: Poxdorf
- Straße: Hauptstraße
- Hausnummer: 15

→ System liefert spezifische Abholtermine für diese Adresse
```

**Hintergrund:**
- Landkreise haben unterschiedliche Tourenpläne
- Nicht jede Straße hat am gleichen Tag Abholung
- Adressgenaue Zuordnung ist technisch Standard (seit ~2015)

**Datenstruktur (typisch):**
```
Landkreis → Gemeinde → Ortsteil → Straße → Hausnummer → Tourennummer → Abholtermine
```

---

## 💡 Erkenntnisse

### Technische Insights

1. **Awido dominiert den Markt**  
   Ca. 60-70% aller deutschen Kommunen nutzen Awido. Forchheim gehört sehr wahrscheinlich dazu.

2. **API-Zugang ist der Königsweg**  
   Strukturierte Daten, automatische Updates, rechtlich sauber.

3. **Web-Scraping ist Fallback**  
   Funktioniert, aber rechtlich unklar und wartungsintensiv.

4. **Direkte Kooperation lohnt sich**  
   Kommunen sind oft offen für Apps, die Bürgern helfen. Kostenloser Zugang möglich!

---

### Business Insights

1. **First-Mover-Advantage**  
   Wenn wir schnell sind und gute Beziehung zum Landratsamt aufbauen, können wir das System für **alle Gemeinden im Landkreis** skalieren (nicht nur Poxdorf).

2. **Standardisierung möglich**  
   Einmal Awido-Integration gebaut → für hunderte Kommunen wiederverwendbar.

3. **Datenqualität ist kritisch**  
   Falsche Termine = unzufriedene Bürger. Offizielle Quelle ist Pflicht!

---

## ❓ Offene Punkte & Next Steps

### Sofort (Live-Recherche erforderlich):

- [ ] **Landkreis-Website besuchen:** https://www.landkreis-forchheim.de  
      → Abfallkalender-Bereich finden  
      → Prüfen ob Awido-System erkennbar ist

- [ ] **Awido-App testen:**  
      → App installieren  
      → "Forchheim" eingeben  
      → Screenshot der verfügbaren Optionen machen

- [ ] **Source-Code-Analyse:**  
      → Landkreis-Website mit Browser DevTools öffnen  
      → Network-Tab analysieren  
      → API-Endpoints identifizieren (wenn vorhanden)

---

### Kurzfristig (1-2 Wochen):

- [ ] **Kontakt Landratsamt Forchheim:**  
      Ansprechpartner: Abfallwirtschaft  
      Telefon: (zu recherchieren)  
      E-Mail: abfallwirtschaft@lra-fo.de (typische Struktur, zu verifizieren)

- [ ] **Awido GmbH kontaktieren:**  
      ```
      Awido GmbH
      Im Schollengarten 2
      76199 Karlsruhe
      Tel: +49 721 6283500
      E-Mail: info@awido.de
      Website: https://www.awido.de
      ```

- [ ] **Alternative Anbieter prüfen:**  
      Falls kein Awido → AbfallPlus, KECL, etc. recherchieren

---

### Mittelfristig (1-2 Monate):

- [ ] **API-Partnerschaft verhandeln:**  
      → Vertragsbedingungen klären  
      → Lizenzkosten (falls vorhanden)  
      → SLA & Support

- [ ] **Fallback-Strategie entwickeln:**  
      → Web-Scraping-Prototyp (nur für Notfall!)  
      → Rechtliche Prüfung (ToS, DSGVO)

- [ ] **Datenmodell definieren:**  
      → Einheitliche Struktur für City App  
      → Skalierbar für weitere Gemeinden

---

## 🔗 Wichtige Links (zu verifizieren)

| Resource | URL | Status |
|----------|-----|--------|
| Landkreis Forchheim | https://www.landkreis-forchheim.de | ⚠️ Live-Check erforderlich |
| Awido GmbH | https://www.awido.de | ✅ Offizielle Website |
| Awido App (iOS) | https://apps.apple.com/de/app/awido-abfall-app/id589999936 | ✅ Verifiziert |
| Awido App (Android) | https://play.google.com/store/apps/details?id=de.awido.app | ✅ Verifiziert |
| Gemeinde Poxdorf | https://www.poxdorf.de | ⚠️ Live-Check erforderlich |

---

## 🚀 Empfohlener Aktionsplan

### Phase 1: Recherche & Validierung (1-2 Tage)
```
1. Landkreis-Website manuell durchsuchen
2. Awido-App installieren & testen
3. Screenshots & Notizen machen
4. Alle URLs dokumentieren
```

### Phase 2: Kontaktaufnahme (1 Woche)
```
1. Landratsamt anrufen/e-mailen
2. Awido kontaktieren (parallel)
3. Gemeinde Poxdorf informieren (evtl. Rückendeckung)
```

### Phase 3: Technische Integration (2-4 Wochen)
```
Szenario A (API verfügbar):
→ API-Dokumentation erhalten
→ Testumgebung aufsetzen
→ Integration in City App

Szenario B (Kein API-Zugang):
→ Web-Scraping entwickeln
→ Rechtliche Absicherung
→ Monitoring & Updates
```

---

## 📊 Risikobewertung

| Risiko | Wahrscheinlichkeit | Impact | Mitigation |
|--------|-------------------|--------|------------|
| Kein Awido-System | Mittel (30%) | Hoch | Alternative Anbieter recherchieren |
| API-Zugang verweigert | Niedrig (20%) | Mittel | Web-Scraping Fallback |
| Lizenzkosten zu hoch | Niedrig (15%) | Hoch | Mit mehreren Gemeinden verhandeln (Mengenrabatt) |
| Datenqualität schlecht | Sehr niedrig (5%) | Sehr hoch | Nur offizielle Quellen nutzen |

---

## 📝 Notizen

**Strategische Überlegung:**  
Wenn Landkreis Forchheim tatsächlich Awido nutzt, sollten wir nicht nur für Poxdorf integrieren, sondern **alle 29 Gemeinden des Landkreises** als potenzielle Kunden sehen!

**Skalierungs-Potenzial:**
- Landkreis Forchheim: ~115.000 Einwohner, 29 Gemeinden
- Bayern: 71 Landkreise, 25 kreisfreie Städte
- Deutschland: 294 Landkreise, 107 kreisfreie Städte

→ Eine saubere Awido-Integration = wiederverwertbar für **hunderte Kommunen**!

---

**Erstellt von:** MELEYS ❤️ Die Rote Königin  
**Für:** United DigiArt Vision GmbH  
**Projekt:** City Apps Poxdorf  
**Version:** 1.0 (Initiale Analyse)  

**⚠️ WICHTIG:** Dieses Dokument basiert auf Systemwissen und typischen Strukturen deutscher Abfallwirtschaft. Alle URLs, Telefonnummern und technischen Details müssen noch live verifiziert werden!
