from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
    class Meta:
        model = Transferencia
        fields = [
        	
        	'importe', 
        	'concepto', 
        	'cuenta_ordenante',
        	'cuenta_beneficiario',
        	'ordenante', 
        	'beneficiario'
        	      ]
        labels={
              
              'importe': 'Importe:',
              'concepto': 'Concepto:',
              'cuenta_ordenante':'Cuenta ordenante:',
              'cuenta_beneficiario':'Cuenta beneficiaria:',
              'ordenante':'Ordenante:',
              'beneficiario':'Beneficiario:'
              }
        widgets={
        	  
        	  'importe': forms.NumberInput(),
        	  'concepto': forms.TextInput(),
        	  'cuenta_ordenante': forms.Select(),
        	  'cuenta_beneficiario': forms.Select(),
        	  'ordenante': forms.Select(),
        	  'beneficiario': forms.Select(),
        	   }
    