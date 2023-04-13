from django.db import models
from django.core.validators import RegexValidator,MaxLengthValidator
from django.forms.models import model_to_dict

from core.seccion.models import Seccion

COMISIONES_CHOICES = (
    ('ORGANIZACIÓN ELECTORAL Y DEFENSA DEL VOTO', 'ORGANIZACIÓN ELECTORAL Y DEFENSA DEL VOTO'),
    ('DIFUSIÓN', 'DIFUSIÓN'),
    ('FORMACIÓN POLÍTICA Y CÍRCULOS DE REFLEXIÓN Y ESTUDIO', 'FORMACIÓN POLÍTICA Y CÍRCULOS DE REFLEXIÓN Y ESTUDIO'),
    ('VINCULACIÓN Y PROMOCIÓN DE CAUSAS Y MOVIMIENTOS POPULARES Y SOCIALES O LABORALES CULTURALES', 'VINCULACIÓN Y PROMOCIÓN DE CAUSAS Y MOVIMIENTOS POPULARES Y SOCIALES O LABORALES CULTURALES'),
    ('SALUD', 'SALUD'),
    ('DEPORTIVAS', 'DEPORTIVAS'),
)
# Create your models here.
class Persona(models.Model):
    seccion = models.ForeignKey(Seccion,verbose_name='Seccion',on_delete=models.CASCADE, blank=False, null=False)
    comision = models.CharField(max_length=150, choices=COMISIONES_CHOICES)
    nombre = models.CharField(verbose_name='Nombre', max_length= 150, blank=False,null=False)
    apellido_paterno = models.CharField(verbose_name='Apellido Paterno', max_length= 150, blank=False,null=False)
    apellido_materno = models.CharField(verbose_name='Apellido Materno', max_length= 150, blank=False,null=False)
    calle = models.CharField(verbose_name='Calle', max_length= 150, blank=False,null=False)
    numero_exterior = models.CharField(verbose_name='Numero Exterior', max_length= 25, blank=False,null=False)
    numero_interior = models.CharField(verbose_name='Numero Interior', max_length= 25, blank=True,null=True)
    colonia = models.CharField(verbose_name='Colonia', max_length= 150, blank=False,null=False)
    telefono = models.CharField(verbose_name='Telefono', max_length= 15, blank=False,null=False)
    codigo_postal = models.CharField(verbose_name='Codigo Postal', max_length= 5, blank=False,null=False)
    clave_electoral = models.CharField(max_length=18, unique=True,validators=[RegexValidator(r'^[a-zA-Z0-9 ]*$', 'SOLO SE PERMITEN NUMEROS Y LETRAS'),MaxLengthValidator(18, message='ESTE CAMPO DEBE TENER EXACTAMENTE 18 CARACTERES.')])
    curp = models.CharField(max_length=18, unique=True, validators=[RegexValidator(r'^[a-zA-Z0-9 ]*$', 'SOLO SE PERMITEN NUMEROS Y LETRAS'),MaxLengthValidator(18, message='ESTE CAMPO DEBE TENER EXACTAMENTE 18 CARACTERES.')])
    correo_electronico = models.EmailField(verbose_name='Correo Electronico', max_length=150,blank=True,null=True)
    facebook = models.CharField(verbose_name='Facebook', max_length= 150, blank=True,null=True)
    twitter = models.CharField(verbose_name='Twitter', max_length= 150, blank=True,null=True)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return f'{self.curp} {self.apellido_paterno} {self.apellido_materno} {self.nombre}'
    
    def toJSON(self):
        item = model_to_dict(self)
        item['seccion'] = self.seccion.toJSON()
        return item
    
        
    



