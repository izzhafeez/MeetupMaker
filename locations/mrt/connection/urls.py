from django.urls import path

from .views import create_connection, delete_connection, connection_detail, update_connection

app_name = 'connections'
urlpatterns = [
  path('new/', create_connection, name='create_connection'),
  path('<int:pk>/', connection_detail, name='connection_detail'),
  path('<int:pk>/update/', update_connection, name='update_connection'),
  path('<int:pk>/delete/', delete_connection, name='delete_connection')
]