from rest_framework import serializers
from .models import PointOfInterest

class SlotsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =PointOfInterest
        fields = ('area_name', 'parking_name', 'city', 'zipcode', 'capacity', 'image', 'position')
