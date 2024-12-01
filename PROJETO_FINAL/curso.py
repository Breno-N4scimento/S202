class Curso:
    def __init__(self, curso_id, nome, professor):
        self.course_id = curso_id
        self.name = nome
        self.professor = professor

    def to_dict(self):
        return {
            "_id": self.course_id,
            "nome": self.name,
            "professor": self.professor
        }
