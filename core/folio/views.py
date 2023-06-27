from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.http.response import JsonResponse
from django.views.generic import CreateView,TemplateView,ListView,UpdateView,DeleteView
from .models import Folio
from django.shortcuts import render
from .forms import FolioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from core.user.mixins import ChangedPasswordMixin
from core.user.mixins import ValidatePermissionRequiredMixin
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Count

class FolioListView(LoginRequiredMixin,ChangedPasswordMixin,ValidatePermissionRequiredMixin,ListView):
    model = Folio
    permission_required = 'folio.view_folio'
    template_name = "folio/list.html"
    
    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Folios'
        context['create_url'] = reverse_lazy('folio:folio_createview')
        context['list_url'] = reverse_lazy('folio:folio_listview')
        context['entity'] = 'Folios'
        return context

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for folio in Folio.objects.all():
                    #print(i.fraccion)
                    data.append(folio.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

class FolioCreateView(LoginRequiredMixin,ChangedPasswordMixin,ValidatePermissionRequiredMixin,CreateView):
    model = Folio
    form_class = FolioForm
    permission_required = 'folio.add_folio'
    template_name = 'folio/create.html'
    success_url = reverse_lazy('folio:folio_listview')

    def get_context_data(self,**kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Creacion de un Folio'
        context['entity'] = 'Folios'
        context['list_url'] = reverse_lazy('folio:folio_listview')
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

class FolioDeleteView(LoginRequiredMixin,ChangedPasswordMixin,ValidatePermissionRequiredMixin,DeleteView):
    model = Folio
    template_name = 'folio/delete.html'
    success_url = reverse_lazy('folio:folio_listview')
    permission_required = 'folio.delete_folio'


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
        context['title'] = 'Eliminación de un Folio'
        context['entity'] = 'Folio'
        context['list_url'] = reverse_lazy('folio:folio_listview')
        return context

class FolioUpdateView(LoginRequiredMixin,ChangedPasswordMixin,ValidatePermissionRequiredMixin,UpdateView):
    model = Folio
    form_class = FolioForm
    template_name = 'folio/create.html'
    success_url = reverse_lazy('folio:folio_listview')
    permission_required = 'folio.change_folio'
    
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
        context['title'] = 'Edición de un Folio'
        context['entity'] = 'Folios'
        context['list_url'] = reverse_lazy('folio:folio_listview')
        context['action'] = 'edit'
        return context
