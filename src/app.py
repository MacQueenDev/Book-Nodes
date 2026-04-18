from flask import Flask, jsonify    
from .models import db, Livro, Conexao
from .engine import obter_recomendacoes 
import os

app = Flask(__name__)
basedir= os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +os.path.join(basedir, '../data/database.db')
db.init_app(app)

@app.route('/')
def home():
    return "" \
    "MVP Book-Nodes Rodando !, acesse /teste-grafo para ver a recomendação."

@app.route('/teste-grafo')
def teste():
    recs = obter_recomendacoes(1)
    return jsonify({"livro_visto": 1, "recomendados_pelo_dijkstra": recs})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)