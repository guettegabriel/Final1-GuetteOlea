import datetime

from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import *
from .forms import *
from django.db.models import Q

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from django.contrib.auth import logout



from django.contrib import messages


from .forms import UpdateUserForm, UpdateProfileForm

from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse
from .forms import CommentForm





def inicio(request):
    
 
    return render(request,"ProyectoFinalApp/index.html")

def about(request):
    
 
    return render(request,"ProyectoFinalApp/about.html")





#logout

def logout_view(request):
    logout(request)
    return redirect ('inicio')
    
    
    

def nuevo_usuario(request):
    if request.method == "POST":
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            u = formulario.save()
            profile = Profile.objects.create(user=u)
            profile.save()
            u.save()
            return redirect("crear_usuario")
    else:
        formulario = UserCreationForm()
    return render(request, 'ProyectoFinalApp/nuevousuario.html', {'formulario': formulario} )


    
def login_user(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('inicio')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    return render(request, 'ProyectoFinalApp/ingresar.html',context={'form':AuthenticationForm()})
            
                     
                
@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
           
            messages.success(request, 'Actualizacion Correcta')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'ProyectoFinalApp/profile.html', {'user_form': user_form, 'profile_form': profile_form})       


def Segas(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            Segas = Sega.objects.filter( Q(nombre__icontains=search) | Q(genero__icontains=search) ).values()

            return render(request,"ProyectoFinalApp/Sega.html",{"Segas":Segas, "search":True, "busqueda":search})

    Segas = Sega.objects.all()

    return render(request,"ProyectoFinalApp/Sega.html",{"Segas":Segas})

def crear_Sega(request):
    
    # post
    if request.method == "POST":
        
        formulario = NuevoJuegoS(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            Segas = Sega(nombre=info["nombre"],genero=info["genero"], año=info["anio"])
            Segas.save()

            return redirect("Sega")

        return render(request,"ProyectoFinalApp/formulario_Sega.html",{"form":formulario})

    # get
    
    formulario = NuevoJuegoS()
    return render(request,"ProyectoFinalApp/formulario_Sega.html",{"form":formulario})

def eliminar_Sega(request,Sega_id):

    Segas = Sega.objects.get(id=Sega_id)
    Segas.delete()

    return redirect("Sega")

def editar_Sega(request,Segas_id):

    Segas = Sega.objects.get(id=Segas_id)

    if request.method == "POST":

        formulario = NuevoJuegoS(request.POST)

        if formulario.is_valid():
            
            info_Sega = formulario.cleaned_data
            
            Segas.nombre = info_Sega["nombre"]
            Segas.genero = info_Sega["genero"]
            Segas.año = info_Sega["año"]
            Segas.descripcion = info_Sega["descripcion"]
            Segas.save()

            return redirect("Sega")

    # get
    formulario = NuevoJuegoS(initial={"nombre":Segas.nombre, "genero":Segas.genero, "año": Segas.año})
    
    return render(request,"ProyectoFinalrApp/formulario_Sega.html",{"form":formulario})

class SegaList(ListView):

    model = Sega
    template_name = "ProyectoFinalApp/Segas_list.html"
    context_object_name = 'Segas'

class SegaDetail(DetailView):

    model = Sega
    template_name = "ProyectoFinalApp/Sega_detail.html"
    context_object_name = 'Segas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
       
    

class SegaCreate(CreateView):

    model = Sega
    success_url = "/blog/Sega" # atenciooooooooon!!!! a la primer /
    fields = ["nombre", "genero", "año", "descrpcion"]

class SegaUpdate(UpdateView):

    model = Sega
    success_url = "/blog/Sega" # atenciooooooooon!!!! a la primer /
    fields = ["nombre", "genero", "año", "descripcion"]

class SegaDelete(DeleteView):

    model = Sega
    success_url = "/blog/Sega/list" # atenciooooooooon!!!! a la primer /


def GameBoys(request):
    
    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            GameBoys = GameBoy.objects.filter( Q(nombre__icontains=search) | Q(genero__icontains=search) ).values()

            return render(request,"ProyectoFinalApp/GameBoy.html",{"GameBoy":GameBoys, "search":True, "busqueda":search})

    GameBoys = GameBoy.objects.all()

    return render(request,"ProyectoFinalApp/GameBoy.html",{"GameBoys":GameBoys})

def crear_GameBoy(request):
    
    # post
    if request.method == "POST":
        
        formulario = NuevoJuegoG(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            GameBoys = GameBoy(nombre=info["nombre"],genero=info["genero"], año=info["anio"])
            GameBoys.save()

            return redirect("GameBoy")

        return render(request,"ProyectoFinalApp/formulario_GameBoy.html",{"form":formulario})

    # get
    formulario = NuevoJuegoG()
    return render(request,"ProyectoFinalApp/formulario_GameBoy.html",{"form":formulario})

def eliminar_GameBoy(request,GameBoy_id):

    GameBoys = GameBoy.objects.get(id=GameBoy_id)
    GameBoy.delete()

    return redirect("GameBoy")

def editar_GameBoy(request,GameBoy_id):

    GameBoys = GameBoy.objects.get(id=GameBoy_id)

    if request.method == "POST":

        formulario = NuevoJuegoG(request.POST)

        if formulario.is_valid():
            
            info_GameBoy = formulario.cleaned_data
            
            GameBoy.nombre = info_GameBoy["nombre"]
            GameBoy.genero = info_GameBoy["genero"]
            GameBoy.año = info_GameBoy["año"]
            GameBoy.save()

            return redirect("GameBoy")

    # get
    formulario = NuevoJuegoG(initial={"Nombre":GameBoy.nombre, "Genero":GameBoy.genero, "Año": GameBoy.año})
    
    return render(request,"ProyectoFinalrApp/formulario_GameBoy.html",{"form":formulario})

class GameBoyList(ListView):

    model = GameBoy
    template_name = "ProyectoFinalApp/GameBoy_list.html"

class GameBoyDetail(DetailView):

    model = GameBoy
    template_name = "ProyectoFinalApp/GameBoy_detail.html"

class GameBoyCreate(CreateView):

    model = GameBoy
    success_url = "/blog/GameBoy" # atenciooooooooon!!!! a la primer /
    fields = ["nombre", "genero", "año"]

class GameBoyUpdate(UpdateView):

    model = GameBoy
    success_url = "/blog/GameBoy" # atenciooooooooon!!!! a la primer /
    fields = ["nombre", "genero", "año"]

class GameBoyDelete(DeleteView):

    model = GameBoy
    success_url = "/blog/GameBoy" # atenciooooooooon!!!! a la primer /
    
def Ness(request):
    
    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            Ness = Nes.objects.filter( Q(nombre__icontains=search) | Q(genero__icontains=search) ).values()

            return render(request,"ProyectoFinalApp/Nes.html",{"Ness":Ness, "search":True, "busqueda":search})

    Ness = Nes.objects.all()

    return render(request,"ProyectoFinalApp/Nes.html",{"Ness":Ness})

def crear_Nes(request):
    
    # post
    if request.method == "POST":
        
        formulario = NuevoJuegoN(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            Ness = Nes(nombre=info["nombre"],genero=info["genero"], año=info["anio"])
            Ness.save()

            return redirect("Nes")

        return render(request,"ProyectoFinalApp/formulario_Nes.html",{"form":formulario})

    # get
    formulario = NuevoJuegoN()
    return render(request,"ProyectoFinalApp/formulario_Nes.html",{"form":formulario})

def eliminar_Nes(request,Nes_id):

    Ness = Nes.objects.get(id=Nes_id)
    Ness.delete()

    return redirect("Nes")

def editar_Nes(request,Nes_id):

    Ness = Nes.objects.get(id=Nes_id)

    if request.method == "POST":

        formulario = NuevoJuegoN(request.POST)

        if formulario.is_valid():
            
            info_Nes = formulario.cleaned_data
            
            Ness.nombre = info_Nes["nombre"]
            Ness.genero = info_Nes["genero"]
            Ness.año = info_Nes["año"]
            Ness.save()

            return redirect("Nes")

    # get
    formulario = NuevoJuegoN(initial={"Nombre":Ness.nombre, "Genero":Ness.genero, "Año": Ness.año})
    
    return render(request,"ProyectoFinalrApp/formulario_Nes.html",{"form":formulario})

class NesList(ListView):

    model = Nes
    template_name = "ProyectoFinalApp/Nes_list.html"

class NesDetail(DetailView):

    model = Nes
    template_name = "ProyectoFinalApp/Nes_detail.html"

class NesCreate(CreateView):

    model = Nes
    success_url = "/blog/Nes/list" # atenciooooooooon!!!! a la primer /
    fields = ["nombre", "genero", "año"]

class NesUpdate(UpdateView):

    model = Nes
    success_url = "/blog/Nes/list" # atenciooooooooon!!!! a la primer /
    fields = ["nombre", "genero", "año"]

class NesDelete(DeleteView):

    model = Nes
    success_url = "/blog/Nes/list" # atenciooooooooon!!!! a la primer /


def base(request):
    return render(request,"ProyectoFinalApp/base.html",{})

class SegaComment(SingleObjectMixin, FormView):
    model = Sega
    form_class = CommentForm
    template_name = 'post_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(SegaComment, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse('Sega_detail', kwargs={'pk': post.pk}) + '#comments'