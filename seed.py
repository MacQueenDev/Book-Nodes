import sys
import os
from werkzeug.security import generate_password_hash
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from app import app
from models import db, Livro, Conexao, Usuario

def popular():
    with app.app_context():      
        print("Limpando banco...")
        db.drop_all()
        db.create_all()
        
        print("Criando usuário Admin...")
        senha_criptografada = generate_password_hash("123")
        admin = Usuario(nome="admin", email="admin@email.com", senha=senha_criptografada)
        db.session.add(admin)
        db.session.commit()
    
      
        dados_reais = [
            {"autor": "J.R.R. Tolkien", "cat": "Fantasia", "livros": ["O Hobbit", "A Sociedade do Anel", "As Duas Torres", "O Retorno do Rei", "Os Filhos de Húrin"]},
            {"autor": "J.R.R. Tolkien", "cat": "Mitologia", "livros": ["O Silmarillion", "Beren e Lúthien", "A Queda de Gondolin"]},
            {"autor": "J.K. Rowling", "cat": "Fantasia", "livros": ["Harry Potter e a Pedra Filosofal", "Harry Potter e a Câmara Secreta", "Harry Potter e o Prisioneiro de Azkaban", "Harry Potter e o Cálice de Fogo", "Harry Potter e a Ordem da Fênix", "Harry Potter e o Enigma do Príncipe", "Harry Potter e as Relíquias da Morte"]},
            {"autor": "J.K. Rowling", "cat": "Suspense", "livros": ["O Chamado do Cuco", "O Bicho-da-Seda", "Vocação para o Mal"]},
            {"autor": "Stephen King", "cat": "Terror", "livros": ["It: A Coisa", "O Iluminado", "Carrie", "O Cemitério", "Misery", "Doutor Sono"]},
            {"autor": "Stephen King", "cat": "Suspense", "livros": ["Mr. Mercedes", "Achados e Perdidos", "O Último Turno", "Joyland"]},
            {"autor": "Agatha Christie", "cat": "Suspense", "livros": ["E Não Sobrou Nenhum", "O Assassinato no Expresso Oriente", "Morte no Nilo", "A Noite das Bruxas", "O Assassinato de Roger Ackroyd"]},
            {"autor": "George R.R. Martin", "cat": "Fantasia", "livros": ["A Guerra dos Tronos", "A Fúria dos Reis", "A Tormenta de Espadas", "O Festim dos Corvos", "A Dança dos Dragões", "Fogo e Sangue"]},
            {"autor": "Isaac Asimov", "cat": "Ficção Científica", "livros": ["Fundação", "Fundação e Império", "Segunda Fundação", "Eu, Robô", "Os Próprios Deuses", "O Fim da Eternidade"]},
            {"autor": "Arthur Conan Doyle", "cat": "Suspense", "livros": ["Um Estudo em Vermelho", "O Signo dos Quatro", "O Cão dos Baskerville", "O Vale do Medo", "As Aventuras de Sherlock Holmes"]},
            {"autor": "Dan Brown", "cat": "Suspense", "livros": ["O Código Da Vinci", "Anjos e Demônios", "O Símbolo Perdido", "Inferno", "Origem", "Fortaleza Digital"]},
            {"autor": "H.P. Lovecraft", "cat": "Terror", "livros": ["O Chamado de Cthulhu", "Nas Montanhas da Loucura", "A Sombra sobre Innsmouth", "O Horror de Dunwich"]},
            {"autor": "Rick Riordan", "cat": "Fantasia", "livros": ["O Ladrão de Raios", "O Mar de Monstros", "A Maldição do Titã", "A Batalha do Labirinto", "O Último Olimpiano"]},
            {"autor": "C.S. Lewis", "cat": "Fantasia", "livros": ["O Leão, a Feiticeira e o Guarda-Roupa", "Príncipe Caspian", "A Viagem do Peregrino da Alvorada", "A Cadeira de Prata"]},
            {"autor": "Frank Herbert", "cat": "Ficção Científica", "livros": ["Duna", "Messias de Duna", "Filhos de Duna", "Imperador Deus de Duna"]},
            {"autor": "Neil Gaiman", "cat": "Fantasia", "livros": ["American Gods", "Lugar Nenhum", "Coraline", "O Oceano no Fim do Caminho"]},
            {"autor": "Harlan Coben", "cat": "Suspense", "livros": ["Não Conte a Ninguém", "O Inocente", "A Promessa", "Fique Comigo", "Seis Anos Depois"]},
            {"autor": "Bram Stoker", "cat": "Terror", "livros": ["Drácula", "O Convidado de Drácula", "A Jóia das Sete Estrelas"]}
        ]

        
        print("Cadastrando 100 livros reais...")
        total = 0
        for grupo in dados_reais:
            for titulo in grupo["livros"]:
                if total >= 100: break
                novo = Livro(
                    titulo=titulo,
                    autor=grupo["autor"],
                    categoria=grupo["cat"],
                    preco=round(39.90 + (total % 10), 2),
                    resumo=f"Uma obra clássica de {grupo['autor']} que redefine o gênero {grupo['cat']}.",
                    foto_url="https://via.placeholder.com/300x450?text=Capa+Livro" # Usando placeholder para garantir que carrega
                )
                db.session.add(novo)
                total += 1
        
        db.session.commit()

            # arestas
        print("Construindo conexões (Dijkstra-ready)...")
        livros = Livro.query.all()
        for i in range(len(livros)):
            for j in range(i + 1, len(livros)):
                l1, l2 = livros[i], livros[j]
                peso = None
                
                if l1.autor == l2.autor and l1.categoria == l2.categoria:
                    peso = 0.5
                elif l1.autor == l2.autor:
                    peso = 1.0
                elif l1.categoria == l2.categoria:
                    peso = 2.0
                
                if peso:
                    db.session.add(Conexao(livro_id_1=l1.id, livro_id_2=l2.id, peso=peso))
            
            if i % 10 == 0: db.session.commit()

        db.session.commit()
        print(f"Sucesso! {total} livros reais cadastrados.")

if __name__ == "__main__":
    popular()