from django.db import models
from core.modelos.entidades.Pessoa import Pessoa
from core.modelos.entidades.Endereco import Endereco

class Curriculo(models.Model):
    objetivo = models.CharField(max_lenght=500)
    pessoa =  models.OneToOneField(
        Pessoa, on_delete=models.CASCADE, null=False, verbose_name='responsavel do curriculo')
    idLattes = models.CharField(max_lenght=10)
    pretensaoSalarial = models.FloatField()
    ultimaAtualizacao = models.DateField()
    titulo = models.CharField(max_lenght=30)
    endereco = models.OneToOneField(
        Endereco, on_delete=models.CASCADE, null=False, verbose_name='endereco do curriculo')
    enperiencia = models.CharField(max_lenght=500)
    competencias = models.CharField(max_lenght=500)
    formacoes = models.CharField(max_lenght=500)
    