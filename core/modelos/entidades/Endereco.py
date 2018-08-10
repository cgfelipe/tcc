from django.db import models


class Endereco (models.Model):
    cep = models.CharField(max_length=10)
    logradouro = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50)
    referencia = models.CharField(max_length=50)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=2)
    pais = models.CharField(max_length=30)
