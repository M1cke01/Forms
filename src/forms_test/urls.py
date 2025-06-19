from django.contrib import admin
from django.urls import path

from .views import home
from .views import registro_view, login_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name='forms'),
    path("registro/", registro_view, name='registro'),
    # path("login/", auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("login/", login_view, name='login'),
]
