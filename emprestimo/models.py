from django.db import models

from usuario.models import Usuario

class Emprestimo (models.Model):
    livro = models.ForeignKey("livro.Livro", on_delete=models.CASCADE)
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name="emprestimo"
    )
    dataEmprestimo = models.DateField()
    
class Devolucao(models.Model):
    emprestimo = models.ForeignKey("emprestimo.Emprestimo", on_delete=models.CASCADE)
    dataDevolucao = models.DateField()



