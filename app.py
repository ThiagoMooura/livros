from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
  {
    "id": 1,
    "titulo": "O Hobbit",
    "autor": "J.R.R. Tolkien"
  },
  {
    "id": 2,
    "titulo": "1984",
    "autor": "George Orwell"
  },
  {
    "id": 3,
    "titulo": "Dom Quixote",
    "autor": "Miguel de Cervantes"
  },
  {
    "id": 4,
    "titulo": "A Revolução dos Bichos",
    "autor": "George Orwell"
  },
  {
    "id": 5,
    "titulo": "Cem Anos de Solidão",
    "autor": "Gabriel García Márquez"
  }
]



#consultar todos
@app.route('/livros', methods=['GET'])
def obterLivros():
    return jsonify(livros)

#consultar por id
@app.route('/livros/<int:id>', methods=['GET'])
def obterLivroPorId(id):
    for livro in livros:
        if (livro.get('id')) == id:
            return jsonify(livro)
        
#editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editarLivroPorId(id):
    livroAlterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livroAlterado)
            return jsonify(livros[indice])
        
#criar
@app.route('/livros', methods=['POST'])
def incluirNovoLivro():
    novoLivro = request.get_json()
    livros.append(novoLivro)
    return jsonify(livros)

#excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluirLivro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)