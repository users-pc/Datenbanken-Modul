from django.db import models

# Create your models here.

class Hochschulen(models.Model):
    kurzname = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=200)
    typ = models.CharField(max_length=50)
    trägerschaft = models.CharField(max_length=50)
    bundesland = models.CharField(max_length=50)
    anz_studis = models.IntegerField(null=True)
    gründungsjahr = models.IntegerField(null=True)
    promotionsrecht = models.BooleanField()
    habilitationsrecht = models.BooleanField()
    straße = models.CharField(max_length=200)
    postleitzahl = models.IntegerField(null=True)
    ort = models.CharField(max_length=50)
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)
    homepage = models.URLField(blank=True)

    def __str__(self):
        return self.name + " (" + self.kurzname + ")"
    

class Bevölkerung(models.Model):
    ort = models.CharField(max_length=50)
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)
    name= models.CharField(max_length=50)
    total_population = models.IntegerField(null=True)
    male_population = models.IntegerField(null=True)
    female_population = models.IntegerField(null=True)
    
    def __str__(self):
        return self.ort + " (" + self.total_population + ")"


