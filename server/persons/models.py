from django.db import models

from django.db.models import Model, TextField

# Create your models here.
class Person(Model):
  name = TextField(
    primary_key=True
  )
  
  home_address = models.ForeignKey(
    'locations.Location',
    on_delete=models.CASCADE,
    related_name='home_address'
  )
  
  outside_address = models.ForeignKey(
    "locations.Location",
    on_delete=models.CASCADE,
    related_name='outside_address'
  )
