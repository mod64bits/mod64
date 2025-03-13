from .models import Fornecedor
from bootstrap_modal_forms.forms import BSModalModelForm


class FornecedorModelForm(BSModalModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'
