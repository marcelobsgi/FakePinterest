#Cria as rotas do site (links)
from flask import render_template, url_for
from fakepinterest import app

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/perfil/<usuario>")
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)
