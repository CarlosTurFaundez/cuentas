
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from cuentas import views
from cuentas.views import home, login, transferencia
from cuentas.views import mi_usuario_cuentas, mi_cuenta_detalle, register, banco_central



urlpatterns = [
    path('', login),
    path('home', home),
    path('admin/', admin.site.urls),
    path('register', register),
    path('banco_central', banco_central),
    path('login', login),
    path('mis_cuentas', mi_usuario_cuentas),
    path('mis_movimientos/<id>', mi_cuenta_detalle, name= 'mis_movimientos'),
    path('transferencias/<id>',transferencia, name='transferencias'),

] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
