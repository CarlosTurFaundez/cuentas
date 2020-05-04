from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Cuenta, Transferencia

# Extendemos del original
class Registro(UserCreationForm):
    # Ahora el campo username es de tipo email y cambiamos su texto
    username = forms.EmailField(label="Correo electrónico")
    first_name=forms.CharField(max_length=10, label="Nombre")
    last_name=forms.CharField(max_length=40, label='Apellidos')

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name" ,"password1", "password2"]


class TransferenciaForm(forms.ModelForm):
    importe=forms.DecimalField( min_value=0.01)

    class Meta:
        model=Transferencia
        fields ='__all__'
        
     

        
        
     
   
