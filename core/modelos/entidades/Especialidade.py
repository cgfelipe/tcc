from django.db import models

# Entidade auxiliar


class Especialidade(models.Model):
    titulo = models.CharField(max_length=20)
