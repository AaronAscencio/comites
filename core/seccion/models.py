from django.db import models
from django.forms.models import model_to_dict

# Create your models here.
class Distrito(models.Model):
    numero = models.IntegerField(verbose_name='Numero',null=False,blank=False, unique=True)
    
    class Meta:
        verbose_name = 'Distrito'
        verbose_name_plural = 'Distritos'
    
    def __str__(self):
        return f'DISTRITO: {self.numero}'
    
    def toJSON(self):
        return model_to_dict(self)
    
class Municipio(models.Model):
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150,blank=False,null=False)
    
    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        
    def __str__(self):
        return f'{self.nombre}'
    
    def toJSON(self):
        item = model_to_dict(self)
        item['distrito'] = self.distrito.toJSON()
        return item
    
class Seccion(models.Model):
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    numero = models.IntegerField(verbose_name='Seccion',blank=False,null=False,unique=True)
    
    class Meta:
        verbose_name = 'Seccion'
        verbose_name_plural = 'Secciones'
    
    def __str__(self):
        return f'{self.numero}'
    
    def toJSON(self):
        item = model_to_dict(self)
        item['municipio'] = self.municipio.toJSON()
        return item

class Colonia(models.Model):
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    tipo_de_seccion = models.CharField(verbose_name='Tipo de Seccion',blank=False,null=False,max_length=150)
    tipo_de_colonia = models.CharField(verbose_name='Tipo de Colonia',blank=False,null=False,max_length=150)
    nombre = models.CharField(verbose_name='Nombre de la Colonia',blank=False,null=False,max_length=150)
    cp = models.CharField(verbose_name='Codigo Postal',blank=True,null=True,max_length=5)

    class Meta:
        verbose_name = 'Colonia'
        verbose_name_plural = 'Colonias'
    
    def __str__(self):
        return f'{self.tipo_de_colonia} - {self.nombre}'
    
    def toJSON(self):
        item = model_to_dict(self)
        item['seccion'] = self.seccion.toJSON()
        return item


    
