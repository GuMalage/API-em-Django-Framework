from django.db import models
from usuario.models import Usuario
from livro.models import Livro

class Emprestimo(models.Model):
    livro = models.ForeignKey(
        Livro,
        on_delete=models.CASCADE,
        related_name="emprestimos"
    )
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name="emprestimos"
    )
    dataEmprestimo = models.DateField()

class Devolucao(models.Model):
    emprestimo = models.ForeignKey(
        "emprestimo.Emprestimo",
        on_delete=models.CASCADE
    )
    dataDevolucao = models.DateField()