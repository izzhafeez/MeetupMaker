from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render, redirect

from .forms import ConnectionForm
from .models import Connection

def create_connection(request: HttpRequest):
  if request.method == 'POST':
    form = ConnectionForm(request.POST)
    if form.is_valid():
      # Create a new Connection object with the form data
      connection: Connection = form.save()
      # Redirect to the detail view for the new Connection
      return redirect('connection_detail', pk=connection.pk)
  else:
    # Display a blank form for creating a new Connection
    form = ConnectionForm()
  return render(request, 'create_connection.html', {'form': form})

def connection_detail(request: HttpRequest, pk):
  connection = get_object_or_404(Connection, pk=pk)
  return render(request, 'connection_detail.html', {'connection': connection})

def update_connection(request: HttpRequest, pk):
  connection = get_object_or_404(Connection, pk=pk)
  if request.method == 'POST':
    form = ConnectionForm(request.POST, instance=connection)
    if form.is_valid():
      form.save()
      return redirect('connection_detail', pk=pk)
  else:
    form = ConnectionForm(instance=connection)
  return render(request, 'update_connection.html', {'form': form})

def delete_connection(request: HttpRequest, pk):
  connection = get_object_or_404(Connection, pk=pk)
  if request.method == 'POST':
    connection.delete()
    return redirect('connection_list')
  
  context = {'connection': Connection}
  return render(request, 'delete_connection.html', context=context)