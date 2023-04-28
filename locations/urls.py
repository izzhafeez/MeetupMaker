from django.urls import include, path

app_name = 'locations'
urlpatterns = [
  path('mrt/', include('locations.mrt.urls')),
  path('destination/', include('locations.destination.urls'))
]