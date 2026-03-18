from django.shortcuts import render
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from emprestimo.models import Emprestimo
from emprestimo.models import Devolucao
from livro.models import Livro
from usuario.models import Usuario
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

        emprestimo = Emprestimo.objects.create(
            livro=livro,
            usuario=usuario,
            dataEmprestimo=data["dataEmprestimo"]
        )

        usuario.possuiEmprestimoAtivo = True
        usuario.save()

        livro.emUso = True
        livro.save()

        response_data = {
            "Usuario": usuario.nome,
            "Livro Emprestado": livro.titulo,
            "Data do Emprestimo": emprestimo.dataEmprestimo
        }


        return JsonResponse(response_data, safe=False)

    return JsonResponse({"erro": "Método não permitido"})

@csrf_exempt
def cadastrar_devolucao(request):
    if request.method == "POST":
        data = json.loads(request.body)

        emprestimo = get_object_or_404(Emprestimo, pk=data["emprestimo"])

        if Devolucao.objects.filter(emprestimo=emprestimo).exists():
            return JsonResponse({"erro": "Este empréstimo já foi devolvido"}, status=400)

        usuario = emprestimo.usuario
        livro = emprestimo.livro

        devolucao = Devolucao.objects.create(
            emprestimo=emprestimo,
            dataDevolucao=data["dataDevolucao"],
        )

        usuario.possuiEmprestimoAtivo = False
        usuario.save()

        livro.emUso = False
        livro.save()

        response_data = {
            "Usuario": usuario.nome,
            "Livro Devolvido": livro.titulo,
            "Data da Devolução": devolucao.dataDevolucao
        }

        return JsonResponse(response_data, safe=False)

    return JsonResponse({"erro": "Método não permitido"}, status=405)
            
        
def listar_emprestimos_usuario(request, id):
    if request.method == "GET":
        usuario = get_object_or_404(Usuario, pk=id)
        emprestimos = usuario.emprestimos.all()

        response_data = []
        for e in emprestimos:

            devolucao = Devolucao.objects.filter(emprestimo=e).first()

            response_data.append({
                "livro": e.livro.titulo,
                "Data do Emprestimo": e.dataEmprestimo,
                "Data de Devolucao": devolucao.dataDevolucao if devolucao else "Empréstimo ativo"
            })

        return JsonResponse(response_data, safe=False)

    return JsonResponse({"erro": "Método não permitido"}, status=405)