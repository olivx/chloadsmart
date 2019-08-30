from django.contrib.gis.db import models

# Create your models here.


class Cargo(models.Model):

    product = models.CharField(max_length=200)
    origin_city = models.CharField(max_length=50)
    origin_state = models.CharField(max_length=50)
    destination_city = models.CharField(max_length=50)
    destination_state = models.CharField(max_length=50)
    
    origin_point = models.PointField(
        'longitude/latitude',
        help_text="To generate the map for your location")
    destination_point = models.PointField(
        'longitude/latitude', 
        help_text="To generate the map for your location")


    def __str__(self):
        return self.product


class Truck(models.Model):

    truck = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    point = models.PointField(
        'longitude/latitude', 
        help_text="To generate the map for your location")


    def __str__(self):
        return self.truck


