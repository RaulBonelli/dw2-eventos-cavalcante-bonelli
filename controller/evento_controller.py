# controllers/evento_controller.py
from flask import Blueprint, render_template, request, redirect
from models.evento import Evento
from data.memoria import eventos

evento_bp = Blueprint("evento", __name__)

@evento_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        evento = Evento(
            request.form["nome"],
            request.form["data"],
            request.form["local"],
        )
        eventos.append(evento)
        return redirect("/")
    return render_template("index.html", eventos=eventos)

@evento_bp.route("/api/eventos", methods=["GET"])
def api_listar():
lista = []
for evento in EventoDAO.listar():
lista.append(evento.para_dicionario())
# converte em JSON E marca o tipo da resposta
return jsonify(lista)

@evento_bp.route("/api/eventos", methods=["POST"])
def api_cadastrar():
dados = request.get_json()
# VALIDACAO NO SERVIDOR - sempre
if not dados.get("nome") or not dados.get("data"):
return jsonify({"erro": "Faltam campos."}), 400
evento = Evento(nome=dados["nome"],
data=dados["data"])
EventoDAO.salvar(evento)
return jsonify(evento.para_dicionario()), 201

