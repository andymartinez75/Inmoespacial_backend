from flask import jsonify, request
from app import app, db, ma
from modelos.usuario_modelo import Usuario

class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'usu_nombre', 'email', 'clave', 'is_admin')

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

@app.route('/usuarios', methods=['GET'])
def get_Usuarios():
    all_Usuarios = Usuario.query.all()
    result = usuarios_schema.dump(all_Usuarios)
    return jsonify(result)

@app.route('/usuarios/<id>', methods=['GET'])
def get_usuario(id):
    usuario = Usuario.query.get(id)
    return usuario_schema.jsonify(usuario)

@app.route('/usuarios/<id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return usuario_schema.jsonify(usuario)

@app.route('/usuarios', methods=['POST'])
def create_usuario():
    usu_nombre = request.json['usu_nombre']
    email = request.json['email']
    clave = request.json['clave']
    is_admin = request.json.get('is_admin', False)  # Default to False if not provided
    new_usuario = Usuario(usu_nombre, email, clave, is_admin)
    db.session.add(new_usuario)
    db.session.commit()
    return usuario_schema.jsonify(new_usuario)

@app.route('/usuarios/<id>', methods=['PUT'])
def update_usuario(id):
    usuario = Usuario.query.get(id)
    usuario.usu_nombre = request.json['usu_nombre']
    usuario.email = request.json['email']
    usuario.clave = request.json['clave']
    usuario.is_admin = request.json['is_admin']
    db.session.commit()
    return usuario_schema.jsonify(usuario)

@app.route('/usuarios/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('usu_nombre')
    password = data.get('clave')

    usuario = Usuario.query.filter_by(usu_nombre=username).first()

    if usuario and password == usuario.clave:
        if usuario.is_admin:
            return jsonify({"message": "Usuario administrador autenticado", "is_admin": True}), 200
        else:
            return jsonify({"message": "Usuario no administrador autenticado", "is_admin": False}), 200
    else:
        return jsonify({"message": "Error de autenticación: usuario o contraseña incorrectos"}), 401

@app.route('/index.html')
def index():
    return "Página de inicio"
