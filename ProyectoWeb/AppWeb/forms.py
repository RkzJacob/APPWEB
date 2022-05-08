from django import forms
from django.forms import ModelForm
from .models import Medicamento,Consulta

class MedicamentoForm(ModelForm):

    class Meta:
        model = Medicamento
        fields= ['nombreMedicamento','descripcionMedicamento','fabricanteMedicamento','contenidoMedicamento','cantidad','gramaje','imagenPublicacion']


class ConsultaForm(ModelForm):

    class Meta:
        model = Consulta
        fields= ['nombrePersona','Sintomas','diagnostico','medicamentoRecetado']