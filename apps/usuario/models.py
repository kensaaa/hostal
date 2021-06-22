from django.db import models
from apps.habitacion.models import Rubro
from django.contrib.auth.models import User


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    rut = models.CharField('Rut de Empleado',null=False,blank=False,unique=True,max_length=12)
    nombres = models.CharField('Nombres de Empleado',null=False,blank=False,max_length=100)
    apaterno = models.CharField('Apellido Paterno de Empleado',null=False,blank=False,max_length=100)
    amaterno = models.CharField('Apellido Materno de Empleado',null=False,blank=False,max_length=100)
    celular = models.IntegerField('Celular Empleado',null=False)
    correo = models.EmailField('Correo de Empleado',null=False,blank=False)
    direccion = models.CharField('Direccion de Empleado',max_length=200)
    celular = models.IntegerField('Celular de Empleado',null=False)
    usuario = models.IntegerField('Usuario de Empleado',null=True)


    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['rut']


    def __str__(self):
        return self.rut




class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    rut = models.CharField('Rut de Proveedor',null=False,blank=False,unique=True,max_length=12)
    nombre = models.CharField('Nombre de Proveedor',null=False,blank=False,max_length=200)
    celular = models.IntegerField('Celular de Proveedor',null=False)
    correo = models.EmailField('Correo de Proveedor',null=False,blank=False)
    rubro = models.ForeignKey(Rubro,on_delete=models.CASCADE)
    usuario = models.IntegerField('Usuario de Proveedor',null=True)


    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['rut']


    def __str__(self):
        return self.rut






class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    rut = models.CharField('Rut de Cliente',null=False,blank=False,unique=True,max_length=12)
    nombre = models.CharField('Nombre de Cliente',null=False,blank=False,max_length=100)
    celular = models.IntegerField('Celular de Cliente',null=False)
    correo = models.EmailField('Correo de Cliente',null=False,blank=False)
    usuario = models.IntegerField('Usuario de Cliente',null=True)


    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['rut']


    def __str__(self):
        return self.rut
