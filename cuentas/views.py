from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as do_logout,login as do_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Count
from django.db.models import Q
from .models import Cuenta, Transferencia
from .forms import Registro, TransferenciaForm
import uuid


def home(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "cuentas/home.html")

    # En otro caso redireccionamos al login
    return redirect('/login')
 
#Esta es la vista para listar todas las cuentas del usuario activo.

def mi_usuario_cuentas(request):
    
    if request.user.is_authenticated:
        mis_cuentas = Cuenta.objects.all().filter(titular=request.user).order_by('fecha_apertura')

    return render(request, 'cuentas/mis_cuentas.html',{'mis_cuentas':mis_cuentas})


#Esta es la vista para ver los movimientos de una concreta cuenta del usuario activo.

def mi_cuenta_detalle (request, id): 
    if request.user.is_authenticated: 
       
        mis_transferencias =Transferencia.objects.filter(Q(cuenta_ordenante=id)|Q(cuenta_beneficiario=id)).order_by('fecha')
    return render(request, 'cuentas/mis_movimientos.html',{'mis_transferencias':mis_transferencias})



    # Creamos el formulario de autenticación vacío
def register(request):
    form = Registro()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = Registro(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "cuentas/register.html", {'form': form})

def login(request):

    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/mis_cuentas')
           

    # Si llegamos al final renderizamos el formulario
    return render(request, "cuentas/login.html", {'form': form})   

class TransferenciaCrea(CreateView, LoginRequiredMixin): 
    
    model=Transferencia
    form_class=TransferenciaForm
    template_name='cuentas/transferencias.html'
    success_url=reverse_lazy('/mis_cuentas')

    
def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/home')

def en_marcha(request):
    return render(request,"cuentas/en_marcha.html")
