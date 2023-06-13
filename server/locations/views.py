from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .forms import LocationForm
from .models import Location

from common.views import _get_errors_from_form

def list_locations(_: HttpRequest) -> JsonResponse:
  locations = Location.objects.all()
  data = {
    "locations": [location.as_dict for location in locations]
  }
  return JsonResponse(data)

# Create your views here.
@csrf_exempt
def create_location(request: HttpRequest) -> JsonResponse:
  if request.method == 'POST':
    form = LocationForm(request.POST)
    if form.is_valid():
      location: Location = form.save()
      return location.as_json_response
  form = LocationForm()
  return _get_errors_from_form(form)

def read_location(_: HttpRequest, pk) -> JsonResponse:
  location = get_object_or_404(Location, pk=pk)
  return location.as_json_response

@csrf_exempt
def update_location(request: HttpRequest, pk) -> JsonResponse:
  location = get_object_or_404(Location, pk=pk)
  if request.method == 'POST':
    form = LocationForm(request.POST, instance=location)
    if form.is_valid():
      form.save()
      return location.as_json_response
  form = LocationForm()
  return _get_errors_from_form(form)

@csrf_exempt
def delete_location(request: HttpRequest, pk) -> JsonResponse:
  location = get_object_or_404(Location, pk=pk)
  if request.method == 'POST':
    location.delete()
    return JsonResponse({})
  return JsonResponse({}, status=400)
