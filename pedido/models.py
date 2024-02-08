from django.db import models
from fondue_app.models import User
from produto.models import Produto
from datetime import datetime
from django.utils import timezone


class CupomDesconto(models.Model):
    codigo = models.CharField(max_length=8, unique=True)
    desconto = models.FloatField()
    usos = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.codigo


class Pedido(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    total = models.FloatField()
    troco = models.CharField(blank=True, max_length=20)
    cupom = models.ForeignKey(CupomDesconto, null=True,
                              blank=True, on_delete=models.CASCADE)
    pagamento = models.CharField(max_length=20)
    data = models.DateTimeField(default=timezone.now)
    entregue = models.BooleanField(default=False)

    def __str__(self):
        return self.cliente


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco = models.FloatField()
    descricao = models.TextField()
    adicionais = models.TextField()
