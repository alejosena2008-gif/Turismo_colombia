from django.test import TestCase
from django.urls import reverse

class TurismoColTests(TestCase):
    def test_home_page_status_200(self):
        """Verifica que la página principal carga con código 200."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'TurismoCol')

    def test_search_existing_country(self):
        """Verifica la búsqueda de un país existente."""
        response = self.client.get(reverse('home'), {'q': 'Brasil'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Brasil')

    def test_search_no_results(self):
        """Verifica el manejo de estados sin coincidencias."""
        response = self.client.get(reverse('home'), {'q': 'PaisFicticioXYZ'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No se encontraron destinos')