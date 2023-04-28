from django.urls import path

from .views import create_platform, delete_platform, platform_detail, update_platform

app_name = 'platforms'
urlpatterns = [
  path('new/', create_platform, name='create_platform'),
  path('<str:pk>/', platform_detail, name='platform_detail'),
  path('<str:pk>/update/', update_platform, name='update_platform'),
  path('<str:pk>/delete/', delete_platform, name='delete_platform')
]