from django.contrib import admin
from blog.models import Autor, Articulo, Seccion, Contacto
# Register your models here.

admin.site.register(Autor)
admin.site.register(Articulo)
admin.site.register(Seccion)
admin.site.register(Contacto)
