from django.test import TestCase
from clinica.forms import *

class UsuarioFromCajaNegra(TestCase):
    def test_formulario_caja_negra(self):
        form_data = {
            'primer_apellido':'Gomez',
            'numero_documento':12345678,

        }

        form= UsuarioForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('primer_nombre', form.errors)
        print(f"Se probo la falla en el formulario de primer_nombre porque es un campo obligatorio de ingreso ")