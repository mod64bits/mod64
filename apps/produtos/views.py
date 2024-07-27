import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from .models import Fabricante
from .forms import FabricanteForm
from apps.base.views import addBaseView, editBaseView

def fabricante_index(request):
    pass


def add_Fabricante(request):
    return addBaseView(request, FabricanteForm, 'produtos/fabricante/form.html')

def edit_Fabricante(request, pk):
    return editBaseView(request, pk, Fabricante, FabricanteForm, 'produtos/fabricante/form.html')

