# Datenbanken-Modul

## Aufgabe 1: Konzeption der Datenvisualisierung

### Zielsetzung
Wir möchten mit unserer Website folgende Fragen beantworten:
- In welcher Region gibt es die meisten Hochschulen?
- Wie hoch ist die Bevölkerungsdichte in den Regionen mit den meisten Hochschulen?
- Besteht ein Zusammenhang zwischen der Anzahl der Hochschulen und der Bevölkerungsdichte?

### Projekt-Idee
Unsere interaktive Visualisierungswebsite soll nicht nur Antworten liefern, sondern auch Zusammenhänge verdeutlichen. Sie ermöglicht dem Benutzer, die Daten aus verschiedenen Perspektiven zu betrachten und individuell zu analysieren.

### Voraussetzungen
- **PostgreSQL**: Datenbank
- **Django**: Webframework für Python
- **Folium**: Kartenvisualisierung
- **Nominatim**: Koordinatendatenbank von OpenStreetMap
- **Plotly**: Diagrammerstellung in Python
- **Bootstrap**: Vorlage von shuffle.dev

### Umsetzungsschritte
1. Einrichtung von Django
2. Einrichtung von PostgreSQL
3. Erstellung der Datenbanktabellen mit Django ORM
4. Import der Dateien `hochschulen.csv` und `bevölkerung.csv`
5. Geocodierung der Adressen mit Nominatim
6. Entwicklung der Website mit JavaScript, HTML, CSS und Bootstrap

## Aufgabe 2: Datenvisualisierung

### Kartenvisualisierung
- **hochschule.csv**:
  - Adresse
  - Name
  - Bundesland
  - Anzahl Studierende
  - Koordinaten
  - Optional: Website

### Heatmap
- **bevölkerung.csv**:
  - Anzahl
  - Insgesamt
  - Männlich
  - Weiblich
  - Koordinaten der Bundesländer

### Diagramme
- **Streudiagramm**: Anzahl der Studierenden in Abhängigkeit von der Bevölkerungsdichte.
- **Balkendiagramm**: Anzahl der Hochschulen im Vergleich zur Bevölkerungsdichte nach Bundesland.

## Aufgabe 3: Datenzugriff
Die Daten können auf der Website unter [Link zur Website] eingesehen werden.
![image](https://github.com/users-pc/Datenbanken-Modul/assets/60401089/c6d7a17e-8558-4fe0-8cea-7d48d5c29ac2)


## Aufgabe 4: Weitere Schritte
[Hier weitere Schritte einfügen]

