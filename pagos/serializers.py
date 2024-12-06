from rest_framework import serializers
from .models import Capacity, NuevaTablaPagos, TablaDePagoCapacity, SLAReport

import math
import logging
from rest_framework import serializers
from .models import Capacity

logger = logging.getLogger(__name__)

class CapacitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Capacity
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        for key, value in data.items():
            if isinstance(value, float) and math.isnan(value):
                logger.warning(f"Campo '{key}' con valor NaN en el registro ID: {instance.id}")
                data[key] = None  # O cualquier valor predeterminado que consideres apropiado
        return data

from rest_framework import serializers
from .models import NuevaTablaPagos

class NuevaTablaPagosSerializer(serializers.ModelSerializer):
    class Meta:
        model = NuevaTablaPagos
        fields = '__all__'


from rest_framework import serializers
from .models import TablaDePagoCapacity

class TablaDePagoCapacitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TablaDePagoCapacity
        fields = '__all__'

class SLAReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SLAReport
        fields = '__all__'  # Incluir todos los campos del modelo


