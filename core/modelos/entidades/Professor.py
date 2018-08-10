from django.db import models
from core.modelos.entidades.Pessoa import Pessoa
from core.modelos.entidades.Escolaridade import Escolaridade
from core.modelos.entidades.Especialidade import Especialidade


class Professor(Pessoa):
    escolaridade = models.OneToOneField(
        Escolaridade, on_delete=models.CASCADE, null=False, verbose_name='escolaridade do professor')
    inscricao = models.CharField(max_length=10, null=False)
    dataAdmissao = models.DateField(null=False)
    interino = models.BooleanField(null=False)
    concursado = models.BooleanField(null=False)
    especialidade = models.ForeignKey(
        Especialidade, on_delete=models.CASCADE, null=False, verbose_name='especialidades do professor'
    )
    salario = models.FloatField(null=False)
    agenciaBancaria = models.CharField()
    contaBancaria = models.CharField()
