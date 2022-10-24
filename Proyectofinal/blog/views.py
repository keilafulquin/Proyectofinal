
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import (
    Autor, 
    Contacto, 
    Articulo
)
from blog.form import (
    ArticuloForm, 
    AutorForm, 
    SeccionForm, 
    ContactoForm
)

# Create your views here.


def mostrar_inicio(request):
    return render(request, 'blog/inicio.html')


def autores(request):
    if request.method == "GET":
        mi_formulario = AutorForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "blog/autores.html", context=contexto)
    if request.method == "POST":

        mi_formulario = AutorForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Autor(
                nombre=datos_ingresados_por_usuario["nombre"],
                apellido=datos_ingresados_por_usuario["apellido"],
                edad=datos_ingresados_por_usuario["edad"],
                profesion=datos_ingresados_por_usuario["profesion"]
            )
            nuevo_modelo.save()

            return render(request, "blog/inicio.html")

        contexto = {"formulario": mi_formulario}
        return render(request, "blog/autores.html", context=contexto)

        
def articulos(request):
    if request.method == "GET":
        mi_formulario = ArticuloForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "blog/articulos.html", context=contexto)

    if request.method == "POST":

        mi_formulario = ArticuloForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Articulo(
                titulo=datos_ingresados_por_usuario["titulo"],
                texto=datos_ingresados_por_usuario["texto"],
                fecha=datos_ingresados_por_usuario["fecha"],
            )
            nuevo_modelo.save()

            return render(request, "blog/inicio.html")

        contexto = {"formulario": mi_formulario}
        return render(request, "blog/articulos.html", context=contexto)


def seccion(request):
    mi_formulario = SeccionForm()
    contexto = {"formulario": mi_formulario}
    
    return render(request, 'blog/seccion.html', context=contexto)


def contacto(request):
    if request.method == "GET":
        mi_formulario = ContactoForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "blog/contacto.html", context=contexto)

    if request.method == "POST":

        mi_formulario = ContactoForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Contacto(
                nombre=datos_ingresados_por_usuario["nombre"],
                apellido=datos_ingresados_por_usuario["apellido"],
                email=datos_ingresados_por_usuario["email"],
                telefono=datos_ingresados_por_usuario["telefono"],
            )
            nuevo_modelo.save()

            return render(request, "blog/inicio.html")

        contexto = {"formulario": mi_formulario}
        return render(request, "blog/contacto.html", context=contexto)


def buscar_articulo(request):
    if request.method == "GET":
        return render(request, "blog/busqueda-articulo.html")

    if request.method == "POST":
        titulo_para_buscar = request.POST["titulo"]
        resultados_de_busqueda = Articulo.objects.filter(titulo=titulo_para_buscar)
        contexto = {"resultados": resultados_de_busqueda}
        return render(request, "blog/resultado1.html", context=contexto)


def buscar_autor(request):
    if request.method == "GET":
        return render(request, "blog/busqueda-autor.html")

    if request.method == "POST":
        nombre_para_buscar = request.POST["nombre"]
        resultados_de_busqueda = Autor.objects.filter(nombre=nombre_para_buscar)
        contexto = {"resultados": resultados_de_busqueda}
        return render(request, "blog/resultado2.html", context=contexto)


def buscar_contacto(request):
    if request.method == "GET":
        return render(request, "blog/busqueda-contacto.html")

    if request.method == "POST":
        nombre_para_buscar = request.POST["nombre"]
        resultados_de_busqueda = Contacto.objects.filter(nombre=nombre_para_buscar)
        contexto = {"resultados": resultados_de_busqueda}
        return render(request, "blog/resultado3", context=contexto)

  