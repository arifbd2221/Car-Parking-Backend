from rest_framework import viewsets
from .models import PointOfInterest
from .serializers import SlotsSerializers

class SlotsViewset(viewsets.ModelViewSet):
    queryset = PointOfInterest.objects.all()
    serializer_class = SlotsSerializers
