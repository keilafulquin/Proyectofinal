
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Autor, Contacto, Articulo


# Create your views here.


def mostrar_inicio(request):
    return render(request, 'blog/inicio.html')


def autores(request):
    if request.method != 'POST':
        return render(request, "blog/autores.html")
    else: 
        autor = Autor(nombre=request.POST['nombre'], apellido=request.POST['apellido'],edad=request.POST['edad'],profesion=request.POST['profesion'])
        autor.save()
        return render(request,"blog/inicio.html")

        

def articulos(request):
    if request.method != 'POST':
        return render(request, "blog/articulos.html")
    else: 
       
        articulo = Articulo(titulo=request.POST['titulo'], texto=request.POST['texto'])
        articulo.save()
        return render(request,"blog/inicio.html")
    



def seccion(request):
    return render(request, 'blog/seccion.html')


def contacto(request):
    return render(request, 'blog/contacto.html')


    
def formulario(request):
    if request.method != 'POST':
        return render(request, "blog/formulario.html")
    else:
        
        contacto = Contacto(nombre=request.POST['nombre'], apellido=request.POST['apellido'],email=request.POST['email'],telefono=request.POST['telefono'])
        contacto.save()
        return render(request,"blog/inicio.html")
    

def buscar(request):

    if  request.GET["profesion"]:

	      
            profesion = request.GET['profesion'] 
            autores = Autor.objects.filter(autor__icontains=autorbuscado)

            return render(request, "blog/inicio.html", {"autorbuscado":autorbuscado, "autores":autores})

    else: 

	         
            respuesta = "No enviaste datos"
            return HttpResponse(respuesta)    