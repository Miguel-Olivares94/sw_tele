from pagos.models import (
    Capacity, EspecialidadUsuario, Team, Tecnico, Area, ZonaOperativa,
    ZonaAdjudicacion, Proyecto, NombreTecnico, NombreTeam, TablaDePagoCapacity, ActualizacionDePagos
)
from pagos.utils import obtener_proyecto, limpiar_texto, fuzz
from django.db import transaction, IntegrityError
from fuzzywuzzy import process
import hashlib
from datetime import datetime


# Función para obtener precios
def obtener_precio_especialidad(especialidad):
    especialidad_limpia = limpiar_texto(especialidad)
    items_pagos = ActualizacionDePagos.objects.values_list('item', 'nuevo_precio_2024')
    items_lista = [limpiar_texto(item[0]) for item in items_pagos]

    mejor_coincidencia = process.extractOne(especialidad_limpia, items_lista, scorer=fuzz.ratio)
    if mejor_coincidencia:
        indice_coincidencia = items_lista.index(mejor_coincidencia[0])
        return items_pagos[indice_coincidencia][1]
    return None


# Función para generar códigos únicos
def generar_codigo_unico(base_codigo):
    base_codigo_limpio = limpiar_texto(base_codigo)
    codigo_hash = hashlib.md5(f"{base_codigo_limpio}{datetime.now()}".encode()).hexdigest()[:8]
    return f"{base_codigo_limpio}-{codigo_hash}"


# Poblar las tablas desde Capacity
def poblar_tablas_desde_capacity():
    with transaction.atomic():  # Iniciar una transacción atómica
        for capacity in Capacity.objects.all():
            # Poblar EspecialidadUsuario
            especialidad, _ = EspecialidadUsuario.objects.get_or_create(
                nombre=capacity.especialidad_usuario,
                defaults={'descripcion': 'Automático desde Capacity', 'precio': 0.00}
            )

            # Poblar Team
            team, _ = Team.objects.get_or_create(nombre=capacity.nombre_team)

            # Poblar Técnico
            tecnico, _ = Tecnico.objects.get_or_create(
                nombre=capacity.nombre_tecnico,
                defaults={'especialidad': especialidad}
            )

            # Poblar Área
            area, _ = Area.objects.get_or_create(nombre=capacity.area)

            # Poblar Zona Operativa
            zona_operativa, _ = ZonaOperativa.objects.get_or_create(nombre=capacity.zona_operacional)

            # Poblar Zona de Adjudicación con códigos únicos
            if capacity.zona_adjudicacion:
                codigo_unico = generar_codigo_unico(capacity.zona_adjudicacion)
                ZonaAdjudicacion.objects.update_or_create(
                    nombre=capacity.zona_adjudicacion,
                    defaults={'codigo': codigo_unico}
                )

            # Poblar Proyecto
            nombre_proyecto = obtener_proyecto(capacity.nombre_team)
            Proyecto.objects.get_or_create(
                nombre=nombre_proyecto,
                defaults={'descripcion': 'Proyecto derivado del nombre del equipo'}
            )

            # Poblar NombreTecnico y NombreTeam
            NombreTecnico.objects.get_or_create(nombre=capacity.nombre_tecnico)
            NombreTeam.objects.get_or_create(nombre=capacity.nombre_team)

            print(f"Datos de {capacity.nombre_tecnico} poblados correctamente.")


# Asignar precios a especialidades desde ActualizacionDePagos
def asignar_precios_desde_actualizacion():
    for capacity in Capacity.objects.all():
        precio = obtener_precio_especialidad(capacity.especialidad_usuario)
        if precio:
            EspecialidadUsuario.objects.update_or_create(
                nombre=capacity.especialidad_usuario,
                defaults={'descripcion': 'Actualizado con precio', 'precio': precio}
            )
            print(f"Precio asignado a {capacity.especialidad_usuario}: {precio}")
        else:
            print(f"Precio no encontrado para {capacity.especialidad_usuario}")


# Sincronizar fechas entre Capacity y TablaDePagoCapacity
def sincronizar_fechas():
    for registro in TablaDePagoCapacity.objects.all():
        capacidad = Capacity.objects.filter(
            nombre_tecnico=registro.nombre_tecnico,
            nombre_team=registro.nombre_team,
            especialidad_usuario=registro.especialidad_usuario
        ).first()

        if capacidad:
            registro.fecha = capacidad.fecha_extract_registro
            registro.save()
            print(f"Fecha sincronizada para {registro.nombre_tecnico}")
        else:
            print(f"No se encontró Capacity para {registro.nombre_tecnico}")


# Función principal
def ejecutar_proceso():
    print("Iniciando el proceso ETL...")
    poblar_tablas_desde_capacity()
    asignar_precios_desde_actualizacion()
    sincronizar_fechas()
    print("Proceso completado exitosamente.")
