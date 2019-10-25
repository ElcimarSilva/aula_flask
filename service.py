from pymongo import MongoClient

from conexcao import MongoConnect

class Aluno():

    conexao = None

    def __init__(self):
        self.conexao = MongoConnect()

    def save(self, json):
        # aluno = {'nome': nome, 'sobrenome': sobrenome, 'curso': curso}
        return self.conexao.save(json)


    def att(self,id,json):
        # aluno = {'nome': nome, 'sobrenome': sobrenome, 'curso': curso}
        self.conexao.att({"_id": id}, {"$set": json})

    def deleta(self, find):
        self.conexao.deleta({"_id": find})

    def ler(self, acha):
        self.conexao.ler({"nome":acha},{"_id":0})

