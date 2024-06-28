from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from app import db,app

class Usuario(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    usu_nombre = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    clave = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    
    def __init__(self, usu_nombre, email, clave, is_admin=False):
        self.usu_nombre = usu_nombre
        self.email = email
        self.clave = clave
        self.is_admin = is_admin

with app.app_context():
    db.create_all()  # aqui crea todas las tablas

