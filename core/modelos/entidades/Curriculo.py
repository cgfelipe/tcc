from django.db import models


class Curriculo(models.Model):
    objetivo = models.CharField(max_lenght=500)
