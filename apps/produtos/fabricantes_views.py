from apps.base.views import BaseViews
from apps.produtos.models import Fabricante

from .forms import FabricanteForm

fabricante = BaseViews(Fabricante, FabricanteForm, 'fabricanteListChanged')

def index(request):
    return fabricante.index_view(request, 'produtos/fabricantes/index.html')


def add_Fabricante(request):
    return addBaseView(request, FabricanteForm, 'produtos/fabricante/form.html')

def edit_Fabricante(request, pk):
    return editBaseView(request, pk, Fabricante, FabricanteForm, 'produtos/fabricante/form.html')