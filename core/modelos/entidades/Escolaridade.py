from django.db import models

# Entidade auxiliar


class Escolaridade(models.Model):
    titulo = models.CharField(max_length=20)
