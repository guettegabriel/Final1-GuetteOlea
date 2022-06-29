from django import forms


class NuevoJuegoS(forms.Form):

    nombre = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    anio = forms.DateField()

class NuevoJuegoG(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    anio = forms.DateField()
    
class NuevoJuegoN(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    anio = forms.DateField()