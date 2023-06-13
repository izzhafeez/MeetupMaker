from typing import Any, Dict, List

from django.db.models import AutoField, CASCADE, ForeignKey, Model
from django.http import JsonResponse

from locations.models import Location
from persons.models import Person

# Create your models here.
class Meetup(Model):
  meetup_id = AutoField(primary_key=True)
  
  location: Location = ForeignKey(
    'locations.location',
    on_delete=CASCADE
  )
  
  @property
  def as_dict(self) -> Dict[str, Any]:
    participations: List[Participate] = Participate.objects.filter(meetup=self.meetup_id)
    participants: List[Person] = [p.participant for p in participations]
    return {
      'meetup_id': self.meetup_id,
      'location': self.location.as_dict,
      'participants': [p.as_dict for p in participants]
    }
    
  @property
  def as_json_response(self) -> JsonResponse:
    data = self.as_dict
    return JsonResponse(data)
  
class Participate(Model):
  meetup_id: Meetup = ForeignKey(
    'meetups.Meetup',
    on_delete=CASCADE
  )
  
  participant: Person = ForeignKey(
    'persons.Person',
    on_delete=CASCADE
  )
  