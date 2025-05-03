from django.db import models
from dojos.models import Dojo  # si la app se llama dojos

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    dojo = models.ForeignKey(Dojo, on_delete=models.CASCADE, related_name='alumnos')
    estado = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
