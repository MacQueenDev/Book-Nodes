import networkx as nx
from .models import Conexao

def obter_recomendacoes(livro_id):
    G = nx.Graph()
    
    conexoes = Conexao.query.all()
    for c in conexoes:
        G.add_edge(c.livro_origem_id, c.livro_destino_id, weight=c.peso)
    
    try:
        distancias, caminhos = nx.single_source_dijkstra(G, source=livro_id)
        
        recomendados = sorted(distancias.items(), key=lambda x: x[1])[1:4]
        return [item[0] for item in recomendados]
    except:
        return [] 