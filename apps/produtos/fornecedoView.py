import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from apps.produtos.forms import FornecedorForm
from apps.produtos.models import Fornecedor


def index_fornecedor(request):
    return render(request, 'produtos/fornecedor/index.html')

def list_fornecedor(request):
    return render(request, 'produtos/fornecedor/fornecedor_list.html', {
        'fornecedores': Fornecedor.objects.all()
    })

def add_fornecedor(request):
    if request.method == "POST":
        form = FornecedorForm(request.POST)
        if form.is_valid():
            fornecedor = form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "fornecedorListChanged": None,
                        "showMessage": f"{fornecedor.nome} Adcionado."
                    })
                })
    else:
        form = FornecedorForm()
    return render(request, 'produtos/fornecedor/fornecedor_form.html', {
        'form': form,
    })

def edit_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method == "POST":
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "fornecedorListChanged": None,
                        "showMessage": f"{fornecedor.nome} Atuializado."
                    })
                }
            )
    else:
        form = FornecedorForm(instance=fornecedor)
    return render(request, 'produtos/fornecedor/fornecedor_form.html', {
        'form': form,
        'fornecedor': fornecedor,
    })

@require_POST
def remove_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    fornecedor.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "fornecedorListChanged": None,
                "showMessage": f"{fornecedor.nome} deletado."
            })
        })