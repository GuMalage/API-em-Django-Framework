from django.shortcuts import get_object_or_404
from usuario.models import Usuario
from usuario.forms import UsuarioForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET, require_http_methods
import json
from django.http import JsonResponse


@csrf_exempt
@require_POST
def cadastrar_usuario(request):
    data = json.loads(request.body)
    form = UsuarioForm(data)

    if form.is_valid():
        usuario = form.save()
        return JsonResponse({
            "Nome": usuario.nome,
            "Cpf": usuario.cpf
        })
    else:
        return JsonResponse({"erros": form.errors}, status=400)


@csrf_exempt
@require_http_methods(["PUT"])
def atualizar_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    data = json.loads(request.body)
    form = UsuarioForm(data, instance=usuario)

    if form.is_valid():
        form.save()
        return JsonResponse({
            "Nome": usuario.nome,
            "Cpf": usuario.cpf
        })
    else:
        return JsonResponse({"erros": form.errors}, status=400)


@csrf_exempt
@require_http_methods(["DELETE"])
def deletar_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    usuario.delete()
    return JsonResponse({"msg": "Usuario deletado com sucesso"})


@require_GET
def buscar_usuario_por_id(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    return JsonResponse({
        "nome": usuario.nome,
        "cpf": usuario.cpf,
        "Status de Emprestimo": "Possui Emprestimo em Aberto" if usuario.possuiEmprestimoAtivo else "Usuário Apto a Emprestimo"
    })


@require_GET
def listar_usuarios(request):
    usuarios = Usuario.objects.all()

    data = []
    for usuario in usuarios:
        data.append({
            "nome": usuario.nome,
            "cpf": usuario.cpf,
            "Status de Emprestimo": "Possui Emprestimo em Aberto" if usuario.possuiEmprestimoAtivo else "Usuário Apto a Emprestimo"
        })

    return JsonResponse(data, safe=False)