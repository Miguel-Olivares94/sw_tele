from django.core.management.base import BaseCommand
from pagos.models import Capacity
from django.db.models import Count

class Command(BaseCommand):
    help = 'Eliminar duplicados de Capacity manteniendo la primera entrada'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Buscando duplicados en Capacity...'))
        
        duplicados = Capacity.objects.values('nombre_tecnico', 'fecha_extract_registro').annotate(count=Count('id')).filter(count__gt=1)
        
        if not duplicados:
            self.stdout.write(self.style.SUCCESS('No se encontraron duplicados.'))
            return

        for entry in duplicados:
            Capacity.objects.filter(
                nombre_tecnico=entry['nombre_tecnico'], 
                fecha_extract_registro=entry['fecha_extract_registro']
            ).order_by('id')[1:].delete()

        self.stdout.write(self.style.SUCCESS('Duplicados eliminados con éxito.'))
