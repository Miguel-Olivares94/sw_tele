from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.forms import modelformset_factory
from .models import CustomUser, Capacity, LPU,NuevaTablaPagos

# Authentication Forms
class CustomAuthenticationForm(AuthenticationForm):
    """
    Formulario personalizado para la autenticación de usuarios.
    Permite el inicio de sesión con RUT y contraseña.
    """
    username = forms.CharField(
        label='RUT',
        max_length=12,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RUT'}),
        error_messages={
            'required': 'Este campo es obligatorio.',
            'invalid': 'Ingrese un RUT válido.'
        }
    )
    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        error_messages={
            'required': 'Este campo es obligatorio.'
        }
    )
    remember_me = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )

class CustomUserCreationForm(UserCreationForm):
    """
    Formulario personalizado para la creación de usuarios.
    Incluye campos adicionales como nombres, celular y email.
    """
    first_name = forms.CharField(max_length=30, required=True)
    last_name_paterno = forms.CharField(max_length=30, required=True)
    last_name_materno = forms.CharField(max_length=30, required=True)
    celular = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = (
            'rut', 'first_name', 'last_name_paterno', 
            'last_name_materno', 'celular', 'email', 
            'password1', 'password2'
        )

class CustomUserChangeForm(UserChangeForm):
    """
    Formulario personalizado para la actualización de datos de usuarios.
    Permite editar la información existente del usuario.
    """
    class Meta:
        model = CustomUser
        fields = (
            'rut', 'first_name', 'last_name_paterno', 
            'last_name_materno', 'celular', 'email'
        )

# Formulario para cargar archivos Excel
from django import forms

from django import forms

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField(label='Selecciona un archivo Excel')


class ExcelUploadForm(forms.Form):
    """
    Formulario para la carga de archivos Excel.
    """
    excel_file = forms.FileField(label='Seleccione el archivo Excel')

from django import forms
from .models import Capacity

from django import forms
from .models import Capacity

from django import forms
from .models import Capacity
from django import forms
from django.forms.models import modelformset_factory
from .models import Capacity

class CapacityForm(forms.ModelForm):
    rut_tecnico = forms.CharField(required=True, label='RUT Técnico')

    class Meta:
        model = Capacity
        fields = [
            'fecha_extract_registro', 'nombre_tecnico', 'nombre_team', 'especialidad_usuario',
            'area', 'rut_tecnico', 'zona_operacional', 'zona_adjudicacion', 'especialidad_team',
            'capacidad', 'total_hh', 'phi', 'total_hh_phi'
        ]
        
        widgets = {
            'fecha_extract_registro': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'nombre_tecnico': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_team': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidad_usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'area': forms.TextInput(attrs={'class': 'form-control'}),
            'rut_tecnico': forms.TextInput(attrs={'class': 'form-control'}),
            'zona_operacional': forms.TextInput(attrs={'class': 'form-control'}),
            'zona_adjudicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidad_team': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_hh': forms.NumberInput(attrs={'class': 'form-control'}),
            'phi': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_hh_phi': forms.NumberInput(attrs={'class': 'form-control'}),
        }

CapacityFormSet = modelformset_factory(Capacity, form=CapacityForm, extra=0)

from .models import NuevaTablaPagos

# pagos/forms.py

from django import forms
from .models import NuevaTablaPagos

