from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from app import db,app

class Planeta(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(1000), nullable=False)
    duracion_dia = db.Column(db.String(50), nullable=False)
    cantidad_lunas = db.Column(db.Integer, nullable=False)
    precio_metro_cuad = db.Column(db.String(50), nullable=False)
    oferta = db.Column(db.Boolean, nullable=False)
    imagen = db.Column(db.String(400), nullable=False)

    def __init__(self, nombre, descripcion, duracion_dia, cantidad_lunas, precio_metro_cuad, oferta, imagen):
        self.nombre = nombre
        self.descripcion = descripcion
        self.duracion_dia = duracion_dia
        self.cantidad_lunas = cantidad_lunas
        self.precio_metro_cuad = precio_metro_cuad
        self.oferta = oferta
        self.imagen = imagen

with app.app_context():
    db.create_all()  # aqui crea todas las tablas



