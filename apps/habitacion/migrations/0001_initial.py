# Generated by Django 3.2.3 on 2021-06-16 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado_Habitacion',
            fields=[
                ('id_estado_habitacion', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50, verbose_name='Estado Habitacion')),
            ],
            options={
                'verbose_name': 'Estado Habitacion',
                'verbose_name_plural': 'Estados de Habitacion',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='Rubro',
            fields=[
                ('id_rubro', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de Habitacion')),
            ],
            options={
                'verbose_name': 'Rubro',
                'verbose_name_plural': 'Rubros',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Tipo_Habitacion',
            fields=[
                ('id_tipo_habitacion', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50, verbose_name='Tipo Habitacion')),
            ],
            options={
                'verbose_name': 'Tipo Habitacion',
                'verbose_name_plural': 'Tipo de Habitaciones',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('num_habitacion', models.AutoField(primary_key=True, serialize=False)),
                ('valor', models.IntegerField(verbose_name='Valor de Habitacion')),
                ('accesorio', models.TextField(blank=True, max_length=255, null=True, verbose_name='Accesorios de la Habitacion')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habitacion.estado_habitacion')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habitacion.tipo_habitacion')),
            ],
            options={
                'verbose_name': 'Habitacion',
                'verbose_name_plural': 'Habitaciones',
                'ordering': ['num_habitacion'],
            },
        ),
    ]
