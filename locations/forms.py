from typing import Any, Dict

from django.forms import ModelForm

from .models import Location, NamedLocation

class LocationForm(ModelForm):
  class Meta:
    model = Location
    fields = ['latitude', 'longitude']
    
  def clean(self) -> Dict[str, Any]:
    cleaned_data = super().clean()
    return cleaned_data
    
class NamedLocationForm(LocationForm):
  class Meta(LocationForm.Meta):
    model = NamedLocation
    fields = LocationForm.Meta.fields + ['name']
    
  def clean(self) -> Dict[str, Any]:
    cleaned_data = super().clean()
    return cleaned_data
    