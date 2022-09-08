from django import forms



class EquipoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    pais = forms.CharField(max_length=50)


class JugadorFormulario(forms.Form):   
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    fecha_nacimiento = forms.DateField(required=True)

class PosicionFormulario(forms.Form):   
    posicion = forms.CharField(max_length=30)
    equipo = forms.CharField(max_length=30)
    