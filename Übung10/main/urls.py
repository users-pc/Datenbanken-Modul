from django.urls import path    
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('hochschulen', views.hochschulen, name="hochschulen"),
    path('bevölkerung', views.bevölkerung, name="bevölkerung"),
    #------------ Visualisierung durch Diagramme etc. ------------------
    path('visual', views.visual, name="visual"),
    path('hochschulenvisual', views.hochschulenvisual, name="hochschulenvisual"),
    # ------------ Karte ------------------
    path('karten', views.karten, name="karten"),
    path('hochschulkarte', views.hochschulenmap, name="hochschulkarte"),
    path('bevölerungkarte', views.bevölkerungsheatmap, name="bevölkerungskarte"),
]