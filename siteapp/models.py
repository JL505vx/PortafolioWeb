"""
Modelos de datos para evolucionar el portafolio a contenido dinamico.

No son obligatorios para mostrar la pagina actual (que usa template estatico),
pero dejan el proyecto listo para migrar a admin + base de datos.
"""
from django.db import models


class Project(models.Model):
    """
    Proyecto tecnico mostrado en el portafolio.

    Estructura pensada para backend + deploy demo + repositorio.
    """

    title = models.CharField(max_length=150)
    problem = models.TextField()
    solution = models.TextField()
    stack = models.CharField(max_length=250)
    impact = models.CharField(max_length=250, blank=True)
    learning = models.TextField(blank=True)
    repo_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.title


class Certification(models.Model):
    """
    Curso o certificacion tecnica del perfil.
    """

    name = models.CharField(max_length=160)
    provider = models.CharField(max_length=160, blank=True)
    year = models.CharField(max_length=20, blank=True)
    summary = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Certificacion"
        verbose_name_plural = "Certificaciones"

    def __str__(self):
        base = self.name
        return f"{base} ({self.year})" if self.year else base
