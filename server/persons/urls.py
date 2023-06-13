from django.urls import path

from .views import list_persons, create_person, read_person, update_person, delete_person

urlpatterns = [
  path('', list_persons, name="list_person"),
  path('create/', create_person, name='create_person'),
  path('<str:pk>/', read_person, name='read_person'),
  path('<str:pk>/update/', update_person, name='update_person'),
  path('<str:pk>/delete/', delete_person, name='delete_person') 
]