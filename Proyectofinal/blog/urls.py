
from django import views
from django.urls import path



from blog.views import (
    mostrar_inicio, 
    autores, 
    articulos, 
    seccion, 
    contacto, 
    buscar_articulo, 
    buscar_autor, 
    buscar_contacto
)


urlpatterns = [
    path('inicio/', mostrar_inicio, name = "Inicio"),
    path('autores/', autores, name = "Autores"),
    path('articulos/', articulos, name = "Articulos"),
    path('seccion/', seccion, name = "Secciones"),
    path('contacto/', contacto, name = "Contacto"),
    path('buscar-articulo/', buscar_articulo),
    path('buscar-autor/', buscar_autor),
    path('buscar-contacto/', buscar_contacto),
]