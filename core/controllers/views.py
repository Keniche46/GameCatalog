from flask import render_template, request, redirect, url_for
from core import db
from core.models.models import Game
import os
from werkzeug.utils import secure_filename
import uuid

UPLOAD_FOLDER = "core/static/img"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def init_app(app):

    @app.route("/")
    def index():
        games = Game.query.all()
        generos = sorted(set(game.genero for game in games))
        return render_template("index.html", games=games, generos=generos)

    @app.route("/view/<int:id>")
    def view_game(id):
        game = Game.query.get_or_404(id)
        return render_template("view_game.html", game=game)

    @app.route("/add", methods=["GET", "POST"])
    def add_game():
        if request.method == "POST":
            nome = request.form["nome"]
            genero = request.form["genero"]
            nota = request.form["nota"]
            descricao = request.form["descricao"]

            imagem = request.files.get("imagem")
            if imagem and imagem.filename.strip() != "":
                ext = os.path.splitext(imagem.filename)[1]
                nome_arquivo = f"{uuid.uuid4().hex}{ext}"  # nome único
                caminho = os.path.join(UPLOAD_FOLDER, nome_arquivo)
                imagem.save(caminho)
            else:
                nome_arquivo = None

            game = Game(
                nome=nome,
                genero=genero,
                nota=nota,
                imagem=nome_arquivo,
                descricao=descricao
            )

            db.session.add(game)
            db.session.commit()

            return redirect(url_for("index"))

        return render_template("add_game.html")

    @app.route("/edit/<int:id>", methods=["GET", "POST"])
    def edit_game(id):
        game = Game.query.get_or_404(id)

        if request.method == "POST":
            game.nome = request.form["nome"]
            game.genero = request.form["genero"]
            game.nota = request.form["nota"]
            game.descricao = request.form["descricao"]

            imagem = request.files.get("imagem")
            if imagem and imagem.filename.strip() != "":
                # apagar imagem antiga se existir
                if game.imagem:
                    caminho_antigo = os.path.join(UPLOAD_FOLDER, game.imagem)
                    if os.path.exists(caminho_antigo):
                        os.remove(caminho_antigo)
                ext = os.path.splitext(imagem.filename)[1]
                nome_arquivo = f"{uuid.uuid4().hex}{ext}"
                caminho = os.path.join(UPLOAD_FOLDER, nome_arquivo)
                imagem.save(caminho)
                game.imagem = nome_arquivo

            db.session.commit()
            return redirect(url_for("view_game", id=game.id))

        return render_template("edit_game.html", game=game)

    @app.route("/delete/<int:id>", methods=["POST"])
    def delete_game(id):
        game = Game.query.get_or_404(id)


        if game.imagem:
            caminho = os.path.join(UPLOAD_FOLDER, game.imagem)
            if os.path.exists(caminho):
                os.remove(caminho)

        db.session.delete(game)
        db.session.commit()
        return redirect(url_for("index"))
