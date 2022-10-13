
from django import views
from django.urls import path
from blog.views import mostrar_inicio, autores, articulos, seccion, contacto

urlpatterns = [
    path('inicio/', mostrar_inicio, name = "Inicio"),
    path('autor/', autores, name = "Autores"),
    path('articulo/', articulos, name = "Articulos"),
    path('seccion/', seccion, name = "Secciones"),
    path('contacto/', contacto, name = "Contacto"),
]