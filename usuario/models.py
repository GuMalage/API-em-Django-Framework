from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    possuiEmprestimoAtivo = models.BooleanField(default=False)