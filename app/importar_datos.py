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
    cliente = Cliente(
        id=cliente_id,
        nombre=f"{row['Nombres']} {row['Apellido Paterno']} {row['Apellido Materno']}",
        informacion_contacto=informacion_contacto
    )
    session.add(cliente)

    prestamo = Prestamo(
        id=row['N° Credito'], 
        monto_otorgado=row['Monto otorgado'],
        cargo=row['Cargo'],
        total_a_pagar=row['Total a pagar'],
        primer_pago=row['Primer pago'],
        tarifa=row['Tarifa'],
        cliente_id=cliente_id  
    )
    session.add(prestamo)

session.commit()

#datos de agentes
for _, row in excel_data.iterrows():
    agente = Agente(
        nombre=row['Agente']  # 
        # por ahora lo q hay en el excel
    )
    session.add(agente)

session.commit()
session.close()
