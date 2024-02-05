from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class Cep(models.Model):
    cep = models.CharField(max_length=10, unique=True)

    def __str__(self) -> str:
        return self.cep


class Rua(models.Model):
    rua = models.CharField(max_length=256)
    cep = models.ForeignKey(Cep, default=1, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.rua


class Bairro(models.Model):
    bairro = models.CharField(max_length=120)
    rua = models.ManyToManyField(Rua)

    def __str__(self) -> str:
        return self.bairro


class Cidade(models.Model):
    cidade = models.CharField(max_length=120)
    bairro = models.ForeignKey(Bairro, default=1, on_delete=models.DO_NOTHING)
    rua = models.ForeignKey(Rua, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.cidade


class User(AbstractUser, BaseUserManager):
    username = models.CharField(max_length=120, unique=True)
    email = models.EmailField(max_length=256)
    password = models.CharField(max_length=264)
    endereco = models.ManyToManyField(Rua)
    cep = models.ManyToManyField(Cep)
    bairro = models.ManyToManyField(Bairro)
    cidade = models.ManyToManyField(Cidade)
    data_nascimento = models.DateField(default=None, blank=True, null=True)

    def __str__(self) -> str:
        return self.username
