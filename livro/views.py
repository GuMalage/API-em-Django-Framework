from django.shortcuts import render
from django.shortcuts import get_object_or_404
from livro.models import Livro
from livro.forms import LivroForm
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse


#def cadastrar_livro_semForm(request):
#    if request.method == "POST":
#        titulo = request.POST.get("titulo")
#        autor = request.POST.get("preco")
#        genero = request.POST.get("genero")
#        emUso = request.POST.get("emUso")
#        Livro.objects.create(
#            titulo=titulo,
#            autor=autor,
#            genero=genero,
#            emUso=emUso,
#        )

@csrf_exempt
def cadastrar_livro(request):
    if request.method == "POST":
        data = json.loads(request.body)
        form = LivroForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({"msg": "Livro Cadastrado com sucesso"})
        else:
            return JsonResponse({"erro": form.errors})
    
    return JsonResponse({"erro": "Método não permitido"})

@csrf_exempt
def atualizar_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)

    if request.method == 'POST':
        data = json.loads(request.body)
        form = LivroForm(data, instance=livro)
        if form.is_valid():
            form.save()
            return JsonResponse({"msg": "Usuario Atualizado com sucesso"})
    else:
        return JsonResponse({"erros": form.errors})

    return JsonResponse({"erro": "Método não permitido"})

def deletar_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    if livro != 404:
        livro.delete()
        return JsonResponse({"msg": "Usuário deletado com sucesso"})
    else:
        return JsonResponse({"msg": "Usuário não encontrado"})


def buscar_livro_por_id(request, id):
    livro = get_object_or_404(Livro, pk=id)
    return JsonResponse({
        "titulo": livro.titulo,
        "autor": livro.autor,
        "genero": livro.genero,
        "Status": "Emprestado" if livro.emUso else "Disponível",
    })

def listar_livros(request):
    livros = Livro.objects.all()

    data = []
    for livro in livros:
        data.append({
            "titulo": livro.titulo,
            "autor": livro.autor
        })

    return JsonResponse(data, safe=False)
