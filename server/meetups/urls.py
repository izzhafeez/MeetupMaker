from django.urls import path

from .views import list_meetups, create_meetup, read_meetup, delete_meetup

urlpatterns = [
  path('', list_meetups, name="list_meetup"),
  path('create/', create_meetup, name='create_meetup'),
  path('<str:pk>/', read_meetup, name='read_meetup'),
  path('<str:pk>/delete/', delete_meetup, name='delete_meetup') 
]