class NuevaTablaPagosForm(forms.ModelForm):
    class Meta:
        model = NuevaTablaPagos
        fields = '__all__'  # Incluye todos los campos del modelo

        widgets = {
            'sociedad': forms.Select(attrs={'class': 'form-control'}),
            'material': forms.Select(attrs={'class': 'form-control'}),
            'especialidad': forms.Select(attrs={'class': 'form-control'}),
            'zona_adjudicacion': forms.Select(attrs={'class': 'form-control'}),
            'zona_operacional': forms.Select(attrs={'class': 'form-control'}),
            'nuevo_precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'desvio_porcentaje': forms.NumberInput(attrs={'class': 'form-control'}),
            'area': forms.Select(attrs={'class': 'form-control'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control'}),  # Widget para 'anio'
        }

    def clean_anio(self):
        anio = self.cleaned_data.get('anio')
        if anio:
            if anio < 1900 or anio > 2100:
                raise forms.ValidationError("Ingrese un año válido entre 1900 y 2100.")
        return anio

# Forms for the LPU model
from django import forms


class LPUExcelUploadForm(forms.Form):
    excel_file = forms.FileField(label='Seleccione el archivo Excel')


from django import forms
from .models import LPU

class LPUForm(forms.ModelForm):
    class Meta:
        model = LPU
        fields = '__all__'  # o los campos específicos que deseas incluir
        widgets = {
            'numero_de_tarea': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_red': forms.TextInput(attrs={'class': 'form-control'}),
            'area_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'zona_adjudicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'zona_operativa': forms.TextInput(attrs={'class': 'form-control'}),
            'sap_fijo_lpu': forms.TextInput(attrs={'class': 'form-control'}),
            'sap_capex_lpu': forms.TextInput(attrs={'class': 'form-control'}),
            'sap_opex_lpu': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_de_trabajo': forms.TextInput(attrs={'class': 'form-control'}),
            'item_lpu': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_mdm': forms.NumberInput(attrs={'class': 'form-control'}),
            'servicios': forms.NumberInput(attrs={'class': 'form-control'}),
            'factor_multiplicador': forms.NumberInput(attrs={'class': 'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
            'pagada': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'fecha_finalizacion_tarea': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_ingreso_trans_sap': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'tiempo_trans_sap': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_ingreso_validar_trans_sap': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'tiempo_validar_trans_sap': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_de_proyecto': forms.TextInput(attrs={'class': 'form-control'}),
            'ano_finalizacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'mes_finalizacion': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class LPUFilterForm(forms.Form):
    """
    Formulario para filtrar registros del modelo LPU.
    Permite filtrar por número de tarea, tipo de red y estado de trabajo.
    """
    numero_de_tarea = forms.ChoiceField(
        choices=[('', 'Seleccione una tarea')],
        label='Número de Tarea',
        required=False
    )
    tipo_red = forms.ChoiceField(
        choices=[('', 'Seleccione un tipo de red')],
        label='Tipo Red',
        required=False
    )
    estado_de_trabajo = forms.ChoiceField(
        choices=[('', 'Seleccione un estado')],
        label='Estado de Trabajo',
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            # Cargar las opciones de número de tarea
            tarea_choices = [(tarea, tarea) for tarea in LPU.objects.values_list('numero_de_tarea', flat=True).distinct()]
            self.fields['numero_de_tarea'].choices = [('', 'Seleccione una tarea')] + tarea_choices

            # Cargar las opciones de tipo de red
            tipo_red_choices = [(tipo, tipo) for tipo in LPU.objects.values_list('tipo_red', flat=True).distinct()]
            self.fields['tipo_red'].choices = [('', 'Seleccione un tipo de red')] + tipo_red_choices

            # Cargar las opciones de estado de trabajo
            estado_choices = [(estado, estado) for estado in LPU.objects.values_list('estado_de_trabajo', flat=True).distinct()]
            self.fields['estado_de_trabajo'].choices = [('', 'Seleccione un estado')] + estado_choices
        except Exception as e:
            # Si hay algún error (por ejemplo, si la tabla no existe aún), mantener las opciones por defecto
            print(f"Error al cargar las opciones del formulario: {e}")


from django import forms
from .models import SLAReport

class SLAReportForm(forms.ModelForm):
    class Meta:
        model = SLAReport
        fields = '__all__'  # O selecciona los campos que quieras usar en el formulario


from django import forms
from .models import PrecioEspecialidad, NuevaTablaPagos

class PrecioEspecialidadForm(forms.ModelForm):
    class Meta:
        model = PrecioEspecialidad
        fields = '__all__'

    # Crear campos con opciones basadas en los valores únicos de la tabla NuevaTablaPagos
    especialidad = forms.ModelChoiceField(
        queryset=NuevaTablaPagos.objects.values_list('especialidad', flat=True).distinct(),
        widget=forms.Select,
        required=True,
        label="Especialidad"
    )

    zona_adjudicacion = forms.ModelChoiceField(
        queryset=NuevaTablaPagos.objects.values_list('zona_adjudicacion', flat=True).distinct(),
        widget=forms.Select,
        required=True,
        label="Zona de adjudicación"
    )

    zona_operacional = forms.ModelChoiceField(
        queryset=NuevaTablaPagos.objects.values_list('zona_operacional', flat=True).distinct(),
        widget=forms.Select,
        required=True,
        label="Zona Operacional"
    )

    area = forms.ModelChoiceField(
        queryset=NuevaTablaPagos.objects.values_list('area', flat=True).distinct(),
        widget=forms.Select,
        required=True,
        label="Área"
    )

    sociedad = forms.ModelChoiceField(
        queryset=NuevaTablaPagos.objects.values_list('sociedad', flat=True).distinct(),
        widget=forms.Select,
        required=True,
        label="Sociedad"
    )

    material = forms.ModelChoiceField(
        queryset=NuevaTablaPagos.objects.values_list('material', flat=True).distinct(),
        widget=forms.Select,
        required=True,
        label="Material"
    )

# pagos/forms.py

# pagos/forms.py

from django import forms
from .models import SLAReport  # Asegúrate de que SLAReport esté definido en models.py

class GenerarTablaSLAMesForm(forms.ModelForm):
    class Meta:
        model = SLAReport
        fields = ['fecha', 'bonus_o_malus']  # Reemplaza con los campos que necesites
        widgets = {
            'fecha': forms.SelectDateWidget(),  # Widget para seleccionar fecha
            'bonus_o_malus': forms.NumberInput(attrs={'step': '0.01'}),
        }
