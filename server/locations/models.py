from __future__ import annotations
from typing import Any, Dict

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import DecimalField, Model, TextField
from django.http import JsonResponse

# Create your models here.
class Location(Model):
  name = TextField(
    primary_key=True
  )
  
  latitude = DecimalField(
    decimal_places=8,
    max_digits=9,
    validators=[
      MinValueValidator(1.23776),
      MaxValueValidator(1.47066)
    ]
  )
  
  longitude = DecimalField(
    decimal_places=8,
    max_digits=11,
    validators=[
      MinValueValidator(103.61751),
      MaxValueValidator(104.04360)
    ]
  )
  
  @property
  def as_dict(self) -> Dict[str, Any]:
    return {
      "name": self.name,
      "latitude": self.latitude,
      "longitude": self.longitude
    }
  
  @property
  def as_json_response(self) -> JsonResponse:
    data = self.as_dict
    return JsonResponse(data)
  
  def get_distance_to(self, lat, lng) -> float:
    return 111.33 * (
      (self.latitude - lat) ** 2 \
      + (self.longitude - lng) ** 2
    ) ** 0.5
  