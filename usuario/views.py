from django.shortcuts import render
from django.shortcuts import get_object_or_404
from usuario.models import Usuario
from usuario.forms import UsuarioForm
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

def cadastrar_usuario_semForm(request):
    if request.method == 'POST':
        nome = request.POST.get("nome")
        cpf = request.POST.get("cpf")
        possuiEmprestimoAtivo = request.P
        OST.get("possuiEmprestimoAtivo")

        Usuario.objects.create(
            nome=nome,
            cpf=cpf,
            possuiEmprestimoAtivo=possuiEmprestimoAtivo,
        )

@csrf_exempt
def cadastrar_usuario(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        form = UsuarioForm(data)

        if form.is_valid():
            form.save()
            return JsonResponse({"msg": "Usuário criado"})
        else:
            return JsonResponse({"erros": form.errors})

    return JsonResponse({"erro": "Método não permitido"})

def atualizar_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return ()
    else:
        form = UsuarioForm(instance=usuario)

def deletar_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    usuario.delete()

def buscar_usuario_por_id(request, id):
    usuario = get_object_or_404(Usuario, pk=id)

def listar_usuarios(request):
    usuario = Usuario.objects.all()
    return render(request, "usuario.html", {"usuarios": usuario})
