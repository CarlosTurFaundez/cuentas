
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from cuentas import views
from cuentas.views import home, login, logout
from cuentas.views import en_marcha, mi_usuario_cuentas, mi_cuenta_detalle, register, TransferenciaCrea



urlpatterns = [
    path('', home),
    path('home', home),
    path('admin/', admin.site.urls),
    path('register', register),
    path('en_marcha', en_marcha),
    path('login', login),
    path('logout',logout),
    path('mis_cuentas', mi_usuario_cuentas),
    path('mis_movimientos/<id>', mi_cuenta_detalle, name= 'mis_movimientos'),
    path('transferencias/<id>', TransferenciaCrea.as_view(), name='mis_transferencias'),

] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
