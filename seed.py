from src.app import app
from src.models import db, Livro, Conexao

def popular():
    with app.app_context():
        # 1. Cria as tabelas no SQLite
        db.create_all()
        
        # 2. Limpa dados antigos (bom para testes)
        Conexao.query.delete()
        Livro.query.delete()

        # 3. Adiciona Livros
        l1 = Livro(titulo="O Cortiço", autor="Aluísio Azevedo", categoria="Clássico", 
                   resumo="Um estudo sobre o naturalismo no Brasil.", 
                   foto_url="https://link_da_foto.com/foto.jpg", preco=29.90)
        
        l2 = Livro(titulo="Dom Casmurro", autor="Machado de Assis", categoria="Clássico", 
                   resumo="A dúvida de Bentinho.", 
                   foto_url="https://link_da_foto.com/foto2.jpg", preco=35.00)

        db.session.add_all([l1, l2])
        db.session.commit()

        # 4. Adiciona Conexão para o Dijkstra (Livro 1 ligado ao 2 com peso baixo)
        c1 = Conexao(livro_origem_id=l1.id, livro_destino_id=l2.id, peso=1.0)
        db.session.add(c1)
        db.session.commit()
        
        print("✅ Banco de dados populado com sucesso!")

if __name__ == "__main__":
    popular()