from django.db import models
from geoposition import Geoposition
from geoposition.fields import GeopositionField

def getDefaultLatPosition():
    lat = 23.810475327766582
    return lat

def getDefaultLonPosition():
    lon = 90.4119873046875
    return lon


class PointOfInterest(models.Model):
    area_name = models.CharField(max_length=100)
    parking_name = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    capacity = models.IntegerField()
    price_per_hour = models.IntegerField(default=0)
    opening_time = models.TimeField(null=True, blank=True)
    closing_time = models.TimeField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    position = GeopositionField(blank=True)

    class Meta:
        verbose_name_plural = 'points of interest'
