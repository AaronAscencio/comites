from django.urls import path
from .views import *

app_name = 'persona'

urlpatterns = [
    path('list/',PersonaListView.as_view(),name='persona_listview'),
    path('create/',PersonaCreateView.as_view(),name='persona_createview'),
    path('update/<int:pk>/',PersonaUpdateView.as_view(),name='persona_updateview'),
    path('delete/<int:pk>/',PersonaDeleteView.as_view(),name='persona_deleteview'),
]

