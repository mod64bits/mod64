from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Cliente
from .forms import ClienteModelForm

from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView

class ClienteListView(ListView):
    model = Cliente


class ClienteCreateView(BSModalCreateView):
    template_name = 'clientes/cliente_novo.html'
    form_class = ClienteModelForm
    success_message = 'Success: Cliente Cadastrado com Sucesso.'
    success_url = reverse_lazy('clientes:list-cliente')


class ClienteUpdateView(BSModalUpdateView):
    model = Cliente
    template_name = 'clientes/cliente_update.html'
    form_class = ClienteModelForm
    success_message = 'Success: Cliente Atualizado com Sucesso.'
    success_url = reverse_lazy('clientes:list-cliente')


class ClienteDeleteView(BSModalDeleteView):
    model = Cliente
    template_name = 'clientes/cliente_delete.html'
    success_message = 'Success: Cliente deletado com Sucesso.'
    success_url = reverse_lazy('clientes:list-cliente')