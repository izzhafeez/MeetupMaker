from django.apps import AppConfig

class LocationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'locations'
    
    def ready(self):
        # import and include the submodules
        import locations.mrt
        