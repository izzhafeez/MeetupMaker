from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render, redirect

from .forms import StationForm
from .models import Station

def create_station(request: HttpRequest):
  if request.method == 'POST':
    form = StationForm(request.POST)
    if form.is_valid():
      # Create a new Station object with the form data
      station: Station = form.save()
      # Redirect to the detail view for the new Station
      return redirect('station_detail', pk=station.pk)
  else:
    # Display a blank form for creating a new Station
    form = StationForm()
  return render(request, 'create_station.html', {'form': form})

def station_detail(request: HttpRequest, pk):
  station = get_object_or_404(Station, pk=pk)
  return render(request, 'station_detail.html', {'station': station})

def update_station(request: HttpRequest, pk):
  station = get_object_or_404(Station, pk=pk)
  if request.method == 'POST':
    form = StationForm(request.POST, instance=station)
    if form.is_valid():
      form.save()
      return redirect('station_detail', pk=pk)
  else:
    form = StationForm(instance=station)
  return render(request, 'update_station.html', {'form': form})

def delete_station(request: HttpRequest, pk):
  station = get_object_or_404(Station, pk=pk)
  if request.method == 'POST':
    station.delete()
    return redirect('station_list')
  
  context = {'station': station}
  return render(request, 'delete_station.html', context=context)