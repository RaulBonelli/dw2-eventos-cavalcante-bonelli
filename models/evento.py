# Model - entidade Evento.
# O atributo id e a chave primaria: fica None enquanto o evento existe
# apenas em memoria e recebe valor quando o registro vem do banco.
from app import db
 
class Evento:
    def __init__(self, nome, data, local, vagas, id=None):
        self.id = id
        self.nome = nome
        self.data = data
        self.local = local
        self.vagas = vagas
 
class Evento(db.Model):             # Aula 7
    id   = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    data = db.Column(db.String(10),  nullable=False)
    local = db.Column(db.String(120), nullable=False)
    vagas = db.Column(db.Integer, nullable=False)
 
