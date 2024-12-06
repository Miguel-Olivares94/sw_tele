from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import (
    CustomUser,
    Team,
    EspecialidadUsuario,
    Tecnico,
    Area,
    ZonaOperativa,
    NombreTecnico,
    NombreTeam,
    Proyecto,
    Capacity,
    FechaExtractRegistro,
    LPU,
    ResumenPago,
    ZonaAdjudicacion,
    SLAReport,
    NuevaTablaPagos,
    TablaDePagoCapacity,
    PrecioEspecialidad,
)
from .forms import PrecioEspecialidadForm

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('rut', 'first_name', 'last_name_paterno', 'last_name_materno', 'celular', 'email', 'is_staff', 'is_active')
    search_fields = ('rut', 'first_name', 'last_name_paterno', 'last_name_materno', 'email')
    list_filter = ('is_staff', 'is_active')
    ordering = ('rut',)
    fieldsets = (
        (None, {'fields': ('rut', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'last_name_paterno', 'last_name_materno', 'celular', 'email')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas Importantes', {'fields': ('last_login', 'date_joined')}),
    )

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(EspecialidadUsuario)
class EspecialidadUsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio')
    search_fields = ('nombre', 'descripcion')
    list_editable = ('precio',)
    list_filter = ('nombre',)

@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especialidad')
    search_fields = ('nombre', 'especialidad__nombre')
    list_filter = ('especialidad',)

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(PrecioEspecialidad)
class PrecioEspecialidadAdmin(admin.ModelAdmin):
    form = PrecioEspecialidadForm
    list_display = ('especialidad', 'zona_adjudicacion', 'zona_operacional', 'area', 'anio', 'precio')
    list_filter = ('anio', 'zona_adjudicacion', 'zona_operacional', 'area')
    search_fields = ('especialidad', 'zona_adjudicacion', 'zona_operacional', 'area')

@admin.register(ZonaOperativa)
class ZonaOperativaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)
    list_per_page = 20

    fieldsets = (
        (None, {
            'fields': ('nombre',)
        }),
    )

    class Meta:
        verbose_name = 'Zona Operativa'
        verbose_name_plural = 'Zonas Operativas'

@admin.register(NombreTecnico)
class NombreTecnicoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(NombreTeam)
class NombreTeamAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    filter_horizontal = ('tecnicos',)

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')

@admin.register(Capacity)
class CapacityAdmin(admin.ModelAdmin):
    list_display = ('nombre_tecnico', 'nombre_team', 'especialidad_usuario', 'area', 'rut_tecnico', 'zona_operacional', 'capacidad', 'total_hh', 'phi', 'total_hh_phi')
    search_fields = ('nombre_tecnico', 'nombre_team', 'especialidad_usuario', 'rut_tecnico', 'zona_operacional')
    list_filter = ('zona_operacional', 'especialidad_usuario', 'area')
    list_per_page = 50
    readonly_fields = ('created_at', 'updated_at')

@admin.register(NuevaTablaPagos)
class NuevaTablaPagosAdmin(admin.ModelAdmin):
    list_display = ('sociedad', 'material', 'especialidad', 'zona_adjudicacion', 'zona_operacional', 'nuevo_precio', 'desvio_porcentaje', 'area')
    search_fields = ('sociedad', 'material', 'especialidad', 'zona_adjudicacion', 'zona_operacional', 'area')
    list_filter = ('zona_adjudicacion', 'zona_operacional', 'area')

@admin.register(FechaExtractRegistro)
class FechaExtractRegistroAdmin(admin.ModelAdmin):
    list_display = ('nombre_tecnico', 'fecha_extract_registro', 'nombre_team', 'especialidad_usuario', 'area', 'rut_tecnico', 'zona_operacional', 'zona_adjudicacion', 'capacidad', 'total_hh', 'phi', 'total_hh_phi', 'mes_pago')
    search_fields = ('nombre_tecnico', 'nombre_team', 'especialidad_usuario', 'rut_tecnico', 'zona_operacional')
    list_filter = ('mes_pago', 'zona_operacional', 'especialidad_usuario', 'area')

@admin.register(LPU)
class LPUAdmin(admin.ModelAdmin):
    list_display = ('numero_de_tarea', 'tipo_red', 'area_empresa', 'zona_adjudicacion', 'estado_de_trabajo', 'total', 'pagada')
    search_fields = ('numero_de_tarea', 'tipo_red', 'area_empresa', 'zona_adjudicacion', 'estado_de_trabajo')
    list_filter = ('tipo_red', 'estado_de_trabajo', 'pagada')
    actions = ['exportar_csv', 'marcar_pagadas']

    def exportar_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="lpu.csv"'
        writer = csv.writer(response)
        writer.writerow(['Número de Tarea', 'Tipo de Red', 'Área/Empresa', 'Zona Adjudicación', 'Estado de Trabajo', 'Total', 'Pagada'])
        for lpu in queryset:
            writer.writerow([lpu.numero_de_tarea, lpu.tipo_red, lpu.area_empresa, lpu.zona_adjudicacion, lpu.estado_de_trabajo, lpu.total, lpu.pagada])
        return response
    exportar_csv.short_description = "Exportar seleccionados a CSV"

    def marcar_pagadas(self, request, queryset):
        queryset.update(pagada =True)
    marcar_pagadas.short_description = "Marcar como pagadas las LPU seleccionadas"

@admin.register(ResumenPago)
class ResumenPagoAdmin(admin.ModelAdmin):
    list_display = ('zona', 'especialidad', 'gastos_administrativos', 'lpu', 'sla', 'vehiculo', 'total_general')
    search_fields = ('zona',)

@admin.register(ZonaAdjudicacion)
class ZonaAdjudicacionAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    search_fields = ('codigo', 'nombre')

@admin.register(SLAReport)
class SLAReportAdmin(admin.ModelAdmin):
    list_display = ['zona_adjudicacion', 'zona_operativa', 'bonus_o_malus', 'proyecto']
    list_filter = ['zona_adjudicacion', 'proyecto']
