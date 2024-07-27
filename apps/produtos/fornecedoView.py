import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from apps.produtos.forms import FornecedorForm
from apps.produtos.models import Fornecedor
from apps.base.views import addBaseView, editBaseView

def index_fornecedor(request):
    return render(request, 'produtos/fornecedor/index.html')

def list_fornecedor(request):
    return render(request, 'produtos/fornecedor/fornecedor_list.html', {
        'fornecedores': Fornecedor.objects.all()
    })


def add_fornecedor(request):
    return addBaseView(request, FornecedorForm, 'produtos/fornecedor/fornecedor_form.html' )


def edit_fornecedor(request, pk):
    return editBaseView(request, pk, Fornecedor, FornecedorForm,'produtos/fornecedor/fornecedor_form.html')


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