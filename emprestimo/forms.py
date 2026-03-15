from django import forms
from emprestimo.models import Emprestimo
from emprestimo.models import Devolucao

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo 
        fields = ['livro', 'usuario', 'dataEmprestimo']

class DevolucaoForm(forms.ModelForm):
    class Meta:  
        model = Devolucao
        fields = ['emprestimo', 'dataDevolucao']