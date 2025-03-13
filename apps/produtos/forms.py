from bootstrap_modal_forms.forms import BSModalModelForm
from .models import ProdutoCategoria, ProdutoFabricante, Produto



class ProdutoCategoriaModelForm(BSModalModelForm):
    class Meta:
        model = ProdutoCategoria
        fields = '__all__'


class ProdutoFabricanteModelForm(BSModalModelForm):
    class Meta:
        model = ProdutoFabricante
        fields = '__all__'


class ProdutoModelForm(BSModalModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

