from django.shortcuts import render,redirect


#Pag home
def home(request):
    return render(request,'AppWeb/home.html')
#Pag iniciar sesión
def iniciarSesion(request):
    return render(request,'AppWeb/iniciar sesion.html')

#Pag panel medico
def panelMedico(request):
    return render(request,'AppWeb/panel medico.html')
    #Descompocisión panel medico #Pag registrar consulta medica
def registrarConsulta(request):
    return render(request,'AppWeb/RegistrarConsulta.html') 
    #Descompocisión panel medico #Pag revisar stock de medicamentos
def revisarStock(request):
    return render(request,'AppWeb/revisar stock.html') 


#Pag panel bodeguero
def panelBodeguero(request):
    return render(request,'AppWeb/panel bodeguero.html')
    #Descompocisión panel bodeguero #Pag registrar medicamentos
def registrarMedicamentos(request):
    return render(request,'AppWeb/registrarMedicamento.html')
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
    return render(request,'AppWeb/consultar medicamentos.html')
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
    return render(request,'AppWeb/registrar cuentas.html')
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


