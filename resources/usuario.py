from flask_restful import Resource, reqparse
from models.UsuarioModel import UsuarioModel


class Usuarios(Resource):
    def get(self):
        return {'usuarios':[Usuario.json() for Usuario in UsuarioModel.query.all()]}

class Usuario(Resource):
    args = reqparse.RequestParser()
    args.add_argument('nome', type=str, required=True, help="Esse 'nome' não pode ser deixado em branco")
    args.add_argument('email')

    def get(self, usuario_id):
        usuario = UsuarioModel.buscar_usuario(usuario_id)
        if usuario:
            return usuario.json()
        return {'message':'Usuario ID({})  não encontrado'.format(usuario_id)}, 404

    '''def post(self, usuario_id):
        if UsuarioModel.buscar_usuario(usuario_id):
            return {'message': 'Usuario id {} já existe'.format(usuario_id)}, 400
        dados = Usuario.args.parse_args()
        usuario = UsuarioModel(usuario_id, **dados)
        try:
            usuario.salvar_usuario()
        except:
            return {'message': 'Erro no servidor ao tentar salvar Usuario'}, 500
        return usuario.json()'''

    def put(self, usuario_id):
        dados = Usuario.args.parse_args()
        usuario_encontrado = UsuarioModel.buscar_usuario(usuario_id)
        if usuario_encontrado:
            usuario_encontrado.atualizar_usuario(**dados)
            usuario_encontrado.salvar_usuario()
            return usuario_encontrado.json(), 200
        usuario = UsuarioModel(usuario_id, **dados)
        usuario.salvar_usuario()
        return usuario.json(), 201

    def delete(self, usuario_id):
        usuario = UsuarioModel.buscar_usuario(usuario_id)
        if usuario:
            usuario.excluir_usuario()
            return {'message': 'Usuario deletado'}
        return {'message' : 'Usuario não encontrado'}, 404

class NovoUsuario(Resource):
    def post(self):
        atributos = reqparse.RequestParser()
        atributos.add_argument('nome', type=str)
        atributos.add_argument('email', type=str)
        dados = atributos.parse_args()
        usuario = UsuarioModel(**dados)
        usuario.salvar_usuario()
        return {'message': 'Usuário criado com sucesso!'}, 201