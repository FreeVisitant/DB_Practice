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
   - **Etiqueta**: atiende.

3. **Cliente - Préstamo**
   - **Tipo de Relación**: Uno a muchos.
   - **Descripción**: Un cliente puede recibir varios préstamos.
   - **Etiqueta**: recibe.

4. **Préstamo - Pago**
   - **Tipo de Relación**: Uno a muchos.
   - **Descripción**: Un préstamo puede tener varios pagos asociados.
   - **Etiqueta**: tiene pagos.

5. **Agente - Préstamo**
   - **Tipo de Relación**: Uno a muchos.
   - **Descripción**: Un agente puede gestionar  a varios préstamos.
   - **Etiqueta**: gestiona.

6. **Préstamo - Descuento**
   - **Tipo de Relación**: Uno a muchos.
   - **Descripción**: Un préstamo puede tener varios descuentos aplicables en diferentes semanas.
   - **Etiqueta**: tiene descuentos.


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


