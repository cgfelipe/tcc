from django.db import models
from core.modelos.entidades.Endereco import Endereco


class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    nomeMae = models.CharField(max_length=200)
    dataNascimento = models.DateField()
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=30)
    endereco = models.OneToOneField(
        Endereco, on_delete=models.CASCADE, null=False, verbose_name='endereço da pessoa')
    usuario = models.CharField(max_length=20)
    senha = models.CharField(max_length=50)
    cpf = models.CharField(primary_key=True, max_lenght=11)
    rg = models.CharField(max_length=8)
