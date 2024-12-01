from pymongo import MongoClient

class GerenciadorBD:
    def __init__(self, uri="mongodb://localhost:27017", nome_bd="sistema_faculdade"):
        self.cliente = MongoClient(uri)
        self.banco = self.cliente[nome_bd]  # Atributo correto

    def inserir(self, colecao, dados):
        return self.banco[colecao].insert_one(dados)

    def buscar_todos(self, colecao):
        return list(self.banco[colecao].find())

    def buscar_um(self, colecao, filtro):
        return self.banco[colecao].find_one(filtro)

    def atualizar(self, colecao, filtro, novos_dados):
        return self.banco[colecao].update_one(filtro, {"$set": novos_dados})

    def deletar(self, colecao, filtro):
        return self.banco[colecao].delete_one(filtro)  # Correção aqui para self.banco
