from typing import List

# Create your views here.
from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .api import get_best_location_from_participants, get_participants
from .models import Meetup, Participate

from common.views import _get_errors_from_form

def list_meetups(_: HttpRequest) -> JsonResponse:
  meetups = Meetup.objects.all()
  data = {
    "meetups": [meetup.as_dict for meetup in meetups]
  }
  return JsonResponse(data)

# Create your views here.
@csrf_exempt
def create_meetup(request: HttpRequest) -> JsonResponse:
  if request.method == 'POST':
    participant_names = request.POST.getlist('participants')
    participants, unknown_participants = get_participants(participant_names)
    best_location = get_best_location_from_participants(participants)
    
    meetup = Meetup(
      location=best_location
    )
    meetup.save()
    
    for participant in participants:
      participate = Participate(
        meetup=meetup,
        participant=participant
      )
      participate.save()
      
    return meetup.as_json_response
  
  errors = {
    'participants': ', '.join(unknown_participants) + 'unknown.'
  }
  return JsonResponse({'errors': errors}, status=400)

def read_meetup(_: HttpRequest, pk) -> JsonResponse:
  meetup = get_object_or_404(Meetup, pk=pk)
  return meetup.as_json_response

@csrf_exempt
def delete_meetup(request: HttpRequest, pk) -> JsonResponse:
  meetup = get_object_or_404(Meetup, pk=pk)
  if request.method == 'POST':
    meetup.delete()
    return JsonResponse({})
  return JsonResponse({}, status=400)
