from __future__ import annotations

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import CharField, DecimalField, Model

MIN_LATITUDE = 1.23776
MAX_LATITUDE = 1.47066
MIN_LONGITUDE = 103.61751
MAX_LONGITUDE = 104.04360

# Create your models here.
class Location(Model):
  latitude = DecimalField(
    decimal_places=8,
    max_digits=9,
    validators=[
      MinValueValidator(MIN_LATITUDE),
      MaxValueValidator(MAX_LATITUDE)
      ],
    blank=False
    )
  longitude = DecimalField(
    decimal_places=8,
    max_digits=11,
    validators=[
      MinValueValidator(MIN_LONGITUDE),
      MaxValueValidator(MAX_LONGITUDE)
      ],
    blank=False
    )
  
  def distance_to(self, location: Location) -> float:
    delta_lat = float(self.latitude)-float(location.latitude)
    delta_lon = float(self.longitude)-float(location.longitude)
    raw_distance = (delta_lat ** 2 + delta_lon ** 2) ** 0.5
    return 111.33 * raw_distance
  
  class Meta:
    abstract = True
  
class NamedLocation(Location):
  name = CharField(max_length=50, unique=True, primary_key=True)
  