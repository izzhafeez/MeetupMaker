from django.urls import path

from . import views

urlpatterns = [
  path('mrt/create/', views.create, name="create_mrt"),
  path('mrt/read/', views.read, name="read_mrt"),
  path('mrt/delete/', views.delete, name="delete_mrt")
]