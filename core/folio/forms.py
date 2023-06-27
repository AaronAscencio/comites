from django.forms import *
from .models import Folio


class FolioForm(ModelForm):
    numero = IntegerField(min_value=1000,max_value=9999999,label='Numero de Folio')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['referente'].widget.attrs.update({'class': 'select2'})
        self.fields['numero'].widget.attrs.update({'maxlength': '7'})
    
    
    class Meta:
        model = Folio
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