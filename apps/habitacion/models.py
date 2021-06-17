from django.db import models


class Rubro(models.Model):
    id_rubro = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de Habitacion',max_length=100,null=False,blank=False)


    class Meta:
        verbose_name = 'Rubro'
        verbose_name_plural = 'Rubros'
        ordering = ['nombre']


    def __str__(self):
        return self.nombre




class Tipo_Habitacion(models.Model):
    id_tipo_habitacion = models.AutoField(primary_key=True)
    descripcion =  models.CharField('Tipo Habitacion',null=False,blank=False,max_length=50)


    class Meta:
        verbose_name = 'Tipo Habitacion'
        verbose_name_plural = 'Tipo de Habitaciones'
        ordering = ['descripcion']


    def __str__(self):
        return self.descripcion






class Estado_Habitacion(models.Model):
    id_estado_habitacion = models.AutoField(primary_key=True)
    descripcion =  models.CharField('Estado Habitacion',null=False,blank=False,max_length=50)


    class Meta:
        verbose_name = 'Estado Habitacion'
        verbose_name_plural = 'Estados de Habitacion'
        ordering = ['descripcion']


    def __str__(self):
        return self.descripcion






class Habitacion(models.Model):
    num_habitacion = models.AutoField(primary_key=True)
    valor = models.IntegerField('Valor de Habitacion',null=False)
    accesorio = models.TextField('Accesorios de la Habitacion',null=True,blank=True,max_length=255)
    estado = models.ForeignKey(Estado_Habitacion,on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo_Habitacion,on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Habitacion'
        verbose_name_plural = 'Habitaciones'
        ordering = ['num_habitacion']


    def __str__(self):
        return str(self.num_habitacion)
