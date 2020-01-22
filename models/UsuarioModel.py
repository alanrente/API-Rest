from sql_alchemy import db

class UsuarioModel(db.Model):
    __tablename__ = 'usuarios'

    usuario_id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120))
    email = db.Column(db.String(50))

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def json(self):
        return {
            'usuario_id': self.usuario_id,
            'nome': self.nome,
            'email':self.email
        }

    @classmethod
    def buscar_usuario(cls, usuario_id):
        usuario = cls.query.filter_by(usuario_id=usuario_id).first()
        if usuario:
            return usuario
        return None

    def salvar_usuario(self):
        db.session.add(self)
        db.session.commit()

    def atualizar_usuario(self, nome, email):
        self.nome = nome
        self.email = email

    def excluir_usuario(self):
        db.session.delete(self)
        db.session.commit()
