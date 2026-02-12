# 0003 - City Apps (Städte-Apps für deutsche Kommunen)

**Projekt-ID:** 0003
**Erstellt:** 2026-02-06
**Status:** 🚧 Research & Konzeptphase

---

## 🎯 Ziel

Premium Stadt-Apps für deutsche Städte und Gemeinden entwickeln und verkaufen (B2G - Business to Government).

---

## 💡 Idee (Dino, 06.02.2026)

> "Viele Städte und Dörfer hier in Deutschland haben eine ziemlich schlechte App. Gegebenenfalls gar keine App. Meine Idee ist, dass wir für sie Apps entwickeln und verkaufen."

**Kern-Vision:**
- Premium-Look wie Dubai (DubaiNow als Vorbild)
- Wichtige Features wie Müllkalender mit Push-Erinnerungen
- Native Apps (kein WebView-Murks)

---

## 🔧 Tech Stack

| Komponente | Lösung | Begründung |
|------------|--------|------------|
| Framework | **Flutter** | Native Performance, eine Codebase für iOS + Android |
| Backend | TBD | Firebase? Supabase? Custom? |
| Push | Firebase Cloud Messaging | Standard für mobile Push |
| Design | Figma → Flutter | Premium UI/UX |

**Warum Flutter statt React Native:**
- Kompiliert zu nativem ARM-Code
- Premium-Look einfacher erreichbar
- Bessere Performance für komplexe UIs

---

## 📱 Kern-Features (MVP)

| Feature | Beschreibung | Priorität |
|---------|--------------|-----------|
| 🗑️ Müllkalender | + Push-Erinnerung "Morgen Gelbe Tonne!" | P0 |
| 📰 News | Stadtmitteilungen, Veranstaltungen | P0 |
| 📞 Mängelmelder | Foto + GPS → Stadt informieren | P1 |
| 🏛️ Bürgerservice | Öffnungszeiten, Kontakte, Formulare | P1 |
| 📍 POIs | Sehenswürdigkeiten, Parkplätze, etc. | P2 |
| 🚌 ÖPNV | Integration lokaler Verkehrsbetriebe | P2 |

---

## 🌍 Markt & Wettbewerb

### Goldstandard: DubaiNow
- 320+ Services von 50+ Behörden
- EINE App für ALLES
- Premium UX/UI

### Deutsche Konkurrenz

| Anbieter | Typ | Preis | Stärke | Schwäche |
|----------|-----|-------|--------|----------|
| **Citykey** (Telekom) | White-Label | Unbekannt (teuer?) | Brand, Standard | Wenig flexibel, corporate Look |
| **VillageApp** | SaaS | <€1/Einwohner/Jahr | Günstig | Basic Features |
| **Smart Village App** | Open Source | Setup-Kosten | Flexibel | Braucht Dev-Know-how |

### Unsere Marktlücke
- **Premium-Design** — Deutsche Apps sehen "funktional" aus, nicht "wow"
- **Flexibilität** — Individuell anpassbar, nicht Standard-Template
- **Moderne UX** — 2026, nicht 2015

---

## 💰 Geschäftsmodell (Entwurf)

**Zielgruppe:** Städte 10.000 - 100.000 Einwohner
- Zu klein für eigenes Dev-Team
- Zu groß um nichts zu haben
- Haben Digitalisierungsbudget

**Preisidee:**
- Setup-Fee: €5.000 - €15.000
- Monatlich: €200 - €500 (Hosting, Support, Updates)
- ODER: €0,50 - €1,50 pro Einwohner/Jahr

**App Store Strategie:**
- Stadt hat eigenen Apple Developer Account ($99/Jahr)
- Wir entwickeln, sie publishen unter ihrem Namen
- Professioneller + kein Risiko für uns

---

## 📋 Nächste Schritte

- [ ] UI/UX Mockups für "Musterstadt" erstellen
- [ ] Feature-Matrix definieren (was ist im Basis-Paket, was Add-on)
- [ ] Pitch-Deck für Kommunen
- [ ] Flutter-Prototyp bauen
- [ ] Erste Kommunen kontaktieren

---

## 📁 Projektstruktur

```
0003_city-apps/
├── README.md              ← Du bist hier
├── NOTES.md               ← Laufende Notizen
├── research/
│   └── market-analysis.md ← Marktanalyse (fertig)
└── design/
    └── (Mockups kommen hier)
```

---

## 🔗 Referenzen

- [DubaiNow](https://www.digitaldubai.ae/apps-services/details/dubai-now) — Goldstandard
- [Citykey](https://citykey.app/) — Deutsche Konkurrenz (Telekom)
- [VillageApp](https://www.villageapp.de) — Budget-Option
