from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
CORS(app)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/inmoespacial'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Importar los controladores
from controladores.planeta_controlador import *
from controladores.usuario_controlador import *
from controladores.compra_controlador import *

# Programa principal
if __name__ == '__main__':
    app.run(debug=True, port=5000)
