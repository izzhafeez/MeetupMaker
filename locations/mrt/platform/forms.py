from typing import Any, Dict

from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import CODE_VALIDATION_MESSAGE, Platform

class PlatformForm(ModelForm):
  class Meta:
    model = Platform
    fields = ['code', 'station']
  
  def clean(self) -> Dict[str, Any]:
    cleaned_data = super().clean()
    code = cleaned_data['code']
    if len(code) < 2:
      raise ValidationError(CODE_VALIDATION_MESSAGE)
    cleaned_data['line'] = code[:2]
    return cleaned_data
  