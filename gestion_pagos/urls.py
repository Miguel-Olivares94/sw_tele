from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pagos import views
from django.contrib.auth import views as auth_views  # Importa auth_views para la vista de login

# Crear un enrutador para las vistas de la API
router = routers.DefaultRouter()
router.register(r'capacity', views.CapacityViewSet)  # Registro de Capacity API ViewSet
router.register(r'nuevatablapagos', views.NuevaTablaPagosViewSet)  # Registro de NuevaTablaPagos API ViewSet
router.register(r'tabladedepagocapacity', views.TablaDePagoCapacityViewSet)  # Registro de TablaDePagoCapacity API ViewSet
router.register(r'slareport', views.SLAReportViewSet)  # Registro de SLAReport API ViewSet

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración
    path('pagos/', include('pagos.urls')),  # Incluir las rutas de la app 'pagos'
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('api/', include(router.urls)),  # Incluir las rutas de la API con Django Rest Framework
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # Autenticación API

    # Ruta por defecto para redireccionar a una página inicial
    path('', views.index, name='index'),  # Ruta principal (index)
]
