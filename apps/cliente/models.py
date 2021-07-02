from django.db import models
from apps.compra.models import Orden_Compra
from apps.habitacion.models import Tipo_Habitacion
from apps.comedor.models import Tipo_Comedor

class Listado_Trabajador(models.Model):
    id_trabajador = models.AutoField(primary_key=True)
    rut = models.CharField('Rut',unique=True,max_length=12)
    nombres = models.CharField('Nombres',null=False,blank=False,max_length=100)
    apaterno = models.CharField('Apellido Paterno',null=False,blank=False,max_length=100)
    amaterno = models.CharField('Apellido Materno',null=False,blank=False,max_length=100)
    celular = models.IntegerField('Celular',null=False)
    tipo_comedor = models.ForeignKey(Tipo_Comedor,on_delete=models.CASCADE)
    tipo_habitacion = models.ForeignKey(Tipo_Habitacion,on_delete=models.CASCADE)
    orden_compra = models.ForeignKey(Orden_Compra,on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadores'
        ordering = ['orden_compra']


    def __str__(self):
        return str(self.rut)
