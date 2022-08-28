import ast
from django.core.serializers import serialize
from django.http import JsonResponse

from ..models import Coordinates, Mall

# Create your views here.
def jsonify_single(obj):
  return ast.literal_eval(serialize('json', [obj]))

def create(request):
  if request.method == 'POST':
    try:
      lat = float(request.POST['lat'])
      lon = float(request.POST['lon'])
      name = request.POST['name']
      stores = request.POST['stores']
      
      coords = Coordinates(lat=lat,lon=lon)
      coords.save()
      
      mall = Mall(coords=coords, name=name, stores=stores)
      mall.save()
      
      return JsonResponse({ 'mall': jsonify_single(mall) })
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
      name = request.POST['name']
      mall = Mall.objects.get(name=name).delete()
      return JsonResponse({ 'deleted': True })
    except ValueError:
      return JsonResponse({ 'err': 'Value Error' })
    except AttributeError:
      return JsonResponse({ 'err': 'Needs name' })
    except Exception as e:
      return JsonResponse({ 'err': str(e) })
  return JsonResponse({})