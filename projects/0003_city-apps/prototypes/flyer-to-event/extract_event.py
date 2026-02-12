#!/usr/bin/env python3
"""
Flyer-to-Event Prototyp
Extrahiert Event-Informationen aus Flyern/Postern mittels GPT-4 Vision
"""

import base64
import json
import sys
from pathlib import Path

try:
    from openai import OpenAI
except ImportError:
    print("❌ OpenAI nicht installiert. Bitte: pip install openai")
    sys.exit(1)


def encode_image(image_path: str) -> str:
    """Bild als Base64 encodieren"""
    with open(image_path, "rb") as f:
        return base64.standard_b64encode(f.read()).decode("utf-8")


def get_image_type(path: str) -> str:
    """MIME-Type aus Dateiendung"""
    suffix = Path(path).suffix.lower()
    types = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".webp": "image/webp",
    }
    return types.get(suffix, "image/jpeg")


def extract_event_from_flyer(image_path: str) -> dict:
    """
    Analysiert ein Flyer-Bild und extrahiert strukturierte Event-Daten.
    """
    client = OpenAI()
    
    base64_image = encode_image(image_path)
    image_type = get_image_type(image_path)
    
    prompt = """Analysiere dieses Flyer/Poster-Bild und extrahiere alle Event-Informationen.

Antworte NUR mit einem JSON-Objekt in diesem Format:
{
    "event_name": "Name der Veranstaltung",
    "date": "YYYY-MM-DD (wenn erkennbar, sonst null)",
    "time_start": "HH:MM (wenn erkennbar, sonst null)",
    "time_end": "HH:MM (wenn erkennbar, sonst null)",
    "location": "Ort/Adresse der Veranstaltung",
    "description": "Kurze Beschreibung (2-3 Sätze)",
    "organizer": "Veranstalter (wenn erkennbar, sonst null)",
    "contact": "Kontaktinfo (wenn erkennbar, sonst null)",
    "category": "Eine von: dorffest, konzert, markt, sport, kirche, verein, kinder, senioren, kultur, sonstiges",
    "price": "Eintritt/Kosten (wenn erkennbar, sonst null)",
    "extracted_text": "Der gesamte erkannte Text vom Flyer"
}

Wenn etwas nicht erkennbar ist, setze den Wert auf null.
Antworte NUR mit dem JSON, keine Erklärungen."""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:{image_type};base64,{base64_image}",
                            "detail": "high"
                        }
                    }
                ]
            }
        ],
        max_tokens=1000,
    )
    
    result_text = response.choices[0].message.content.strip()
    
    # JSON aus Antwort extrahieren (falls in Codeblock)
    if "```json" in result_text:
        result_text = result_text.split("```json")[1].split("```")[0].strip()
    elif "```" in result_text:
        result_text = result_text.split("```")[1].split("```")[0].strip()
    
    return json.loads(result_text)


def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_event.py <bild-pfad>")
        print("Beispiel: python extract_event.py flyer.jpg")
        sys.exit(1)
    
    image_path = sys.argv[1]
    
    if not Path(image_path).exists():
        print(f"❌ Datei nicht gefunden: {image_path}")
        sys.exit(1)
    
    print(f"📸 Analysiere: {image_path}")
    print("🤖 GPT-4 Vision läuft...")
    
    try:
        event_data = extract_event_from_flyer(image_path)
        
        print("\n✅ Event extrahiert!\n")
        print("=" * 50)
        print(f"📌 {event_data.get('event_name', 'Unbekannt')}")
        print("=" * 50)
        
        if event_data.get('date'):
            print(f"📅 Datum: {event_data['date']}")
        if event_data.get('time_start'):
            time_str = event_data['time_start']
            if event_data.get('time_end'):
                time_str += f" - {event_data['time_end']}"
            print(f"🕐 Zeit: {time_str}")
        if event_data.get('location'):
            print(f"📍 Ort: {event_data['location']}")
        if event_data.get('category'):
            print(f"🏷️  Kategorie: {event_data['category']}")
        if event_data.get('organizer'):
            print(f"👤 Veranstalter: {event_data['organizer']}")
        if event_data.get('price'):
            print(f"💰 Eintritt: {event_data['price']}")
        if event_data.get('description'):
            print(f"\n📝 Beschreibung:\n{event_data['description']}")
        
        print("\n" + "=" * 50)
        print("📄 Vollständiges JSON:")
        print(json.dumps(event_data, indent=2, ensure_ascii=False))
        
        # JSON speichern
        output_path = Path(image_path).stem + "_event.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(event_data, f, indent=2, ensure_ascii=False)
        print(f"\n💾 Gespeichert: {output_path}")
        
    except json.JSONDecodeError as e:
        print(f"❌ JSON Parse Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Fehler: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
