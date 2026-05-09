import sys
from pathlib import Path
from types import SimpleNamespace

# Permite que o pytest encontre os arquivos dentro da pasta src
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

import engine


# Testa o caso base do Dijkstra:
# verifica se o algoritmo recomenda os livros pela menor distância.
def test_dijkstra_caso_base(monkeypatch):
    conexoes_fake = [
        SimpleNamespace(livro_id_1=1, livro_id_2=2, peso=1),
        SimpleNamespace(livro_id_1=1, livro_id_2=3, peso=5),
        SimpleNamespace(livro_id_1=2, livro_id_2=3, peso=1),
    ]

    query_fake = SimpleNamespace(all=lambda: conexoes_fake)
    conexao_fake = SimpleNamespace(query=query_fake)

    monkeypatch.setattr(engine, "Conexao", conexao_fake)

    resultado = engine.obter_recomendacoes(livro_id_inicial=1)

    assert resultado == [2, 3]


# Testa o grafo vazio:
# verifica se o algoritmo retorna lista vazia quando não há conexões.
def test_dijkstra_grafo_vazio(monkeypatch):
    conexoes_fake = []

    query_fake = SimpleNamespace(all=lambda: conexoes_fake)
    conexao_fake = SimpleNamespace(query=query_fake)

    monkeypatch.setattr(engine, "Conexao", conexao_fake)

    resultado = engine.obter_recomendacoes(livro_id_inicial=1)

    assert resultado == []


# Testa o grafo completo:
# verifica se o algoritmo funciona quando todos os livros estão conectados.
def test_dijkstra_grafo_completo(monkeypatch):
    conexoes_fake = [
        SimpleNamespace(livro_id_1=1, livro_id_2=2, peso=1),
        SimpleNamespace(livro_id_1=1, livro_id_2=3, peso=2),
        SimpleNamespace(livro_id_1=1, livro_id_2=4, peso=3),
        SimpleNamespace(livro_id_1=2, livro_id_2=3, peso=4),
        SimpleNamespace(livro_id_1=2, livro_id_2=4, peso=5),
        SimpleNamespace(livro_id_1=3, livro_id_2=4, peso=6),
    ]

    query_fake = SimpleNamespace(all=lambda: conexoes_fake)
    conexao_fake = SimpleNamespace(query=query_fake)

    monkeypatch.setattr(engine, "Conexao", conexao_fake)

    resultado = engine.obter_recomendacoes(livro_id_inicial=1)

    assert resultado == [2, 3, 4]