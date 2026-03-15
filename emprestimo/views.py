from django.shortcuts import render
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from emprestimo.models import Emprestimo
from emprestimo.models import Devolucao
from livro.models import Livro
from usuario.models import Usuario
from emprestimo.forms import EmprestimoForm, DevolucaoForm
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse


@csrf_exempt
def cadastrar_emprestimo(request):
    if request.method == "POST":
        data = json.loads(request.body)

        livro = get_object_or_404(Livro, pk=data["livro"])
        usuario = get_object_or_404(Usuario, pk=data["usuario"])

        if usuario.possuiEmprestimoAtivo:
            return JsonResponse({"erro": "O usuário possui empréstimo ativo"})

        if livro.emUso:
            return JsonResponse({"erro": "O livro está em uso"})

        Emprestimo.objects.create(
            livro=livro,
            usuario=usuario,
            dataEmprestimo=data["dataEmprestimo"]
        )

        usuario.possuiEmprestimoAtivo = True
        usuario.save()

        livro.emUso = True
        livro.save()

        return JsonResponse({"msg": "Empréstimo cadastrado com sucesso"})

    return JsonResponse({"erro": "Método não permitido"})

@csrf_exempt
def cadastrar_devolucao(request):
    if request.method == "POST":
        data = json.loads(request.body)

        emprestimo = get_object_or_404(Emprestimo, pk=data["emprestimo"])

        usuario = emprestimo.usuario
        livro = emprestimo.livro 

      
        Devolucao.objects.create(
            emprestimo=emprestimo,
            dataDevolucao=data["datadevolucao"],
       )
            
        usuario.possuiEmprestimoAtivo = False
        usuario.save()

        livro.emUso = False
        livro.save()

        return JsonResponse({"msg": "Devoluçao registrada com sucesso"})

    return JsonResponse({"erro": "Método não permitido"})
            
        
def listar_emprestimos_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    emprestimos = usuario.emprestimos.all()

    data = []
    for e in emprestimos:
        data.append({
            "livro": e.livro.titulo,
            "dataEmprestimo": e.dataEmprestimo
        })

    return JsonResponse(data, safe=False)