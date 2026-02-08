from django.apps import AppConfig


class SiteappConfig(AppConfig):
    """
    Configuracion declarativa de la app.
    Django la usa para registrar metadata de siteapp.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'siteapp'
