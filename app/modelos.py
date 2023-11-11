from . import db  

class Agencia(db.Model):
    __tablename__ = 'agencias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    nivel = db.Column(db.String(50))
    ubicacion = db.Column(db.String(255))

class Agente(db.Model):
    __tablename__ = 'agentes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    agencia_id = db.Column(db.Integer, db.ForeignKey('agencias.id'))

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    informacion_contacto = db.Column(db.Text)

class Prestamo(db.Model):
    __tablename__ = 'prestamos'
    id = db.Column(db.Integer, primary_key=True)
    monto = db.Column(db.Numeric(12, 2), nullable=False)
    fecha_inicio = db.Column(db.Date, nullable=False)
    estado = db.Column(db.String(50))
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))

class Pago(db.Model):
    __tablename__ = 'pagos'
    id = db.Column(db.Integer, primary_key=True)
    monto = db.Column(db.Numeric(12, 2), nullable=False)
    fecha_pago = db.Column(db.Date, nullable=False)
    prestamo_id = db.Column(db.Integer, db.ForeignKey('prestamos.id'))
    agente_id = db.Column(db.Integer, db.ForeignKey('agentes.id'))
    tarifa = db.Column(db.Numeric(12, 2))
