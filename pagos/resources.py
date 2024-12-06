# pagos/resources.py
from import_export import resources
from .models import Capacity

class CapacityResource(resources.ModelResource):
    """
    Recurso para importar y exportar datos del modelo Capacity.
    Facilita la gestión de datos en formatos como CSV, Excel, etc.
    """
    class Meta:
        model = Capacity  # Especifica el modelo que se va a importar/exportar
