from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from app import db,app

class Compra(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    id_planeta = db.Column(db.Integer, db.ForeignKey('planeta.id'), nullable=False)
    fecha_compra = db.Column(db.DateTime, nullable=False)

    def __init__(self, id_usuario, id_planeta, fecha_compra):
        self.id_usuario = id_usuario
        self.id_planeta = id_planeta
        self.fecha_compra = fecha_compra

with app.app_context():
    db.create_all()  # aqui crea todas las tablas

