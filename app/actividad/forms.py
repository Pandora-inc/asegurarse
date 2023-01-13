from django import forms

from .models import Companias


class CompaniaForm(forms.ModelForm):
    class Meta:
        model = Companias
        fields = '__all__'
