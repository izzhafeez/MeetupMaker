from typing import List

from django.contrib.postgres.fields import ArrayField
from django.forms import CharField, ModelForm, ValidationError

from persons.models import Person

class MeetupForm(ModelForm):
  participants = ArrayField(CharField())
  
  def clean_participants(self):
    participants = self.cleaned_data['participants']
    processed_participants: List[Person] = []
    for participant in participants:
      if not Person.objects.filter(pk=participant).exists():
        raise ValidationError("Person does not exist.")
      processed_participant = Person.objects.get(pk=participant)
      processed_participants.append(processed_participant)
    return processed_participants

  def clean(self):
    cleaned_data = super().clean()
    return cleaned_data
  