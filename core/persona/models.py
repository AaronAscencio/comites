from django.db import models
from django.core.validators import RegexValidator,MaxLengthValidator
from django.forms.models import model_to_dict
from core.referente.models import Referente
from core.seccion.models import Seccion,Colonia
from core.folio.models import Folio

COMISIONES_CHOICES = (
    ('REFERENTE', 'REFERENTE'), 
    ('ENLACE', 'ENLACE'), 
    ('SIMPATIZANTE', 'SIMPATIZANTE'), 
    ('MILITANTE', 'MILITANTE'), 
    ('DEFENSOR DEL VOTO', 'DEFENSOR DEL VOTO')
)
# Create your models here.
class Persona(models.Model):
    seccion = models.ForeignKey(Seccion,verbose_name='Seccion',on_delete=models.CASCADE, blank=False, null=False, related_name='personas_seccion')
    comision = models.CharField(max_length=150, choices=COMISIONES_CHOICES)
    referente_1 =  models.ForeignKey(Referente,verbose_name='Referente 1',on_delete=models.CASCADE, blank=False, null=False, related_name='personas_referente_1')
    referente_2 =  models.ForeignKey(Referente,verbose_name='Referente 2',on_delete=models.CASCADE, blank=False, null=False, related_name='personas_referente_2')
    referente_3 = models.CharField(verbose_name='Referente 3', max_length= 150, blank=False,null=False)
    folio =  models.ForeignKey(Folio,verbose_name='Folio',on_delete=models.CASCADE, blank=False, null=False)
    nombre = models.CharField(verbose_name='Nombre', max_length= 150, blank=False,null=False)
    apellido_paterno = models.CharField(verbose_name='Apellido Paterno', max_length= 150, blank=False,null=False)
    apellido_materno = models.CharField(verbose_name='Apellido Materno', max_length= 150, blank=False,null=False)
    calle = models.CharField(verbose_name='Calle', max_length= 150, blank=False,null=False)
    numero_exterior = models.CharField(verbose_name='Numero Exterior', max_length= 25, blank=False,null=False)
    numero_interior = models.CharField(verbose_name='Numero Interior', max_length= 25, blank=True,null=True)
    colonia = models.ForeignKey(Colonia,verbose_name='Colonia',on_delete=models.CASCADE, blank=False, null=False,related_name='personas_colonia')
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
        item['referente_1'] = self.referente_1.toJSON()
        item['referente_2'] = self.referente_2.toJSON()
        item['seccion'] = self.seccion.toJSON()
        item['colonia'] = self.colonia.toJSON()
        item['folio'] = self.folio.toJSON()
        return item
    
        
    



