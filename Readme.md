## Documentación del Diagrama de Entidad-Relación

### Descripción General
Este diagrama de entidad-relación representa la estructura de la base de datos para el sistema de gestión de préstamos y pagos.

### Entidades y Atributos

1. **Agencia**
   - **ID de Agencia**: Identificador para cada agencia.
   - **Nombre**: Nombre de la agencia.
   - **Nivel**: Nivel o categoría de la agencia.
   - **Relaciones**: 
     - **Agente**: Emplea a varios agentes.
     - **Préstamo**: Origina o administra varios préstamos.

2. **Agente**
   - **ID del Agente**: Identificador para cada agente.
   - **Nombre del Agente**: Nombre completo del agente.
   - **ID de Agencia**: Identificador de la agencia a la que está asignado.
   - **Relaciones**:
     - **Pago**: Gestiona o recibe varios pagos.
     - **Cliente**: Atiende o gestiona a varios clientes.

3. **Cliente**
   - **ID del Cliente**: Identificador para cada cliente.
   - **Nombre del Cliente**: Nombre completo del cliente.
   - **Información de Contacto**: Detalles de contacto como teléfono.
   - **Relaciones**:
     - **Préstamo**: Obtiene varios préstamos.

4. **Préstamo**
   - **ID del Préstamo**: Identificador para cada préstamo.
   - **Monto del Préstamo**: Monto total del préstamo otorgado.
   - **Fecha de Inicio**: Fecha en que se inició el préstamo.
   - **ID del Cliente**: Identificador del cliente que recibió el préstamo.
   - **Relaciones**:
     - **Pago**: Recibe varios pagos.

5. **Pago**
   - **ID del Pago**: Identificador para cada pago.
   - **Monto del Pago**: Monto del pago realizado.
   - **Fecha del Pago**: Fecha en que se realizó el pago.
   - **ID del Préstamo**: Identificador del préstamo asociado a este pago.
   - **ID del Agente**: Identificador del agente que procesó el pago.
   - **Tarifa**: Tarifa asociada con el pago.

### Relaciones

1. **Agencia - Préstamo**
   - **Tipo de Relación**: Uno a muchos.
   - **Descripción**: Cada préstamo es administrado por una agencia específica.
   - **Etiqueta**: administra.

2. **Agente - Cliente**
   - **Tipo de Relación**: Uno a muchos.
   - **Descripción**: Cada agente es responsable de atender a ciertos clientes.
   - **Etiqueta**: atiende.

3. **Agencia - Agente**
   - **Tipo de Relación**: Uno a muchos.
   - **Descripción**: Cada agencia emplea a varios agentes, que son responsables de gestionar los préstamos y pagos.
   - **Etiqueta**: emplea.

4. **Agente - Pago**
   - **Tipo de Relación**: Uno a muchos.
   - **Descripción**: Los agentes gestionan varios pagos de los clientes en relación con los préstamos.
   - **Etiqueta**: gestiona.

5. **Cliente - Préstamo**
   - **Tipo de Relación**: Uno a muchos.
   - **Descripción**: Un cliente puede tener varios préstamos, cada uno con sus propias condiciones y términos.
   - **Etiqueta**: tiene.

6. **Préstamo - Pago**
   - **Tipo de Relación**: Uno a muchos.
   - **Descripción**: Cada préstamo puede tener varios pagos asociados a lo largo de su duración.
   - **Etiqueta**: recibe.

