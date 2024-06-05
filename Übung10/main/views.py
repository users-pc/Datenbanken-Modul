from django.shortcuts import render
from .views_helper import coordinates 
# Create your views here.
def home(request):
    # einfügen der csv
    """
    with open('main/static/hochschulen.csv', 'r') as file:
        data = file.readlines()
        for line in data[1:]:
            line = line.split(';')
            print(line)
    """
    return render(request, 'index.html')