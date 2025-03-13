from apps.base.models import BaseModel
from django.db import models


class Fornecedor(BaseModel):
    nome = models.CharField('Nome', max_length=50)
    documento = models.CharField('Documento', max_length=50, null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=30, null=True, blank=True)
    email = models.EmailField('E-mail', null=True, blank=True)

    def __str__(self):
        return self.nome