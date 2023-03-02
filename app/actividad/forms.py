from django import forms

from .models import Clientes, Companias, Ordenes, Polizas


class CustomClienteChoiseField(forms.ModelChoiceField):

    def label_from_instance(self, obj):
        return obj.nombre.upper()


class PolizasCustomForm(forms.ModelForm):
    clientes = CustomClienteChoiseField(
        label="Cliente", queryset=Clientes.objects.all().order_by("nombre"))

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


class LibrosRubricadosForm(forms.ModelForm):
    """ Formulario para la generación de libros de rendiciones y operaciones """
    
    CHOICES_ENC_RUBR = [
        ('1', 'Imprimir Encabezados'),
        ('2', 'Imprimir Rubricados'),
    ]

    CHOICES_RENDOP = [
        ('1', 'Rendiciones'),
        ('2', 'Operaciones'),
    ]

    rendOp = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES_RENDOP)
    encRubr = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES_ENC_RUBR)
    pagDesde = forms.DecimalField()
    paghasta = forms.DecimalField()

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        if(self.fields['encRubr']==1):
            print("coas")
            self.fields['vigencia_desde'].required = False
            self.fields['vigencia_hasta'].required = False
        else:
            print("shit")
            self.fields['pagDesde'].required = False
            self.fields['paghasta'].required = False
    class Meta:
        """ Meta clase para el formulario de libros """
        model = Ordenes
        fields = ("productor", "vigencia_desde", "vigencia_hasta")


class CompaniaForm(forms.ModelForm):
    class Meta:
        model = Companias
        fields = '__all__'
