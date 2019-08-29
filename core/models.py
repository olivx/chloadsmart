from django.contrib.gis.db import models

# Create your models here.


class Cargo(models.Model):

    product = models.CharField(max_length=200)
    origin_city = models.CharField(max_length=50)
    origin_state = models.CharField(max_length=50)
    origin_point =  models.PointField()
    destination_city = models.CharField(max_length=50)
    destination_state = models.CharField(max_length=50)
    destination_point =  models.PointField()

    def __str__(self):
        return self.product


class Trucks(models.Model):

    truck = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    point = models.PointField()

    def __str__(self):
        return self.truck