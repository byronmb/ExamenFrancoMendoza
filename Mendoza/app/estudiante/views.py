from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse
from .forms import FormularioEstudiante
from app.modelo.models import Estudiante
from django.contrib.auth.decorators import login_required

# Create your views here.

def principal(request):
#    usuario = request.user
    listaEstudiantes = Estudiante.objects.all().order_by('apellidos')
    context = {
        'lista': listaEstudiantes
    }
    return render(request, 'home.html', context)


def crear (request):
    formulario = FormularioEstudiante(request.POST)
    if request.method == 'POST':
        if formulario.is_valid():
            datos = formulario.cleaned_data
            estudiante = Estudiante()
            estudiante.cedula = datos.get('cedula');
            estudiante.apellidos = datos.get('apellidos');
            estudiante.nombre = datos.get('nombre');
            estudiante.genero = datos.get('genero');
            estudiante.matricula = datos.get('matricula');
            estudiante.curso = datos.get('curso');
            estudiante.save()
            return redirect(saludar)

    context = {
        'f': formulario,
        'mensaje': 'Bienvenidos',
    }
    return render(request,'crear.html',context)

def saludar (request):
    return HttpResponse('Esta bien')

def modificar (request):
    dni = request.GET['cedula']
    estudiante = Estudiante.objects.get(cedula=dni)
    formulario = FormularioEstudiante(request.POST, instance=estudiante)

    if request.method == 'post':
        # formulario = FormularioCliente(request.POST, instance=cliente)
        if formulario.isValid():
            datos = formulario.cleaned_data
            estudiante.cedula = datos.get('cedula');
            estudiante.apellidos = datos.get('apellidos');
            estudiante.nombre = datos.get('nombre');
            estudiante.genero = datos.get('genero');
            estudiante.matricula = datos.get('matricula');
            estudiante.curso = datos.get('curso');
            estudiante.save()
            return redirect(saludar)
    context = {
        'f': formulario,
        'mensaje': 'Bienvenidos',
    }
    return render(request, 'crear.html', context)

