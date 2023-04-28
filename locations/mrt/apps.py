from django.apps import AppConfig

class MrtConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'locations.mrt'

    def ready(self):
        # import and include the submodules
        import locations.mrt.station
        import locations.mrt.connection
        import locations.mrt.platform