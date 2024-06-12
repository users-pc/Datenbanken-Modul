from django.shortcuts import render
from .views_helper import coordinates, hopenclosed, uni_vs_fachhochschule,  studis_an_uni_vs_fachhochschule, studis_bundesland
import csv
from .models import Hochschulen, Bevölkerung
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery
import folium 
from folium.plugins import MarkerCluster
# Create your views here.
def home(request):
    # einfügen der csv
    return render(request, 'index.html')

def hochschulen(request):
    """
    with open('/home/users-pc/Studium/Datenbanksysteme/csv-files/hochschulen.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')  # Setzen des Delimiters auf ';'
        counter = 0
        for row in reader:
            # Jetzt repräsentiert `row` eine Liste, in der jedes Element einer durch ';' getrennten Abtrennung entspricht
            counter += 1
            if counter == 1:
                continue
            else:
                print(row)
                if row[7] == "Ja":
                    promotionsrecht = True
                else:
                    promotionsrecht = False
                if row[8] == "Ja":	
                    habilitationsrecht = True
                else:
                    habilitationsrecht = False
                try:
                    anz_studis = int(row[5])
                except:
                    anz_studis = None
                try:
                    gründungs_jahr = int(row[6])
                except:
                    gründungs_jahr = None
                try:
                    postleitzahl = int(row[10])
                except:
                    postleitzahl = None
                koordinaten = coordinates(row[9] + " "+ row[10] +" "+ row[11])
                print(koordinaten)
                if len(row) < 3:
                    print(row[0], "hat weniger als 3 Attribute!")
                    continue
                else:
                    Hochschulen.objects.create(
                        kurzname = row[0],
                        name = row[1],
                        typ = row[2],
                        trägerschaft = row[3],
                        bundesland = row[4],
                        anz_studis = anz_studis,
                        gründungsjahr = gründungs_jahr,
                        promotionsrecht = promotionsrecht,
                        habilitationsrecht = habilitationsrecht,
                        straße = row[9],
                        postleitzahl = postleitzahl,
                        ort = row[11],
                        longitude = koordinaten[1], # Längengrad
                        latitude = koordinaten[0], #Breitengrad
                        homepage = row[12]
                    )
        """
    hochschulen = Hochschulen.objects.all().order_by('id')
    # Full Text SEarch 
    query = request.GET.get('q')
    if query:
        search_vector = SearchVector('name', 'typ', 'trägerschaft', 'bundesland', 'ort')
        search_query = SearchQuery(query)
        
        hochschulen = hochschulen.annotate(
            search=search_vector
        ).filter(search=search_query)
    # Paginator 
    paginator = Paginator(hochschulen, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'hochschulen': page_obj, 'title': 'Quellen'}
    return render(request, 'hochschulen.html', context)


def bevölkerung(request):
    """
    line = 0
    with open('/home/users-pc/Studium/Datenbanksysteme/csv-files/bevoelkerung.csv', 'r', encoding='iso-8859-1') as file:
        reader = csv.reader(file, delimiter=';')  # Setzen des Delimiters auf ';'
        
        for row in reader:
            line += 1
            if line < 10 or row == ['__________']:
                continue
            
            # Jetzt repräsentiert `row` eine Liste, in der jedes Element einer durch ';' getrennten Abtrennung entspricht
            print(row)
            try:
                dg = int(row[0])
            except:
                dg = None
            try:
                total_population = int(row[2])
            except:
                total_population = None
            try:
                male_population = int(row[3])
            except:
                male_population = None
            try:
                feamle_population = int(row[4])
            except:
                feamle_population = None
            koordinaten = coordinates(row[1])
            print(koordinaten)
            Bevölkerung.objects.create(
                ort = row[1],
                longitude = koordinaten[1], # Längengrad
                latitude = koordinaten[0], #Breitengrad
                dg = dg,
                total_population = total_population,
                male_population = male_population,
                female_population = feamle_population,
            )
    """


    bevölkerung = Bevölkerung.objects.all().order_by('id')
    # Full Text SEarch
    query = request.GET.get('q')
    if query:
        search_vector = SearchVector('ort', 'dg')
        search_query = SearchQuery(query)
        
        bevölkerung = bevölkerung.annotate(
            search=search_vector
        ).filter(search=search_query)
    # Paginator
    paginator = Paginator(bevölkerung, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'bevölkerung': page_obj, 'title': 'Bevölkerung'}
    return render(request, 'bevölkerung.html', context)
# ------------------------------------------------------------------------------------------------------------------------------- Visualisierung/Diagramme
# Zur Navigation
def visual(request):
    return render(request, 'visual.html')

