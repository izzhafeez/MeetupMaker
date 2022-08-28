from django.urls import path

from . import views

urlpatterns = [
  path('malls/create/', views.create, name="create_malls"),
  path('malls/read/', views.read, name="read_malls"),
  path('malls/delete/', views.delete, name="delete_malls")
]