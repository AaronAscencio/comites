from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from core.user.mixins import ChangedPasswordMixin

class DashboardView(LoginRequiredMixin,ChangedPasswordMixin,TemplateView):
    template_name = 'dashboard.html'