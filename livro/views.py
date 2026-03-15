from django.shortcuts import render
from django.shortcuts import get_object_or_404
from livro.models import Livro
from livro.forms import LivroForm

def cadastrar_livro_semForm(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        autor = request.POST.get("preco")
        genero = request.POST.get("genero")
        emUso = request.POST.get("emUso")

        Livro.objects.create(
            titulo=titulo,
            autor=autor,
            genero=genero,
            emUso=emUso,
        )

def cadastrar_livro(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save
            return()
        else:
            form = LivroForm()

def atualizar_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)

    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return ()
    else:
        form = LivroForm(instance=livro)

def deletar_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    livro.delete()

def buscar_livro_por_id(request, id):
    livro = get_object_or_404(Livro, pk=id)

def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, "livros.html", {"livros": livros})
