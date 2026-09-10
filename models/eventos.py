from database import db

class Eventos(db.Model):
    __tablename__ = "eventos"
    
    id_evento = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(500), nullable=False)
    data = db.Column(db.String(10), nullable=False)
    local = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    quantidade_participantes = db.Column(db.Integer, nullable=False)
    