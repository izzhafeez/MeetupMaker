from django.urls import path

from .views import list_locations, create_location, read_location, update_location, delete_location

urlpatterns = [
  path('', list_locations, name="list_location"),
  path('create/', create_location, name='create_location'),
  path('<str:pk>/', read_location, name='read_location'),
  path('<str:pk>/update/', update_location, name='update_location'),
  path('<str:pk>/delete/', delete_location, name='delete_location') 
]