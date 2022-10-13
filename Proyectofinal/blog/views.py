from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Autor

# Create your views here.


def mostrar_inicio(request):
    return render(request, 'blog/inicio.html')


def autores(request):
    if request.method != "POST":
        return render(request, "blog/autores.html")

    autor = Autor(nombre=request.POST["nombre"], apellido=request.POST["apellido"], edad=request.POST["edad"], profesion=request.POST["profesion"])
    autor.save()
    return render(request, 'blog/autores.html')


def articulos(request):
    return render(request, 'blog/articulos.html')


def seccion(request):
    return render(request, 'blog/seccion.html')


def contacto(request):
    return render(request, 'blog/contacto.html')

def busqueda(request):
    return render(request, "AppCoder/buscar.html")
    