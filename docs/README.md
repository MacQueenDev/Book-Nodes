
# 🚀 Nome do Projeto
 ![Logo](img/logo.png)

**Projeto:**
Book-Nodes 

**Resumo:**  

O projeto consiste em um sistema de recomendação de livros para e-commerce utilizando Teoria dos Grafos e o algoritmo de Dijkstra.  

Os livros são representados como vértices e suas relações de similaridade são modeladas como arestas ponderadas, permitindo identificar os livros mais relevantes a partir de um item selecionado pelo usuário.

O sistema foi desenvolvido como parte da disciplina de **Teoria dos Grafos**, utilizando Python, Flask e NetworkX.

---

## 🎯 Objetivo

Desenvolver um sistema capaz de recomendar livros semelhantes com base em relações de compra conjunta, utilizando grafos ponderados e o algoritmo de Dijkstra para calcular os caminhos de menor custo.


---

## 👨‍💻 Tecnologias Utilizadas

- Python 3
- Flask
- SQLite
- CSV
- NetworkX
- HTML5
- CSS3
- Bootstrap
- Git & GitHub

---

## 🗂️ Estrutura do Projeto

```
BOOK-NODES/
│
├── data/
│   ├── database.db
│   ├── grafo_conexoes.csv
│   └── testdata.py
│
├── docs/
│   ├── img/
│   │   ├── cadastrar.png
│   │   ├── Carrinho.png
│   │   ├── diagrama1.jpeg
│   │   ├── diagramaarquitetura.jpeg
│   │   ├── Home.png
│   │   ├── login.png
│   │   ├── logo.png
│   │   └── Perfil.png
│   │
│   ├── E1_Grupo15_Documento de Visão (1).md
│   ├── E2_Grupo15_Designer_técnico.md
│   ├── E3_Book-Nodes.md
│   └── README.md
│
├── src/
│   ├── templates/
│   │   ├── base.html
│   │   ├── carrinho.html
│   │   ├── detalhe.html
│   │   ├── index.html
│   │   ├── login.html
│   │   └── perfil.html
│   │
│   ├── app.py
│   ├── engine.py
│   ├── models.py
│   └── test.py
│
├── tests/
│   └── test_engine.py
│
├── LICENSE
├── requirements.txt
└── seed.py
```

---

## ⚙️ Como Executar

### ✅ Rodando Localmente

```
git clone https://github.com/MacQueenDev/Book-Nodes

cd Book-Nodes

pip install  requirements.txt

python seed.py

python src/app.py

```
## 📸 Demonstrações

### Tela de Entrada

![Tela de entrada](img/login.png)

### Tela de Cadastro

![Tela de cadastro](img/cadastrar.png)

### Tela de Resultado

![Tela de resultado](img/Home.png)

### Tela de Perfil

![Tela de perfil](img/Perfil.png)

### Tela do Carrinho

![Tela do carrinho](img/Carrinho.png)


## 👥 Equipe

| Nome                              | GitHub                                          |
|-----------------------------------|--------------------------------------------------|
| Matheus Silva Soares             | [@Matheus](https://github.com/Matheus686) |
| Marcos Antônio Da Silva Souza    | [@Marcos](https://github.com/MacQueenDev)                                     |
| Gabriel Alves Dias Reis         |  [@Gabriel](https://github.com/gabe-herrera)        |

---

## 🧠 Disciplinas Envolvidas

- Teoria dos Grafos
- Estrutura de Dados
- Desenvolvimento Web

---

## 🏫 Informações Acadêmicas

- Universidade: Universidade Braz Cubas
- Curso: Ciência da Computação
- Semestre: Marcos e Gabriel Reis 4º / Matheus 5º
- Período: Noite
- Professora orientadora: Dra. Andréa Ono Sakai


---

## 📄 Licença

MIT License — sinta-se à vontade para utilizar, estudar e adaptar este projeto.

 © 2025 Matheus Silva, Marcos Oliveira, Gabriel Reis. Todos os direitos reservados.
 
