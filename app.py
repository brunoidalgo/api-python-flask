from flask import Flask, jsonify, request
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)


livros = [
  {
    'id': 1,
    'título': 'O Senhor dos Anéis - A Sociedade do Anel',
    'autor': 'J.R.R Tolkien'
  },
  {
    'id': 2,
    'título': 'Harry Potter e a Pedra Filosofal',
    'autor': 'J.K Howling'
  },
  {
    'id': 3,
    'título': 'James Clear',
    'autor': 'Hábitos Atômicos'
  }
]

livros_novos = pd.DataFrame(livros, columns = ["id","título", "autor"])

db_connection = ...
db_connection = create_engine(db_connection)

print(livros_novos)

# Consultar todos 
@app.route('/livros', methods=['GET'])
def pegar_livro():
  return jsonify(livros)

# Consultar por id
@app.route('/livros/<int:id>', methods=['GET'])
def pegar_livro_id(id):
  for livro in livros:
    if livro.get('id') == id:
      return jsonify(livro)
# Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_id(id):
  livro_alterado = request.get_json()
  for indice, livro in enumerate(livros):
    if livro.get('id') == id:
      livros[indice].update(livro_alterado)
      return jsonify(f'Livro editado com sucesso: {livros[indice]}')
    
# Criar
@app.route('/livros', methods=['POST'])
def criar_livro():
  novo_livro = request.get_json()
  livros.append(novo_livro)

  return jsonify(f'Livro cadastrado com sucesso: {novo_livro}')

# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def  excluir_livro(id):
  for indice, livro in enumerate(livros):
    if livro.get('id') == id:
      del livros[indice]

  return jsonify(f'Livro {id} deletado com sucesso.')

app.run(port=5000,host='localhost',debug=True)