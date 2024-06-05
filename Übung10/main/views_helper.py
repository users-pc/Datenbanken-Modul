import requests
import json 

def coordinates(adresse):
    adresse = adresse
    replacements = {'(Ortsteil)': '', '(Kreis)':'', '(Ortsteil),':',', '(Kreis),':','}
    try:
        for i, j in replacements.items():
            p = adresse.replace(i, j)
    except:
        pass
    
    r = requests.get(f'http://127.0.0.1:8088/search.php?q={p}&format=jsonv2')
    result = json.loads(r.text)
    koordinaten = []
    try:
        #print(result[0]['lat'],result[0]['lon'])
        latitude = result[0]['lat']
        koordinaten.append(str(latitude))
        longitude = result[0]['lon']
        koordinaten.append(str(longitude))
        # Speicherung in der Datenbank
    except:
        print("!!!!!!!!!!!!!!!!! HAT NICHT GEKLAPPT !!!!!!!!!!!!!!!!!!!", p)
        latitude = '0'
        koordinaten.append(str(latitude))
        longitude = '0'
        koordinaten.append(str(longitude))        
        pass
    return koordinaten

"""
Um Inserate innerhalb eines bestimmten Radius basierend auf geographischen Koordinaten zu filtern, können Sie die Haversine-Formel verwenden. Diese Formel berechnet die Entfernung zwischen zwei Punkten auf der Erdoberfläche, gegeben durch ihre Längen- und Breitengrade.

Hier ist ein Pseudocode, wie Sie es implementieren können:

Definieren Sie eine Funktion distance, die die Haversine-Formel verwendet, um die Entfernung zwischen zwei Punkten zu berechnen.
Definieren Sie eine Funktion filter_ads, die eine Liste von Inseraten und einen Punkt (gegeben durch Längen- und Breitengrade) sowie einen Radius als Eingabe nimmt.
In der Funktion filter_ads, gehen Sie durch jedes Inserat in der Liste.
Für jedes Inserat, berechnen Sie die Entfernung zwischen dem Inserat und dem gegebenen Punkt mit der Funktion distance.
Wenn die berechnete Entfernung kleiner oder gleich dem gegebenen Radius ist, fügen Sie das Inserat zu einer neuen Liste hinzu.
Nachdem Sie durch alle Inserate gegangen sind, geben Sie die neue Liste zurück.
Hier ist der Python-Code, der den oben genannten Pseudocode implementiert:

"""
from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r

def filter_ads(ads, lat, lon, radius):
    filtered_ads = []
    for ad in ads:
        ad_lat = ad['latitude']
        ad_lon = ad['longitude']
        distance = haversine(lon, lat, ad_lon, ad_lat)
        if distance <= radius:
            filtered_ads.append(ad)
    return filtered_ads
"""
lat = 52.5200  # Latitude of Berlin
lon = 13.4050  # Longitude of Berlin
radius = 880000  # 1000 kilometers in meters
ads = [
    {'id': 1, 'latitude': 52.5200, 'longitude': 13.4050},  # Berlin
    {'id': 2, 'latitude': 48.8566, 'longitude': 2.3522},  # Paris
    {'id': 3, 'latitude': 51.5074, 'longitude': -0.1278},  # London
]
filtered_ads = filter_ads(ads, lat, lon, radius)

for ad in filtered_ads:
    print(ad)
"""