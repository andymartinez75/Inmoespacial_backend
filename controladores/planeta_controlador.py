from flask import jsonify, request
from app import app, db, ma
from modelos.planeta_modelo import Planeta

class PlanetaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'descripcion', 'duracion_dia', 'cantidad_lunas', 'precio_metro_cuad', 'oferta', 'imagen')

planeta_schema = PlanetaSchema()            # Para traer un planeta
planetas_schema = PlanetaSchema(many=True)  # Para traer múltiples planetas

@app.route('/planetas', methods=['GET'])
def get_planetas():
    all_planetas = Planeta.query.all()
    result = planetas_schema.dump(all_planetas)
    return jsonify(result)

@app.route('/planetas/<id>', methods=['GET'])
def get_planeta(id):
    planeta = Planeta.query.get(id)
    return planeta_schema.jsonify(planeta)

@app.route('/planetas', methods=['POST'])
def create_planeta():
    nombre = request.json['nombre']
    descripcion = request.json['descripcion']
    duracion_dia = request.json['duracion_dia']
    cantidad_lunas = request.json['cantidad_lunas']
    precio_metro_cuad = request.json['precio_metro_cuad']
    oferta = request.json['oferta']
    imagen = request.json['imagen']
    new_planeta = Planeta(nombre, descripcion, duracion_dia, cantidad_lunas, precio_metro_cuad, oferta, imagen)
    db.session.add(new_planeta)
    db.session.commit()
    return planeta_schema.jsonify(new_planeta)

@app.route('/planetas/<id>', methods=['PUT'])
def update_planeta(id):
    planeta = Planeta.query.get(id)
    planeta.nombre = request.json['nombre']
    planeta.descripcion = request.json['descripcion']
    planeta.duracion_dia = request.json['duracion_dia']
    planeta.cantidad_lunas = request.json['cantidad_lunas']
    planeta.precio_metro_cuad = request.json['precio_metro_cuad']
    planeta.oferta = request.json['oferta']
    planeta.imagen = request.json['imagen']
    db.session.commit()
    return planeta_schema.jsonify(planeta)

@app.route('/planetas/<id>', methods=['DELETE'])
def delete_planeta(id):
    planeta = Planeta.query.get(id)
    db.session.delete(planeta)
    db.session.commit()
    return planeta_schema.jsonify(planeta)

@app.route('/')
def bienvenida():
    return "Bienvenidos a Inmoespacial"
