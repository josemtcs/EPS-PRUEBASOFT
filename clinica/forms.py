from django import forms
from django.db.models import Model

from .models import Usuario, Servicio, Triage, OpocisionDonacion, VoluntaAnticipada, Discapacidades, PrestadoresSalud
from datetime import datetime
#from django.forms import


class ServicioForm2(forms.ModelForm):

    triage = forms.ModelChoiceField(
        queryset=Triage.objects.all(),
        widget=forms.Select,
        required=True
    )

    class Meta:
        model = Servicio
        fields = [
            'usuario', 'prestador_salud', 'fecha_atencion', 'hora_atencion',
            'modalidad_servicio', 'grupo_servicio', 'via_ingreso', 'entorno_atencion',
            'causa_atencion', 'triage', 'diagnostico', 't_diagnostico'
        ]

        widgets = {
            'fecha_atencion': forms.DateInput(attrs={'type': 'date'}),
            'hora_atencion': forms.TimeInput(attrs={'type': 'time'}),
        }


class UsuarioForm(forms.ModelForm):

    donacion = forms.ModelChoiceField(
        queryset=OpocisionDonacion.objects.all(),
        widget=forms.Select,
        required=True
    )

    voluntad = forms.ModelChoiceField(
        queryset=VoluntaAnticipada.objects.all(),
        widget=forms.Select,
        required=True
    )


    class Meta:
        model = Usuario
        fields = [
            'tipo_documento', 'numero_documento', 'primer_nombre', 'segundo_nombre',
            'primer_apellido', 'segundo_apellido', 'sexo_biologico', 'ident_genero',
            'ocupacion', 'discapacidad', 'donacion', 'voluntad', 'nacionalidad',
            'pais_residencia', 'departamento_municipio', 'comunidad_etnia', 'etnia',
            'zona_residencia', 'entidad', 'fecha_nacimiento', 'hora_nacimiento',
        ]

        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'hora_nacimiento': forms.TimeInput(attrs={'type': 'time'}),
            'discapacidad': forms.SelectMultiple(attrs={'type': 'text'}),
            'nacionalidad': forms.SelectMultiple(attrs={'type': 'text'}),
        }
