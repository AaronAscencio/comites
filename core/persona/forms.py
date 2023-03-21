from django.forms import *
from core.seccion.models import *
from .models import Persona

class PersonaForm(ModelForm):
    distrito = ModelChoiceField(queryset=Distrito.objects.all())
    municipio = ModelChoiceField(queryset=Municipio.objects.all())
    seccion = ModelChoiceField(queryset=Seccion.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['distrito'].widget.attrs.update({'class': 'select2'})
        self.fields['municipio'].widget.attrs.update({'class': 'select2'})
        self.fields['seccion'].widget.attrs.update({'class': 'select2'})
        self.fields['comision'].widget.attrs.update({'class': 'select2'})
        
        

    class Meta:
        model = Persona
        fields = ['distrito','municipio','seccion','comision','nombre','apellido_paterno','apellido_materno','calle','numero_exterior','numero_interior','colonia','codigo_postal','clave_electoral','curp','telefono','correo_electronico','facebook','twitter']
    
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
