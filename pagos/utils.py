import re

def limpiar_texto_especialidad(texto):
    # Elimina caracteres especiales, quita espacios extra y convierte en mayúsculas
    texto = re.sub(r'[^A-Za-z0-9 ]+', '', texto)  # Elimina caracteres especiales
    texto = texto.strip().upper()  # Elimina espacios en blanco y convierte a mayúsculas
    return texto

from fuzzywuzzy import fuzz

def encontrar_mejor_coincidencia_fuzzy(especialidad_usuario, especialidades):
    mejor_coincidencia = None
    mejor_puntuacion = 0
    
    for especialidad in especialidades:
        puntuacion = fuzz.ratio(especialidad_usuario, especialidad)
        if puntuacion > mejor_puntuacion and puntuacion > 85:  # Umbral más estricto
            mejor_coincidencia = especialidad
            mejor_puntuacion = puntuacion
    
    return mejor_coincidencia if mejor_coincidencia else especialidad_usuario


def mapear_especialidad(especialidad_usuario):
    # Mapeo manual de especialidades para garantizar coincidencias exactas
    mapeo_especialidades = {
        "OPERACIÓN MÓVIL MULTIEXPERTO RED MÓVIL": "MULTIEXPERTO RED MÓVIL (M)",
        "OPERACIÓN FIJA MULTIEXPERTO RED FIBRA": "MULTIEXPERTO RED FIBRA (F)",
        "LOCALIZADOR - EMPALMADOR EXPERTO COBRE / FIBRA": "LOCALIZADOR - EMPALMADOR DE FIBRA",
        # Agregar más mapeos manuales si es necesario
    }
    
    return mapeo_especialidades.get(especialidad_usuario, especialidad_usuario)

def obtener_proyecto(nombre_team):
    # Tu lógica para obtener el proyecto con base en el nombre del equipo
    if 'COMANDO' in nombre_team:
        return 'COMANDO'
    elif 'ONNET' in nombre_team:
        return 'ONNET'
    # Añade más reglas según sea necesario
    return 'PROYECTO_DEFAULT'


def clasificar_especialidad(especialidad_usuario):
    # Lógica para clasificar la especialidad como 'especialidad' o 'vehículo'
    if "VEHÍCULO" in especialidad_usuario.upper():
        return "vehículo"
    return "especialidad"


from .models import TablaDePagoCapacity

from django.db.models import Sum

def calcular_resumen_mensual(mes, anio):
    """
    Calcula el resumen mensual agrupado por proyecto, tipo de especialidad,
    zona de adjudicación y zona operacional.

    Args:
        mes (int): Mes del que se desea calcular el resumen (1-12).
        anio (int): Año del que se desea calcular el resumen.

    Returns:
        dict: Diccionario con los resúmenes agrupados y los totales.
    """
    # Filtrar registros del modelo para el mes y año especificados
    registros = TablaDePagoCapacity.objects.filter(
        fecha__year=anio,
        fecha__month=mes
    )

    # Calcular los resúmenes agrupados
    resumen = registros.values(
        'proyecto', 'tipo_especialidad', 'zona_adjudicacion', 'zona_operacional'
    ).annotate(
        total_horas=Sum('total_hh'),
        total_phi=Sum('phi'),
        total_horas_phi=Sum('total_hh_phi'),
        total_Q=Sum('Q'),
        total_a_pagar=Sum('Total_a_Pago')
    )

    # Calcular totales generales
    totales = registros.aggregate(
        total_horas=Sum('total_hh'),
        total_phi=Sum('phi'),
        total_horas_phi=Sum('total_hh_phi'),
        total_Q=Sum('Q'),
        total_a_pagar=Sum('Total_a_Pago')
    )

    return {
        'resumen': list(resumen),
        'totales': totales,
        'mes': mes,
        'anio': anio,
    }

import re

def limpiar_texto(texto):
    """
    Limpia el texto eliminando espacios adicionales y normalizando mayúsculas.
    """
    if not isinstance(texto, str):
        return ""
    texto_limpio = re.sub(r'\s+', ' ', texto.strip())  # Eliminar espacios adicionales
    return texto_limpio.upper()  # Convertir a mayúsculas
