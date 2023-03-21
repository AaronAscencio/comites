from django.urls import path
from .views import DashboardView
#from apps.home.views import IndexView


app_name = 'dashboard'

urlpatterns = [
    path('',DashboardView.as_view(),name='dashboard'),
]