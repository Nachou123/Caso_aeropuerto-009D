from django.db import models

# Create your models here.



class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=9, verbose_name="Idcliente")
    nombrecliente = models.CharField(max_length=50, verbose_name="nombreCliente")
    destino = models.CharField(max_length=50, verbose_name="Destino")
    correo = models.CharField(max_length=50, verbose_name="Correo")
    fono = models.IntegerField( verbose_name='Fono')

    def __str__(self):
        return self.rut

