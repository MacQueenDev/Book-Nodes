# E3 — MVP: Núcleo Funcional com Primeiras Telas

> **Disciplina:** Teoria dos Grafos  
> **Prazo:** 10 de maio de 2026  
> **Peso:** 25% da nota final  

---

## Identificação do Grupo

| Campo | Preenchimento |
|-------|---------------|
| Nome do projeto | Sistema de Recomendação de Livros baseado em Grafos de Similaridade |
| Repositório GitHub | https://github.com/MacQueenDev/Book-Nodes |
| Integrante 1 | Gabriel Alves Dias Reis - 39840883  |
| Integrante 2 | Marcos Antônio Da Silva Souza - 39815048 |
| Integrante 3 | Matheus Silva Soares - 38714663 |

---

## 1. Como Executar o MVP

> Instrua como rodar o projeto do zero. Alguém que nunca viu o código deve conseguir executar seguindo estas instruções.

**Pré-requisitos:**

```bash
## 1. Como Executar o MVP

```bash
- Python 3.10+
- pip instalado

**Instalação:**

```bash
git clone https://github.com/MacQueenDev/Book-Nodes
cd Book-Nodes
pip install -r requirements.txt
```

**Execução:**

```bash
# Comando para rodar o MVP
python src/app.py
```

**Saída esperada:**

```
O sistema inicia uma aplicação web utilizando Flask. O usuário pode selecionar um livro e visualizar recomendações geradas a partir do algoritmo de Dijkstra, com base nas relações de similaridade entre os livros.
```

---

## 2. Algoritmo Implementado

| Campo | Resposta |
|-------|----------|
| Nome do algoritmo | Dijkstra |
| Arquivo de implementação | src/engine.py |
| Complexidade de tempo |  O((V + E) log V) |
| Complexidade de espaço |  O(V) |

**Trecho do código com comentário de Big-O:**

```python

import networkx as nx
from .models import Conexao

def obter_recomendacoes(livro_id):
    G = nx.Graph()

    # Construção do grafo → O(E)
    conexoes = Conexao.query.all()
    for c in conexoes:
        G.add_edge(c.livro_origem_id, c.livro_destino_id, weight=c.peso)

    try:
        # Dijkstra → O((V + E) log V)
        distancias, caminhos = nx.single_source_dijkstra(G, source=livro_id)

        # Ordenação → O(V log V)
        recomendados = sorted(distancias.items(), key=lambda x: x[1])[1:4]

        return [item[0] for item in recomendados]
    except:
        return []


---

O algoritmo utiliza a função single_source_dijkstra da biblioteca NetworkX para calcular as menores distâncias a partir de um livro de origem. Os livros com menor custo acumulado são considerados mais similares e retornados como recomendação.

## 3. Estrutura do Repositório

> Confirme que a estrutura implementada está de acordo com o E2.

```
Book-Nodes/
├── data/
│ ├── database.db
│ └── dados.csv
│
├── docs/
│ ├── E1.md
│ ├── E2.md
│ └── README.md
│
├── src/
│ ├── app.py
│ ├── engine.py
│ ├── models.py
│ └── templates/
│
├── tests/
│ └── tests.py
│
├── requirements.txt
└── seed.py
```

**Desvios em relação ao E2** *(se houver)*: A estrutura segue o planejado no E2, com adaptação para aplicação web utilizando Flask.

---

## 4. Telas do MVP

> Insira screenshots ou gravações da interface funcionando.

### Tela de Entrada

![Tela de entrada](./assets/mvp_entrada.png)

*Descrição:*

### Tela de Resultado

![Tela de resultado](./assets/mvp_resultado.png)

*Descrição:*

---

## 5. Testes Unitários

| Algoritmo | Caso de teste | Status | Comando para executar |
|-----------|--------------|--------|----------------------|
| | Caso base | ✅ / ❌ | `pytest tests/test_algoritmo.py::test_caso_base` |
| | Grafo vazio | ✅ / ❌ | |
| | Grafo completo | ✅ / ❌ | |

**Como rodar todos os testes:**

```bash
pytest tests/
```

**Resultado atual:**

```
# Cole aqui a saída do pytest / JUnit
```

---

## 6. Histórico de Commits

> Liste os 5+ commits mais relevantes desta entrega.

| Hash (7 chars) | Mensagem | Autor |
|----------------|----------|-------|
| `abc1234` | feat: implementa classe Graph com lista de adjacência | |
| `def5678` | feat: implementa algoritmo Dijkstra | |
| `ghi9012` | test: adiciona testes unitários para Dijkstra | |
| `jkl3456` | feat: leitura de grafo a partir de JSON | |
| `mno7890` | feat: tela de resultado via CLI | |

---

## 7. O que está funcionando / O que ainda falta

| Funcionalidade | Status | Observação |
|---------------|--------|------------|
| Classe do grafo | ✅ Completo | |
| Algoritmo principal | ✅ Completo / 🔄 Parcial | |
| Leitura de arquivo | ✅ Completo / 🔄 Parcial | |
| Tela de entrada | ✅ Completo / 🔄 Parcial | |
| Tela de resultado | ✅ Completo / 🔄 Parcial | |
| Testes unitários | ✅ Completo / 🔄 Parcial | |

---

## Checklist de Entrega

- [ ] Repositório público e acessível
- [ ] .gitignore configurado
- [ ] README com instruções de execução do MVP
- [ ] Algoritmo principal executando sem erros
- [ ] Tela de entrada e tela de resultado demonstráveis
- [ ] 3 testes unitários por algoritmo (mínimo caso base passando)
- [ ] ≥ 5 commits com prefixos semânticos (feat:, fix:, test:, docs:)
- [ ] Ao menos 1 arquivo de grafo de exemplo em `data/`

---

*Teoria dos Grafos — Profa. Dra. Andréa Ono Sakai*
