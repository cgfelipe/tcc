from django.db import models
from core.modelos.entidades.Professor import Professor


class Departamento(models.Model):
    nome = models.CharField(max_length=200)
    dataFundacao = models.DateField()
    diretor = models.OneToOneField(
        Professor, on_delete=models.CASCADE, null=False, verbose_name='diretor do departamento'
    )
    quantidadeSalas = models.IntegerField()
    rendaAnual = models.FloatField()
