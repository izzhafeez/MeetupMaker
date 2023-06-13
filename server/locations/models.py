from django.core.validators import MaxValueValidator, MinValueValidator

from django.db.models import DecimalField, Model, TextField

# Create your models here.
class Location(Model):
  name = TextField(
    primary_key=True
  )
  
  latitude = DecimalField(
    decimal_places=8,
    max_digits=9,
    validators=[
      MinValueValidator(1.23776),
      MaxValueValidator(1.47066)
    ]
  )
  
  longitude = DecimalField(
    decimal_places=8,
    max_digits=11,
    validators=[
      MinValueValidator(103.61751),
      MaxValueValidator(104.04360)
    ]
  )
  