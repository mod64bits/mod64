from apps.base.views import BaseViews
from .models import Fabricante
from .forms import FabricanteForm
from django.views.decorators.http import require_POST

fabricante_obj = BaseViews(
    model=Fabricante,
    form_class=FabricanteForm,
    listChanged='fabricanteListChanged'
)

def index(request):
    return fabricante_obj.index_view(request, 'produtos/fabricante/index.html')

def list(request):
    return fabricante_obj.list_view(request, 'produtos/fabricante/list.html')

def to_add(request):
    return fabricante_obj.add_view(request, 'produtos/fabricante/form.html')
def edit(request, pk):
    return fabricante_obj.edit_view(request, pk, 'produtos/fabricante/form.html')

@require_POST
def delete(request, pk):
    return fabricante_obj.delete_view(request, pk)