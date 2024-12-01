from database import GerenciadorBD
from cli import CLI

def main():
    uri = "mongodb://localhost:27017"  # Ou o URI do seu MongoDB Atlas
    nome_banco = "sistema_estudantes"

    gerenciador_bd = GerenciadorBD(uri, nome_banco)
    cli = CLI(gerenciador_bd)

    while True:
        opcao = cli.exibir_menu()

        if opcao == "1":
            print("\n1. Criar Estudante")
            print("2. Listar Estudantes")
            print("3. Atualizar Estudante")
            print("4. Deletar Estudante")
            sub_opcao = input("Escolha uma opção: ")
            if sub_opcao == "1":
                cli.criar_aluno()
            elif sub_opcao == "2":
                cli.listar_alunos()
            elif sub_opcao == "3":
                cli.atualizar_aluno()
            elif sub_opcao == "4":
                cli.deletar_aluno()
            else:
                print("Opção inválida.")

        elif opcao == "2":
            print("\n1. Criar Curso")
            print("2. Listar Cursos")
            print("3. Atualizar Curso")
            print("4. Deletar Curso")
            sub_opcao = input("Escolha uma opção: ")
            if sub_opcao == "1":
                cli.criar_curso()
            elif sub_opcao == "2":
                cli.listar_cursos()
            elif sub_opcao == "3":
                cli.atualizar_curso()
            elif sub_opcao == "4":
                cli.deletar_curso()
            else:
                print("Opção inválida.")

        elif opcao == "3":
            print("Saindo do sistema. Até mais!")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
