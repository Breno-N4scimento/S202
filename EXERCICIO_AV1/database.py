from pymongo import MongoClient

class Database:
    def __init__(self, uri: str, db_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.motoristas_collection = self.db["Motoristas"]

    def insert_motorista(self, motorista_data):
        self.motoristas_collection.insert_one(motorista_data)

    def find_motorista(self, cnh):
        return self.motoristas_collection.find_one({"cnh": cnh})

    def update_motorista(self, cnh, update_data):
        self.motoristas_collection.update_one({"cnh": cnh}, {"$set": update_data})

    def delete_motorista(self, cnh):
        self.motoristas_collection.delete_one({"cnh": cnh})
