from motorista import Motorista
from database import Database

class MotoristaDAO:
    def __init__(self, db: Database):
        self.db = db

    def create_motorista(self, motorista: Motorista):
        self.db.insert_motorista(motorista.to_dict())

    def read_motorista(self, cnh: str):
        return self.db.find_motorista(cnh)

    def update_motorista(self, cnh: str, update_data: dict):
        self.db.update_motorista(cnh, update_data)

    def delete_motorista(self, cnh: str):
        self.db.delete_motorista(cnh)
