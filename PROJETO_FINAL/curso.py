class Curso:
    def __init__(self, curso_id, nome, professor):
        self.curso_id = curso_id
        self.nome = nome
        self.professor = professor

    def to_dict(self):
        return {
            "id": self.curso_id,  # Garantir que 'id' seja atribuído
            "nome": self.nome,
            "professor": self.professor
        }
