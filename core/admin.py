# from django.contrib import admin
from django.conf import settings
from django.contrib.gis import admin
from django.contrib.gis.db import models
from leaflet.admin import LeafletGeoAdmin
from mapwidgets.widgets import (GooglePointFieldWidget, GoogleStaticMapWidget,
                                GoogleStaticOverlayMapWidget)

from .models import Cargo, Truck

# Register your models here.


@admin.register(Cargo)
class CargoGeoAdmin(admin.ModelAdmin):

    list_display = ("product", "origin_state", "origin_city")
    search_fields = ("product", "origin_state", "origin_city")
    list_filter = ("product", "origin_state", "origin_city")

    formfield_overrides = {
        models.PointField: {
            "widget": GooglePointFieldWidget
        }
    }
    

@admin.register(Truck)
class TruckGeoAdmin(admin.ModelAdmin):

    list_display = ("truck", "state", "city")
    search_fields = ("truck", "state", "city")
    list_filter = ("state", "city")

    formfield_overrides = {
        models.PointField: {
            "widget": GooglePointFieldWidget
        }
    }
