from core import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    nota = db.Column(db.Integer, nullable=False)
    imagem = db.Column(db.String(200), nullable=False)
    descricao = db.Column(db.Text, nullable=False)