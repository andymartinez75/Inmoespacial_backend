from flask import jsonify, request
from app import app, db, ma
from modelos.compra_modelo import Compra

class CompraSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_usuario', 'id_planeta', 'fecha_compra')

compra_schema = CompraSchema()            # Para traer una compra
compras_schema = CompraSchema(many=True)  # Para traer múltiples compras

@app.route('/compras', methods=['GET'])
def get_compras():
    all_compras = Compra.query.all()
    result = compras_schema.dump(all_compras)
    return jsonify(result)

@app.route('/compras/<id>', methods=['GET'])
def get_compra(id):
    compra = Compra.query.get(id)
    return compra_schema.jsonify(compra)

@app.route('/compras', methods=['POST'])
def create_compra():
    id_usuario = request.json['id_usuario']
    id_planeta = request.json['id_planeta']
    fecha_compra = request.json['fecha_compra']
    new_compra = Compra(id_usuario, id_planeta, fecha_compra)
    db.session.add(new_compra)
    db.session.commit()
    return compra_schema.jsonify(new_compra)

@app.route('/compras/<id>', methods=['PUT'])
def update_compra(id):
    compra = Compra.query.get(id)
    compra.id_usuario = request.json['id_usuario']
    compra.id_planeta = request.json['id_planeta']
    compra.fecha_compra = request.json['fecha_compra']
    db.session.commit()
    return compra_schema.jsonify(compra)

@app.route('/compras/<id>', methods=['DELETE'])
def delete_compra(id):
    compra = Compra.query.get(id)
    db.session.delete(compra)
    db.session.commit()
    return compra_schema.jsonify(compra)
