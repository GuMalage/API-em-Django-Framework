from django.contrib import admin
from django.urls import path
from usuario import views as vu
from livro import views as vl
from emprestimo import views as ve

urlpatterns = [
    path('admin/', admin.site.urls),

    #path('cadastrarUsuarioForm/', vu.cadastrar_usuario_semForm),
    path('cadastarUsuario/', vu.cadastrar_usuario),
    path('deletarUsuario/', vu.deletar_usuario),
    path('atualizarUsuario/', vu.atualizar_usuario),
    path('listarUsuario/', vu.listar_usuarios),
    path('buscarUsuarioId/', vu.buscar_usuario_por_id),

    #path('cadastrarLivroForm', vl.cadastrar_livro_semForm),
    path('cadastarLivro/', vl.cadastrar_livro),
    path('deletarLivro/', vl.deletar_livro),
    path('atualizarLivro/', vl.atualizar_livro),
    path('listarLivros/', vl.listar_livros),
    path('buscarLivorsId/', vl.buscar_livro_por_id),

    path('cadastrarEmprestimo/', ve.cadastrar_emprestimo),
    path('cadastrarDevolucao/', ve.cadastrar_devolucao),
    path('listarEmprestimosUsuario/', ve.listar_emprestimos_usuario)
]
