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
    # clientes = CustomClienteChoiseField(label="Cliente", queryset=Clientes.objects.all().order_by("nombre"))

    class Meta:
        model = Polizas
        fields = ("productor", "seccion", "vigencia_desde", "vigencia_hasta")

class CompaniaForm(forms.ModelForm):
    class Meta:
        model = Companias
        fields = '__all__'
