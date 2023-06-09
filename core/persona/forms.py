from django.forms import *
from core.seccion.models import *
from .models import Persona
from core.referente.models import Referente

class PersonaForm(ModelForm):
    distrito = ModelChoiceField(queryset=Distrito.objects.all())
    municipio = ModelChoiceField(queryset=Municipio.objects.all())
    seccion = ModelChoiceField(queryset=Seccion.objects.all())
    colonia = ModelChoiceField(queryset=Colonia.objects.all())
    referente_1 = ModelChoiceField(queryset= Referente.objects.filter(tipo_referente = 'REFERENTE 1'))
    referente_2 = ModelChoiceField(queryset= Referente.objects.filter(tipo_referente = 'REFERENTE 2'))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['distrito'].widget.attrs.update({'class': 'select2'})
        self.fields['municipio'].widget.attrs.update({'class': 'select2'})
        self.fields['seccion'].widget.attrs.update({'class': 'select2'})
        self.fields['comision'].widget.attrs.update({'class': 'select2'})
        self.fields['colonia'].widget.attrs.update({'class': 'select2'})
        self.fields['referente_1'].widget.attrs.update({'class': 'select2'})
        self.fields['referente_2'].widget.attrs.update({'class': 'select2'})
        #self.fields['codigo_postal'].disabled = True
        #self.fields['codigo_postal'].widget.attrs['readonly'] = True 
    class Meta:
        model = Persona
        fields = ['distrito','municipio','seccion','comision','referente_1','referente_2','referente_3','folio','nombre','apellido_paterno','apellido_materno','colonia','codigo_postal','calle','numero_exterior','numero_interior','clave_electoral','curp','telefono','correo_electronico','facebook','twitter']
    
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
