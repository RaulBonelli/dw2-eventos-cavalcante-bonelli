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



