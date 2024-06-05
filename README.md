# Datenbanken-Modul
Aufgabe 1)

Konzeption der Datenvisualisierung: 
    - Karten mit Heatmap mti der dichte der Bevälkerung und wo sich die Hochschulen befinden
    - Intressante Fragen: 
        - In welcher Region gibt es die meisten Hochschulen? 
        - Wie hoch ist die Bevölkerungsdichte in den Regionen mit den meisten Hochschulen?
        -Gibt es einen Zusammenhang zwischen der Anzahl der Hochschulen und der Bevölkerungsdichte?
        
Projekt-Idee: 
    Mit dieser Website möchten wir die zuvor gestellten Fragen umfassend beantworten. Um dies zu erreichen, entwickeln wir eine interaktive Visualisierung, die nicht nur Antworten liefert, sondern auch Zusammenhänge verdeutlicht und dem Benutzer mehrere Betrachtungsweisen ermöglicht.
    Die Website soll intuitiv bedienbar sein und dem Nutzer die Kontrolle über die Darstellung der Daten geben. Durch die Möglichkeit, Filter zu setzen und verschiedene Visualisierungen auszuwählen, kann jeder Benutzer die Informationen auf seine individuellen Bedürfnisse zuschneiden.
    Unsere Website dient nicht nur der Informationsbereitstellung, sondern als umfassendes Werkzeug zur Datenerkundung. Durch die interaktive Visualisierung und die Möglichkeit zur individuellen Analyse, ermöglicht sie es jedem Nutzer, die komplexen Zusammenhänge zwischen Hochschulen und Bevölkerungsentwicklung zu verstehen.
Voraussetzungen:
    -PostgreSQL (Datenbank)
    -Django (Webframework für Python)
    -Folium (Kartenvisualisierung)
    -Nominatim (Datenbank von Openstreetmap auf PostgreSQL mit Koordinaten für jede Adresse)
    -Plotly (Ermöglicht Diagramme in Python -> Datenvisualisierung)
    -Bootstrap Vorlage von shuffle.dev
Schritte: 
    1. Wir setzen Django auf 
    2. Wir setzen PostgreSQL auf 
    3. Wir erstellen die Tabellen über ein ORM von Django (Embedded SQL)
    4. Impotieren der Datein hochschulen.csv und bevölkerung.csv  
    5. Geocodierung (Geocoding): Adressen, werden in Koordinaten umgewandelt mithilfe von Nominatim und in der Datenbank gespeichert
    6. Views Funktionen schreiben und Website per Javascript, Html, CSS fertigstellen mithilfe von Bootstrap

Aufgabe 2)

1) 
Wir unterteilen für jede Visualisierung die Wichtigkeit der Daten jeweils anders.

Karten: 
    
Darstellung -> hochschule.csv   
    - Adresse (Straße, Postleitzahl, Ort)
    - Namen
    - Bundesland (Für Filter)
    - Anzahl Studierende
    - Koordinaten (Nominatim)
    Optional: Website 

Heatmap -> bevölkerung.csv 
    - Anzahl
    - Insgesamt
    - männlich (Filter)
    - weiblich (Filter)
    - Koordinaten vom Bundesland (Nominatim)

Diagramm 1 (Streudiagramm: Ein Streudiagramm, das die Anzahl der Studierenden an einer Hochschule in Abhängigkeit von der Bevölkerungsdichte in der Region darstellt.): 
    - Anzahl der Studierenden 
    - Adresse (Koordinaten)
    - Hochschul Namen 

Diagramm 2 (Balkendiagramm: Ein Balkendiagramm, das die Anzahl der Hochschulen in verschiedenen Regionen mit der jeweiligen Bevölkerungsdichte vergleicht):
    - Anzahl der Hochschulen (Nach Bundesland) 
    - Bevölkerungsdichte (Wird nach qkm oder qm umgerechnet)



2.) und 3.)
Es handelt sich hierbei nur um die Tabllen Hochschulen und Bevölkerung. 
Django selber hat im default schon ein User model, dass wir in unserem ERM-Diagramm berücksichtigen. 
Unter dem Ordner "er-und-erm-diagramme" finden Sie alle ganzen Digramme.

4.) 
Mithilfe dieses Artikel haben wir für unserer Django_Projekt "Übung10" eine Datenbank mit PostgreSQL erstellt:
https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-20-04

path: Übung10/main/models.py finden sie das Relationale Model dargestellt über die Django-ORM. 


Aufgabe 3) 

Unter .... können sie die Daten auf der Website einsehen

Aufgabe 4)






