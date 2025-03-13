from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import ProdutoCategoria, ProdutoFabricante, Produto
from .forms import ProdutoCategoriaModelForm, ProdutoFabricanteModelForm, ProdutoModelForm

from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView


class ProdutoFabricanteListView(ListView):
    model = ProdutoFabricante
    template_name = 'produtos/fabricante_produto_list.html'


class ProdutoFabricanteCreateView(BSModalCreateView):
    template_name = 'produtos/fabricante_produto_novo.html'
    form_class = ProdutoFabricanteModelForm
    success_message = 'Success: Fabricante Cadastrado com Sucesso.'
    success_url = reverse_lazy('produtos:list-fabricante')


class ProdutoFabricanteUpdateView(BSModalUpdateView):
    model = ProdutoFabricante
    template_name = 'produtos/fabricante_produto_update.html'
    form_class = ProdutoCategoriaModelForm
    success_message = 'Success: Fabricante Atualizado com Sucesso.'
    success_url = reverse_lazy('produtos:list-fabricante')


class ProdutoFabricanteDeleteView(BSModalDeleteView):
    model = ProdutoFabricante
    template_name = 'produtos/fabricante_produto_delete.html'
    success_message = 'Success: Fabricante deletado com Sucesso.'
    success_url = reverse_lazy('produtos:list-fabricante')


class ProdutoCategoriaListView(ListView):
    model = ProdutoCategoria
    template_name = 'produtos/categoria_produto_list.html'

class ProdutoCategoriaCreateView(BSModalCreateView):
    template_name = 'produtos/categoria_produto_novo.html'
    form_class = ProdutoCategoriaModelForm
    success_message = 'Success: Categoria Cadastrado com Sucesso.'
    success_url = reverse_lazy('produtos:list-produto-categoria')


class ProdutoCategoriaUpdateView(BSModalUpdateView):
    model = ProdutoCategoria
    template_name = 'produtos/categoria_produto_update.html'
    form_class = ProdutoCategoriaModelForm
    success_message = 'Success: Categoria Atualizado com Sucesso.'
    success_url = reverse_lazy('produtos:list-produto-categoria')


class ProdutoCategoriaDeleteView(BSModalDeleteView):
    model = ProdutoCategoria
    template_name = 'produtos/categoria_produto_delete.html'
    success_message = 'Success: Categoria deletado com Sucesso.'
    success_url = reverse_lazy('produtos:list-produto-categoria')


class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/produto_list.html'

class ProdutoCreateView(BSModalCreateView):
    template_name = 'produtos/produto_novo.html'
    form_class = ProdutoModelForm
    success_message = 'Success: Produto Cadastrado com Sucesso.'
    success_url = reverse_lazy('produtos:list-produto')


class ProdutoUpdateView(BSModalUpdateView):
    model = Produto
    template_name = 'produtos/produto_update.html'
    form_class = ProdutoModelForm
    success_message = 'Success: Produto Atualizado com Sucesso.'
    success_url = reverse_lazy('produtos:list-produto')


class ProdutoDeleteView(BSModalDeleteView):
    model = Produto
    template_name = 'produtos/produto_delete.html'
    success_message = 'Success: Categoria deletado com Sucesso.'
    success_url = reverse_lazy('produtos:list-produto')