from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:V1s1t%40nt@localhost/db_bank'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

db = SQLAlchemy(app)

# Asegúrate de que los nombres de los archivos y las importaciones coincidan con la estructura de tu proyecto
from app.models import Agencia, Agente, Cliente, Prestamo, Pago
from app import routes  # Si tienes un archivo llamado routes.py para tus rutas
