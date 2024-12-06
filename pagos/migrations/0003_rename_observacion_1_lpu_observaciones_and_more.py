# Generated by Django 5.1.1 on 2024-11-14 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0002_rename_nuevo_precio_2024_tabladepagocapacity_nuevo_precio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lpu',
            old_name='observacion_1',
            new_name='observaciones',
        ),
        migrations.RemoveField(
            model_name='lpu',
            name='observacion_2',
        ),
        migrations.AddField(
            model_name='lpu',
            name='derivada_pago_septiembre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lpu',
            name='hem_pago_septiembre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lpu',
            name='monto_pagado_hem_septiembre',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='lpu',
            name='area_empresa',
            field=models.CharField(max_length=255, verbose_name='Área/Empresa'),
        ),
        migrations.AlterField(
            model_name='lpu',
            name='fecha_final',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lpu',
            name='fecha_finalizacion_tarea',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lpu',
            name='fecha_ingreso_trans_sap',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lpu',
            name='fecha_ingreso_validar_trans_sap',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lpu',
            name='mes_finalizacion',
            field=models.CharField(max_length=255),
        ),
    ]
