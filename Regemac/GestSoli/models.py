from django.db import models

# Create your models here.

class Solicitud(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    cliente = models.CharField(max_length=50)
    sucursal = models.CharField(max_length=50)
    direccion = models.CharField(max_length=150)
    solicitante = models.CharField(max_length=50)
    prioridad = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.codigo, self.prioridad)

