"""
Pruebas iniciales para validar disponibilidad del home.

Agregar mas pruebas aqui conforme el proyecto crezca.
"""
from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    """
    Verifica que la pagina principal responda correctamente.
    """

    def test_home_status_code_200(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
