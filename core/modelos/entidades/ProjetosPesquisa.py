from django.db import models
from core.modelos.entidades.Professor import Professor

class ProjetoDePesquisa(models.Model):
    idLattes = models.CharField(max_length=100)
    titulo = models.CharField(max_length=200)
    inicio = models.DateField()
    fim = models.DateField()
    keywords = models.ArrayField(ArrayField(models.CharField(max_length=200)))
    valorProjeto = models.FloatField()
    situacao = models.CharField(max_length=200)
    alunos = models.CharField(max_length=200)
    professor= models.OneToOneField(
       Professor, on_delete=models.CASCADE, null=False, verbose_name='professor orientador')
    departamentoResponsavel = 