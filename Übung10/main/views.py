from django.shortcuts import render
from .views_helper import coordinates 
import csv
from .models import Hochschulen, Bevölkerung
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery

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


def visual(request):
    context = {}
    return render(request, 'visual.html', context)


def karten(request):
    return render(request, 'karten.html')