
from django import views
from django.urls import path


from blog.views import mostrar_inicio, autores, articulos, seccion, contacto, formulario, buscar


urlpatterns = [
    path('inicio/', mostrar_inicio, name = "Inicio"),
    path('autores/', autores, name = "Autores"),
    path('articulos/', articulos, name = "Articulos"),
    path('seccion/', seccion, name = "Secciones"),
    path('contacto/', contacto, name = "Contacto"),
    path('formulario/', formulario, name = "Formulario"),
    path('buscar/', buscar),
    #path('busqueda/', busqueda, name="Busqueda")
    
]