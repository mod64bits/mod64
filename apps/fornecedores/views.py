from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Fornecedor
from .forms import FornecedorModelForm

from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView

class FornecedorListView(ListView):
    model = Fornecedor


class FornecedorCreateView(BSModalCreateView):
    template_name = 'fornecedores/fornecedor_novo.html'
    form_class = FornecedorModelForm
    success_message = 'Success: Fornecedor Cadastrado com Sucesso.'
    success_url = reverse_lazy('fornecedores:list-fornecedor')


class FornecedorUpdateView(BSModalUpdateView):
    model = Fornecedor
    template_name = 'fornecedores/fornecedor_update.html'
    form_class = FornecedorModelForm
    success_message = 'Success: Fornecedor Atualizado com Sucesso.'
    success_url = reverse_lazy('fornecedores:list-fornecedor')


class FornecedorDeleteView(BSModalDeleteView):
    model = Fornecedor
    template_name = 'fornecedores/fornecedor_delete.html'
    success_message = 'Success: Fornecedor deletado com Sucesso.'
    success_url = reverse_lazy('fornecedores:list-fornecedor')