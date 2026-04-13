from django.shortcuts import get_object_or_404
from emprestimo.models import Emprestimo, Devolucao
from livro.models import Livro
from usuario.models import Usuario
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json
from django.http import JsonResponse


@csrf_exempt
@require_POST
def cadastrar_emprestimo(request):
    data = json.loads(request.body)

    livro = get_object_or_404(Livro, pk=data["livro"])
    usuario = get_object_or_404(Usuario, pk=data["usuario"])

    if usuario.possuiEmprestimoAtivo:
        return JsonResponse({"erro": "O usuário possui empréstimo ativo"}, status=400)

    if livro.emUso:
        return JsonResponse({"erro": "O livro está em uso"}, status=400)

    emprestimo = Emprestimo.objects.create(
        livro=livro,
        usuario=usuario,
        dataEmprestimo=data["dataEmprestimo"]
    )

    usuario.possuiEmprestimoAtivo = True
    usuario.save()

    livro.emUso = True
    livro.save()

    return JsonResponse({
        "Usuario": usuario.nome,
        "Livro Emprestado": livro.titulo,
        "Data do Emprestimo": emprestimo.dataEmprestimo
    })


@csrf_exempt
@require_POST
def cadastrar_devolucao(request):
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

    return JsonResponse({
        "Usuario": usuario.nome,
        "Livro Devolvido": livro.titulo,
        "Data da Devolução": devolucao.dataDevolucao
    })


@require_GET
def listar_emprestimos_usuario(id):
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