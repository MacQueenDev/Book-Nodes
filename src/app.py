from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Livro, Conexao, Usuario, Carrinho, Compra
from engine import obter_recomendacoes 
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'andrea'

basedir= os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +os.path.join(basedir, '../data/database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' 

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))


@app.route('/')
def home():
    livros = Livro.query.all()
    return render_template('index.html', livros=livros)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha_digitada = request.form.get('senha')
        
        user = Usuario.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.senha, senha_digitada):
            login_user(user)
            flash('Logado com sucesso!', 'success')
            return redirect(url_for('home'))
        
        flash('E-mail ou senha inválidos.', 'danger')
    return render_template('login.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        
        if Usuario.query.filter_by(email=email).first():
            flash('Este e-mail já está cadastrado.', 'danger')
            return redirect(url_for('login')) 
        
        novo_usuario = Usuario(
            nome=nome,
            email=email,
            senha=generate_password_hash(senha)
        )
        db.session.add(novo_usuario)
        db.session.commit()

        login_user(novo_usuario)
        flash('Conta criada com sucesso!', 'success')
        return redirect(url_for('home'))
    
    return redirect(url_for('login')) 


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/livro/<int:id>')
def detalhes(id):
    livro_objeto = Livro.query.get_or_404(id)
    ids_recomendados = obter_recomendacoes(id)
    recomendados = Livro.query.filter(Livro.id.in_(ids_recomendados)).all()
    return render_template('detalhe.html', livro=livro_objeto, recomendados=recomendados)


@app.route('/perfil')
@login_required
def perfil():
    compras = Compra.query.filter_by(usuario_id=current_user.id).all()
    return render_template('perfil.html')


@app.route('/carrinho')
@login_required
def carrinho():
    itens = Carrinho.query.filter_by(usuario_id=current_user.id).all()
    total = sum(item.livro.preco * item.quantidade for item in itens)
    return render_template('carrinho.html', itens=itens, total=total)
 

@app.route('/adicionar_carrinho/<int:livro_id>')
@login_required
def adicionar_carrinho(livro_id):
    item_existente = Carrinho.query.filter_by(
        usuario_id=current_user.id, 
        livro_id=livro_id
    ).first()

    if item_existente:
        item_existente.quantidade += 1
    else:
        novo_item = Carrinho(usuario_id=current_user.id, livro_id=livro_id)
        db.session.add(novo_item)
    
    db.session.commit()
    flash('Livro adicionado ao carrinho!', 'success')
    return redirect(url_for('home'))


@app.route('/finalizar_compra', methods=['POST'])
@login_required
def finalizar_compra():
    itens = Carrinho.query.filter_by(usuario_id=current_user.id).all()  
    if not itens:
        flash("Carrinho vazio!", "warning")
        return redirect(url_for('home'))

    for item in itens:

        print(f"Adicionando peso para o livro {item.livro.id} no perfil do usuário {current_user.id}")
        
        db.session.delete(item)

    db.session.commit()
    
    flash("Compra simulada com sucesso! Seu perfil de recomendações foi atualizado.", "success")
    return redirect(url_for('home'))

if __name__ == '__main__':   
    app.run(debug=True)