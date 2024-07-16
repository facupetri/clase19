from django.urls import path

from .views import cursos, estudiantes, profesores, inicio, entregables

urlpatterns = [
    path('inicio/', inicio),
    path('cursos/', cursos),
    path('estudiantes/', estudiantes),
    path('profesores/', profesores),
    path('entregables/', entregables),
]
