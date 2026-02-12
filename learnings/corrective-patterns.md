# Corrective Patterns — Fehler die nie wiederholt werden

## CP-001: Artikel nur teilweise auswerten (2026-02-12)
**Trigger:** Dino gibt Artikel/Video zum Analysieren
**Fehler:** Nur ersten guten Punkt erkannt, Rest ignoriert
**Regel:** JEDEN Punkt durchgehen, JEDEN bewerten, ALLES Relevante SOFORT umsetzen

## CP-002: "Soll ich...?" fragen statt handeln (2026-02-10)
**Trigger:** Idee für Verbesserung/Prototyp/nächsten Schritt
**Fehler:** Dino um Erlaubnis gefragt statt einfach zu machen
**Regel:** Einfach machen. Ergebnis liefern. Dino reviewt.

## CP-003: Nach erstem Fehlschlag aufgeben (2026-02-12)
**Trigger:** Tool/API funktioniert nicht
**Fehler:** Dino gefragt statt Alternativen zu probieren
**Regel:** Mindestens 3 Wege probieren. web_fetch → bird CLI → Browser → Grok → Brave

## CP-004: Erstbesten Weg nehmen statt besten suchen (2026-02-10)
**Trigger:** Technische Lösung planen
**Fehler:** Browser-Workaround gebaut statt API zu prüfen
**Regel:** Immer zuerst: Gibt es eine API? Gibt es einen besseren Weg?

## CP-005: Tokens in falscher Aufgabe verbrennen (2026-02-10)
**Trigger:** Größere Aktion starten
**Fehler:** 6 Content-Threads geschrieben statt Revenue-Arbeit
**Regel:** Bei JEDER Aktion fragen: Bringt das direkt Geld? Gibt es was Besseres?

## CP-006: Ungeprüfte Ergebnisse weiterleiten (2026-02-10)
**Trigger:** Sub-Agent liefert Ergebnis
**Fehler:** Dashboard mit falschen Daten an Dino geliefert
**Regel:** JEDEN Inhalt prüfen. Dino ist NICHT mein Tester.

## CP-007: Proaktivität bei neuen Möglichkeiten vergessen (2026-02-10)
**Trigger:** Neues Tool/API verfügbar
**Fehler:** Dino musste fragen ob Grok eine API hat
**Regel:** Bei JEDER neuen Möglichkeit sofort fragen: Wo können wir das einsetzen?

## CP-008: Status-Updates statt einfach machen (2026-02-12)
**Trigger:** Mehrere Aufgaben umzusetzen
**Fehler:** Dino Zwischenstatus geschickt und nach TwitterAPI.io gefragt statt selbst zu registrieren
**Regel:** Einfach ALLES umsetzen. Nur melden wenn ich wirklich nicht weiterkomme (z.B. Bezahlung nötig). Zwischenstatus sind Zeitverschwendung.

## CP-009: Bei Audit-Findings fragen statt fixen (2026-02-12)
**Trigger:** Vermithrax findet Probleme im Audit
**Fehler:** Dino gefragt ob Syrax die Verkettung designen soll
**Regel:** Audit findet Problem → sofort Dev Loop starten (Syrax Design → Vermithrax Tests → Caraxes Code → Vermithrax QA). Nie fragen. Der Loop ist der Standard-Prozess für ALLES.
