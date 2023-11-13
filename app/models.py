from . import db  

class Agencia(db.Model):
    __tablename__ = 'agencias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    nivel = db.Column(db.String(50))
    ubicacion = db.Column(db.String(255))
    agentes = db.relationship('Agente', backref='agencia', lazy=True)

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
    clientes = db.relationship('Cliente', backref='agente', lazy=True)
    prestamos = db.relationship('Prestamo', backref='agente', lazy=True)
   
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'agencia_id': self.agencia_id
        }


class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.String(255), primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    informacion_contacto = db.Column(db.Text)
    agente_id = db.Column(db.Integer, db.ForeignKey('agentes.id'))
    prestamos = db.relationship('Prestamo', backref='cliente', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'informacion_contacto': self.informacion_contacto,
        }


class Prestamo(db.Model):
    __tablename__ = 'prestamos'
    id = db.Column(db.Integer, primary_key=True)
    monto_otorgado = db.Column(db.Numeric(12, 2), nullable=False)
    cargo = db.Column(db.Numeric(12, 2))
    total_a_pagar = db.Column(db.Numeric(12, 2))
    primer_pago = db.Column(db.Date)
    tarifa = db.Column(db.Numeric(12, 2))
    fecha_inicio = db.Column(db.Date, nullable=False)
    estado = db.Column(db.String(50))
    cliente_id = db.Column(db.String(255), db.ForeignKey('clientes.id'))
    agente_id = db.Column(db.Integer, db.ForeignKey('agentes.id'))
    pagos = db.relationship('Pago', backref='prestamo', lazy=True)
    descuentos = db.relationship('Descuento', backref='prestamo', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'monto_otorgado': self.monto_otorgado,
            'cargo': self.cargo,
            'total_a_pagar': self.total_a_pagar,
            'primer_pago': self.primer_pago,
            'tarifa': self.tarifa,
            'fecha_inicio': self.fecha_inicio,
            'estado': self.estado,
            'cliente_id': self.cliente_id,
            'agente_id': self.agente_id
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

class Descuento(db.Model):
    __tablename__ = 'descuentos'
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255))
    semana = db.Column(db.Integer)
    porcentaje_descuento = db.Column(db.Numeric(5, 2))
    prestamo_id = db.Column(db.Integer, db.ForeignKey('prestamos.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'descripcion': self.descripcion,
            'semana': self.semana,
            'porcentaje_descuento': self.porcentaje_descuento,
            'prestamo_id': self.prestamo_id
        }