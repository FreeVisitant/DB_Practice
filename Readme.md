
### Ideas de optimización de los Algoritmos, Cmbios y Sugerencias:

1.  Sustitucion de los algoritmos de ordenación, se pueden hacer eficientes. Sugerencia: quicksort o mergesort para manejar grandes conjuntos de datos antes de realizar operaciones como la importación de datos, de gran utilidad para la ordenación. Una vez los datos ordenados una búsqueda binaria aseguraría una disminución en la complejidad algorítmica. Para Crud la idea de trabajo con árboles me parece más atractiva, implmentar un AVL mejoraría mucho las tareas de añadir, quitar, etc......

2. Optimizar las consultas SQL, como elegir adecuadamente índices, reescribir subconsultas como joins cuando es más eficiente, consultar mejoras mas dinámicas, para grandes cantidades de datos se recomienda trabajar con la mochila :). Bromas aparte, uso de programación dinámica para tareas repetitivas.......



## Documentación del Diagrama de Entidad-Relación


### Entidades y Atributos

1. **Agencia**
   - **ID de Agencia**: Identificador único para cada agencia.
   - **Nombre**: Nombre de la agencia.
   - **Nivel**: Nivel o categoría de la agencia.
   - **Relaciones**: 
     - **Agente**: Emplea a varios agentes.
     - **Préstamo**: Administra varios préstamos.

2. **Agente**
   - **ID del Agente**: Identificador único para cada agente.
   - **Nombre del Agente**: Nombre completo del agente.
   - **ID de Agencia**: llave foránea que identifica la agencia a la que está asignado el agente.
   - **Relaciones**:
     - **Cliente**: Atiende a varios clientes.
     - **Préstamo**: Asociado a los préstamos gestionados o cobrados.

3. **Cliente**
   - **ID del Cliente**: Identificador único para cada cliente.
   - **Nombre del Cliente**: Nombre completo del cliente.
   - **Información de Contacto**: Detalles de contacto como teléfono, dirección, código postal.
   - **Relaciones**:
     - **Préstamo**: Recibe uno o más préstamos.

4. **Préstamo**
   - **ID del Préstamo**: Identificador único para cada préstamo.
   - **Monto del Préstamo**: Monto total del préstamo otorgado.
   - **Fecha de Inicio**: Fecha en que se inició el préstamo.
   - **Duración del Préstamo**: Tiempo estipulado para el pago del préstamo.
   - **ID del Cliente**: llave foránea que identifica al cliente que recibió el préstamo.
   - **Relaciones**:
     - **Pago**: Vinculado a varios pagos.
     - **Descuento**: Puede tener descuentos aplicables en diferentes semanas.

5. **Pago**
   - **ID del Pago**: Identificador único para cada pago.
   - **Monto del Pago**: Monto del pago realizado.
   - **Fecha del Pago**: Fecha en que se realizó el pago.
   - **ID del Préstamo**: llave foránea que identifica el préstamo asociado a este pago.
   - **ID del Agente**: llave foránea que identifica al agente que procesó el pago.
   - **Tarifa**: Tarifa aplicada al pago, si corresponde.

6. **Descuento**
   - **ID del Descuento**: Identificador único para cada descuento.
   - **Descripción del Crédito**: Descripción del crédito al que se aplica el descuento.
   - **Semana**: Semana en la que se aplica el descuento.
   - **Porcentaje de Descuento**: Porcentaje de descuento aplicado.
   - **ID del Préstamo**: Llave foránea que vincula el descuento con un préstamo específico.

### Relaciones

1. **Agencia - Agente**
   - **Tipo de Relación**: Uno a muchos.
   - **Descripción**: Una agencia emplea a varios agentes.
   - **Etiqueta**: emplea.

2. **Agente - Cliente**
   - **Tipo de Relación**: Uno a muchos.
   - **Descripción**: Un agente atiende a varios clientes.
   - **Etiqueta**: Atiende.

3. **Cliente - Préstamo**
   - **Tipo de Relación**: Uno a muchos.
   - **Descripción**: Un cliente puede recibir varios préstamos.
   - **Etiqueta**: recibe.

4. **Préstamo - Pago**
   - **Tipo de Relación**: Uno a muchos.
   - **Descripción**: Un préstamo puede tener varios pagos asociados.
   - **Etiqueta**: Recibe.

5. **Agente - Préstamo**
   - **Tipo de Relación**: Uno a muchos.
   - **Descripción**: Un agente puede gestionar  a varios préstamos.
   - **Etiqueta**: gestiona.

6. **Préstamo - Descuento**
   - **Tipo de Relación**: Uno a muchos.
   - **Descripción**: Un préstamo puede tener varios descuentos aplicables en diferentes semanas.
   - **Etiqueta**: tiene descuentos.

Nota: La relación entre el agente y el pago, cuya relevancia depende de cómo se manejen los procesos de pago en la organización. Si los agentes están directamente involucrados en los pagos, la relación es válida; de lo contrario, podría ser más una asociación indirecta con los préstamos(lo mismo sucede con agencia préstamo).

Vamos a demostrar que el modelo entidad-relación y la base de datos cumplen con las formas normales:

### 1. Primera Forma Normal (1FN)

Una tabla está en la 1FN si:
- Todos los atributos contienen solo valores atómicos (no hay grupos o conjuntos de valores).
- Cada registro (fila) es único.

