from pymongo import MongoClient

class GerenciadorBD:
    def __init__(self, uri, nome_banco):
        self.client = MongoClient(uri)
        self.db = self.client[nome_banco]

    def buscar_um(self, collection, filtro):
        return self.db[collection].find_one(filtro)

    def buscar_todos(self, collection):
        return list(self.db[collection].find())

    def inserir(self, collection, dados):
        self.db[collection].insert_one(dados)

    def atualizar(self, collection, filtro, novos_dados):
        self.db[collection].update_one(filtro, {"$set": novos_dados})

    def deletar(self, collection, filtro):
        return self.db[collection].delete_one(filtro)
