import ast
from django.core.serializers import serialize
from django.http import JsonResponse
from itertools import combinations
import numpy as np

# Create your views here.
circles = [
	{
		"r": 2,
		"x": 0,
		"y": 1
	},
	{
		"r": 1,
		"x": 1,
		"y": 0
	},
	{
		"r": 1.5,
		"x": -1,
		"y": -1
	},
	{
		"r": 2.5,
		"x": 2,
		"y": 2.5
	}
]

def find_circle_intersections(circles):
	r1 = circles[0]["r"]
	x1 = circles[0]["x"]
	y1 = circles[0]["y"]
	r2 = circles[1]["r"]
	x2 = circles[1]["x"]
	y2 = circles[1]["y"]
	R = ((x2-x1)**2 + (y2-y1)**2)**0.5
	c1 = (r1**2-r2**2)/(2*R**2)
	c2 = 0.5*(2*(r1**2 + r2**2)/R**2 - ((r1**2-r2**2)**2)/R**4 - 1)**0.5
			
	x = 0.5*(x1+x2) + c1*(x2-x1)
	dx = c2*(y2-y1)
	y = 0.5*(y1+y2) + c1*(y2-y1)
	dy = c2*(x1-x2)
	if type(dx) == complex or type(dy) == complex:
		return [(x, y), (x, y)]
	return [(x-dx, y-dy), (x+dx, y+dy)]

def is_within(circle, point):
	r = circle["r"]
	x1 = circle["x"]
	y1 = circle["y"]
	x2 = point[0]
	y2 = point[1]
	R = ((x2-x1)**2 + (y2-y1)**2)**0.5
	return R <= r

def find_center_from_circles(circles):
	points = []
	for c in combinations(circles, 2):
		points.extend(find_circle_intersections(c))

	passable_points = []
	for point in points:
		passable = True
		for circle in circles:
			if not is_within(circle, point):
				passable = False
		if passable:
			passable_points.append(point)

	if len(passable_points) == 0:
		return (0,0)
	else:		   
		return (
			np.mean([point[0] for point in passable_points]),
			np.mean([point[1] for point in passable_points])
		)
  
def jsonify_single(obj):
  return ast.literal_eval(serialize('json', [obj]))
		
def find(request):
  if request.method == 'POST':
    try:
      name = request.POST['name']
      # mall = Mall.objects.get(name=name)
      
      return JsonResponse({ 'mall': jsonify_single(None) })
    except ValueError as e:
      return JsonResponse({ 'err': f'Value Error: {str(e)}' })
    except AttributeError:
      return JsonResponse({ 'err': 'Needs name, lat and lon' })
    except Exception as e:
      return JsonResponse({ 'err': str(e) })
  return JsonResponse({})