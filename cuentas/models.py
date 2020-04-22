from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q

from django.contrib.auth.models import AbstractUser

from django.utils import timezone

class Cuenta(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    fecha_apertura = models.DateTimeField()
    saldo_inicio = models.DecimalField( max_digits=20, decimal_places=2)
    titular = models.ForeignKey( User, on_delete=models.CASCADE, blank=False, default=False)
    
    def __str__(self):
        return '%s %s' % (self.id, self.titular.last_name)

    @property
    
    def saldo(self):
#esta propiedad, nos permite calcular el saldo de la cuenta, tomando en consideración la suma de todas
#las transferencias entrantes a cuyo resultado restaremos la suma de todas las transferencias salientes
#almacenadas en la base de datos#

        lista_salientes= Transferencia.objects.filter(cuenta_ordenante=self)
        total_saliente=0
        for saliente in lista_salientes:
            total_saliente+=total_saliente+saliente.importe
        lista_entrantes=Transferencia.objects.filter(cuenta_beneficiario=self)
        total_entrante=0
        for entrante in lista_entrantes:
            total_entrante+=total_entrante + entrante.importe
      
        return self.saldo_inicio +total_entrante- total_saliente

    @property
    def saldo_fecha(self):
        return self._foo
   
    @property
    def saldo_global(self):
        lista_salientes= Transferencia.objects.filter(ordenante=self.titular)
        total_saliente=0
        for saliente in lista_salientes:
            total_saliente+=total_saliente+saliente.importe
        lista_entrantes=Transferencia.objects.filter(beneficiario=self.titular)
        total_entrante=0
        for entrante in lista_entrantes:
            total_entrante+=total_entrante + entrante.importe
      
        return self.saldo_inicio +total_entrante- total_saliente
    @property
    def numero_de_cuentas(self):
        cuantas_cuentas=Cuenta.objects.filter(titular=self.titular)
        return self.cuantas_cuentas.count()

class Transferencia (models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    fecha =models.DateTimeField(default = timezone.now, editable=False)
    importe = models.DecimalField(max_digits=20, decimal_places=2)
    cuenta_ordenante=models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='cuenta_ordenante')
    concepto= models.CharField(max_length=90)
    cuenta_beneficiario=models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='cuenta_beneficiario')
    ordenante= models.ForeignKey(User, on_delete= models.CASCADE, related_name='ordenante',)
    beneficiario = models.ForeignKey (User, on_delete= models.CASCADE, related_name='beneficiario')
  
    



    

   
 


