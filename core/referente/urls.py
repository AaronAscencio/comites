from django.urls import path
from .views import *

app_name = 'referente'

urlpatterns = [
    path('list/',ReferenteListView.as_view(),name='referente_listview'),
    path('create/',ReferenteCreateView.as_view(),name='referente_createview'),
    path('delete/<int:pk>/',ReferenteDeleteView.as_view(),name='referente_deleteview'),
    path('update/<int:pk>/',ReferenteUpdateView.as_view(),name='referente_updateview'),
]
