from flask import Blueprint, render_template, request, redirect, url_for
from models.eventos import Eventos
from database import db

evento_bp = Blueprint("evento", __name__)

@evento_bp.route("/")
def index():
    return render_template("index.html")

@evento_bp.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        nome = request.form.get("nome")
        descricao = request.form.get("descricao")
        data = request.form.get("data")
        local = request.form.get("local")
        categoria = request.form.get("categoria")
        qnt_pessoas = request.form.get("participantes")
        
        evento =Eventos(
            nome=nome, descricao=descricao, data=data, local=local, categoria=categoria, quantidade_participantes = qnt_pessoas
        )
        
        db.session.add(evento)
        db.session.commit()
        
        return redirect(url_for("evento.index"))
    return render_template("cadastro.html")

@evento_bp.route("/eventos")
def eventos():
    eventos = Eventos.query.all()
    return render_template("eventos.html", eventos=eventos)

@evento_bp.route("/detalhe/<int:id>")
def detalhe(id):
    evento = Eventos.query.get(id)
    return render_template("detalhe.html", evento=evento)

@evento_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    evento = Eventos.query.get(id)
    if request.method == "POST":
        evento.nome = request.form.get("nome")
        evento.descricao = request.form.get("descricao")
        evento.data = request.form.get("data")
        evento.local = request.form.get("local")
        evento.categoria = request.form.get("categoria")
        evento.quantidade_participantes = request.form.get("participantes")
        
        db.session.commit()
        
        return redirect(url_for("evento.index"))
    return render_template("editar.html", evento=evento)

@evento_bp.route("/deletar/<int:id>", methods=["GET", "POST"])
def deletar(id):
    evento = Eventos.query.get(id)
    if request.method == "POST":
        db.session.delete(evento)
        db.session.commit()
        
        return redirect(url_for("evento.index"))
    return render_template("deletar.html", evento=evento)
