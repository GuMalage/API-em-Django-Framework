"""
URL configuration for biblioteca_pontoPena project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usuario import views as vu
from livro import views as vl
from emprestimo import views as ve

urlpatterns = [
    path('admin/', admin.site.urls),

    path('cadastrarUsuario/', vu.cadastrar_usuario_semForm),
    path('cadastarUsuario/', vu.cadastrar_usuario),
    path('deletarUsuario/', vu.deletar_usuario),
    path('atualizarUsuario/', vu.atualizar_usuario),
    path('listarUsuario/', vu.listar_usuarios),
    path('buscarUsuarioId/', vu.buscar_usuario_por_id),

    path('cadastrarLivroForm', vl.cadastrar_livro_semForm),
    path('cadastarLivro/', vl.cadastrar_livro),
    path('deletarLivro/', vl.deletar_livro),
    path('atualizarLivro/', vl.atualizar_livro),
    path('listarLivros/', vl.listar_livros),
    path('buscarLivorsId/', vl.buscar_livro_por_id),

    path('cadastrarEmprestimo/', ve.cadastrar_emprestimo),
    path('cadastrarDevolucao/', ve.cadastrar_devolucao),
    path('listarEmprestimosUsuario/', ve.listar_emprestimos_usuario)
]
