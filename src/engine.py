from models import Conexao

def obter_recomendacoes(livro_id_inicial):
    conexoes = Conexao.query.all()
    grafo = {}
    
    for c in conexoes:
        if c.livro_id_1 not in grafo: grafo[c.livro_id_1] = {}
        if c.livro_id_2 not in grafo: grafo[c.livro_id_2] = {}
        grafo[c.livro_id_1][c.livro_id_2] = c.peso
        grafo[c.livro_id_2][c.livro_id_1] = c.peso

    if livro_id_inicial not in grafo:
        return []
    
    distancias = {no: float('infinity') for no in grafo}
    distancias[livro_id_inicial] = 0 
    visitados = set()

    while len(visitados) < len(grafo):
        no_atual = None
        for no in grafo:
            if no not in visitados:
                if no_atual is None or distancias[no] < distancias[no_atual]:
                    no_atual = no
        
        if no_atual is None or distancias[no_atual] == float('infinity'):
            break
            
        visitados.add(no_atual)

        for vizinho, peso in grafo[no_atual].items():
            nova_distancia = distancias[no_atual] + peso
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia

    recomendados_ordenados = sorted(distancias, key=distancias.get)
    
    return [id for id in recomendados_ordenados if id != livro_id_inicial][:5]