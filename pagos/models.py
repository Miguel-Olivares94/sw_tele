from django.db import models
from django.contrib.auth.models import AbstractUser 

# Modelo de usuario personalizado
class CustomUser (AbstractUser ):
    rut = models.CharField(max_length=12, unique=True)
    first_name = models.CharField(max_length=30)
    last_name_paterno = models.CharField(max_length=30)
    last_name_materno = models.CharField(max_length=30)
    celular = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'rut'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name_paterno', 'last_name_materno', 'celular', 'email']

    def __str__(self):
        return self.rut

# Modelo de Team
class Team(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo de Especialidad de Usuario
class EspecialidadUsuario(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.nombre} - {self.precio}'

# Modelo de Técnico
class Tecnico(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.ForeignKey(EspecialidadUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

# Modelo de Especialidad
class Especialidad(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre

# Modelo de Nueva Tabla de Pagos
class NuevaTablaPagos(models.Model):
    sociedad = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=255)
    zona_adjudicacion = models.CharField(max_length=255)
    zona_operacional = models.CharField(max_length=255)
    nuevo_precio = models.DecimalField(max_digits=10, decimal_places=2)
    desvio_porcentaje = models.DecimalField(max_digits=5, decimal_places=4)
    area = models.CharField(max_length=255)
    anio = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.sociedad} - {self.material} - {self.especialidad}"

# Modelo de Área
class Area(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo de SLA Report
class SLAReport(models.Model):
    zona_adjudicacion = models.CharField(max_length=255)
    zona_operativa = models.CharField(max_length=255)
    bonus_o_malus = models.DecimalField(max_digits=12, decimal_places=2)
    proyecto = models.CharField(max_length=255)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.zona_adjudicacion} - {self.proyecto}"

# Modelo de LPU
class LPU(models.Model):
    numero_de_tarea = models.CharField(max_length=255)
    tipo_red = models.CharField(max_length=255)
    area_empresa = models.CharField(max_length=255)
    zona_adjudicacion = models.CharField(max_length=255)
    zona_operativa = models.CharField(max_length=255)
    zona_cluster = models.CharField(max_length=255)
    estado_de_trabajo = models.CharField(max_length=255)
    sap_fijo_lpu = models.CharField(max_length=255)
    sap_capex_lpu = models.CharField(max_length=255)
    sap_opex_lpu = models.CharField(max_length=255)
    item_lpu = models.CharField(max_length=255)
    precio_mdm = models.DecimalField(max_digits=10, decimal_places=2)
    servicios = models.CharField(max_length=255)
    factor_multiplicador = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado_presupuesto = models.CharField(max_length=255)
    pagada = models.BooleanField(default=False)
    fecha_finalizacion_tarea = models.DateTimeField(null=True, blank=True)
    fecha_ingreso_trans_sap = models.DateTimeField(null=True, blank=True)
    tiempo_trans_sap = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha_ingreso_validar_trans_sap = models.DateTimeField(null=True, blank=True)
    tiempo_validar_trans_sap = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha_final = models.DateTimeField(null=True, blank=True)
    nombre_de_proyecto = models.CharField(max_length=255)
    ano_finalizacion = models.IntegerField()
    mes_finalizacion = models.CharField(max_length=3)  # Almacena el mes como abreviatura de texto (por ejemplo, "oct")
    tipo_red2 = models.CharField(max_length=255)
    observaciones = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.numero_de_tarea} - {self.nombre_de_proyecto}"
    def pagada_si_no(self):
        return "SI" if self.pagada else "NO"



# pagos/models.py
class ZonaOperativa(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo de Nombre de Técnico
class NombreTecnico(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo de Nombre de Team
class NombreTeam(models.Model):
    nombre = models.CharField(max_length=100)
    tecnicos = models.ManyToManyField(Tecnico, blank=True)

    def __str__(self):
        return self.nombre

# Modelo de Proyecto
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)  
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

# Modelo de Capacidad
class Capacity(models.Model):
    fecha_extract_registro = models.DateField()
    nombre_tecnico = models.CharField(max_length=100)
    nombre_team = models.CharField(max_length=100)
    especialidad_usuario = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    rut_tecnico = models.CharField(max_length=12)
    zona_operacional = models.CharField(max_length=100)
    zona_adjudicacion = models.CharField(max_length=100)
    especialidad_team = models.CharField(max_length=100)
    capacidad = models.FloatField()
    total_hh = models.FloatField()
    phi = models.FloatField(null=True, blank=True)
    total_hh_phi = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def Q(self):
        return self.total_hh_phi / 176 if self.total_hh_phi else 0

    @property
    def precio(self):
        # Implementa aquí la lógica de asignación de precios (basada en utils.py)
        return 1142004  

    @property
    def total_a_pago(self):
        return self.Q * self.precio    


# Modelo de Fecha Extract Registro
class FechaExtractRegistro(models.Model):
    nombre_tecnico = models.CharField(max_length=100)
    fecha_extract_registro = models.DateField()
    nombre_team = models.CharField(max_length=100)
    especialidad_usuario = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    rut_tecnico = models.CharField(max_length=100)
    zona_operacional = models.CharField(max_length=100)
    zona_adjudicacion = models.CharField(max_length=100)
    capacidad = models.DecimalField(max_digits=10, decimal_places=2)
    total_hh = models.DecimalField(max_digits=10, decimal_places=2)
    phi = models.DecimalField(max_digits=10, decimal_places=2)
    total_hh_phi = models.DecimalField(max_digits=10, decimal_places=2)
    mes_pago = models.CharField(max_length=7, default='2024-01')


# Modelo de Resumen de Pago
class ResumenPago(models.Model):
    zona = models.CharField(max_length=255)
    especialidad = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    gastos_administrativos = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    lpu = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    sla = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    vehiculo = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    total_general = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return self.zona

# Modelo de Zona de Adjudicación
class ZonaAdjudicacion(models.Model):
    codigo = models.CharField(max_length=20, unique=True)  
    nombre = models.CharField(max_length=100)  

    def __str__(self):
        return f'{self.codigo} - {self.nombre}'
from django.db import models

class TablaDePagoCapacity(models.Model):
    nombre_tecnico = models.CharField(max_length=255)
    nombre_team = models.CharField(max_length=255)
    especialidad_usuario = models.CharField(max_length=255)
    rut_tecnico = models.CharField(max_length=12)
    zona_operacional = models.CharField(max_length=255)
    zona_adjudicacion = models.CharField(max_length=255)
    total_hh = models.DecimalField(max_digits=10, decimal_places=2)
    phi = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_hh_phi = models.DecimalField(max_digits=10, decimal_places=2)
    nuevo_precio = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    Q = models.DecimalField(max_digits=10, decimal_places=2)
    Total_a_Pago = models.DecimalField(max_digits=12, decimal_places=2)
    tipo_red = models.CharField(max_length=50)
    proyecto = models.CharField(max_length=255)
    tipo_especialidad = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    fecha = models.DateField(null=True, blank=True)  # Nuevo campo de fecha

    def __str__(self):
        return self.nombre_tecnico

# Modelo de PrecioEspecialidad
class PrecioEspecialidad(models.Model):
    sociedad = models.CharField(max_length=255, blank=True, null=True)  
    material = models.CharField(max_length=255, blank=True, null=True)  
    especialidad = models.CharField(max_length=255)
    zona_adjudicacion = models.CharField(max_length=255)
    zona_operacional = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    anio = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    desvio_porcentaje = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)  

    class Meta:
        unique_together = ['especialidad', 'zona_adjudicacion', 'zona_operacional', 'area', 'anio']

    def __str__(self):
        return f"{self.especialidad} - {self.anio}"
    
    
class ActualizacionDePagos(models.Model):
    item = models.CharField(max_length=255)
    nuevo_precio_2024 = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.item} - {self.nuevo_precio_2024}"
