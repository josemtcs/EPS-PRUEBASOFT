from gc import get_objects

from django.contrib.messages import success
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from .forms import ServicioForm2, UsuarioForm
from .models import *
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView


from django.views.generic import ListView

from clinica.models import Usuario


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class Pacientes(TemplateView):
    template_name = 'Paciente.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class ServicioPaciente(TemplateView):
    template_name = 'ServicioPaciente.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class ListaPacientes(ListView):
    model = Usuario
    template_name = 'pacientes/pacientes.html'
    context_object_name = 'pacientes'

class ListaServicios(ListView):
    model = Servicio
    template_name = 'servicios/servicios.html'
    context_object_name = 'servicios'

def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioForm2(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Servicio agregado con éxito!")
            return redirect('servicios')
    else:
        form = ServicioForm2()
    return render(request, 'servicios/formulario_servicio.html', {'form': form})

@csrf_exempt
def crear_triage(request):
    if request.method == 'POST':
        fecha = request.POST.get('fechaTriage')
        hora = request.POST.get('horaTriage')
        clasificacion = request.POST.get('ClasificacionTriage')
        nuevo_triage = Triage.objects.create(
            fechaTriage=fecha,
            horaTriage=hora,
            ClasificacionTriage=clasificacion
        )
        return JsonResponse({
            'success': True,
            'id': nuevo_triage.idTriage,
            'clasificacion': nuevo_triage.get_ClasificacionTriage_display()
        })
    return JsonResponse({'success': False})

def eliminar_servicio(request, id_servicio):
    servicio = get_object_or_404(Servicio, idServicioSalud=id_servicio)

    if request.method == 'POST':
        servicio.delete()
        messages.warning(request,'El Servicio ha sido eliminado')
        return JsonResponse({'success': True})

    return JsonResponse({'success': False})

def editar_servicio(request, id_servicio):
    servicio = get_object_or_404(Servicio, idServicioSalud=id_servicio)
    if request.method == 'POST':
        form = ServicioForm2(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            messages.success(request,'Servicio Editado con Exito')
            return redirect('servicios')

    else:
        form = ServicioForm2(instance=servicio)

    return render(request, 'servicios/edicion_servicio.html', {'form': form})

def crear_usuario(request):

    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente agregado con exito')
            return redirect('pacientes')
    else:
        form = UsuarioForm()

    return render(request, 'pacientes/formulario_paciente.html', {
        'form': form,
    })

@csrf_exempt
def crear_donacion(request):
    if request.method == 'POST':
        manifestacion = request.POST.get('manifestacionOpo')
        fecha = request.POST.get('fechaDonacion')
        nuevo_donacion = OpocisionDonacion.objects.create(
            manifestacionOpo=manifestacion,
            fechaDonacion=fecha
        )
        return JsonResponse({
            'success': True,
            'id': nuevo_donacion.idDonacion,
            'manifestacion': nuevo_donacion.get_manifestacionOpo_display()
        })
    return JsonResponse({'success': False})

@csrf_exempt
def crear_voluntad(request):
    if request.method == 'POST':
        documento_voluntad = request.POST.get('docVoluntad')
        fecha = request.POST.get('fecha')
        prestador_salud = request.POST.get('codPrestadorSalud')
        nuevo_voluntad = VoluntaAnticipada.objects.create(
            docVoluntad=documento_voluntad,
            fecha=fecha,
            codPrestadorSalud=prestador_salud
        )
        return JsonResponse({
            'success': True,
            'id': nuevo_voluntad.idVoluntad,
            'prestador_salud': nuevo_voluntad.codPrestadorSalud
        })

    return JsonResponse({'success': False})
