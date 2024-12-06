from django.apps import AppConfig

class PagosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pagos'

    def ready(self):
        # Evita hacer consultas a la base de datos aquí
        pass
