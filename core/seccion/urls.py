from django.urls import path
from .views import *

urlpatterns = [
    path('distrito/',load_distritos,name='load_distrito'),
    path('municipio/',load_municipios,name='load_municipio'),
    path('seccion/',load_secciones,name='seccion'),
    path('colonia/',load_colonias,name='load_colonia'),
    path('complemento/',load_complemento,name='load_complemento')
]

