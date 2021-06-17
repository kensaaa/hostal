from django.db import models



class Tipo_Comedor(models.Model):
    id_tipo_comedor = models.AutoField(primary_key=True)
    descripcion = models.CharField('Tipo Comedor',null=False,blank=False,max_length=50)


    class Meta:
        verbose_name = 'Comedor'
        verbose_name_plural = 'Tipos de Comedor'
        ordering = ['descripcion']


    def __str__(self):
        return self.descripcion






class Plato(models.Model):
    id_plato = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de Plato',null=False,blank=False,max_length=100)
    descripcion = models.CharField('Descripcion de Plato',null=False,blank=False,max_length=255)
    comedor = models.ForeignKey(Tipo_Comedor,on_delete=models.CASCADE)
    valor =  models.IntegerField('Valor de Plato',null=False)


    class Meta:
        verbose_name = 'Plato'
        verbose_name_plural = 'Platos'
        ordering = ['nombre']


    def __str__(self):
        return self.nombre


