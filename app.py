from flask import Flask,request, jsonify, session, redirect, url_for, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
CORS(app)
app.secret_key = 'your_secret_key'

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://andymar75:usuario75@andymar75.mysql.pythonanywhere-services.com/andymar75$default'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Importar los controladores
from controladores.planeta_controlador import Planeta
from controladores.usuario_controlador import Usuario
from controladores.compra_controlador import Compra



if __name__ == '__main__':
    app.run(debug=True, port=5000)