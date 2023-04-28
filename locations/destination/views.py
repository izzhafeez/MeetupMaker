from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render, redirect

from .forms import DestinationForm
from .models import Destination

def create_destination(request: HttpRequest):
  if request.method == 'POST':
    form = DestinationForm(request.POST)
    if form.is_valid():
      # Create a new Destination object with the form data
      destination: Destination = form.save()
      # Redirect to the detail view for the new Destination
      return redirect('destination_detail', pk=destination.pk)
  else:
    # Display a blank form for creating a new Destination
    form = DestinationForm()
  return render(request, 'create_destination.html', {'form': form})

def destination_detail(request: HttpRequest, pk):
  destination = get_object_or_404(Destination, pk=pk)
  return render(request, 'destination_detail.html', {'destination': destination})

def update_destination(request: HttpRequest, pk):
  destination = get_object_or_404(Destination, pk=pk)
  if request.method == 'POST':
    form = DestinationForm(request.POST, instance=destination)
    if form.is_valid():
      form.save()
      return redirect('destination_detail', pk=pk)
  else:
    form = DestinationForm(instance=destination)
  return render(request, 'update_destination.html', {'form': form})

def delete_destination(request: HttpRequest, pk):
  destination = get_object_or_404(Destination, pk=pk)
  if request.method == 'POST':
    destination.delete()
    return redirect('destination_list')
  
  context = {'destination': destination}
  return render(request, 'delete_destination.html', context=context)