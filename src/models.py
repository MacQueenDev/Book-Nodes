from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(300), nullable=False)

    def set_senha(self, senha):
        self.senha = generate_password_hash(senha)

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100))
    categoria = db.Column(db.String(50))  
    resumo = db.Column(db.Text)           
    foto_url = db.Column(db.String(500)) 
    preco = db.Column(db.Float, default=0.0)

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    livro_id = db.Column(db.Integer, db.ForeignKey('livro.id'), nullable=False)
    data_compra = db.Column(db.DateTime, default=db.func.current_timestamp())
    livro = db.relationship('Livro')

class Carrinho(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    livro_id = db.Column(db.Integer, db.ForeignKey('livro.id'), nullable=False)
    quantidade = db.Column(db.Integer, default=1)
    livro = db.relationship('Livro', backref='carrinhos')
    usuario = db.relationship('Usuario', backref='itens_carrinho')

class Conexao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    livro_id_1 = db.Column(db.Integer, db.ForeignKey('livro.id'))
    livro_id_2 = db.Column(db.Integer, db.ForeignKey('livro.id'))
    peso = db.Column(db.Float, default=5.0) 