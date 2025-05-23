# Generated by Django 5.0.14 on 2025-05-03 18:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dojos', '0002_dojo_create_at_dojo_estado_dojo_update_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('estado', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('dojo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alumnos', to='dojos.dojo')),
            ],
        ),
    ]
