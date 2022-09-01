from django.urls import include, path

from . import views

urlpatterns = [
  path('find', views.find, name='meetup_find'),
]