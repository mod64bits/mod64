from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from apps.base.models import BaseModel



class Fabricante(BaseModel):
    nome = models.CharField("Nome", max_length=200)

    class Meta:
        verbose_name = 'Fabricante'
        verbose_name_plural = 'Frabricantes'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Fornecedor(BaseModel):
    TIPO_CLIENTE_CHOICE = [
        ("CPF", "CPF"),
        ("CNPJ", "CNPJ"),
    ]
    tipo = models.CharField('Tipo', max_length=4, choices=TIPO_CLIENTE_CHOICE, default="CNPJ")
    nome = models.CharField('Nome', max_length=50)
    documento = models.CharField('Documento', max_length=50, null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=30, null=True, blank=True)
    email = models.EmailField('E-mail', null=True, blank=True)

    class Meta:
        verbose_name = 'Fornecedo'
        verbose_name_plural = 'Fornecedores'
        ordering = ['nome']

    def __str__(self):
        return self.nome



class Produto(BaseModel):
    nome = models.CharField("Nome", max_length=150)
    fabricante = models.ForeignKey(
        Fabricante,
        on_delete=models.SET_NULL,
        verbose_name="Fabricante",
        related_name="produto_fabricante",
        null=True,
        blank=True
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


