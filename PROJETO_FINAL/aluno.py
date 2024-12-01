class Aluno:
    def __init__(self, student_id, nome, idade, email):
        self.student_id = student_id
        self.name = nome
        self.age = idade
        self.email = email

    def to_dict(self):
        return {
            "id": self.student_id,
            "nome": self.name,
            "idade": self.age,
            "email": self.email
        }
