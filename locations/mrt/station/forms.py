from typing import Any, Dict

from .models import Station
from ...forms import NamedLocationForm

class StationForm(NamedLocationForm):
  class Meta:
    model = Station
    fields = NamedLocationForm.Meta.fields
  
  def clean(self) -> Dict[str, Any]:
    cleaned_data = super().clean()
    return cleaned_data
  