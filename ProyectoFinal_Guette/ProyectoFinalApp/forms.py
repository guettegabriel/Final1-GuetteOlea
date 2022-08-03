from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Comment


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

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']

    def __init__(self, *args, **kwargs):
        """Save the request with the form so it can be accessed in clean_*()"""
        self.request = kwargs.pop('request', None)
        super(CommentForm, self).__init__(*args, **kwargs)

    def clean_name(self):
        """Make sure people don't use my name"""
        data = self.cleaned_data['name']
        if not self.request.user.is_authenticated and data.lower().strip() == 'samuel':
            raise ValidationError("Sorry, you cannot use this name.")
        return data


