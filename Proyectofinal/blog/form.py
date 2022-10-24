from django import forms


class ArticuloForm(forms.Form):
    titulo = forms.CharField(max_length=30)
    texto = forms.CharField(max_length=500)
    fecha = forms.DateField()


class AutorForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    profesion = forms.CharField(max_length=30)


class SeccionForm(forms.Form):
    titulo = forms.CharField(max_length=30)


class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    telefono = forms.IntegerField()
    