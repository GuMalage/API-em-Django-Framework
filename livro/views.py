from django.shortcuts import get_object_or_404
from livro.models import Livro
from livro.forms import LivroForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_http_methods, require_GET
import json
from django.http import JsonResponse


@csrf_exempt
@require_POST
def cadastrar_livro(request):
    data = json.loads(request.body)
    form = LivroForm(data)

    if form.is_valid():
        livro = form.save()
        return JsonResponse({
            "Titulo": livro.titulo,
            "Autor": livro.autor,
            "Genero": livro.genero
        })
    else:
        return JsonResponse({"erro": form.errors}, status=400)


@csrf_exempt
@require_http_methods(["PUT"])
def atualizar_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    data = json.loads(request.body)
    form = LivroForm(data, instance=livro)

    if form.is_valid():
        form.save()
        return JsonResponse({
            "Titulo": livro.titulo,
            "Autor": livro.autor,
            "Genero": livro.genero
        })
    else:
        return JsonResponse({"erros": form.errors}, status=400)


@csrf_exempt
@require_http_methods(["DELETE"])
def deletar_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    livro.delete()
    return JsonResponse({"msg": "Livro deletado com sucesso"})


@require_GET
def buscar_livro_por_id(request, id):
    livro = get_object_or_404(Livro, pk=id)
    return JsonResponse({
        "titulo": livro.titulo,
        "autor": livro.autor,
        "genero": livro.genero,
        "Status": "Emprestado" if livro.emUso else "Disponível",
    })


@require_GET
def listar_livros(request):
    livros = Livro.objects.all()

    data = []
    for livro in livros:
        data.append({
            "titulo": livro.titulo,
            "autor": livro.autor,
            "genero": livro.genero,
            "Status": "Emprestado" if livro.emUso else "Disponível",
        })

    return JsonResponse(data, safe=False)