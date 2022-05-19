from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import MedicamentoForm,ConsultaForm,customUserForm,RetiroMedicamentoForm
from .models import Medicamento,Consulta,Retiro
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User


#Pag home
def home(request):
    return render(request,'AppWeb/home.html')


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
            messages.success(request,"Datos guardados correctamente")
        else:
            messages.error(request,"No te has registrado correctamente")
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
            messages.success(request,"Datos guardados correctamente")
        else:
            messages.error(request,"No se ha registrado el medicamento")
            
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
    #cargo los datos de los medicamentos 
    datos ={
        'ConMedicamento' : ConMedicamento
    }
    return render(request,'AppWeb/consultar medicamentos.html',datos)


    #Descompocisión panel farmaceutico #Pag reservar medicamentos
def reservarMedicamentos(request): 
    return render(request,'AppWeb/reservarMedicamentos.html')

    #Descompocisión panel farmaceutico #Pag retiro de medicamentos
def retiroMedicamentos(request):
    Res =Retiro.objects.all()
    datos={
        'Res' :Res,
        'form': RetiroMedicamentoForm
    }
    if request.method == 'POST':
        formulariod= RetiroMedicamentoForm(request.POST)

        if formulariod.is_valid:
            formulariod.save()
            messages.success(request,"Datos guardados correctamente")
        else:
            messages.error(request,"No se ha guardado el retiro del medicamento")
    return render(request,'AppWeb/retiroMedicamentos.html',datos)


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
        else:
            messages.error(request,"No se ha podido registrar el usuario")
        data['form']= formulario
    return render(request,'registration/registro.html',data)


    #Descompocisión panel admin #Pag modificar cuentas de usuario
def modificarCuentas(request,id):
    Cu=User.objects.get(username=id)

    dic={
        'form':customUserForm(instance=Cu)
    }

    if request.method == 'POST':
        formulario=customUserForm(data=request.POST,instance=Cu)

        if formulario.is_valid:
            formulario.save()
            messages.success(request,"Datos modificados con exito")
        else:
            messages.error(request,"Los datos no fueron modificados")
    
    return render(request,'AppWeb/modificar cuentas.html',dic)
    #Descompocisión panel admin #Pag eliminar cuentas de usuario

def eliminarCuentas(request,id):
    user=User.objects.get(username=id)

    user.delete()

    return redirect(to="verCuentas")
    
    #Descompocisión panel admin #Pag generar informes
def generarInformes(request):
    return render(request,'AppWeb/generacionInformes.html')
    #Descompocisión panel admin #Pag ver cuentas del sistema
def verCuentas(request):
    Cu =User.objects.all()
    #cargo los datos de publicaciones de artes con todos sus datos en los artistas 
    datos ={
        'Cu' : Cu
    }
    return render(request,'AppWeb/ver cuentas.html',datos)


