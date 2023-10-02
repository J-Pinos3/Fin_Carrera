from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Cliente(models.Model):
    cedula = models.IntegerField(validators=[MaxValueValidator(99999999999)])
    nombre= models.CharField(max_length=3)
    apellido = models.CharField(max_length=10)
    fecha_nacimiento = models.CharField(max_length = 20)
    dependencia = models.CharField(max_length = 20)
    ciudad = models.CharField(max_length = 10)
    direccion = models.CharField(max_length = 20)
    telefono = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20)

    def __str__(self):
        return(f"{self.nombre} {self.apellido}")