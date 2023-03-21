from .models import Persona
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from core.user.mixins import ChangedPasswordMixin,ValidatePermissionRequiredMixin
from django.views.generic import CreateView,TemplateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.http.response import JsonResponse
from .forms import PersonaForm
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from core.seccion.models import *

# Create your views here.
class PersonaListView(LoginRequiredMixin,ChangedPasswordMixin,ValidatePermissionRequiredMixin,ListView):
    model = Persona
    permission_required = 'persona.view_persona'
    template_name = "persona/list.html"
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Personas'
        context['create_url'] = reverse_lazy('persona:persona_createview')
        context['list_url'] = reverse_lazy('persona:persona_listview')
        context['entity'] = 'Persona'
        return context

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for persona in Persona.objects.all():
                    data.append(persona.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

class PersonaCreateView(LoginRequiredMixin,ChangedPasswordMixin,ValidatePermissionRequiredMixin,CreateView):
    model = Persona
    form_class = PersonaForm
    permission_required = 'persona.add_persona'
    template_name = 'persona/create.html'
    success_url = reverse_lazy('persona:persona_listview')
    
    def get_context_data(self,**kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Creacion de Persona'
        context['entity'] = 'Persona'
        context['list_url'] = reverse_lazy('persona:persona_listview')
        context['action'] = 'add'
        
        return context

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            elif action == 'search_municipios':
                data = []
                id = request.POST['id']
                for municipio in Municipio.objects.filter(distrito__id = id):
                    data.append({
                        'id':municipio.id,
                        'text':f'{municipio.nombre}'
                    })
            elif action == 'search_secciones':
                data = []
                id = request.POST['id']
                for seccion in Seccion.objects.filter(municipio__pk = id):
                  data.append({
                        'id':seccion.id,
                        'text':f'{seccion.numero}'
                    })  
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data,safe=False)

class PersonaUpdateView(LoginRequiredMixin,ChangedPasswordMixin,ValidatePermissionRequiredMixin,UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'persona/create.html'
    success_url = reverse_lazy('persona:persona_listview')
    permission_required = 'persona.change_persona'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                form = form.save()
            elif action == 'set_selects':
                data['secciones'] = []
                data['municipios'] = []
                data['distrito_selected'] = self.object.seccion.municipio.distrito.pk
                data['municipio_selected'] = self.object.seccion.municipio.pk
                data['seccion_selected'] = self.object.seccion.pk
                secciones = Seccion.objects.filter(municipio = self.object.seccion.municipio)
                for seccion in secciones:
                    data['secciones'].append({
                        'id':seccion.id,
                        'text':f'{seccion.numero}'
                    })
                municipios = Municipio.objects.filter(distrito = self.object.seccion.municipio.distrito)
                for municipio in municipios:
                    data['municipios'].append({
                        'id':municipio.id,
                        'text':f'{municipio.nombre}'
                    })
            elif action == 'search_municipios':
                data = []
                id = request.POST['id']
                for municipio in Municipio.objects.filter(distrito__id = id):
                    data.append({
                        'id':municipio.id,
                        'text':f'{municipio.nombre}'
                    })
            elif action == 'search_secciones':
                data = []
                id = request.POST['id']
                for seccion in Seccion.objects.filter(municipio__pk = id):
                  data.append({
                        'id':seccion.id,
                        'text':f'{seccion.numero}'
                    })      

            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data,safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de una Persona'
        context['entity'] = 'Persona'
        context['list_url'] = reverse_lazy('persona:persona_listview')
        context['action'] = 'edit'
        return context

class PersonaDeleteView(LoginRequiredMixin,ChangedPasswordMixin,ValidatePermissionRequiredMixin,DeleteView):
    model = Persona
    template_name = 'persona/delete.html'
    success_url = reverse_lazy('persona:persona_listview')
    permission_required = 'persona.delete_persona'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una Persona'
        context['entity'] = 'Persona'
        context['list_url'] = reverse_lazy('persona:persona_listview')
        return context