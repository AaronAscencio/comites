from django.urls import path
from .views import LoginFormView,LogoutView

app_name = 'login'

urlpatterns = [
    path("login/",LoginFormView.as_view(),name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),
]