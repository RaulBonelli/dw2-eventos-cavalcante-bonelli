# Sistema Web de Gestao de Eventos Academicos
# Desenvolvimento Web II (DW2) - Aula 6
# Etapa 2: persistencia com SQL direto (MVC + DAO + SQLite)
#
# Diferenca para a Aula 4: os eventos nao ficam mais em uma lista na
# memoria - sao gravados no banco e sobrevivem ao reinicio.
#
# Como executar (na raiz do projeto, com o venv ativo):
#     pip install -r requirements.txt
#     python app.py
 
from flask import Flask
from controllers.evento_controller import evento_bp
from database import criar_tabelas
 
app = Flask(__name__)
app.register_blueprint(evento_bp)
 
if __name__ == "__main__":
    criar_tabelas()
    app.run(debug=True)
 