from django.urls import path

from . import views
from .coordinates import views as c_views

urlpatterns = [
  path('', views.index, name='index'),
]