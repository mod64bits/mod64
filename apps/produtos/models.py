from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from apps.base.models import BaseModel
from apps.fornecedores.models import Fornecedor

class ProdutoCategoria(BaseModel):
    nome = models.CharField('Nome', max_length=50)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class ProdutoFabricante(BaseModel):
    nome = models.CharField("Nome", max_length=50)

    class Meta:
        verbose_name = 'Fabricante'
        verbose_name_plural = 'Frabricantes'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Produto(BaseModel):
    nome = models.CharField("Nome", max_length=150)
    fabricante = models.ForeignKey(
        ProdutoFabricante,
        on_delete=models.SET_NULL,
        verbose_name="Fabricante",
        related_name="produto_fabricante",
        null=True,
        blank=True
    )
    codigo = models.CharField("Codigo", max_length=20, unique=True, null=True, blank=True)
    categoria = models.ForeignKey(
        ProdutoCategoria,
        on_delete=models.CASCADE,
        verbose_name='Categoria',
        related_name='p_categoria'
    )
    fornecedor = models.ForeignKey(
        Fornecedor,
        on_delete=models.CASCADE,
        verbose_name='Fornecedor',
        related_name='p_fornecedor'
    )
    link_produto = models.URLField('Link Produto', null=True, blank=True)
    preco_compra = models.DecimalField(max_digits=16, decimal_places=2, validators=[
                                MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))

    def __str__(self):
        return f"{self.nome} --{self.preco_compra}"