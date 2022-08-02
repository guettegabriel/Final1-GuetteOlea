from django import forms
from django.contrib.auth.models import User
from .models import Profile


class NuevoJuegoS(forms.Form):

    nombre = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    anio = forms.DateField()
    descripcion = forms.CharField(max_length=300)

class NuevoJuegoG(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    anio = forms.DateField()
    
class NuevoJuegoN(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    anio = forms.DateField()
    
#Profiles

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']


