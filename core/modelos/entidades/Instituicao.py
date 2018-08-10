from django.db import models
from core.modelos.entidades.Endereco import Endereco
from core.modelos.entidades.Pessoa import Pessoa
from core.modelos.entidades.Departamento import Departamento


class Instituicao(models.Model):
    nome = models.CharField()
    cnpj = models.CharField(primary_key=True)
    endereco = models.OneToOneField(
        Endereco, on_delete=models.CASCADE, null=False, verbose_name='endereço da instituição')
    fundador = models.OneToOneField(
        Pessoa, on_delete=models.CASCADE, null=False, verbose_name='fundador da instituição')
    dataFundacao = models.DateField()
    site = models.CharField()
    telefone = models.CharField()
    numeroFuncionarios = models.IntegerField()
    departamentos = models.ForeignKey(
        Departamento, on_delete=models.CASCADE, verbose_name='lista de departamentos')
    rendaAnual = models.FloatField()
