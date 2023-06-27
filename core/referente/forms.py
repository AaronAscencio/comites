from django.forms import *
from .models import Referente


class ReferenteForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
    
    
    class Meta:
        model = Referente
        fields = '__all__'
        #exclude = ['municipio']
    
    def save(self,commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                referente = form.save(commit=False)
                referente.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data