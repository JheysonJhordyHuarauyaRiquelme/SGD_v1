from django.db import models
from dojos.models import Dojo  # Importamos el modelo Dojo
from alumnos.models import Alumno  # Importamos el modelo Alumno

class Pago(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    concepto = models.CharField(max_length=100)
    fecha_pago = models.DateTimeField()
    estado = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    dojo = models.ForeignKey(Dojo, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pago de {self.alumno} por {self.concepto}"
