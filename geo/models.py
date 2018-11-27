"""
131072
271118 - initial
geo/models.py



"""


# =============

from django.db import models
from django_google_maps import fields as map_fields

# Create your models here.


class Geo_Info(models.Model):

    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
