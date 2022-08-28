import ast
from django.core.serializers import serialize
from django.http import JsonResponse

from ..models import Coordinates, Halal, Mall

# Create your views here.
def jsonify_single(obj):
  return ast.literal_eval(serialize('json', [obj]))

def create(request):
  if request.method == 'POST':
    try:
      lat = float(request.POST['lat'])
      lon = float(request.POST['lon'])
      name = request.POST['name']
      unit = request.POST['unit']
      mall = request.POST['mall']
      
      coords = Coordinates(lat=lat,lon=lon)
      coords.save()
      
      mallObject = Mall.objects.get(name=name)
      mallObject.halals += 1
      mallObject.save()
      
      halal = Halal(coords=coords, name=name, unit=unit, mall=mallObject)
      halal.save()
      
      return JsonResponse({ 'halal': jsonify_single(halal) })
    except ValueError as e:
      return JsonResponse({ 'err': f'Value Error: {str(e)}' })
    except AttributeError:
      return JsonResponse({ 'err': 'Needs name, lat and lon' })
    except Exception as e:
      return JsonResponse({ 'err': str(e) })
  return JsonResponse({})

def delete(request):
  if request.method == 'POST':
    try:
      mall = request.POST['mall']
      name = request.POST['name']
      halal = Halal.objects.get(name=name, mall=mall).delete()
      return JsonResponse({ 'deleted': True })
    except ValueError:
      return JsonResponse({ 'err': 'Value Error' })
    except AttributeError:
      return JsonResponse({ 'err': 'Needs name' })
    except Exception as e:
      return JsonResponse({ 'err': str(e) })
  return JsonResponse({})