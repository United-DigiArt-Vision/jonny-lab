# Flyer-to-Event Prototyp 📸➡️📅

Extrahiert automatisch Event-Informationen aus Flyern/Postern mittels GPT-4 Vision.

## Wie es funktioniert

1. Bürger fotografiert einen Flyer/Poster
2. Bild wird an GPT-4 Vision geschickt
3. AI extrahiert strukturierte Daten:
   - Event-Name
   - Datum & Uhrzeit
   - Ort
   - Beschreibung
   - Kategorie
   - Veranstalter
   - Kontakt
   - Preis

## Nutzung

```bash
# Voraussetzung: OpenAI API Key als OPENAI_API_KEY Umgebungsvariable

python extract_event.py flyer.jpg
```

## Output

```json
{
    "event_name": "Sommerfest Pinzberg",
    "date": "2026-07-15",
    "time_start": "14:00",
    "time_end": "22:00",
    "location": "Dorfplatz Pinzberg",
    "description": "Großes Sommerfest mit Live-Musik, Essen und Getränken.",
    "category": "dorffest",
    "organizer": "Gemeinde Pinzberg",
    "price": "Eintritt frei"
}
```

## Nächste Schritte

- [ ] Web-Interface für einfaches Upload
- [ ] Integration in City App API
- [ ] Duplikat-Erkennung
- [ ] Moderator-Review-Workflow
- [ ] Push-Notification wenn Event erstellt

## Teil der Vision

Dieses Feature macht jeden Bürger zum Digitalisierungs-Agenten für seine Gemeinde.
Real-World → Digital-World Transformation mit minimalem Aufwand.
