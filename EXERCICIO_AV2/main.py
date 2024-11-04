from database import Database
from teacher_crud import TeacherCRUD


def main():

    db = Database(uri="bolt://localhost:7687", user="neo4j", password="password")
    teacher_crud = TeacherCRUD(db)

    while True:
        print("\nEscolha uma opção:")
        print("1. Criar Teacher")
        print("2. Ler Teacher")
        print("3. Atualizar Teacher")
        print("4. Deletar Teacher")
        print("5. Sair")

        choice = input("Opção: ")

        if choice == "1":
            name = input("Nome do professor: ")
            ano_nasc = int(input("Ano de nascimento: "))
            cpf = input("CPF: ")
            teacher_crud.create(name, ano_nasc, cpf)
            print(f"Teacher '{name}' criado com sucesso.")

        elif choice == "2":
            name = input("Nome do professor para buscar: ")
            result = teacher_crud.read(name)
            print("Resultado:", result)

        elif choice == "3":
            name = input("Nome do professor para atualizar: ")
            newCpf = input("Novo CPF: ")
            teacher_crud.update(name, newCpf)
            print(f"CPF do Teacher '{name}' atualizado com sucesso.")

        elif choice == "4":
            name = input("Nome do professor para deletar: ")
            teacher_crud.delete(name)
            print(f"Teacher '{name}' deletado com sucesso.")

        elif choice == "5":
            print("Encerrando o sistema.")
            break

        else:
            print("Opção inválida, tente novamente.")

    db.close()


if __name__ == "__main__":
    main()
