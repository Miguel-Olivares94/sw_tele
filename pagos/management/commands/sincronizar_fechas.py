from django.core.management.base import BaseCommand
from pagos.models import TablaDePagoCapacity, Capacity

class Command(BaseCommand):
    help = 'Sincroniza las fechas entre Capacity y TablaDePagoCapacity'

    def handle(self, *args, **kwargs):
        for registro in TablaDePagoCapacity.objects.all():
            capacidad = Capacity.objects.filter(
                nombre_tecnico=registro.nombre_tecnico,
                nombre_team=registro.nombre_team,
                especialidad_usuario=registro.especialidad_usuario
            ).first()

            if capacidad:
                registro.fecha = capacidad.fecha_extract_registro
                registro.save()
                self.stdout.write(self.style.SUCCESS(f"Fecha sincronizada para {registro.nombre_tecnico}"))
            else:
                self.stdout.write(self.style.WARNING(f"No se encontró Capacity para {registro.nombre_tecnico}"))
