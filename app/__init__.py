from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:V1s1t%40nt@localhost/DB_Bank'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

db = SQLAlchemy(app)


from app.modelos import Agencia, Agente, Cliente, Prestamo, Pago


from app import rut
