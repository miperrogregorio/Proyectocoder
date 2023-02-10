from django.urls import path
from AppCoder import views 


urlpatterns = [
    path('', views.inicio),
    path('cursos/', views.curso, name="Curso" ),
    path('profesores/', views.profesores),
    path('estudiantes/', views.estudiantes),
    path('entregables/', views.entregables),



]