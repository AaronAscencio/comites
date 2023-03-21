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
    nombre = models.CharField(max_length=150,blank=False,null=False,unique=True)
    
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
    
