from django.db import models
from core.modelos.entidades.Pessoa import Pessoa
from core.modelos.entidades.Escolaridade import Escolaridade


class Estudante(Pessoa):
    matricula = models.CharField(primary_key=True, max_lenght=11)
    escolaridade = models.OneToOneField(
        Escolaridade, on_delete=models.CASCADE, null=False, verbose_name='escolaridade do aluno')
    dataMatricula = models.DateField()
    dataColacao = models.DateField()
    usosRestauranteUniversitario = models.IntegerField()
    coeficienteRendimento = models.FloatField()
    bolsista = models.BooleanField()
    bolsa = models.FloatField()
    agenciaBancaria = models.CharField()
    contaBancaria = models.CharField()
