from django.shortcuts import render
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from .models import Emprestimo
from .models import Devolucao
from livro.models import Livro
from usuario.models import Usuario

def cadastrar_emprestimo(request):
    if request.method == "POST":
        livro_id = request.POST.get("titulo")
        usuario_id = request.POST.get("preco")
        dataEmprestimo = request.POST.get("dataEmprestimo")

        livro = get_object_or_404(Livro, pk=livro_id)
        usuario = get_object_or_404(Usuario, pk=usuario_id)

        if usuario.possuiEmprestimoAtivo == True:
            return("O usuario possui emprestimo ativo!")
        
        if livro.emUso == True:
            return("O livro está em uso:(")

        try:
            Emprestimo.objects.create(
                livro=livro,
                usuario=usuario,
                dataEmprestimo=dataEmprestimo,
            )
            usuario.possuiEmprestimoAtivo = True
            usuario.save()
            livro.emUso = True
            livro.save()
            return()
        except:
            return()

def cadastrar_devolucao(request):
    if request.method == "POST":
        emprestimo_id = request.POST.get("emprestimo")
        dataDevolucao = request.POST.get("dataDevolucao")
            
        emprestimo = get_object_or_404(Emprestimo, pk=emprestimo_id)

        usuario = emprestimo.usuario
        livro = emprestimo.livro 

        try:
            Devolucao.objects.create(
                emprestimo=emprestimo,
                dataDevolucao=dataDevolucao,
            )
            usuario.possuiEmprestimoAtivo = False
            usuario.save()

            livro.emUso = False
            livro.save()
            return()
        except:
            return()
        
def listar_emprestimos_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    return usuario.emprestimo.all()