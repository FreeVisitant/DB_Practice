from . import db  

class Agencia(db.Model):
    __tablename__ = 'agencias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    nivel = db.Column(db.String(50))
    ubicacion = db.Column(db.String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'nivel': self.nivel,
            'ubicacion': self.ubicacion
        }

class Agente(db.Model):
    __tablename__ = 'agentes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    agencia_id = db.Column(db.Integer, db.ForeignKey('agencias.id'))
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'agencia_id': self.agencia_id
        }


class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    informacion_contacto = db.Column(db.Text)
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'informacion_contacto': self.informacion_contacto,
        }


class Prestamo(db.Model):
    __tablename__ = 'prestamos'
    id = db.Column(db.Integer, primary_key=True)
    monto = db.Column(db.Numeric(12, 2), nullable=False)
    fecha_inicio = db.Column(db.Date, nullable=False)
    estado = db.Column(db.String(50))
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    def to_dict(self):
        return {
            'id': self.id,
            'monto': self.monto,
            'fecha_inicio': self.fecha_inicio,
            'estado': self.estado,
            'cliente_id': self.cliente_id
        }


class Pago(db.Model):
    __tablename__ = 'pagos'
    id = db.Column(db.Integer, primary_key=True)
    monto = db.Column(db.Numeric(12, 2), nullable=False)
    fecha_pago = db.Column(db.Date, nullable=False)
    prestamo_id = db.Column(db.Integer, db.ForeignKey('prestamos.id'))
    agente_id = db.Column(db.Integer, db.ForeignKey('agentes.id'))
    tarifa = db.Column(db.Numeric(12, 2))
    def to_dict(self):
        return {
            'id': self.id,
            'monto': self.monto,
            'fecha_pago': self.fecha_pago,
            'prestamo_id': self.prestamo_id,
            'agente_id': self.agente_id,
            'tarifa': self.tarifa,
        }

