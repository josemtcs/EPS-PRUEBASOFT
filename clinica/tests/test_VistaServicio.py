from django.test import TestCase
from django.urls import reverse


class VistaServicioTestCase(TestCase):
    def test_carga_servicio(self):
        response = self.client.get(reverse('servicios'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'servicios/servicios.html')
        self.assertIn('servicios', response.context)
        print("La lista de  servicios de salud se ha probado correctamente")


