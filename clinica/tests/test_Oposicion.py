from django.test import TestCase
from clinica.models import OpocisionDonacion

class OposicionDonacionTestCase(TestCase):
    def test_str_method(self):
        op= OpocisionDonacion.objects.create(manifestacionOpo="01")
        print(f"Se creo exitosamente con ID: {op.idDonacion}")
        self.assertEqual(op.manifestacionOpo,"01", msg="No se creó la manifestación con '01'")