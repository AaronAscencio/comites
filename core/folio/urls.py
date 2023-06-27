from django.urls import path
from .views import *

app_name = 'folio'

urlpatterns = [
    path('list/',FolioListView.as_view(),name='folio_listview'),
    path('create/',FolioCreateView.as_view(),name='folio_createview'),
    path('delete/<int:pk>/',FolioDeleteView.as_view(),name='folio_deleteview'),
    path('update/<int:pk>/',FolioUpdateView.as_view(),name='folio_updateview'),
]
