from django.db import models
from django.contrib.auth.models import User
from Tecnicos.models import Tecnico
from clientes.models import Cliente
# Create your models here.
class Ticket(models.Model):
    codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=20)
    id_tecnico = models.ForeignKey(Tecnico, related_name="tecnicos", on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, related_name="clientes", on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = 'Tickets'

    #para que en el django admin,
    #la tarea se muestre como <titulo de la tarea>
    def __str__(self) -> str:
        return self.codigo
