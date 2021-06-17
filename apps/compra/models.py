from django.db import models
from apps.comedor.models import Tipo_Comedor
from apps.usuario.models import Cliente
from apps.habitacion.models import Habitacion
from apps.comedor.models import Plato


class Pago(models.Model):
    num_pago = models.AutoField(primary_key=True)
    valor_total = models.IntegerField('Monto Pagado',null=False)
    fecha_pago = models.DateField('Fecha de Pago',auto_now=False,auto_now_add=True)


    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
        ordering = ['num_pago']


    def __str__(self):
        return str(self.num_pago)



class Orden_Compra(models.Model):
    num_compra = models.AutoField(primary_key=True)
    fecha_inicio = models.DateField('Fecha Inicio Reservacion',null=False)
    fecha_termino = models.DateField('Fecha Termino Reservacion',null=False)
    fecha_compra = models.DateField('Fecha de compra Reservacion',auto_now=False,auto_now_add=True)
    monto_total = models.IntegerField('Monto Total',null=True)
    pago = models.ForeignKey(Pago,on_delete=models.CASCADE,null=True)
    estado = models.BooleanField('Iniciada / Finalizado',default=False)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Ordene Compra'
        verbose_name_plural = 'Ordenes de Compras'
        ordering = ['num_compra']


    def __str__(self):
        return str(self.num_compra)



class Huesped(models.Model):
    id_huesped = models.AutoField(primary_key=True)
    rut = models.CharField('Rut de Huesped',unique=True,max_length=12)
    nombres = models.CharField('Nombres de Huesped',null=False,blank=False,max_length=100)
    apaterno = models.CharField('Apellido Paterno de Huesped',null=False,blank=False,max_length=100)
    amaterno = models.CharField('Apellido Materno de Huesped',null=False,blank=False,max_length=100)
    celular = models.IntegerField('Celular Huesped',null=False)
    orden_compra = models.ForeignKey(Orden_Compra,on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion,on_delete=models.CASCADE)
    tipo_comedor = models.ForeignKey(Tipo_Comedor,on_delete=models.CASCADE)
    fecha_ingreso = models.DateField('Fecha ingreso',auto_now=False,auto_now_add=True)
    fecha_salida = models.DateField('Fecha salida',null=True)
    activo = models.BooleanField('Activo / No activo',default=True)


    class Meta:
        verbose_name = 'Huesped'
        verbose_name_plural = 'Huespedes'
        ordering = ['rut']


    def __str__(self):
        return self.rut






class Gasto_Huesped_Plato(models.Model):
    id_gasto = models.AutoField(primary_key=True)
    fecha_gasto = models.DateField('Fecha de Consumo',auto_now=False,auto_now_add=True)
    huesped = models.ForeignKey(Huesped,on_delete=models.CASCADE)
    plato = models.ForeignKey(Plato,on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Gasto Cliente'
        verbose_name_plural = 'Gastos del Huesped'
        ordering = ['id_gasto']


    def __str__(self):
        return str(self.fecha_gasto)
