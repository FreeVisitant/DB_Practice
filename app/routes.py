from app import app, db
from flask import request, jsonify
from app.models import Agencia, Agente, Pago, Prestamo, Cliente

@app.route('/')
def home():
    return 'psssss!'

# Obtener todas las agencias
@app.route('/agencias', methods=['GET'])
def get_agencias():
    agencias = Agencia.query.all()
    return jsonify([agencia.to_dict() for agencia in agencias])

# Obtener una agencia por su ID
@app.route('/agencias/<int:id>', methods=['GET'])
def get_agencia(id):
    agencia = Agencia.query.get_or_404(id)
    return jsonify(agencia.to_dict())

# Crear una nueva agencia
@app.route('/agencias', methods=['POST'])
def create_agencia():
    data = request.json
    nueva_agencia = Agencia(nombre=data['nombre'], nivel=data.get('nivel'), ubicacion=data.get('ubicacion'))
    db.session.add(nueva_agencia)
    db.session.commit()
    return jsonify(nueva_agencia.to_dict()), 201

# Actualizar una agencia existente
@app.route('/agencias/<int:id>', methods=['PUT'])
def update_agencia(id):
    agencia = Agencia.query.get_or_404(id)
    data = request.json
    agencia.nombre = data.get('nombre', agencia.nombre)
    agencia.nivel = data.get('nivel', agencia.nivel)
    agencia.ubicacion = data.get('ubicacion', agencia.ubicacion)
    db.session.commit()
    return jsonify(agencia.to_dict())

# Eliminar una agencia
@app.route('/agencias/<int:id>', methods=['DELETE'])
def delete_agencia(id):
    agencia = Agencia.query.get_or_404(id)
    db.session.delete(agencia)
    db.session.commit()
    return jsonify({'mensaje': 'Agencia eliminada'})




# Obtener todos los agentes
@app.route('/agentes', methods=['GET'])
def get_agentes():
    agentes = Agente.query.all()
    return jsonify([agente.to_dict() for agente in agentes])

# Obtener un agente por su ID
@app.route('/agentes/<int:id>', methods=['GET'])
def get_agente(id):
    agente = Agente.query.get_or_404(id)
    return jsonify(agente.to_dict())

# Crear un nuevo agente
@app.route('/agentes', methods=['POST'])
def create_agente():
    data = request.json
    nueva_agencia = Agencia.query.get_or_404(data['agencia_id'])
    nuevo_agente = Agente(nombre=data['nombre'], agencia_id=nueva_agencia.id)
    db.session.add(nuevo_agente)
    db.session.commit()
    return jsonify(nuevo_agente.to_dict()), 201

# Actualizar un agente existente
@app.route('/agentes/<int:id>', methods=['PUT'])
def update_agente(id):
    agente = Agente.query.get_or_404(id)
    data = request.json
    agente.nombre = data.get('nombre', agente.nombre)
    # Asegúrate de que la agencia a la que se asigna el agente exista
    if 'agencia_id' in data:
        nueva_agencia = Agencia.query.get_or_404(data['agencia_id'])
        agente.agencia_id = nueva_agencia.id
    db.session.commit()
    return jsonify(agente.to_dict())

# Eliminar un agente
@app.route('/agentes/<int:id>', methods=['DELETE'])
def delete_agente(id):
    agente = Agente.query.get_or_404(id)
    db.session.delete(agente)
    db.session.commit()
    return jsonify({'mensaje': 'Agente eliminado'})
