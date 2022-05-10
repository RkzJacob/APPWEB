from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import MedicamentoForm,ConsultaForm,customUserForm
from .models import Medicamento,Consulta
from django.contrib.auth import authenticate,login


#Pag home
def home(request):
    return render(request,'AppWeb/home.html')
#Pag iniciar sesión
def iniciarSesion(request):
    return render(request,'AppWeb//registrar/iniciar sesion.html')

#Pag panel medico
def panelMedico(request):
    return render(request,'AppWeb/panel medico.html')
    #Descompocisión panel medico #Pag registrar consulta medica
def registrarConsulta(request):
    Con =Consulta.objects.all()
    datos={
        'Con' :Con,
        'form': ConsultaForm
    }
    if request.method == 'POST':
        formulariod= ConsultaForm(request.POST)

        if formulariod.is_valid:
            formulariod.save()
            datos['mensaje']= 'datos guardados correctamente'
        else:
            datos['mensaje']= 'datos no guardados'
    return render(request,'AppWeb/RegistrarConsulta.html',datos) 
    #Descompocisión panel medico #Pag revisar stock de medicamentos
def revisarStock(request):
    return render(request,'AppWeb/revisar stock.html') 


#Pag panel bodeguero
def panelBodeguero(request):
    return render(request,'AppWeb/panel bodeguero.html')
    #Descompocisión panel bodeguero #Pag registrar medicamentos
def registrarMedicamentos(request):
    Med =Medicamento.objects.all()
    datos={
        'Med' :Med,
        'form': MedicamentoForm
    }
    if request.method == 'POST':
        formulariod= MedicamentoForm(request.POST,request.FILES)

        if formulariod.is_valid:
            formulariod.save()
            datos['mensaje']= 'datos guardados correctamente'
        else:
            datos['mensaje']= 'datos no guardados'
            
    return render(request,'AppWeb/registrarMedicamento.html',datos)
    #Descompocisión panel bodeguero #Pag Caducar medicamentos
#def caducarMedicamentos(request):
    #return render(request,'AppWeb/caducarMedicamento.html')


#Pag panel farmaceutico
def panelFarmaceutico(request):
    return render(request,'AppWeb/panel farmaceutico.html')
    #Descompocisión panel farmaceutico #Pag Caducar medicamentos
def caducarMedicamentos(request):
    return render(request,'AppWeb/caducarMedicamento.html')
    #Descompocisión panel farmaceutico #Pag consultar medicamentos
def ConsultarMedicamentos(request):
    ConMedicamento =Medicamento.objects.all()
    #cargo los datos de publicaciones de artes con todos sus datos en los artistas 
    datos ={
        'ConMedicamento' : ConMedicamento
    }

    return render(request,'AppWeb/consultar medicamentos.html',datos)
    #Descompocisión panel farmaceutico #Pag reservar medicamentos
def reservarMedicamentos(request):
    return render(request,'AppWeb/reservarMedicamentos.html')
    #Descompocisión panel farmaceutico #Pag retiro de medicamentos
def retiroMedicamentos(request):
    return render(request,'AppWeb/retiroMedicamentos.html')


#Pag panel admin
def panelAdmin(request):
    return render(request,'AppWeb/panel admin.html')
    #Descompocisión panel admin #Pag Registrar cuentas de usuario
def registrarCuentas(request):
    data ={
        'form':customUserForm()
    }

    if request.method == 'POST':
        formulario=customUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user= authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            messages.success(request,"Te has registrado correctamente")
            return redirect(to="registrarCuentas")
        data['form']= formulario
    return render(request,'registration/registro.html',data)


    #Descompocisión panel admin #Pag modificar cuentas de usuario
def modificarCuentas(request):
    return render(request,'AppWeb/modificar cuentas.html')
    #Descompocisión panel admin #Pag eliminar cuentas de usuario
def eliminarCuentas(request):
    return render(request,'AppWeb/eliminar cuentas.html')
    #Descompocisión panel admin #Pag generar informes
def generarInformes(request):
    return render(request,'AppWeb/generacionInformes.html')
    #Descompocisión panel admin #Pag ver cuentas del sistema
def verCuentas(request):
    return render(request,'AppWeb/ver cuentas.html')


