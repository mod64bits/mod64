from django import forms
from .models import Fornecedor, Fabricante, Produto


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'


class FabricanteForm(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = '__all__'


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'