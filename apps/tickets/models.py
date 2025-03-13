from django.db import models
from apps.base.models import BaseModel
from apps.clientes.models import Cliente
from apps.accounts.models import User


class Ticket(BaseModel):
    STATUS = (
        ('ABERTO', 'ABERTO'),
        ('EM_ATENDIMENTO', 'EM ATENDIMENTO'),
        ('ENCERRADA', 'ENCERRADA'),
        ('CANCELADA', 'CANCELADA')
    )
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        verbose_name='CLIENTE',
        related_name='ticket_cliente',
        null=True,
        blank=True
    )
    solicitante = models.CharField('Solicitantes', max_length=100)
    departamento = models.CharField('Departamento', max_length=100, null=True, blank=True)
    descricao = models.TextField("Descrição do chamado")
    resolucao = models.TextField("Resolução do chamado", null=True, blank=True)
    responsavel = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='responsible_tick',

    )
    iniciado_em = models.DateTimeField(null=True, blank=True)
    status = models.CharField("Status", max_length=15, choices=STATUS, default='ABERTO')
    finalizado_em = models.DateTimeField(null=True, blank=True, editable=False)

    def __str__(self):
        return self.solicitante



