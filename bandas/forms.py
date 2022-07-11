from django import forms

class FormBanda(forms.Form):
    nombre = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    anios_activa = forms.IntegerField(required=False)

class BusquedaBanda (forms.Form):
    nombre = forms.CharField(max_length=30, required = False)