from flask import Flask, jsonify, render_template
from models import db, Livro, Conexao, Usuario
from engine import obter_recomendacoes 
import os

app = Flask(__name__)
basedir= os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +os.path.join(basedir, '../data/database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def home():
    livros = Livro.query.all()
    return render_template('index.html', livros=livros)

@app.route('/livro/<int:id>')
def detalhes(id):
    livro_objeto = Livro.query.get_or_404(id)
    ids_recomendados = obter_recomendacoes(id)
    recomendados = Livro.query.filter(Livro.id.in_(ids_recomendados)).all()

    return render_template('detalhe.html', livro=livro_objeto, recomendados=recomendados)

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)