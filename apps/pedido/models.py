from django.db import models
from apps.usuario.models import Proveedor



class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de Producto',null=False,blank=False,max_length=100)
    descripcion = models.CharField('Descripcion de Producto',null=True,blank=True,max_length=255)
    valor = models.IntegerField('Valor de Producto',null=False)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    fecha_creacion = models.DateField('Fecha de Creacion',auto_now=False,auto_now_add=True)


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']


    def __str__(self):
        return self.nombre





class Orden_Pedido(models.Model):
    num_pedido = models.AutoField(primary_key=True)
    fecha_emision = models.DateField('Fecha Emision Pedido',null=True)
    fecha_recepcion = models.DateField('Fecha Recepcion Pedido',null=True)
    estado = models.BooleanField('Enviado / No Envido',default=False)
    fecha_creacion = models.DateField('Fecha creacion Pedido',auto_now=False,auto_now_add=True)


    class Meta:
        verbose_name = 'Orden Pedido'
        verbose_name_plural = 'Ordenes Pedidos'
        ordering = ['num_pedido']


    def __str__(self):
        return str(self.num_pedido)






class Detalle_Pedido(models.Model):
    id_detalle_pedido = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField('Contidad de Producto',null=False)
    pedido = models.ForeignKey(Orden_Pedido,on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Detalle Pedido'
        verbose_name_plural = 'Detalles de Pedido'
        ordering = ['pedido']


    def __str__(self):
        return str(self.id_detalle_pedido)
