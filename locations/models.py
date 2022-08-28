from __future__ import annotations

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Coordinates(models.Model):
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
  
  def distance_to(self, coords: Coordinates):
    return 111.33*((self.lat-coords.lat)**2 + (self.lon-coords.lon)**2)**0.5

class Mall(models.Model):
  name = models.CharField(max_length=100, unique=True)
  coordinates = models.ForeignKey(Coordinates, on_delete=models.CASCADE)
  stores = models.IntegerField(default=0)
  halals = models.IntegerField(default=0)
  desirability = models.DecimalField(blank=False,
                                     decimal_places=4,
                                     default=0,                      
                                     max_digits=7,
                                     validators=[
                                      MinValueValidator(0),
                                      MaxValueValidator(100)
                                      ])
  def save(self, *args, **kwargs):
    self.desirability = self.stores * self.halals
    super(Mall, self).save(*args, **kwargs)

class Halal(models.Model):
  name = models.CharField(max_length=100)
  coordinates = models.ForeignKey(Coordinates, on_delete=models.CASCADE)
  unit = models.CharField(max_length=100)
  mall = models.ForeignKey(Mall, on_delete=models.CASCADE)

class MRT(models.Model):
  name = models.CharField(max_length=100, unique=True)
  coordinates = models.ForeignKey(Coordinates, on_delete=models.CASCADE)
  malls = models.ForeignKey(Mall, on_delete=models.CASCADE)
  desirability = models.DecimalField(blank=False,
                                     decimal_places=4,
                                     default=0,                      
                                     max_digits=7,
                                     validators=[
                                      MinValueValidator(0),
                                      MaxValueValidator(100)
                                      ])
  
  def save(self, *args, **kwargs):
    coords = self.coordinates
    self.desirability = [coords.distance_to(mall.coordinates) for mall in self.malls]
    super(MRT, self).save(*args, **kwargs)