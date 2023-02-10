from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Estudiantes, Profesor, Entregable
# Create your views here.


def inicio(request):
   return HttpResponse("Vista inicio")

def curso(request):
   return HttpResponse("Vista cursos")

def profesores(request):
   return HttpResponse("Vista prefesores")

def entregables(request):
   return HttpResponse("Vista entregables")  

def estudiantes(request):
   return HttpResponse("Vista estudiantes")   