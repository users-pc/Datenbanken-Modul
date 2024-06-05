import csv
import os 
import pandas as pd

with open('hochschulen.csv', 'r') as file:
    reader = csv.reader(file)
    counter = 0
    for row in reader:
        counter += 1
        if counter > 1:
            break
        else:  
            # Gibt uns die Spalten der Tabellen aus  
            #['\ufeffHochschulkurzname;Hochschulname;Hochschultyp;Trägerschaft;Bundesland;Anzahl Studierende;Gründungsjahr;Promotionsrecht;Habilitationsrecht;Straße;Postleitzahl (Hausanschrift);Ort (Hausanschrift);Home Page']
            print(row)
