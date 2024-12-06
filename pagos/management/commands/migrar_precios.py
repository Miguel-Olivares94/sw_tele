from django.core.management.base import BaseCommand
from pagos.models import NuevaTablaPagos, PrecioEspecialidad

class Command(BaseCommand):
    help = "Migra los precios de las especialidades desde la tabla NuevaTablaPagos a PrecioEspecialidad"

    def handle(self, *args, **kwargs):
        # Obtiene todos los registros de la tabla NuevaTablaPagos
        registros_nueva_tabla = NuevaTablaPagos.objects.all()

        # Contador para llevar un seguimiento de los registros migrados
        migrados = 0

        # Itera sobre los registros de NuevaTablaPagos
        for registro in registros_nueva_tabla:
            # Intenta encontrar o crear un registro en PrecioEspecialidad basado en los datos de NuevaTablaPagos
            precio_especialidad, creado = PrecioEspecialidad.objects.get_or_create(
                especialidad=registro.especialidad,
                zona_adjudicacion=registro.zona_adjudicacion,
                zona_operacional=registro.zona_operacional,
                area=registro.area,
                anio=2024,  # Puedes cambiar el año si es necesario
                defaults={
                    'precio': registro.nuevo_precio_2024,
                }
            )
            
            # Si el registro fue creado o actualizado, incrementar el contador
            if creado:
                migrados += 1

        # Imprime el resultado de la migración
        self.stdout.write(self.style.SUCCESS(f'Migración completada: {migrados} precios migrados a PrecioEspecialidad'))
