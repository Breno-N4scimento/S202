from aluno import Aluno
from curso import Curso

class CLI:
    def __init__(self, gerenciador_bd):
        self.gerenciador_bd = gerenciador_bd

    def exibir_menu(self):
        print("\n=== Sistema de Gerenciamento de Estudantes ===")
        print("1. Gerenciar Estudantes")
        print("2. Gerenciar Cursos")
        print("3. Sair")
        return input("Escolha uma opção: ")

    def criar_aluno(self):
        student_id = input("ID do Estudante: ")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        email = input("E-mail: ")
        aluno = Aluno(student_id, nome, idade, email)
        self.gerenciador_bd.inserir("alunos", aluno.to_dict())
        print("Estudante cadastrado com sucesso!")

    def listar_alunos(self):
        alunos = self.gerenciador_bd.buscar_todos("alunos")
        if not alunos:
            print("Nenhum estudante encontrado.")
            return
        print("\n=== Lista de Estudantes ===")
        for aluno in alunos:
            print(f"{aluno['id']} - {aluno['nome']} ({aluno['idade']} anos, {aluno['email']})")

    def atualizar_aluno(self):
        student_id = input("ID do Estudante a ser atualizado: ")
        aluno = self.gerenciador_bd.buscar_um("alunos", {"id": student_id})
        if not aluno:
            print("Estudante não encontrado.")
            return
        nome = input(f"Novo Nome ({aluno['nome']}): ")
        idade = input(f"Nova Idade ({aluno['idade']}): ")
        idade = int(idade) if idade else aluno['idade']
        email = input(f"Novo E-mail ({aluno['email']}): ")
        email = email if email else aluno['email']
        novos_dados = {"nome": nome, "idade": idade, "email": email}
        self.gerenciador_bd.atualizar("alunos", {"id": student_id}, novos_dados)
        print("Estudante atualizado com sucesso!")

    def deletar_aluno(self):
        student_id = input("ID do Estudante a ser deletado: ")
        result = self.gerenciador_bd.deletar("alunos", {"id": student_id})
        if result.deleted_count > 0:
            print("Estudante deletado com sucesso!")
        else:
            print("Estudante não encontrado.")

    def criar_curso(self):
        curso_id = input("ID do Curso: ")
        nome = input("Nome do Curso: ")
        professor = input("Professor: ")
        curso = Curso(curso_id, nome, professor)
        self.gerenciador_bd.inserir("cursos", curso.to_dict())
        print("Curso cadastrado com sucesso!")

    def listar_cursos(self):
        cursos = self.gerenciador_bd.buscar_todos("cursos")
        if not cursos:
            print("Nenhum curso encontrado.")
            return
        print("\n=== Lista de Cursos ===")
        for curso in cursos:
            print(f"{curso['id']} - {curso['nome']} (Professor: {curso['professor']})")

    def atualizar_curso(self):
        curso_id = input("ID do Curso a ser atualizado: ")
        curso = self.gerenciador_bd.buscar_um("cursos", {"id": curso_id})
        if not curso:
            print("Curso não encontrado.")
            return
        nome = input(f"Novo Nome ({curso['nome']}): ")
        professor = input(f"Novo Professor ({curso['professor']}): ")
        novos_dados = {"nome": nome, "professor": professor}
        self.gerenciador_bd.atualizar("cursos", {"id": curso_id}, novos_dados)
        print("Curso atualizado com sucesso!")

    def deletar_curso(self):
        curso_id = input("ID do Curso a ser deletado: ")
        result = self.gerenciador_bd.deletar("cursos", {"id": curso_id})
        if result.deleted_count > 0:
            print("Curso deletado com sucesso!")
        else:
            print("Curso não encontrado.")
