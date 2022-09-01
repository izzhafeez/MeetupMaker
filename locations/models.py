from __future__ import annotations

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

import math

# Create your models here.
class Location(models.Model):
  lat = models.DecimalField(decimal_places=8,
                            max_digits=9,
                            validators=[
                              MinValueValidator(1.23776),
                              MaxValueValidator(1.47066)
                              ],
                            blank=False,
                            default=0
                            )
  lon = models.DecimalField(decimal_places=8,
                            max_digits=11,
                            validators=[
                              MinValueValidator(103.61751),
                              MaxValueValidator(104.04360)
                              ],
                            blank=False,
                            default=0
                            )
  
  def distance_to(self, location: Location):
    return 111.33*(
      (float(self.lat)-float(location.lat))**2 + (float(self.lon)-float(location.lon))**2)**0.5
  
  class Meta:
    abstract = True
  
## Fix using https://stackoverflow.com/questions/30964936/multiple-default-values-specified-for-column-id-of-the-table
class MRT(Location):
  name = models.CharField(max_length=100, unique=True, primary_key=True)
  code = models.CharField(max_length=100, unique=True)

class Mall(Location):
  name = models.CharField(max_length=100, unique=True, primary_key=True)
  stores = models.IntegerField(default=0)
  halals = models.IntegerField(default=0)
  mrt = models.ForeignKey(MRT,
                          on_delete=models.CASCADE,
                          default=None,
                          related_name="malls",
                          to_field="name",
                          db_column="mrt")
  desirability = models.DecimalField(blank=False,
                                     decimal_places=4,
                                     default=0.0,                      
                                     max_digits=7,
                                     validators=[
                                      MinValueValidator(0),
                                      MaxValueValidator(100)
                                      ])
  def save(self, *args, **kwargs):
    distance = self.distance_to(self.mrt)
    self.desirability = math.log2(self.stores)/max(distance, 0.3)
    super(Mall, self).save(*args, **kwargs)

class Halal(Location):
  name = models.CharField(max_length=100)
  unit = models.CharField(max_length=100)
  mall = models.ForeignKey(Mall,
                           on_delete=models.CASCADE,
                           default=None,
                           related_name="halal_stores",
                           to_field="name",
                           db_column="mall")