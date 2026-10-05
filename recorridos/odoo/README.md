# Módulo Odoo: Recorridos

Guarda en Odoo los recorridos que hacen los técnicos con la app
(`../app/`). Funciona en **Odoo 19 Online** como módulo de datos (igual que
*Entregas*).

## Qué agrega

- **Obras**: cada obra junta todos sus recorridos (día 2, día 4, día 8…) y
  lleva su status **En curso / Completado / Cancelado**. Por defecto solo se
  ven las obras en curso (quita el filtro para ver las demás). Se crean solas
  con el primer recorrido de esa obra.
- Historial completo: un recorrido corregido el mismo día guarda el PDF
  anterior en su historial; si se manda en otra fecha, se crea un recorrido
  nuevo.

- App **Recorridos** con la lista de recorridos: fecha, obra, cotización,
  técnico, conteo 🔴 🟡 🔵 🟢, % cableado, % terminado y el PDF.
- Ficha de cada recorrido con el **PDF visible dentro de Odoo** y chatter.
- En la **cotización**, botón **Recorridos** con los de esa obra y un mensaje
  en su historial cada vez que llega uno.
- Gráfica de avance por mes.
- Webhook *“Recorridos: recibir desde la app de técnicos”* (Ajustes →
  Técnico → Automatizaciones) que recibe el PDF desde la app.

## Instalar

1. Odoo → **Aplicaciones → Importar módulo** → sube `recorridos_vX_Y_Z.zip` (el más reciente).
2. Abre la app **Recorridos → Conectar app de técnicos**. Se abre la app ya
   conectada a tu Odoo; copia ese enlace y mándalo a tus técnicos.
3. Cada técnico abre el enlace (con internet) y lo instala como siempre.
   Si ya tenía la app instalada: **toca el nombre de la obra → Conexión con
   Odoo → pega el enlace**.

## Planos de obras (la app los baja de Odoo)

- En la **orden de venta**, pestaña **Planos**: sube los que necesites
  (Canalizaciones, Especiales, Trayectorias u Otro). Al abrir uno se ve la
  vista previa.
- Una obra está **viva** si su orden tiene plano y la obra no está en
  *Completado* ni *Cancelado*. Solo las vivas aparecen en la app.
- En la app, **Planos de obras** lista las obras vivas; se elige el plano y el
  recorrido queda ligado a esa orden y a ese plano. Los planos bajados se guardan en el iPad
  para usarlos sin señal.
- Tras actualizar el módulo, vuelve a mandar el enlace de **Conectar app de
  técnicos** (ahora trae también el acceso a los planos).

## Corregir nombres de obra

- **Renombrar**: abre la obra y cambia el nombre.
- **Mover recorridos**: en la lista de Recorridos selecciónalos y cambia
  **Obra** en uno; se aplica a todos los seleccionados. Luego borra la obra
  que quedó vacía.
- Los siguientes recorridos que lleguen con el mismo nombre mal escrito se
  van solos a la obra correcta.

## Cómo se liga con la cotización

Con el nombre de obra que escribe el técnico, el webhook busca **una sola**
cotización por número (`S00123`), referencia del cliente o nombre del
cliente. Si no la encuentra o hay varias, el recorrido queda **sin cotización
ligada** (filtro en la lista) y se asigna a mano en la ficha.

## Seguridad

La dirección del webhook solo permite **crear o actualizar recorridos**.
Si se filtra, en la automatización usa **Rotar UUID** y vuelve a mandar el
enlace de *Conectar app de técnicos*.

## Probado

Se probó en un Odoo 19 Community local: importación limpia, envío de un PDF de
13 MB, liga automática con la cotización, reenvío del mismo recorrido
(se actualiza, no se duplica), envío sin señal que sube al volver el internet,
y reimportación del módulo conservando la dirección del webhook.
