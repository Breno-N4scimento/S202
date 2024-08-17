class Professor:
    def __init__(self,nome):
        self.nome=nome

    def ministra_aula(self,aula):
        return f"O professor {self.nome} está ministrando uma aula sobre {aula}"

class Aluno:
    def __init__(self,nome):
        self.nome=nome

    def presenca(self):
        return f"O aluno {self.nome} está presente."

class Aula:
    def __init__(self, professor, assunto):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.appenxd(aluno)

    def listar_presenca(self):
        lista_presenca = f"Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:\n"
        for aluno in self.alunos:
            lista_presenca += aluno.presenca() + "\n"
        return lista_presenca.strip()


professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aula = Aula(professor, "POO")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)

print(aula.listar_presenca())
