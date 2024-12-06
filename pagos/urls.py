# pagos/urls.py

from django.urls import path, include
from rest_framework import routers
from . import views
from .views import cargar_sla_excel
from .views import ver_resumen_mensual  # Ajusta según la ubicación de la vista


from .views import generar_tabla_pago_mes, sla_dashboard, resumen_pagos_sla
# Inicializar el enrutador de DRF y registrar los ViewSets
router = routers.DefaultRouter()
router.register(r'capacity', views.CapacityViewSet)
router.register(r'nuevatabladepagos', views.NuevaTablaPagosViewSet)
router.register(r'tabla_de_pago_capacity', views.TablaDePagoCapacityViewSet)
router.register(r'sla_report', views.SLAReportViewSet)
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Rutas de autenticación y navegación
    path('', views.index, name='index'),
        path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('menu/', views.menu, name='menu'),

    # Rutas relacionadas con TablaDePagoCapacity
    path('dashboard_tabladepago_capacity/', views.dashboard_tabladepago_capacity, name='dashboard_tabladepago_capacity'),
    path('pago_capacity/<int:year>/<int:month>/', views.ver_tabla_pago_capacity_mes, name='ver_tabla_pago_capacity_mes'),
    path('descargar_tabla_pago_capacity/<int:year>/<int:month>/', views.descargar_tabla_pago_capacity_mes, name='descargar_tabla_pago_capacity_mes'),


    # Rutas relacionadas con LPU
    path('lpu/', views.ver_lpu, name='ver_lpu'),
    path('lpu/crear/', views.crear_lpu, name='crear_lpu'),
    path('lpu/editar/<int:pk>/', views.editar_lpu, name='editar_lpu'),
    path('lpu/eliminar/<int:pk>/', views.eliminar_lpu, name='eliminar_lpu'),
    path('dashboard_lpu/', views.dashboard_lpu, name='dashboard_lpu'),
    path('lpu/ver/<int:year>/<int:month>/', views.ver_lpu_por_mes, name='ver_lpu_por_mes'),
    path('download-lpu-excel/', views.download_lpu_excel, name='download_lpu_excel'),

    # Rutas relacionadas con Capacity
    path('dashboard_capacity/', views.dashboard_capacity, name='dashboard_capacity'),
    path('cargar_excel/', views.cargar_excel, name='cargar_excel'),
    path('capacity/<int:year>/<int:month>/', views.ver_datos_capacity_mes, name='ver_datos_capacity_mes'),
    path('editar_capacity/<int:id>/', views.editar_capacity, name='editar_capacity'),
    path('eliminar_capacity/<int:pk>/', views.eliminar_capacity, name='eliminar_capacity'),
    path('crear_capacity/', views.crear_capacity, name='crear_capacity'),
    path('ver_todos_los_datos_capacity/', views.ver_todos_los_datos_capacity, name='ver_todos_los_datos_capacity'),

    # Rutas de NuevaTablaPagos
    path('nuevatabladepagos/', views.ver_nuevatabladepagos, name='nuevatabladepagos'),
    path('nuevatabladepagos/crear/', views.crear_nuevatabladepagos, name='crear_nuevatabladepagos'),
    path('nuevatabladepagos/editar/<int:pk>/', views.editar_nuevatabladepagos, name='editar_nuevatabladepagos'),
    path('nuevatabladepagos/eliminar/<int:pk>/', views.eliminar_nuevatabladepagos, name='eliminar_nuevatabladepagos'),
    path('nueva_tabla_pagos/', views.buscar_nueva_tabla_pagos, name='buscar_nueva_tabla_pagos'),
    path('cargar-nueva-tabla-pagos/', views.cargar_nueva_tabla_pagos, name='cargar_nueva_tabla_pagos'),
    path('dashboard-precios-especialidades/', views.dashboard_precios_especialidades, name='dashboard_precios_especialidades'),

    # Rutas de generación de tablas de pago y descarga de Excel
    path('generar_tabla_pago_capacity_mes/<int:year>/<int:month>/', views.generar_tabla_pago_capacity_mes, name='generar_tabla_pago_capacity_mes'),
    path('descargar_nueva_tabla_pagos/', views.descargar_nueva_tabla_pagos, name='descargar_nueva_tabla_pagos'),
    path('descargar_excel/<int:year>/<int:month>/', views.descargar_excel_pago_capacity, name='descargar_excel_pago_capacity'),
    path('descargar-capacity-por-mes/<int:year>/<int:month>/', views.descargar_capacity_por_mes, name='descargar_capacity_por_mes'),
    path('descargar-capacity/', views.descargar_capacity, name='descargar_capacity'),

    # Otras rutas
    path('pagos/resumen-pagos/', views.ver_resumen_pagos, name='ver_resumen_pagos'),

    # Rutas relacionadas con SLAReport
    path('sla/', views.ver_sla_report, name='ver_sla_report'),
    path('sla/crear/', views.crear_sla_report, name='crear_sla_report'),
    path('sla/editar/<int:pk>/', views.editar_sla_report, name='editar_sla_report'),
    path('sla/eliminar/<int:pk>/', views.eliminar_sla_report, name='eliminar_sla_report'),
    path('cargar-sla-excel/', cargar_sla_excel, name='cargar_sla_excel'),

    # Ruta para sla-dashboard
    path('sla-dashboard/', sla_dashboard, name='sla_dashboard'),
    path('resumen-pagos-sla/', resumen_pagos_sla, name='resumen_pagos_sla'),
    path('ver-datos-sla-mes/<int:year>/<int:month>/', views.ver_datos_sla_mes, name='ver_datos_sla_mes'),
    path('descargar-sla-por-mes/<int:year>/<int:month>/', views.descargar_sla_por_mes, name='descargar_sla_por_mes'),
    path('ver-todos-datos-sla/', views.ver_todos_los_datos_sla, name='ver_todos_los_datos_sla'),
    path('descargar-sla/', views.descargar_sla, name='descargar_sla'),
    path('generar-tabla-pago/<int:year>/<int:month>/', generar_tabla_pago_mes, name='generar_tabla_pago_mes'),

    # Ruta para generar tabla de pago SLA por mes y año
    path('sla/generar/<int:year>/<int:month>/', views.generar_tabla_pago_sla_mes, name='generar_tabla_pago_sla_mes'),

    # Ruta para ver precios por año
    path('precios/<int:anio>/', views.ver_precios_por_anio, name='ver_precios_por_anio'),
    path('ver-todos-precios-especialidades/', views.ver_todos_precios_especialidades, name='ver_todos_precios_especialidades'),

    # Ruta para cargar tabla LPU
    path('cargar_tabla_lpu/', views.cargar_tabla_lpu, name='cargar_tabla_lpu'),  # Asegúrate de añadir esta línea

    # API REST (utilizando router para los ViewSets)
    path('api/', include(router.urls)),  # Incluye todas las rutas de la API registradas con el router
    path('resumen-mensual/<int:month>/<int:year>/', ver_resumen_mensual, name='ver_resumen_mensual'),
    path('editar/<int:id>/', views.editar_registro, name='editar_registro'),
    path('eliminar/<int:id>/', views.eliminar_registro, name='eliminar_registro'),

]
