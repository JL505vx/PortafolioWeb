"""
Vistas de la app siteapp.

Por ahora usamos una vista simple que renderiza el home.
En futuras iteraciones, esta vista puede leer datos de modelos
para proyectos, certificaciones y experiencia.
"""
from django.shortcuts import render


def home(request):
    """
    Renderiza la portada del portafolio.

    request: objeto HttpRequest enviado por el navegador.
    return: respuesta HTML construida desde templates/siteapp/home.html.
    """
    return render(request, "siteapp/home.html")
