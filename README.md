# 📚 Sistema de Emprestimo e Devolução de Livros - API Django

API desenvolvida em Django para gerenciamento de usuários, livros, empréstimos e devoluções.

---

## 🚀 Tecnologias

* Python
* Django
* JSON (requisições e respostas)

---

## 📌 Funcionalidades

* Cadastro, atualização, listagem e remoção de usuários
* Cadastro e gerenciamento de livros
* Controle de empréstimos e devoluções
* Regras de negócio:

  * Usuário não pode ter mais de um empréstimo ativo
  * Livro não pode ser emprestado se estiver em uso

---

## 🔗 Endpoints

### 🔐 Admin

* `/admin/` → Interface administrativa do Django

---

### 👤 Usuários

* `POST /cadastarUsuario` → Cadastrar usuário
* `PUT /atualizarUsuario/<int:id>` → Atualizar usuário
* `DELETE /deletarUsuario/<int:id>` → Deletar usuário
* `GET /listarUsuario` → Listar usuários
* `GET /buscarUsuarioId/<int:id>` → Buscar usuário por ID

---

### 📖 Livros

* `POST /cadastarLivro` → Cadastrar livro
* `PUT /atualizarLivro/<int:id>` → Atualizar livro
* `DELETE /deletarLivro/<int:id>` → Deletar livro
* `GET /listarLivros` → Listar livros
* `GET /buscarLivorsId/<int:id>` → Buscar livro por ID

---

### 🔄 Empréstimos e Devoluções

* `POST /cadastrarEmprestimo` → Realizar empréstimo
* `POST /cadastrarDevolucao` → Registrar devolução
* `GET /listarEmprestimosUsuario/<int:id>` → Listar empréstimos de um usuário


## ⚠️ Observações

* A API utiliza JSON para entrada e saída de dados
* Métodos HTTP utilizados:

  * GET → consulta
  * POST → criação
  * PUT → atualização
  * DELETE → remoção
* Algumas rotas utilizam `csrf_exempt` (apenas para testes)

---

## ▶️ Como executar

```bash
python manage.py runserver
```

Guia Rápido Para a Utilização do Framework: https://docs.google.com/document/d/1Zn5os1ZFLASyINd9qBTltfDMLiGPeVHlBUuRzQv_7To/edit?tab=t.0#heading=h.exe6o94nstt0
Apresentação do Projeto: https://docs.google.com/presentation/d/1MFuuOrB8OvQtlDtJ7PpMW8qeS_WE7ggYAqWTQ7WqbPI/edit?usp=sharing
