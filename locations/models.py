from __future__ import annotations

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Location(models.Model):
  lat = models.DecimalField(decimal_places=8,
                            max_digits=9,
                            validators=[
                              MinValueValidator(1.23776),
                              MaxValueValidator(1.47066)
                              ],
                            blank=False
                            )
  lon = models.DecimalField(decimal_places=8,
                            max_digits=11,
                            validators=[
                              MinValueValidator(103.61751),
                              MaxValueValidator(104.04360)
                              ],
                            blank=False
                            )
  
  def distance_to(self, location: Location):
    return 111.33*((self.lat-location.lat)**2 + (self.lon-location.lon)**2)**0.5
  
  class Meta:
    abstract = True
  
class MRT(Location):
  name = models.CharField(max_length=100, unique=True)

class Mall(Location):
  name = models.CharField(max_length=100, unique=True)
  stores = models.IntegerField(default=0)
  halals = models.IntegerField(default=0)
  mrt = models.ForeignKey(MRT, on_delete=models.CASCADE, default=None)
  desirability = models.DecimalField(blank=False,
                                     decimal_places=4,
                                     default=0.0,                      
                                     max_digits=7,
                                     validators=[
                                      MinValueValidator(0),
                                      MaxValueValidator(100)
                                      ])
  def save(self, *args, **kwargs):
    self.desirability = 1/self.distance_to(self.mrt)
    super(Mall, self).save(*args, **kwargs)

class Halal(Location):
  name = models.CharField(max_length=100)
  unit = models.CharField(max_length=100)
  mall = models.ForeignKey(Mall, on_delete=models.CASCADE, default=None)