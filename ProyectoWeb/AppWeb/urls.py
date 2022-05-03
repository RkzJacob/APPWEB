from django.urls import path
from django.urls.resolvers import URLPattern
from .views import home,panelAdmin,panelMedico,panelBodeguero,panelFarmaceutico,caducarMedicamentos,eliminarCuentas,generarInformes,iniciarSesion,modificarCuentas,ConsultarMedicamentos,registrarConsulta,registrarCuentas,registrarMedicamentos,reservarMedicamentos,retiroMedicamentos,revisarStock,verCuentas

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('',home,name='home'),
    path('Panel_medico/',panelMedico,name='panelMedico'),
    path('Panel_bodeguero/',panelBodeguero,name='panelBodeguero'),
    path('Panel_farmaceutico/',panelFarmaceutico,name='panelFarmaceutico'),
    path('registrar_medicamentos/',registrarMedicamentos,name='registrarMedicamentos'),


]

