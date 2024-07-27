from django import forms
from .models import Fornecedor, Fabricante


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'


class FabricanteForm(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = '__all__'