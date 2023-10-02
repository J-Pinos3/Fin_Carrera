from django.db import models

# Create your models here.
class Tecnico(models.Model):
    nombre= models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    cedula = models.CharField(max_length = 20)
    fecha_nacimiento = models.CharField(max_length = 20)
    genero = models.CharField(max_length = 20)
    ciudad = models.CharField(max_length = 20)
    direccion = models.CharField(max_length = 20)
    telefono = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20)

    def __str__(self):
        return(f"{self.nombre} {self.apellido}")