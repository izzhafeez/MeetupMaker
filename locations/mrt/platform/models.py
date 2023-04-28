from django.core.validators import RegexValidator
from django.db.models import CASCADE, CharField, ForeignKey, Model

from ..station.models import Station

CODE_VALIDATION_MESSAGE = 'Code must start with two letters, followed by an integer, and an optional ending letter.'

class Platform(Model):
  code_validator = RegexValidator(
    regex=r'^[a-zA-Z]{2}\d+[a-zA-Z]?$',
    message=CODE_VALIDATION_MESSAGE
    )
  
  code = CharField(
    max_length=5,
    unique=True,
    primary_key=True,
    blank=False,
    validators=[code_validator]
    )
  
  station = ForeignKey(
    Station,
    on_delete=CASCADE,
    related_name='platforms',
    blank=False
    )
  