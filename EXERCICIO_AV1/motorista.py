class Motorista:
    def __init__(self, nome: str, cnh: str, veiculo: str, corridas: list):
        self.nome = nome
        self.cnh = cnh
        self.veiculo = veiculo
        self.corridas = corridas

    def to_dict(self):
        return \
        {
            "nome": self.nome,
            "cnh": self.cnh,
            "veiculo": self.veiculo,
            "corridas": [corrida.to_dict() for corrida in self.corridas]
        }
