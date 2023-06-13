from typing import Any, Dict

from django.db.models import CASCADE, ForeignKey, Model, TextField
from django.http import JsonResponse

from locations.models import Location

# Create your models here.
class Person(Model):
  name = TextField(
    primary_key=True
  )
  
  home_address: Location = ForeignKey(
    'locations.Location',
    on_delete=CASCADE,
    related_name='home_address'
  )
  
  outside_address: Location = ForeignKey(
    "locations.Location",
    on_delete=CASCADE,
    related_name='outside_address'
  )
  
  @property
  def as_dict(self) -> Dict[str, Any]:
    return {
      'name': self.name,
      'home_address': self.home_address.as_dict,
      'outside_address': self.outside_address.as_dict
    }
    
  @property    
  def as_json_response(self) -> JsonResponse:
    data = self.as_dict
    return JsonResponse(data)
  