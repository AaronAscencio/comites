from django.db import models
from django.forms.models import model_to_dict

# Create your models here.

TIPOS_REFERENTE_CHOICES = (
    ('REFERENTE 1', 'REFERENTE 1'), 
    ('REFERENTE 2', 'REFERENTE 2'),
    ('REFERENTE 3', 'REFERENTE 3'),  
)


class Referente(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length= 150, blank=False,null=False)
    apellido_paterno = models.CharField(verbose_name='Apellido Paterno', max_length= 150, blank=False,null=False)
    apellido_materno = models.CharField(verbose_name='Apellido Materno', max_length= 150, blank=False,null=False)
    tipo_referente = models.CharField(max_length=150, choices=TIPOS_REFERENTE_CHOICES)

    class Meta:
        verbose_name = 'Referente'
        verbose_name_plural = 'Referentes'

    def __str__(self):
        return f'{self.tipo_referente} - {self.nombre} {self.apellido_paterno} {self.apellido_materno}'
    
    def toJSON(self):
        item = model_to_dict(self)
        return item
    