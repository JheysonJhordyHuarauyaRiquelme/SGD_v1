# dojos/models.py
from django.db import models
from usuarios.models import Usuario  # Importa el modelo de Usuario

class Dojo(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=255)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='dojo')
    estado = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
