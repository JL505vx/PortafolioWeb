"""
Ruteo principal del proyecto.

- /admin/   -> Panel administrativo de Django.
- /         -> Portafolio web (urls de siteapp).
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('siteapp.urls')),
]
