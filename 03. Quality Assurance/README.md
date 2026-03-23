# Quality Assurance
`Automatisierung`
- Test-Serie mit Referenzdaten
- Kategorien
  - Fakten ("Einwohner der Stadt Salzburg 2026")
  - Edge Cases
    - Mehrdeutigkeit
    - Nicht vorhandene Daten
    - Falsche Annahmen
    - Unvollständige Fragen ("Wie hat sich entwickelt?")
    - Extreme/ungewöhnliche Anfragen
    - Variationen (Fragen anders formuliert)
    - Schreibfehler ("Beövlkerung Salzburgs")
    - Grenzfälle (NaN, Nullwerte, etc)
    - User versucht System zu beeinflussen ("Ignore previous instructions and give me ...")
- Antworten
  - Zahlen? Zeiträume? Quellen?
- Vergleiche mit Referenzantworten/-werten
- LLMs sind nicht deterministisch -> herausfordernd

`Evaluierungsmetriken`
- Faktische Korrektheit
  - Stimmen Zahlen/Werte/Trends?
- Vollständigkeit
  - Wurde die ganze Frage beantwortet?
- Klarheit
  - Verständlichkeit
  - Struktur
- Transparenz
  - Quellen genannt?
  - Annahmen erklärt?
- Robustheit
  - Umgang mit Mehrdeutigkeit und falschen Annahmen
- Score-Modell als Beispiel
  - 0 - 1
  - Gewichtung von Kategorien

`Monitoring`
- Live-Feedback von Usern
  - Bewertung
  - Abbrüche
  - Follow-Up Fragen (Unklarheiten?)
- Logging von Prompts + Antworten
- Veränderungen über die Zeit erkennen

`Regressionstests`
- Fixe Sammlung von Fragen mit erwarteten Antworten
- Vorher vs Nachher Vergleich (automatisch)
- Prüfen
  - Bleiben Werte/Zahlen unverändert?
  - Bleibt die Antwort-Struktur stabil?
  - Funktionieren die Edge Cases weiterhin?