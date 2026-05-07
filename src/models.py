from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Usuario(db.Model):
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

class Conexao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    livro_id_1 = db.Column(db.Integer, db.ForeignKey('livro.id'))
    livro_id_2 = db.Column(db.Integer, db.ForeignKey('livro.id'))
    peso = db.Column(db.Float, default=5.0) 