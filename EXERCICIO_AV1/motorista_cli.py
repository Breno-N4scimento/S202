from passageiro import Passageiro
from corrida import Corrida
from motorista import Motorista
from motorista_dao import MotoristaDAO
from database import Database

class MotoristaCLI:
    def __init__(self, motorista_dao: MotoristaDAO):
        self.motorista_dao = motorista_dao

    def menu(self):
        while True:
            print("\n1. Criar Motorista")
            print("2. Ver Motorista")
            print("3. Atualizar Motorista")
            print("4. Deletar Motorista")
            print("5. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.create_motorista()
            elif escolha == '2':
                self.read_motorista()
            elif escolha == '3':
                self.update_motorista()
            elif escolha == '4':
                self.delete_motorista()
            elif escolha == '5':
                break
            else:
                print("Opção inválida.")

    def create_motorista(self):
        nome = input("Nome do Motorista: ")
        cnh = input("CNH do Motorista: ")
        veiculo = input("Veículo do Motorista: ")

        corridas = []
        while True:
            print("\nCriando uma nova corrida:")
            nota = float(input("Nota da Corrida: "))
            distancia = float(input("Distância percorrida (km): "))
            valor = float(input("Valor da Corrida: "))

            nome_passageiro = input("Nome do Passageiro: ")
            documento_passageiro = input("Documento do Passageiro: ")
            passageiro = Passageiro(nome_passageiro, documento_passageiro)

            corrida = Corrida(nota, distancia, valor, passageiro)
            corridas.append(corrida)

            add_outra = input("Adicionar outra corrida? (s/n): ")
            if add_outra.lower() != 's':
                break

        motorista = Motorista(nome, cnh, veiculo, corridas)
        self.motorista_dao.create_motorista(motorista)
        print(f"Motorista {nome} criado com sucesso!")

    def read_motorista(self):
        cnh = input("Informe a CNH do motorista: ")
        motorista = self.motorista_dao.read_motorista(cnh)
        if motorista:
            print(motorista)
        else:
            print("Motorista não encontrado.")

    def update_motorista(self):
        cnh = input("Informe a CNH do motorista: ")
        nome = input("Novo nome (deixe em branco para não alterar): ")
        veiculo = input("Novo veículo (deixe em branco para não alterar): ")

        update_data = {}
        if nome:
            update_data['nome'] = nome
        if veiculo:
            update_data['veiculo'] = veiculo

        self.motorista_dao.update_motorista(cnh, update_data)
        print("Motorista atualizado com sucesso!")

    def delete_motorista(self):
        cnh = input("Informe a CNH do motorista: ")
        self.motorista_dao.delete_motorista(cnh)
        print("Motorista deletado com sucesso!")
