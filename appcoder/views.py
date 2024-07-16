from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, 'appcoder/inicio.html')

def cursos(request):
    return request('appcoder/cursos.html')

def estudiantes(request):
    return HttpResponse('vista de los estudiantes')

def profesores(request):
    return HttpResponse('vista de delos profesores')

def entregables(request):
    return HttpResponse('vista de los entregables')

