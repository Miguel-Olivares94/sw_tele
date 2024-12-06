# Generated by Django 5.1.1 on 2024-10-23 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0003_rename_tipo_red2_lpu_tipo_red_2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrecioEspecialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.CharField(max_length=255)),
                ('zona_adjudicacion', models.CharField(max_length=255)),
                ('zona_operacional', models.CharField(max_length=255)),
                ('area', models.CharField(max_length=255)),
                ('anio', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'unique_together': {('especialidad', 'zona_adjudicacion', 'zona_operacional', 'area', 'anio')},
            },
        ),
    ]