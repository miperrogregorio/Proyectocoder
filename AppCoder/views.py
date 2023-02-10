from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Estudiantes, Profesor, Entregable
# Create your views here.


def curso(self):
    curso = Curso(nombre="Desarrollo web", comision=19881) 
    curso.save()
    documentoDeTexto =f"--> Curso: {curso.nombre} comision:{curso.comision}"
    return HttpResponse(documentoDeTexto)

def estudiante(self):
    estudiante = Estudiantes 