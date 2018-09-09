from django.db import models
from core.modelos.entidades.Estudante import Estudante

class Livro(models.Model):
    titulo = models.CharField()
    autores = models.CharField(max_length=100)
    editora = models.CharField()
    edicao = models.IntegerField()
    valor = models.FloatField()
    dataCriacao = models.DateField()
    ano = models.IntegerField()
    disciplinas = models.CharField()
    estudante = models.OneToOneField(
        Estudante, on_delete=models.CASCADE, null=False, verbose_name='estudante que usa o livro')
    Emprestado = models.BooleanField()

