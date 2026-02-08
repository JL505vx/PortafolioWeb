"""
Rutas de la app del portafolio.

Se separan en este archivo para mantener orden:
- core/urls.py decide "que app atiende cada prefijo".
- siteapp/urls.py decide "que vista responde cada ruta de esta app".
"""
from django.urls import path

from . import views

urlpatterns = [
    # Pagina principal del portafolio.
    path("", views.home, name="home"),
]
