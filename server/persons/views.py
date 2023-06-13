# Create your views here.
from typing import Any, Dict

from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .forms import PersonForm
from .models import Person

from common.views import _get_errors_from_form

def list_persons(_: HttpRequest) -> JsonResponse:
  persons = Person.objects.all()
  data = {
    "persons": [_get_person_as_dict(person) for person in persons]
  }
  return JsonResponse(data)

# Create your views here.
@csrf_exempt
def create_person(request: HttpRequest) -> JsonResponse:
  if request.method == 'POST':
    form = PersonForm(request.POST)
    if form.is_valid():
      person: Person = form.save()
      return _get_person_as_json_response(person)
  form = PersonForm()
  return _get_errors_from_form(form)

def read_person(_: HttpRequest, pk) -> JsonResponse:
  person = get_object_or_404(Person, pk=pk)
  return _get_person_as_json_response(person)

@csrf_exempt
def update_person(request: HttpRequest, pk) -> JsonResponse:
  person = get_object_or_404(Person, pk=pk)
  if request.method == 'POST':
    form = PersonForm(request.POST, instance=person)
    if form.is_valid():
      form.save()
      return _get_person_as_json_response(person)
  form = PersonForm()
  return _get_errors_from_form(form)

@csrf_exempt
def delete_person(request: HttpRequest, pk) -> JsonResponse:
  person = get_object_or_404(Person, pk=pk)
  if request.method == 'POST':
    person.delete()
    return JsonResponse({})
  return JsonResponse({}, status=400)

def _get_person_as_json_response(person: Person) -> JsonResponse:
  data = _get_person_as_dict(person)
  return JsonResponse(data)

def _get_person_as_dict(person: Person) -> Dict[str, Any]:
  return {
    "name": person.name,
    "latitude": person.latitude,
    "longitude": person.longitude
  }
