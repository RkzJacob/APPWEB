from typing import ChainMap
from django.db import models

# Create your models here.
class Medicamento(models.Model):
    codigo = models.CharField(primary_key=True,max_length=5,verbose_name='codigo')
    nombreMedicamento=models.CharField(max_length=40,verbose_name="Nombre")
    descripcionMedicamento=models.CharField(max_length=40,verbose_name="Descripcion")
    fabricanteMedicamento=models.CharField(max_length=40,verbose_name="Fabricante")
    contenidoMedicamento=models.CharField(max_length=40,verbose_name="Contenido")
    cantidad = models.IntegerField(verbose_name='cantidad')
    gramaje = models.IntegerField(verbose_name='gramaje')


    def __str__(self) :
        return self.codigo