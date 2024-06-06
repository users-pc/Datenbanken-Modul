from django.urls import path    
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('hochschulen', views.hochschulen, name="hochschulen"),
    path('bevölkerung', views.bevölkerung, name="bevölkerung"),
]