**Demostración**:
- En las tablas (Agencia, Agente, Cliente, Préstamo, Pago, Descuento), cada atributo contiene un solo valor en cada registro. Por ejemplo, `ID del Cliente`, `Nombre del Cliente`, ........, son todos atómicos.
- Cada registro en estas tablas se puede identificar de manera única mediante su llave primaria (`ID del Préstamo`, `ID del Cliente`).

### 2. Segunda Forma Normal (2FN)

Una tabla está en la 2FN si:
- Está en 1FN.
- Todos los atributos no llave dependen completamente de la llave primaria.

**Demostración**:
- Cada tabla ya está en 1FN.
- En cada tabla, todos los atributos no llave dependen completamente de su llave primaria. Por ejemplo, en la tabla `Préstamo`, atributos como `Monto del Préstamo`, `Fecha de Inicio`, dependen completamente de `ID del Préstamo`.

### 3. Tercera Forma Normal (3FN)

Una tabla está en 3FN si:
- Está en 2FN.
- No hay dependencias transitivas de atributos no llave sobre la llave primaria.

**Demostración**:
- Todas las tablas ya están en 2FN.
- No hay dependencias transitivas en nuestras tablas.En la tabla `Pago`, aunque depende del `Préstamo` (a través de `ID del Préstamo`), no hay atributos en `Pago` que dependan de otros atributos no llave de `Préstamo`. 

### Instrucciones:

1. **Contar la Cantidad de Préstamos en la Base de Datos**:
   ```sql
   SELECT COUNT(*) FROM prestamos;
   ```
   
2. **Listar Todos los Agentes y la Cantidad de Préstamos que Manejan**:
   ```sql
   SELECT agente_id, COUNT(*) AS numero_de_prestamos
   FROM prestamos
   GROUP BY agente_id;
   ```
   
3. **Verificar un Agente Específico y sus Préstamos Asociados**:
   ```sql
   SELECT *
   FROM prestamos
   WHERE agente_id = 'AGP001';
   ```
   
4. **Verificar la Unicidad de la Combinación Agente y Préstamo**:
   ```sql
   SELECT agente_id, id, COUNT(*)
   FROM prestamos
   GROUP BY agente_id, id
   HAVING COUNT(*) > 1;
   ```
   
5. **Listar Detalles de un Préstamo Específico**:
   ```sql
   SELECT *
   FROM prestamos
   WHERE id = 'id_prestamo';  -- Reemplazar 'id_prestamo' con el ID real del préstamo que se desea verificar verificar
   ```


## Configuración del Entorno

### Entorno Virtual

Un entorno virtual, `venv`, ha sido configurado para aislar las dependencias del proyecto.

### Dependencias

- Flask: 
- SQLAlchemy: 
- psycopg2: 
- pandas: 

## Estructura del Proyecto

El proyecto sigue una estructura típica de Flask, con los siguientes directorios y archivos clave:

- `app/`: Directorio que contiene la lógica 
  - `__init__.py`: Inicializa la aplicación Flask
  - `models.py`: Define los modelos
  - `routes.py`: Rutas para manejar las solicitudes HTTP.
  - `importar_datos.py`: Script para importar datos desde un archivo Excel a la base de datos.
- `data/`: Donde se almacena el archivo Excel con los datos a importar.
- `venv/`: Entorno virtual con las dependencias del proyecto.
- `config.py`: Archivo de configuración para la aplicación Flask.
- `run.py`: Script para ejecutar el servidor de Flask.

## Base de Datos

### Modelo de Datos

La base de datos `db_bank` incluye las siguientes tablas:

- `agencias`: Almacena datos sobre agencias.
- `agentes`: Almacena datos sobre agentes.
- `clientes`: Almacena datos sobre clientes.
- `prestamos`: Almacena datos sobre préstamos.
- `pagos`: Almacena datos sobre pagos.
- `descuentos`: Almacena datos sobre descuentos aplicados a los préstamos.

### Importación de Datos

Los datos se importan desde el archivo Excel `BD PLATA XPRESS 2023. CRUDA SEMANA 44.xlsx`, utilizando el script `importar_datos.py`. Este script lee el archivo Excel, procesa los datos y los inserta en la base de datos correspondiente.

### Iniciar la Aplicación

Para iniciar la aplicación Flask, se utiliza el comando:

```sh
python run.py
```

### Importar Datos

Para importar datos a la base de datos desde el archivo Excel, se ejecuta:

```sh
python -m app.importar_datos
```


## Estado Actual del Proyecto

### Completo **L**

- Base de datos y modelos SQLAlchemy funcionales, funciones de consultas posibles.
- Rutas básicas para operaciones CRUD.

### Pendiente **X**

- Integración completa de modelos con vistas.
- Front-end.
- Pruebas unitarias (Testing).
- Subir las tablas de postgres y comentar el código un poco más, mejorar el informe.

# Instrucciones para Reconstruir la Base de Datos

--Falta por subir.

# Autofeedback :)

-- Mejorar el trabajo con postgressql, me vi en situaciones de dificultad en el trabajo con modelos/importacion_de_datos/tablas en SQL.
-- Estudiar más SQL, faltan cosas por aprender. 
-- Mejorar comentarios en git jeje, trabajar más ordenado, recomendado ToDo List, cosa que me afecto.
-- Mejorar el Debugg.
-- Dejar de impresionarme con Python(siempre me impresionna:)).

