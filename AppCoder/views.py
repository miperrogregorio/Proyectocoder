from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Estudiantes, Profesor, Entregable
# Create your views here.


def inicio(request):
   #return HttpResponse("Vista inicio")
   return render(request, 'AppCoder/inicio.html')

def curso(request):
   #return HttpResponse("Vista cursos")
    return render(request, 'AppCoder/cursos.html')

def profesores(request):
   #return HttpResponse("Vista prefesores")
    return render(request, 'AppCoder/profesores.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')
   #return HttpResponse("Vista entregables")  

def estudiantes(request):
   #return HttpResponse("Vista estudiantes")
   return render(request, 'AppCoder/estudiantes.html')   