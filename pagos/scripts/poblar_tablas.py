from pagos.models import Capacity, EspecialidadUsuario, Team, Tecnico, Area, ZonaOperacional, ZonaAdjudicacion, Proyecto, NombreTecnico, NombreTeam
from pagos.utils import obtener_proyecto, limpiar_texto, fuzz
from django.db import IntegrityError
from datetime import datetime
import hashlib
from datetime import datetime

from pagos.models import  ActualizacionDePagos
from fuzzywuzzy import process



def obtener_precio_especialidad(especialidad):
    # Limpiar el texto de la especialidad
    especialidad_limpia = limpiar_texto(especialidad)

    # Obtener todos los items de ActualizacionDePagos
    items_pagos = ActualizacionDePagos.objects.values_list('item', 'nuevo_precio_2024')
    
    # Crear una lista con los items para la coincidencia aproximada
    items_lista = [limpiar_texto(item[0]) for item in items_pagos]

    # Buscar la mejor coincidencia con fuzzywuzzy
    mejor_coincidencia = process.extractOne(especialidad_limpia, items_lista, scorer=fuzz.ratio)
    
    if mejor_coincidencia:
        # Obtener el índice de la mejor coincidencia
        indice_coincidencia = items_lista.index(mejor_coincidencia[0])
        
        # Obtener el precio correspondiente
        precio = items_pagos[indice_coincidencia][1]
        return precio

    # Si no hay coincidencia, retornar None o un valor por defecto
    return None

def asignar_precios_desde_actualizacion():
    # Iterar sobre todos los registros de Capacity
    for capacity in Capacity.objects.all():
        # Obtener el precio usando la función de coincidencia aproximada
        precio = obtener_precio_especialidad(capacity.especialidad_usuario)
        
        if precio:
            # Actualizar o crear el registro de EspecialidadUsuario con el precio encontrado
            especialidad, created = EspecialidadUsuario.objects.update_or_create(
                nombre=capacity.especialidad_usuario,
                defaults={'descripcion': 'Automático desde Capacity', 'precio': precio}
            )
            print(f"Especialidad: {especialidad.nombre}, Precio asignado: {precio}")
        else:
            print(f"No se encontró precio para la especialidad: {capacity.especialidad_usuario}")


def generar_codigo_unico(base_codigo):
    base_codigo_limpio = limpiar_texto(base_codigo)
    codigo_hash = hashlib.md5(f"{base_codigo_limpio}{datetime.now()}".encode()).hexdigest()[:8]  # Generar un hash único
    codigo_unico = f"{base_codigo_limpio}-{codigo_hash}"
    return codigo_unico

def poblar_tablas_desde_capacity():
    # Iterar sobre todos los registros de Capacity
    for capacity in Capacity.objects.all():
        # Poblar EspecialidadUsuario
        especialidad, created = EspecialidadUsuario.objects.get_or_create(
            nombre=capacity.especialidad_usuario, 
            defaults={'descripcion': 'Automático desde Capacity', 'precio': 0.00}
        )

        # Poblar Team
        team, created = Team.objects.get_or_create(nombre=capacity.nombre_team)

        # Poblar Técnico
        tecnico, created = Tecnico.objects.get_or_create(
            nombre=capacity.nombre_tecnico, 
            defaults={'especialidad': especialidad}
        )

        # Poblar Área
        area, created = Area.objects.get_or_create(nombre=capacity.area)

        # Poblar Zona Operacional
        zona_operacional, created = ZonaOperacional.objects.get_or_create(nombre=capacity.zona_operacional)

        # Poblar Zona de Adjudicación
        if capacity.zona_adjudicacion:
            try:
                codigo_unico = generar_codigo_unico(capacity.zona_adjudicacion)
                zona_adjudicacion, created = ZonaAdjudicacion.objects.get_or_create(
                    nombre=capacity.zona_adjudicacion,
                    defaults={'codigo': codigo_unico}
                )
            except IntegrityError:
                # Si ocurre una duplicidad, generar un nuevo codigo único y reintentar la creación
                codigo_unico = generar_codigo_unico(f"{capacity.zona_adjudicacion}-{datetime.now()}")
                zona_adjudicacion, created = ZonaAdjudicacion.objects.get_or_create(
                    nombre=capacity.zona_adjudicacion,
                    defaults={'codigo': codigo_unico}
                )
                print(f"Advertencia: Código duplicado para {capacity.zona_adjudicacion}. Se ha generado un nuevo código: {codigo_unico}")
                continue

        # Poblar Proyecto
        nombre_proyecto = obtener_proyecto(capacity.nombre_team)
        proyecto, created = Proyecto.objects.get_or_create(
            nombre=nombre_proyecto, 
            defaults={'descripcion': 'Proyecto derivado del nombre del equipo'}
        )

        # Poblar Nombre de Técnico
        nombre_tecnico, created = NombreTecnico.objects.get_or_create(nombre=capacity.nombre_tecnico)

        # Poblar Nombre de Team
        nombre_team, created = NombreTeam.objects.get_or_create(nombre=capacity.nombre_team)

        print(f"Datos del técnico {capacity.nombre_tecnico} guardados correctamente.")

from pagos.models import TablaDePagoCapacity, Capacity

def sincronizar_fechas():
    # Iterar sobre los registros de TablaDePagoCapacity
    for registro in TablaDePagoCapacity.objects.all():
        # Buscar el registro correspondiente en Capacity
        capacidad = Capacity.objects.filter(
            nombre_tecnico=registro.nombre_tecnico,
            nombre_team=registro.nombre_team,
            especialidad_usuario=registro.especialidad_usuario
        ).first()

        # Si existe, sincronizar la fecha
        if capacidad:
            registro.fecha = capacidad.fecha_extract_registro
            registro.save()
        else:
            print(f"No se encontró un registro de Capacity para: {registro.nombre_tecnico}")
