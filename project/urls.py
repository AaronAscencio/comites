"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .settings import MEDIA_ROOT,MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('core.user.urls')),
    path('',include('core.login.urls')),
    path('',include('core.dashboard.urls')),
    path('',include('core.seccion.urls')),
    path('persona/',include('core.persona.urls')),
    path('referente/',include('core.referente.urls')),
    path('folio/',include('core.folio.urls')),
    ]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)