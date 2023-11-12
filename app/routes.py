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
    if not data:
        return jsonify({'mensaje': 'No se proporcionaron datos'}), 400

    nombre = data.get('nombre')
    if not nombre:
        return jsonify({'mensaje': 'El nombre es obligatorio'}), 400

    nueva_agencia = Agencia(nombre=nombre, 
                            nivel=data.get('nivel'), 
                            ubicacion=data.get('ubicacion'))
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
    if not data:
        return jsonify({'mensaje': 'No se proporcionaron datos'}), 400

    nombre = data.get('nombre')
    agencia_id = data.get('agencia_id')
    if not nombre or agencia_id is None:
        return jsonify({'mensaje': 'El nombre y el ID de la agencia son obligatorios'}), 400

    if not Agencia.query.get(agencia_id):
        return jsonify({'mensaje': 'Agencia no encontrada'}), 404

    nuevo_agente = Agente(nombre=nombre, agencia_id=agencia_id)
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



# Obtener todos los clientes
@app.route('/clientes', methods=['GET'])
def get_clientes():
    clientes = Cliente.query.all()
    return jsonify([cliente.to_dict() for cliente in clientes])

# Obtener un cliente por su ID
@app.route('/clientes/<int:id>', methods=['GET'])
def get_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    return jsonify(cliente.to_dict())

# Crear un nuevo cliente
@app.route('/clientes', methods=['POST'])
def create_cliente():
    data = request.json
    if not data:
        return jsonify({'mensaje': 'No se proporcionaron datos'}), 400

    nombre = data.get('nombre')
    if not nombre:
        return jsonify({'mensaje': 'El nombre es obligatorio'}), 400

    nuevo_cliente = Cliente(nombre=nombre, informacion_contacto=data.get('informacion_contacto'))
    db.session.add(nuevo_cliente)
    db.session.commit()
    return jsonify(nuevo_cliente.to_dict()), 201

# Actualizar un cliente existente
@app.route('/clientes/<int:id>', methods=['PUT'])
def update_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    data = request.json
    cliente.nombre = data.get('nombre', cliente.nombre)
    cliente.informacion_contacto = data.get('informacion_contacto', cliente.informacion_contacto)
    db.session.commit()
    return jsonify(cliente.to_dict())

# Eliminar un cliente
@app.route('/clientes/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return jsonify({'mensaje': 'Cliente eliminado'})


# Obtener todos los préstamos
@app.route('/prestamos', methods=['GET'])
def get_prestamos():
    prestamos = Prestamo.query.all()
    return jsonify([prestamo.to_dict() for prestamo in prestamos])

# Obtener un préstamo por su ID
@app.route('/prestamos/<int:id>', methods=['GET'])
def get_prestamo(id):
    prestamo = Prestamo.query.get_or_404(id)
    return jsonify(prestamo.to_dict())

# Crear un nuevo préstamo
@app.route('/prestamos', methods=['POST'])
def create_prestamo():
    data = request.json
    cliente = Cliente.query.get_or_404(data['cliente_id'])
    nuevo_prestamo = Prestamo(monto=data['monto'], fecha_inicio=data['fecha_inicio'], estado=data.get('estado'), cliente_id=cliente.id)
    db.session.add(nuevo_prestamo)
    db.session.commit()
    return jsonify(nuevo_prestamo.to_dict()), 201

# Actualizar un préstamo existente
@app.route('/prestamos/<int:id>', methods=['PUT'])
def update_prestamo(id):
    prestamo = Prestamo.query.get_or_404(id)
    data = request.json
    prestamo.monto = data.get('monto', prestamo.monto)
    prestamo.fecha_inicio = data.get('fecha_inicio', prestamo.fecha_inicio)
    prestamo.estado = data.get('estado', prestamo.estado)
    db.session.commit()
    return jsonify(prestamo.to_dict())

# Eliminar un préstamo
@app.route('/prestamos/<int:id>', methods=['DELETE'])
def delete_prestamo(id):
    prestamo = Prestamo.query.get_or_404(id)
    db.session.delete(prestamo)
    db.session.commit()
    return jsonify({'mensaje': 'Préstamo eliminado'})


# Obtener todos los pagos
@app.route('/pagos', methods=['GET'])
def get_pagos():
    pagos = Pago.query.all()
    return jsonify([pago.to_dict() for pago in pagos])

# Obtener un pago por su ID
@app.route('/pagos/<int:id>', methods=['GET'])
def get_pago(id):
    pago = Pago.query.get_or_404(id)
    return jsonify(pago.to_dict())

# Crear un nuevo pago
@app.route('/pagos', methods=['POST'])
def create_pago():
    data = request.json
    prestamo = Prestamo.query.get_or_404(data['prestamo_id'])
    agente = Agente.query.get_or_404(data['agente_id'])
    nuevo_pago = Pago(monto=data['monto'], fecha_pago=data['fecha_pago'], prestamo_id=prestamo.id, agente_id=agente.id, tarifa=data.get('tarifa'))
    db.session.add(nuevo_pago)
    db.session.commit()
    return jsonify(nuevo_pago.to_dict()), 201

# Actualizar un pago existente
@app.route('/pagos/<int:id>', methods=['PUT'])
def update_pago(id):
    pago = Pago.query.get_or_404(id)
    data = request.json
    pago.monto = data.get('monto', pago.monto)
    pago.fecha_pago = data.get('fecha_pago', pago.fecha_pago)
    pago.tarifa = data.get('tarifa', pago.tarifa)
    db.session.commit()
    return jsonify(pago.to_dict())

# Eliminar un pago
@app.route('/pagos/<int:id>', methods=['DELETE'])
def delete_pago(id):
    pago = Pago.query.get_or_404(id)
    db.session.delete(pago)
    db.session.commit()
    return jsonify({'mensaje': 'Pago eliminado'})



###Rutas adicionales para obtener prestamo de un cliente especifico y ruta para obtener pagos por un agente especifico
@app.route('/clientes/<int:cliente_id>/prestamos', methods=['GET'])
def get_prestamos_cliente(cliente_id):
    prestamos = Prestamo.query.filter_by(cliente_id=cliente_id).all()
    return jsonify([prestamo.to_dict() for prestamo in prestamos])


@app.route('/agentes/<int:agente_id>/pagos', methods=['GET'])
def get_pagos_agente(agente_id):
    pagos = Pago.query.filter_by(agente_id=agente_id).all()
    return jsonify([pago.to_dict() for pago in pagos])
