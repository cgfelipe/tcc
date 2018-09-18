from django.db import models
from core.modelos.entidades.Pessoa import Pessoa
from core.modelos.entidades.Estudante import Estudante
from core.modelos.entidades.Professor import Professor


class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateField()
    estudante = models.OneToOneField(
        Estudante, on_delete=models.CASCADE, null=False, verbose_name='estudante responsavel')
    professor = models.OneToOneField(
        Professor, on_delete=models.CASCADE, null=False, verbose_name='professor orientador')
    resumo = models.CharField(max_length=500)
    paginas = models.IntegerField()
    nota = models.FloatField()
    classificacao = models.CharField(max_length=10)
    apresentacao = models.BooleanField()
    disciplina = models.CharField(max_length=30)


