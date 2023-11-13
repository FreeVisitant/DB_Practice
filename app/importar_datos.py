import pandas as pd
import json
from sqlalchemy import create_engine
from app.models import Cliente, Prestamo, Agente 

# Cadena de conexión y motor de SQLAlchemy
DATABASE_URL = "postgresql://postgres:V1s1t%40nt@localhost/db_bank"
engine = create_engine(DATABASE_URL)

# Ruta del archivo Excel
ruta_excel = r'C:\Users\Visitant\Desktop\DB_Practice\data\BD PLATA XPRESS 2023. CRUDA SEMANA 44.xlsx'  

# Lectura del archivo Excel, omitiendo las dos primeras filas
excel_data = pd.read_excel(ruta_excel, skiprows=2)

# datos para Clientes
for _, row in excel_data.iterrows():
    informacion_contacto = json.dumps({
        "apellido_paterno": row['apellidos paternos'],
        "apellido_materno": row['apellidos maternos'],
        "direccion": row['direccion'],
        "numero_exterior": row['numero exterior'],
        "numero_interior": row['numero interior'],
        "colonia": row['colonia'],
        "codigo_postal": row['codigo postal'],
        "municipio": row['municipio'],
        "estado": row['estado']
    })

    cliente = Cliente(
        id=row['ID de este numero de credito'], 
        nombre=row['Nombres'] + " " + row['apellidos paternos'] + " " + row['apellidos maternos'],
        informacion_contacto=informacion_contacto
    )
    engine.session.add(cliente)

# datos prestamo
for _, row in excel_data.iterrows():
    prestamo = Prestamo(
        id=row['N° Credito'], 
        monto_otorgado=row['Monto otorgado'],
        cargo=row['Cargo'],
        total_a_pagar=row['Total a pagar'],
        primer_pago=row['Primer pago'],
        tarifa=row['Tarifa']
    )
    engine.session.add(prestamo)

#datos de agentes
for _, row in excel_data.iterrows():
    agente = Agente(
        nombre=row['Agente']  # 
        # por ahora lo q hay en el excel
    )
    engine.session.add(agente)

engine.session.commit()
