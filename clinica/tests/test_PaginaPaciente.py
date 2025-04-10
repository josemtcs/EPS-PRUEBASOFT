from django.test import TestCase
from django.urls import reverse

class SimplePageTest(TestCase):
    def test_home_page(self):

        response = self.client.get(reverse('pacientes'))
        self.assertEqual(response.status_code, 200)
        print("Pagina probada correctamente")