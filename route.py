from flask import Flask, request, jsonify
from service import Aluno


aluno=Aluno()


app = Flask(__name__)

@app.route("/")
def index():
    return "isso é um printII!"

@app.route("/minhaaplicacao", methods=['GET'])#lsitar
def get():
    return "teste"

@app.route("/minhaaplicacao", methods=['POST'])#cadastra
def post():
    data = request.json
    aluno.save(data)
    return jsonify(data)

@app.route("/minhaaplicacao/<int:id>", methods=['PUT'])#atualisa
def put(id):
    data = request.json

    return jsonify(data)

@app.route("/minhaaplicacao/<int:id>", methods=['DELETE'])#deleta
def delete(id):
    self.conexao.deleta({"id": id})
    print(id)


if __name__ == '__main__':
    app.run(debug=True)