# pagos/filters.py
from django_filters import rest_framework as filters  # Importa el módulo de filtros de Django REST Framework.
from .models import Capacity  # Importa el modelo Capacity desde el módulo actual.

import django_filters
from django.shortcuts import render
from .models import Capacity
from django.db.models import Q
from django.core.paginator import Paginator  # Para la paginación
from django.contrib.auth.decorators import login_required  # Para requerir autenticación

import django_filters
from .models import Capacity

class CapacityFilter(django_filters.FilterSet):
    # Definir filtros personalizados si es necesario (por ejemplo, rango de fechas)
    fecha_extract_registro = django_filters.DateFromToRangeFilter(label='Rango de Fechas')
    nombre_tecnico = django_filters.CharFilter(lookup_expr='icontains', label='Nombre Técnico')
    rut_tecnico = django_filters.CharFilter(lookup_expr='icontains', label='RUT Técnico')
    especialidad_usuario = django_filters.CharFilter(lookup_expr='icontains', label='Especialidad Usuario')
    zona_operacional = django_filters.CharFilter(lookup_expr='icontains', label='Zona Operacional')
    zona_adjudicacion = django_filters.CharFilter(lookup_expr='icontains', label='Zona Adjudicación')
    area = django_filters.CharFilter(lookup_expr='icontains', label='Área')

    class Meta:
        model = Capacity
        fields = ['nombre_tecnico', 'rut_tecnico', 'especialidad_usuario', 'zona_operacional', 'zona_adjudicacion', 'area']

@login_required
def ver_datos_capacity_mes(request, year, month):
    # Filtrar por año y mes
    datos_list = Capacity.objects.filter(
        fecha_extract_registro__year=year,
        fecha_extract_registro__month=month
    )
    
    # Obtener los valores de los filtros del formulario
    rut_tecnico = request.GET.get('rut_tecnico', '')
    especialidad_usuario = request.GET.get('especialidad_usuario', '')
    zona_operacional = request.GET.get('zona_operacional', '')
    zona_adjudicacion = request.GET.get('zona_adjudicacion', '')
    area = request.GET.get('area', '')

    # Aplicar los filtros si se han enviado
    if rut_tecnico:
        datos_list = datos_list.filter(rut_tecnico__icontains=rut_tecnico)
    if especialidad_usuario:
        datos_list = datos_list.filter(especialidad_usuario__icontains=especialidad_usuario)
    if zona_operacional:
        datos_list = datos_list.filter(zona_operacional__icontains=zona_operacional)
    if zona_adjudicacion:
        datos_list = datos_list.filter(zona_adjudicacion__icontains=zona_adjudicacion)
    if area:
        datos_list = datos_list.filter(area__icontains=area)

    # Paginación
    paginator = Paginator(datos_list, 10)
    page_number = request.GET.get('page')
    datos = paginator.get_page(page_number)

    # Renderizar la plantilla con los datos y filtros
    return render(request, 'pagos/ver_datos_capacity_mes.html', {
        'datos': datos,
        'year': year,
        'month': month,
        'rut_tecnico': rut_tecnico,
        'especialidad_usuario': especialidad_usuario,
        'zona_operacional': zona_operacional,
        'zona_adjudicacion': zona_adjudicacion,
        'area': area,
    })

import django_filters
from .models import TablaDePagoCapacity

class PagoCapacityFilter(django_filters.FilterSet):
    class Meta:
        model = TablaDePagoCapacity
        fields = {
            'zona_operacional': ['exact'],
            'proyecto': ['exact'],
            'especialidad_usuario': ['exact'],
            # Puedes agregar más campos aquí según sea necesario
        }
