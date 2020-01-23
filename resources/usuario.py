from flask_restful import Resource, reqparse
from models.UsuarioModel import UsuarioModel


class Usuarios(Resource):
    # Lista todos os Usuarios cadastrados
    def get(self):
        return {'usuarios':[Usuario.json() for Usuario in UsuarioModel.query.all()]}

class Usuario(Resource):
    args = reqparse.RequestParser()
    args.add_argument('nome', type=str)
    args.add_argument('email')

    # Busca um usuário específico
    def get(self, usuario_id):
        usuario = UsuarioModel.buscar_usuario(usuario_id)
        if usuario:
            return usuario.json()
        return {'message':'Usuario ID({})  não encontrado'.format(usuario_id)}, 404

    # Atualiza um usuário passando os dados atualizados e o Id
    def put(self, usuario_id):
        dados = Usuario.args.parse_args()
        usuario_encontrado = UsuarioModel.buscar_usuario(usuario_id)
        if usuario_encontrado:
            usuario_encontrado.atualizar_usuario(**dados)
            usuario_encontrado.salvar_usuario()
            return usuario_encontrado.json(), 200
        usuario = UsuarioModel(usuario_id, **dados)
        try:
            usuario.salvar_usuario()
        except:
            return {'message': 'Erro ao tentar atualizar os dados'}
        return usuario.json(), 201

    def delete(self, usuario_id):
        usuario = UsuarioModel.buscar_usuario(usuario_id)
        if usuario:
            try:
                usuario.excluir_usuario()
            except:
                return {'message': 'Erro ao tentar deletar o usuário.'}
            return {'message': 'Usuario deletado'}
        return {'message' : 'Usuario ID[{}] não encontrado'.format(usuario_id)}, 404

class NovoUsuario(Resource):
    def post(self):
        atributos = reqparse.RequestParser()
        atributos.add_argument('nome', type=str, required=True, help="Este campo não pode ser deixado em branco")
        atributos.add_argument('email', type=str)
        dados = atributos.parse_args()
        usuario = UsuarioModel(**dados)
        try:
            usuario.salvar_usuario()
        except:
            return {'message':'Erro ao tentar cadastrar um usuário'}
        return {'message': 'Usuário criado com sucesso!'}, 201