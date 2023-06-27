from django.db import models
from django.forms.models import model_to_dict
from core.referente.models import Referente
from django.core.validators import *

# Create your models here.
class Folio(models.Model):
    numero = models.PositiveIntegerField(
        verbose_name='Numero de Folio',
        help_text='Ingresa un número entre 5 y 7 dígitos',
        validators=[
            MinValueValidator(10000, 'El número debe tener al menos 5 dígitos'),
            MaxValueValidator(9999999, 'El número no puede tener más de 7 dígitos'),
        ],
        unique= True,
        null=False,
        blank=False,
    )
    referente = models.ForeignKey(Referente,on_delete=models.CASCADE,verbose_name='Referente')

    class Meta:
        verbose_name = 'Folio'
        verbose_name_plural = 'Folios'
        

    def __str__(self):
        return f'{self.numero} - {self.referente.tipo_referente} - {self.referente.nombre} {self.referente.apellido_paterno} {self.referente.apellido_materno}'
    
    def toJSON(self):
        item = model_to_dict(self)
        item['referente'] = self.referente.toJSON()
        return item