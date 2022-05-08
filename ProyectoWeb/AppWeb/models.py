from typing import ChainMap
from django.db import models

# Create your models here.
class Medicamento(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombreMedicamento=models.CharField(max_length=40,null=True,verbose_name="Nombre")
    descripcionMedicamento=models.CharField(max_length=40,null=True,verbose_name="Descripcion")
    fabricanteMedicamento=models.CharField(max_length=40,null=True,verbose_name="Fabricante")
    contenidoMedicamento=models.CharField(max_length=40,null=True,verbose_name="Contenido")
    cantidad = models.IntegerField(verbose_name='cantidad',null=True)
    gramaje = models.IntegerField(verbose_name='gramaje',null=True)
    imagenPublicacion=models.ImageField(upload_to="fotopublicaciones",null=True)


    def __str__(self) :
        return self.nombreMedicamento

class Consulta(models.Model):
    codigo2 = models.AutoField(primary_key=True)
    nombrePersona=models.CharField(max_length=40,verbose_name="nombre del paciente")
    Sintomas=models.TextField(max_length=300,null=True,verbose_name="sintomas")
    diagnostico=models.TextField(max_length=300,null=True,verbose_name="diagnostico")
    medicamentoRecetado=models.ForeignKey(Medicamento,on_delete=models.CASCADE)
    

    def __str__(self) :
        return self.nombrePersona