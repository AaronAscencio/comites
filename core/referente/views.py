from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.http.response import JsonResponse
from django.views.generic import CreateView,TemplateView,ListView,UpdateView,DeleteView
from .models import Referente
from django.shortcuts import render
from .forms import ReferenteForm
from django.contrib.auth.mixins import LoginRequiredMixin
from core.user.mixins import ChangedPasswordMixin
from core.user.mixins import ValidatePermissionRequiredMixin
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Count

class ReferenteListView(LoginRequiredMixin,ChangedPasswordMixin,ValidatePermissionRequiredMixin,ListView):
    model = Referente
    permission_required = 'referente.view_referente'
    template_name = "referente/list.html"
    
    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Referentes'
        context['create_url'] = reverse_lazy('referente:referente_createview')
        context['list_url'] = reverse_lazy('referente:referente_listview')
        context['entity'] = 'Referentes'
        return context

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for referente in Referente.objects.all():
                    #print(i.fraccion)
                    data.append(referente.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

class ReferenteCreateView(LoginRequiredMixin,ChangedPasswordMixin,ValidatePermissionRequiredMixin,CreateView):
    model = Referente
    form_class = ReferenteForm
    permission_required = 'referente.add_referente'
    template_name = 'referente/create.html'
    success_url = reverse_lazy('referente:referente_listview')

    def get_context_data(self,**kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Creacion de un Referente'
        context['entity'] = 'Referentes'
        context['list_url'] = reverse_lazy('referente:referente_listview')
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
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data,safe=False)

    
class ReferenteDeleteView(LoginRequiredMixin,ChangedPasswordMixin,ValidatePermissionRequiredMixin,DeleteView):
    model = Referente
    template_name = 'referente/delete.html'
    success_url = reverse_lazy('referente:referente_listview')
    permission_required = 'referente.delete_referente'


    #@method_decorator(login_required)
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
        context['title'] = 'Eliminación de una Fraccion'
        context['entity'] = 'Fracciones'
        context['list_url'] = reverse_lazy('referente:referente_listview')
        return context

class ReferenteUpdateView(LoginRequiredMixin,ChangedPasswordMixin,ValidatePermissionRequiredMixin,UpdateView):
    model = Referente
    form_class = ReferenteForm
    template_name = 'referente/create.html'
    success_url = reverse_lazy('referente:referente_listview')
    permission_required = 'referente.change_referente'
    
    #@method_decorator(login_required)
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
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data,safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un Referente'
        context['entity'] = 'Referentes'
        context['list_url'] = reverse_lazy('referente:referente_listview')
        context['action'] = 'edit'
        return context
