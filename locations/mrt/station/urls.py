from django.urls import path

from .views import create_station, delete_station, station_detail, update_station

app_name = 'stations'
urlpatterns = [
  path('new/', create_station, name='create_station'),
  path('<str:pk>/', station_detail, name='station_detail'),
  path('<str:pk>/update/', update_station, name='update_station'),
  path('<str:pk>/delete/', delete_station, name='delete_station')
]