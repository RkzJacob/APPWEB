
from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Medicamento,Consulta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MedicamentoForm(ModelForm):
    


    class Meta:
        model = Medicamento
        fields= ['nombreMedicamento','descripcionMedicamento','fabricanteMedicamento','contenidoMedicamento','cantidad','gramaje','imagenPublicacion']
        

class ConsultaForm(ModelForm):

    class Meta:
        model = Consulta
        fields= ['nombrePersona','Sintomas','diagnostico','medicamentoRecetado']


class customUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields= ['username','first_name','last_name','email','user_permissions','password1']