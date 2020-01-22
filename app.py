from flask import Flask
from flask_restful import Api
from resources.usuario import Usuarios, Usuario, NovoUsuario

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def db():
    db.create_all()

api.add_resource(Usuarios, '/usuarios')
api.add_resource(Usuario, '/usuarios/<int:usuario_id>')
api.add_resource(NovoUsuario, '/usuarios/novo')


if __name__ == '__main__':
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)