from django.apps import AppConfig

class DestinationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'locations.destination'

    def ready(self):
        # import and include the submodules
        pass