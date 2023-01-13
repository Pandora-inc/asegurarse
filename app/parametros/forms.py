from django import forms
from .models import Tipospedido, Tipospoliza, Mediosdepago, Monedas, Postal


class PostalForm(forms.ModelForm):
    class Meta:
        model = Postal
        fields = '__all__'

class MonedasForm(forms.ModelForm):
    class Meta:
        model = Monedas
        fields = '__all__'


class TiposPedidoForm(forms.ModelForm):
    class Meta:
        model = Tipospedido
        fields = '__all__'


class TiposPolizaForm(forms.ModelForm):
    class Meta:
        model = Tipospoliza
        fields = '__all__'

class MediosDePagoForm(forms.ModelForm):
    class Meta:
        model = Mediosdepago
        fields = '__all__'

