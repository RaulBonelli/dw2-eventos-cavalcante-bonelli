#app.py (monolítico)
from flask import Flask, render_template, request, redirect
from controller.evento_controller import evento_bp

app = Flask(__name__)
app.register_blueprint(evento_bp)

if __name__ == "__main__":
    app.run(debug=True)


app = Flask (_name__)
eventos = []
@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        eventos.append({
        "nome": request.form["nome"],
        "data": request.form["data"],
        "local": request.form["local"],
        })
        return redirect("/")


    
    return render_template("index.html", eventos = Eventos)

