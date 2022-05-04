from django import forms
from django.forms import ModelForm
from .models import Medicamento

class MedicamentoForm(ModelForm):

    class Meta:
        model = Medicamento
        fields= ['codigo','nombreMedicamento','descripcionMedicamento','fabricanteMedicamento','contenidoMedicamento','cantidad','gramaje']