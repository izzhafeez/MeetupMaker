from django.urls import include, path

from . import views
from .malls.urls import urlpatterns as malls_urls
from .mrt.urls import urlpatterns as mrt_urls

urlpatterns = [
  path('', views.index, name='index'),
  *malls_urls,
  *mrt_urls
]