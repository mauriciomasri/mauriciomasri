# Recorridos de obra — Automa

Sustituye los círculos a mano en el plano por una captura digital del técnico,
guardada en Odoo y dibujada en AutoCAD de forma automática.

## Flujo

```
1. AutoCAD   → AUTOMA.lsp numera las salidas sin ID y exporta la lista (CSV)
2. Odoo      → importas la lista de salidas a la obra (una sola vez por obra)
3. Técnico   → en su celular marca cada salida 🔴 🟡 🟢 (+ motivo, nota, foto)
4. Odoo      → importas el recorrido; cada salida queda con su status y su historial
5. AutoCAD   → un comando lee el CSV y dibuja los círculos de color con su nota
6. Odoo      → PDF de pendientes para la obra (lo que le toca al contratista)
```

Los técnicos **no necesitan usuario de Odoo**: capturan en una página web
sencilla desde el celular. Solo tú entras a Odoo.

## Status de cada salida

| Status | Significado | Se captura |
|---|---|---|
| 🔴 Rojo — Falta tubería | No hay canalización | — |
| 🟡 Amarillo — Detalle pendiente | Hay avance, pero falta algo | Motivo + responsable + nota/foto |
| 🟢 Verde — Lista | Tubería en su lugar y cableada | (foto opcional) |

Motivos del amarillo:

- Falta cablear
- Falta bajada de tubería
- Caja mal puesta
- Ubicación ligeramente mal
- Otro (con nota)

Responsable: **Automa** o **Obra** (contratista / albañil).

## ID de cada salida

El ID es la etiqueta que pone `AUTOMA.lsp`: `Prefijo #N` (p. ej. `Cam #3`,
`Bot4 #12`). Es único **por obra**. Las salidas sin etiqueta se numeran con un
comando nuevo del LISP antes de exportar.

## Formato CSV del recorrido

Lo genera la página del técnico; lo leen Odoo (importar) y AutoCAD (círculos).

```csv
obra,fecha,tecnico,salida,planta,status,motivo,responsable,nota
Altezza GH,2026-09-29,Juan,Cam #3,PB,amarillo,Caja mal puesta,Obra,"Caja 5 cm abajo"
Altezza GH,2026-09-29,Juan,Bot4 #12,PA,verde,,,
Altezza GH,2026-09-29,Juan,Vid #2,PB,rojo,,,
```

## Configuración en Odoo 19 (Studio)

Las obras ya existen como **cotización de venta**, así que todo cuelga de ahí.

### 1. App nueva "Recorridos"

Studio → **Nueva app** → nombre `Recorridos`. Crea tres modelos:

**Salidas** (una fila por salida del plano)

| Campo | Tipo en Studio | Notas |
|---|---|---|
| Nombre | Texto (el de default) | El ID: `Cam #3` |
| Obra | Muchos a uno → Pedido de venta | |
| Sistema | Selección | Redes, Audio, Video, Seguridad, Telefonía, Alexa, Site, Iluminación |
| Planta | Selección | PB, PA, Sótano, Azotea (agrega las que uses) |
| Zona | Texto | Cocina, Estancia… (opcional) |
| Status | Selección | Rojo, Amarillo, Verde — **vista con colores (badge)** |
| Motivo | Selección | Lista de arriba |
| Responsable | Selección | Automa, Obra |
| Nota | Texto | |
| Último recorrido | Fecha | |

**Recorridos** (una fila por visita)

| Campo | Tipo en Studio |
|---|---|
| Nombre | Texto (p. ej. `Altezza GH — 29 sep`) |
| Obra | Muchos a uno → Pedido de venta |
| Fecha | Fecha |
| Técnico | Texto (no son usuarios de Odoo) |
| Revisiones | **Líneas** (Studio crea el modelo de líneas solo) |
| Notas generales | Texto multilínea |

**Revisiones** (las líneas del recorrido): Salida (Muchos a uno → Salidas),
Status, Motivo, Responsable, Nota, Foto (Imagen).

### 2. Botones en la cotización

En la vista del pedido de venta, con Studio agrega los **botones inteligentes**
`Salidas` y `Recorridos` (relación por el campo *Obra*).

### 3. Acción automática: actualizar la salida

Ajustes → Técnico → Automatización → Nueva:

- Modelo: **Revisiones** · Disparador: **Al crear**
- Acción: **Ejecutar código**

```python
for rev in records:
    rev.x_studio_salida.write({
        'x_studio_status': rev.x_studio_status,
        'x_studio_motivo': rev.x_studio_motivo,
        'x_studio_responsable': rev.x_studio_responsable,
        'x_studio_nota': rev.x_studio_nota,
        'x_studio_ultimo_recorrido': rev.x_studio_recorrido.x_studio_fecha,
    })
```

> Los nombres `x_studio_...` dependen de cómo los nombres en Studio. Revísalos
> en modo desarrollador (pasando el mouse sobre el campo) y ajústalos aquí.

### 4. Vistas útiles

- **Salidas → Kanban agrupado por Status**: ves de un vistazo qué falta.
- **Salidas → Lista agrupada por Obra y Planta**, con filtro "Responsable = Obra".
- **Recorridos → Gráfica** de salidas por status por fecha (avance mes a mes).

### 5. PDF de pendientes para la obra

Studio → Recorridos → Informes → Nuevo: tabla de Revisiones con status
amarillo/rojo y responsable **Obra** (Salida, Planta, Motivo, Nota, Foto).

## Pendiente

- [ ] Comando LISP: numerar salidas sin ID y exportar lista de salidas (CSV)
- [ ] Comando LISP: dibujar círculos de status desde el CSV del recorrido
- [ ] Página de captura para técnicos (celular)
- [ ] Configurar Studio según esta guía
