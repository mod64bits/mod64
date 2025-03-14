from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import Ticket
from .forms import TicketModelForm
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView


class TicketListView(ListView):
    model = Ticket
    template_name = 'tickets/ticket_list.html'


class TicketCreateView(BSModalCreateView):
    template_name = 'tickets/ticket_novo.html'
    form_class = TicketModelForm
    success_message = 'Success: Ticket Cadastrado com Sucesso.'
    success_url = reverse_lazy('tickets:list-ticket')


class TicketUpdateView(BSModalUpdateView):
    model = TicketModelForm
    template_name = 'tickets/ticket_update.html'
    form_class = TicketModelForm
    success_message = 'Success: ticket Atualizado com Sucesso.'
    success_url = reverse_lazy('tickets:list-ticket')

