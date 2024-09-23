from database import Database
from motorista_dao import MotoristaDAO
from motorista_cli import MotoristaCLI

if __name__ == "__main__":
    db = Database("mongodb://localhost:27017", "app_mobilidade")
    motorista_dao = MotoristaDAO(db)
    cli = MotoristaCLI(motorista_dao)
    cli.menu()
