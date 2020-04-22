from django.contrib import admin


from .models import Cuenta, Transferencia

class CuentaAdmin(admin.ModelAdmin):

	list_display =('id','titular', 'saldo')

class TransferenciaAdmin(admin.ModelAdmin):

	list_display=('fecha', 'importe', 'concepto', 
		'ordenante', 'beneficiario', 'cuenta_ordenante', 'cuenta_beneficiario')


admin.site.register(Cuenta,CuentaAdmin,)
admin.site.register(Transferencia,TransferenciaAdmin)

