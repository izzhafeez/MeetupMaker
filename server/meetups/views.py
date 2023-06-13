# Create your views here.
from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .api import find_closest_location
from .forms import MeetupForm
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
    form = MeetupForm(request.POST)
    if form.is_valid():
      participants = form.cleaned_data['participants']
      locations = [p.home_address for p in participants]
      best_location = find_closest_location(locations)
      
      meetup = Meetup(
        location=best_location
      )
      meetup.save()
      
      for participant in participants:
        participate = Participate(
          meetup_id=meetup.meetup_id,
          participant=participant
        )
        participate.save()
        
      return meetup.as_json_response
  form = MeetupForm()
  return _get_errors_from_form(form)

def read_meetup(_: HttpRequest, pk) -> JsonResponse:
  meetup = get_object_or_404(Meetup, pk=pk)
  return meetup.as_json_response

@csrf_exempt
def update_meetup(request: HttpRequest, pk) -> JsonResponse:
  meetup = get_object_or_404(Meetup, pk=pk)
  if request.method == 'POST':
    form = MeetupForm(request.POST, instance=meetup)
    if form.is_valid():
      form.save()
      return meetup.as_json_response
  form = MeetupForm()
  return _get_errors_from_form(form)

@csrf_exempt
def delete_meetup(request: HttpRequest, pk) -> JsonResponse:
  meetup = get_object_or_404(Meetup, pk=pk)
  if request.method == 'POST':
    meetup.delete()
    return JsonResponse({})
  return JsonResponse({}, status=400)
