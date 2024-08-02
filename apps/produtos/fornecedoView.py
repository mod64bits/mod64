from apps.base.views import BaseViews
from .models import Fornecedor
from .forms import FornecedorForm
from django.views.decorators.http import require_POST

fornecedor_obj = BaseViews(
    model=Fornecedor,
    form_class=FornecedorForm,
    listChanged='fornecedorListChanged'
)

def index(request):
    return fornecedor_obj.index_view(request, 'produtos/fornecedor/index.html')

def list(request):
    return fornecedor_obj.list_view(request, 'produtos/fornecedor/fornecedor_list.html')

def to_add(request):
    return fornecedor_obj.add_view(request,'produtos/fornecedor/fornecedor_form.html' )

def edit(request, pk):
    return fornecedor_obj.edit_view(request, pk,'produtos/fornecedor/fornecedor_form.html')

@require_POST
def delete(request, pk):
    return fornecedor_obj.delete_view(request, pk)