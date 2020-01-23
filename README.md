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

**Para listar todos os usuários:**
* chame a rota: /usuarios

**Para listar um usuário especifíco:**
* chame a rota: /usuarios/ID*

**Para atualizar um usuário:**
* chame a rota: /usuarios/ID*

**Para deletar um usuário:**
* chame a rota: /usuarios/ID*

*ID deve ser um inteiro criado na rota "novo" correspondente ao "usuario_id"

#### Todos os testes foram realizados através do aplicativo Postman.