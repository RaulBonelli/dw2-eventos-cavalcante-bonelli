# Model - entidade Evento.
# O atributo id e a chave primaria: fica None enquanto o evento existe
# apenas em memoria e recebe valor quando o registro vem do banco.


class Evento:
    def __init__(self, nome, data, local, vagas, id=None):
        self.id = id
        self.nome = nome
        self.data = data
        self.local = local
        self.vagas = vagas
