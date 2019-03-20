from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Slots import views

router = routers.DefaultRouter()
router.register('slots', views.SlotsViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
