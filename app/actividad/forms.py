from django import forms

from .models import Clientes, Companias, Polizas

class CustomClienteChoiseField(forms.ModelChoiceField):

    def label_from_instance(self, obj):
        return obj.nombre.upper()


class PolizasCustomForm(forms.ModelForm):
    clientes = CustomClienteChoiseField(label="Cliente", queryset=Clientes.objects.all().order_by("nombre"))

    class Meta:
        model = Clientes
        fields = "__all__"


class VencimientoPolizasForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['productor'].required = False
        self.fields['seccion'].required = False
        self.fields['vigencia_desde'].required = False
    class Meta:
        model = Polizas
        fields = ("productor", "seccion", "vigencia_desde", "vigencia_hasta")


class ClientesPolizasForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['cliente'].required = False
        self.fields['seccion'].required = False
        self.fields['vigencia_desde'].required = False
        
    class Meta:
        model = Polizas
        fields = ("cliente", "seccion", "vigencia_desde", "vigencia_hasta")



class CompaniaForm(forms.ModelForm):
    class Meta:
        model = Companias
        fields = '__all__'
