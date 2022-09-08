from django import forms
import datetime


class EquipoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    pais = forms.IntegerField()


class JugadorFormulario(forms.Form):   
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    fecha_nacimiento = forms.DateField(required=False)

class PosicionFormulario(forms.Form):   
    posicion = forms.CharField(max_length=30)
    equipo = forms.CharField(max_length=30)
    