from django.db.models import CASCADE, ForeignKey, Model

from ..platform.models import Platform

class Connection(Model):
  start_platform = ForeignKey(
    Platform,
    on_delete=CASCADE,
    related_name='start_connection',
    blank=False)
  
  end_platform = ForeignKey(
    Platform,
    on_delete=CASCADE,
    related_name='end_connection',
    blank=False)