def hochschulenvisual(request):
    hochschulen = Hochschulen.objects.all()
    hopenclosed_plotly=hopenclosed(hochschulen)
    uni_vs_fachhochschule_plotly=uni_vs_fachhochschule(hochschulen)
    studis_an_uni_vs_fachhochschule_plotly=studis_an_uni_vs_fachhochschule(hochschulen)
    studis_bundesland_plotly=studis_bundesland(hochschulen)
    context = {'hopenclosed': hopenclosed_plotly,'uni_vs_fachhochschule': uni_vs_fachhochschule_plotly, 'studis_an_uni_vs_fachhochschule': studis_an_uni_vs_fachhochschule_plotly,'title': 'Visualisierung', 'studis_bundesland': studis_bundesland_plotly}
    return render(request, 'hochschulenvisual.html', context)





# ------------------------------------------------------------------------------------------------------------------------------- Karten 
# Zur Navigation
def karten(request):
    return render(request, 'karten.html')

def hochschulenmap(request):
     # Karte von Folium mit allen hochschulen in deutschland
    m = folium.Map(width='100%',height='70%',location=[51.165707, 10.452764], zoom_start=5, name="Inserate")    
    map_cluster = MarkerCluster().add_to(m)
    for hochschule in Hochschulen.objects.all():
        html = f'<a href="{hochschule.homepage}"> {hochschule.name} </a>'
        folium.Marker(
            location=[hochschule.latitude, hochschule.longitude],
            popup=html, # Im Popup kann ein a href zu der homepage der Hochschule eingefügt werden

            icon=folium.Icon(color='blue')
        ).add_to(map_cluster)


    context = {'map': m._repr_html_(), 'title': 'Karte'}
    return render(request, 'hochschulenmap.html', context)

import pandas as pd
import requests
import json

def bevölkerungsheatmap(request):
    # Mache eine choropleth map mit der Bevölkerungsdichte in Deutschland mit Folium 
    # Die Daten für die Bevölkerungsdichte sind in der Bevölkerungstabelle gespeichert
    geo_data='https://raw.githubusercontent.com/isellsoap/deutschlandGeoJSON/master/2_bundeslaender/4_niedrig.geo.json',
    # geojson importieren und file herunterladen

    geojson_data_install = requests.get(geo_data)
    with open('geojson_data.json', 'wb') as f:
        f.write(geojson_data_install.content)
    

    population = Bevölkerung.objects.all()
    bundesländer = ['Baden-Württemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen', 'Hamburg', 'Hessen', 'Mecklenburg-Vorpommern', 'Niedersachsen', 'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland', 'Sachsen', 'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thüringen']
    # Filtere die Daten für die Bundesländer
    for i in population:
        # Koordinaten für die Orte werden benötigt schauen, ob es im Bundesland liegt
        from .views_helper import haversine
        koordinaten = [i.latitude, i.longitude]
        # jetzt soll unter den geojson_data_install die Koordinaten der Orte mit den Koordinaten der Bundesländer verglichen werden
        for bundesland in bundesländer:
            # Koordinaten der Bundesländer
            bundesland_koordinaten = []
            with open('geojson_data.json') as f:
                data = json.load(f)
                for feature in data['features']:
                    if feature['properties']['name'] == bundesland:
                        bundesland_koordinaten = feature['geometry']['coordinates']
                        break
            # Jetzt haben wir die Koordinaten der Bundesländer und die Koordinaten der Orte
            # Jetzt schauen wir, ob die Koordinaten der Orte in den Koordinaten der Bundesländer liegen
            if haversine(koordinaten, bundesland_koordinaten) == True:
                print(i.ort, "liegt in", bundesland)
                i.bundesland = bundesland
                i.save()

    # Population in Deutschland als pd.DataFrame
    population_df = pd.DataFrame.from_records(population.values())
    m = folium.Map(width='100%',height='70%',location=[51.165707, 10.452764], zoom_start=5, name="Inserate")
    # Lade die GeoJson Datei für die Bundesländer
    folium.Choropleth(
        geo_data='https://raw.githubusercontent.com/isellsoap/deutschlandGeoJSON/master/2_bundeslaender/4_niedrig.geo.json',
        name='choropleth',
        data=population_df,
        # Spalte mit der Bevölkerungsdichte und den Koordinaten der Orte
        columns=['ort', 'total_population'],
        key_on='feature.properties.name',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Bevölkerungsdichte'
    ).add_to(m)
    context = {'map': m._repr_html_(), 'title': 'Karte'}
    return render(request, 'bevölkerungsheatmap.html', context)