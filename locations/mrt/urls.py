from django.urls import path, include

app_name = 'locations.mrt'
urlpatterns = [
  path('station/', include('locations.mrt.station.urls', namespace='stations')),
  path('platform/', include('locations.mrt.platform.urls', namespace='platforms')),
  path('connection/', include('locations.mrt.connection.urls', namespace='connections'))
]