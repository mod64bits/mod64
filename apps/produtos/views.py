from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Fornecedor

class ListaFornecedores(ListView):
    model = Fornecedor
