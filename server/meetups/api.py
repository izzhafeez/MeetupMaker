from typing import List, Tuple

from locations.models import Location
from persons.models import Person

def find_closest_location(locations: List[Location]) -> Location:
  print(locations)
  assert len(locations) > 0
  
  mid_lat, mid_lng = find_midpoint(locations)
  all_locations: List[Location] = Location.objects.all()
  
  best_distance: float = float("inf")
  best_location: Location = None
  for location in all_locations:
    distance = location.get_distance_to(mid_lat, mid_lng)
    if distance < best_distance:
      best_distance = distance
      best_location = location
  
  if best_location is None:
    raise Exception("No Location found.")
  
  return best_location

def find_midpoint(locations: List[Location]) -> Tuple[float, float]:
  n = len(locations)
  assert n > 0
  
  mid_lat: float = sum(l.latitude for l in locations) / n
  mid_lng: float = sum(l.longitude for l in locations) / n
  
  return (mid_lat, mid_lng)

def get_participants(names: List[str]) -> Tuple[List[Person], List[str]]:
  participants: List[Person] = []
  unknown_participants: List[str] = []
  for name in list(names):
    if not Person.objects.filter(pk=name).exists():
      unknown_participants.append(name)
    participant = Person.objects.get(pk=name)
    participants.append(participant)
  return participants, unknown_participants

def get_best_location_from_participants(participants: List[Person]) -> Location:
  locations = [p.home_address for p in participants]
  return find_closest_location(locations)
  