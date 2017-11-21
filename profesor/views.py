from django.shortcuts import render
from django.contrib import messages
from .forms import GradoForm, MateriaForm
from profesor.models import Profesor, Grado, Materia
# Create your views here.
def grado_nueva(request):
    if request.method == "POST":
        formulario = GradoForm(request.POST)
        if formulario.is_valid():
            grado = Grado.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['cupo'])
            for profesor_id in request.POST.getlist('porfesores'):
                materia = Materia(profesor_id=profesor_id, grado_id = grado.id)
                actuacion.save()
            messages.add_message(request, messages.SUCCESS, 'Grado Guardada Exitosamente')
    else:
        formulario = GradoForm()
    return render(request, 'profesor/grado_editar.html', {'formulario': formulario})

def materia_nuevo(request):
    if request.method == "POST":
        formulario = MateriaForm(request.POST)
        if formulario.is_valid():
            materia = Materia.objects.create(nombre=formulario.cleaned_data['nombre'])
            for profesor_id in request.POST.getlist('porfesores'):
                materia = Materia(profesor_id=profesor_id, grado_id = grado.id)
                actuacion.save()
    else:
        formulario = MateriaForm()
    return render(request, 'profesor/materia_editar.html', {'formulario': formulario})

def materia_listar(request):
    materia = Materia.objects.all()
    return render(request, 'profesor/materia_listar.html', {'materia':materia})
