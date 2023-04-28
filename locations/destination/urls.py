from django.urls import path

from .views import create_destination, delete_destination, destination_detail, update_destination

app_name = 'destinations'
urlpatterns = [
  path('new/', create_destination, name='create_destination'),
  path('<str:pk>/', destination_detail, name='destination_detail'),
  path('<str:pk>/update/', update_destination, name='update_destination'),
  path('<str:pk>/delete/', delete_destination, name='delete_destination')
]