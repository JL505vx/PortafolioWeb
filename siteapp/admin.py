"""
Configuracion del panel admin para gestionar contenido dinamico.
"""
from django.contrib import admin

from .models import Certification, Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Vista admin para proyectos.
    """

    list_display = ("title", "stack", "is_featured", "order")
    list_filter = ("is_featured",)
    search_fields = ("title", "stack", "problem", "solution")
    ordering = ("order", "id")


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    """
    Vista admin para certificaciones.
    """

    list_display = ("name", "provider", "year", "order")
    search_fields = ("name", "provider", "summary")
    ordering = ("order", "id")
