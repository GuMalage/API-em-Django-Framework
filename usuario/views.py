from django.shortcuts import render
from django.shortcuts import get_object_or_404
from usuario.models import Usuario
from usuario.forms import UsuarioForm
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

#def cadastrar_usuario_semForm(request):
#    if request.method == 'POST':
#        nome = request.POST.get("nome")
#        cpf = request.POST.get("cpf")
#        possuiEmprestimoAtivo = request.P
#        OST.get("possuiEmprestimoAtivo")
#        Usuario.objects.create(
#            nome=nome,
#            cpf=cpf,
#            possuiEmprestimoAtivo=possuiEmprestimoAtivo,
#        )

@csrf_exempt
def cadastrar_usuario(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        form = UsuarioForm(data)

        if form.is_valid():
            form.save()
            return JsonResponse({"msg": "Usuário criado com sucesso"})
        else:
            return JsonResponse({"erros": form.errors})

    return JsonResponse({"erro": "Método não permitido"})

@csrf_exempt
def atualizar_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)

    if request.method == 'PUT':
        data = json.loads(request.body)
        form = UsuarioForm(data, instance=usuario)
        if form.is_valid():
            form.save()
            return JsonResponse({"msg": "Usuario Atualizado com sucesso"})
    else:
       return JsonResponse({"erro": form.errors})
    
    return JsonResponse({"erro": "Método não permitido"})

@csrf_exempt  
def deletar_usuario(request, id):
    if request.method == "DELETE":
        usuario = get_object_or_404(Usuario, pk=id)
        usuario.delete()
        return JsonResponse({"msg": "Usuario deletado com sucesso"})
    
    return JsonResponse({"erro": "Método não permitido"})
    


def buscar_usuario_por_id(request, id):
    if request.method == "GET":
        usuario = get_object_or_404(Usuario, pk=id)
        return JsonResponse({
            "nome": usuario.nome,
            "cpf": usuario.cpf,
            "Status de Emprestimo": "Possui Emprestimo em Aberto" if usuario.possuiEmprestimoAtivo else "Usuário Apto a Emprestimo"
        })

def listar_usuarios(request):
     if request.method == "GET":
        usuario = Usuario.objects.all()
        
        data = []
        for usuario in usuario:
            data.append({
                "nome": usuario.nome,
                "cpf": usuario.cpf,
                "Status de Emprestimo": "Possui Emprestimo em Aberto" if usuario.possuiEmprestimoAtivo else "Usuário Apto a Emprestimo"
            })
        return JsonResponse(data, safe=False)
