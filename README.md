**Instruções de Uso**
-

**Modelo da Api:**

{
    "nome":"Texto",
    "email":"Texto"
}

Inicie a api pelo app.py.

Todas as extensões utilizadas e instaladas estão no arquivo requirements.txt.

Foi utilizado um ambiente virtual (virtualenv) para realizar o desenvolvimento da API

**Para criar um usuário:**
* chame a rota: /usuarios/novo
* utilize o método POST

**Para listar todos os usuários:**
* chame a rota: /usuarios
* utilize o método GET

**Para listar um usuário especifíco:**
* chame a rota: /usuarios/ID*
* utilize o método GET

**Para atualizar um usuário:**
* chame a rota: /usuarios/ID*
* utilize o método PUT

**Para deletar um usuário:**
* chame a rota: /usuarios/ID*
* utilize o método DELETE

*ID deve ser um inteiro criado na rota "novo" correspondente ao "usuario_id"

#### Todos os testes foram realizados através do aplicativo Postman.
