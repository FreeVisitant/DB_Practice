import pandas as pd
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Cliente, Prestamo, Agente 

DATABASE_URL = "postgresql://postgres:V1s1t%40nt@localhost/db_bank"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

ruta_excel = r'C:\Users\Visitant\Desktop\DB_Practice\data\BD PLATA XPRESS 2023. CRUDA SEMANA 44.xlsx'  

excel_data = pd.read_excel(ruta_excel, skiprows=2)
print(excel_data.columns)
session = Session()

# Importación de datos para Clientes
for _, row in excel_data.iterrows():
    informacion_contacto = json.dumps({
        "apellido_paterno": row['Apellido Paterno'],
        "apellido_materno": row['Apellido Materno'],
        "direccion": row['Direccion'],
        "numero_exterior": row['No.Exterior'],
        "numero_interior": row['No. Interior'],
        "colonia": row['Colonia'],
        "codigo_postal": row['Codigo postal'],
        "municipio": row['Municipio'],
        "estado": row['Estado']
    })

    cliente_id = str(row['ID ']).strip()  # Convertir a cadena y eliminar espacios

    # Verificar si el cliente ya existe en la base de datos
    cliente_existente = session.query(Cliente).filter_by(id=cliente_id).first()
    if cliente_existente:
        # Si el cliente ya existe, omitir este registro y continuar con el siguiente
        continue

    # Crear un nuevo cliente si no existe
    cliente = Cliente(
        id=cliente_id,
        nombre=f"{row['Nombres']} {row['Apellido Paterno']} {row['Apellido Materno']}",
        informacion_contacto=informacion_contacto
    )
    session.add(cliente)

# Intentar hacer commit de todos los cambios al final del proceso
try:
    session.commit()
except Exception as e:
    session.rollback()  # Revertir cambios en caso de error
    raise e
finally:
    session.close()  # Cerrar la sesión al finalizar

# Importación de datos para Prestamos
for _, row in excel_data.iterrows():
    prestamo_id = str(row['N° Credito'])
    prestamo_existente = session.query(Prestamo).filter_by(id=prestamo_id).first()
    
    if not prestamo_existente:
        prestamo = Prestamo(
            id=prestamo_id, 
            monto_otorgado=row['Monto otorgado'],
            cargo=row['Cargo'],
            total_a_pagar=row['Total a pagar'],
            primer_pago=row['Primer pago'],
            tarifa=row['Tarifa'],
            cliente_id=cliente_id,
            agente_id=row['Agente']   
        )
        session.add(prestamo)


try:
    session.commit()
except Exception as e:
    session.rollback()  # Revertir cambios en caso de error
    raise e
finally:
    session.close()  # Cerrar la sesión al finalizar

# datos de agentes
agentes_unicos = set()  # Para mantener un registro de los agentes únicos ya añadidos

for _, row in excel_data.iterrows():
    agente_id = row['Agente']
    
    # Verificar si el agente ya fue añadido
    if agente_id not in agentes_unicos:
        agente = Agente(
            id=agente_id,
            nombre=row['Agente']  
        )
        session.add(agente)
        agentes_unicos.add(agente_id)

session.commit()
session.close()


session.commit()
session.close()
