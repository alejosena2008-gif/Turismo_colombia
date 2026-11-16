
from django.urls import path
from . import views
from . import auth_views

urlpatterns = [
    # Página principal
    path('', views.home, name='home'),

    # Autenticación de usuarios
    path('login/', auth_views.iniciar_sesion, name='login'),
    path('registro/', auth_views.registrarse, name='registro'),
    path('logout/', auth_views.cerrar_sesion, name='logout'),
]
