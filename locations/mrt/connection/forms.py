from typing import Any, Dict

from django.forms import ModelForm

from ..connection.models import Connection

class ConnectionForm(ModelForm):
  class Meta:
    model = Connection
    fields = ['start_platform', 'end_platform']
  
  def clean(self) -> Dict[str, Any]:
    cleaned_data = super().clean()
    return cleaned_data