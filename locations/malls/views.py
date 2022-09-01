import ast
from django.core.serializers import serialize
from django.http import JsonResponse

from ..models import Mall, MRT

# Create your views here.
def jsonify_single(obj):
  return ast.literal_eval(serialize('json', [obj]))

def create(request):
  if request.method == 'POST':
    try:
      lat = float(request.POST['lat'])
      lon = float(request.POST['lon'])
      name = request.POST['name']
      stores = int(request.POST['stores'])
      halals = 0
      mrt = request.POST["mrt"]
      mrt_obj = MRT.objects.get(name=mrt)
      
      Mall.objects.update_or_create(lat=lat,
                                    lon=lon,
                                    name=name,
                                    stores=stores,
                                    halals=halals,
                                    mrt=mrt_obj)
      
      mall = Mall.objects.get(name=name)
      
      return JsonResponse({ 'mall': jsonify_single(mall) })
    except ValueError as e:
      return JsonResponse({ 'err': f'Value Error: {str(e)}' })
    except AttributeError as e:
      return JsonResponse({ 'err': f'Attribute Error: {str(e)}' })
    except Exception as e:
      return JsonResponse({ 'err': str(e) })
  return JsonResponse({})

def read(request):
  if request.method == 'POST':
    try:
      name = request.POST['name']
      mall = Mall.objects.get(name=name)
      
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