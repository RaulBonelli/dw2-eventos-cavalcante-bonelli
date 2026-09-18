# A PROVA DOS NOVE - mostra que os dados sao persistentes.
# Este script nao sobe o servidor: ele apenas consulta o banco.
#
# Como usar:
#   1. Rode "python app.py" e cadastre alguns eventos.
#   2. Encerre o servidor com Ctrl+C.
#   3. Rode "python consultar.py".
#   4. Os eventos continuam la, porque foram gravados no banco.

from dao.evento_dao import EventoDAO

eventos = EventoDAO.listar()

print("Eventos gravados no banco:", len(eventos))
print()

for e in eventos:
    print(e.id, e.data, e.nome, e.local, e.vagas)

print()
print("Os dados sobreviveram ao encerramento da aplicacao.")
