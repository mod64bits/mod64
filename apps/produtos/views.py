from apps.base.views import BaseViews
from .models import Produto
from .forms import ProdutoForm
from django.views.decorators.http import require_POST

produto_obj = BaseViews(
    model=Produto,
    form_class=ProdutoForm,
    listChanged='produtoListChanged'
)

def index(request):
    return produto_obj.index_view(request, 'produtos/index.html')

def list(request):
    return produto_obj.list_view(request, 'produtos/list.html')

def to_add(request):
    return produto_obj.add_view(request, 'produtos/form.html')
def edit(request, pk):
    return produto_obj.edit_view(request, pk, 'produtos/form.html')

@require_POST
def delete(request, pk):
    return produto_obj.delete_view(request, pk)