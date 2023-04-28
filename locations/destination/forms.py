from typing import Any, Dict

from .models import Destination
from ..forms import NamedLocationForm

class DestinationForm(NamedLocationForm):
  class Meta:
    model = Destination
    fields = NamedLocationForm.Meta.fields
  
  def clean(self) -> Dict[str, Any]:
    cleaned_data = super().clean()
    return cleaned_data
  