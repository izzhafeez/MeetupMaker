from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render, redirect

from .forms import PlatformForm
from .models import Platform

def create_platform(request: HttpRequest):
  if request.method == 'POST':
    form = PlatformForm(request.POST)
    if form.is_valid():
      # Create a new Platform object with the form data
      platform: Platform = form.save()
      # Redirect to the detail view for the new Platform
      return redirect('platform_detail', pk=platform.pk)
  else:
    # Display a blank form for creating a new Platform
    form = PlatformForm()
  return render(request, 'create_platform.html', {'form': form})

def platform_detail(request: HttpRequest, pk):
  platform = get_object_or_404(Platform, pk=pk)
  return render(request, 'platform_detail.html', {'platform': platform})

def update_platform(request: HttpRequest, pk):
  platform = get_object_or_404(Platform, pk=pk)
  if request.method == 'POST':
    form = PlatformForm(request.POST, instance=platform)
    if form.is_valid():
      form.save()
      return redirect('platform_detail', pk=pk)
  else:
    form = PlatformForm(instance=platform)
  return render(request, 'update_platform.html', {'form': form})

def delete_platform(request: HttpRequest, pk):
  platform = get_object_or_404(Platform, pk=pk)
  if request.method == 'POST':
    platform.delete()
    return redirect('platform_list')
  
  context = {'platform': Platform}
  return render(request, 'delete_platform.html', context=context)