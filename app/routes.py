from app import app
from flask import jsonify
from app.models import Agencia

@app.route('/')
def home():
    return 'Bienvenido a mi aplicación Flask!'

@app.route('/agencias', methods=['GET'])
def get_agencias():
    agencias = Agencia.query.all()
    return jsonify([agencia.to_dict() for agencia in agencias])

# Continuar con las rutas para los otros modelos...
