from app import app, db
from flask import jsonify, request
from app.modelos import Agencia, Agente, Cliente, Prestamo, Pago


@app.route('/agencias', methods=['GET'])
def get_agencias():
    agencias = Agencia.query.all()
    return jsonify([agencia.to_dict() for agencia in agencias])

#falta implementar resto de modelos
