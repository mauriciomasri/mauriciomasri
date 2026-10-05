# Encargo para Cowork: instalar y probar Recorridos v1.9.3 en el Odoo de Automa

Hola. Soy Mauricio (Automa). Este módulo lo hizo Claude Code, que no tiene acceso a mi Odoo. Te pido que lo instales y lo pruebes en el Odoo real.

## Datos

- **Odoo:** https://automaproyecto.odoo.com (Odoo 19 Online, Enterprise, con Studio, Ventas y Firma electrónica).
- **Archivo a instalar:** `recorridos_v1_9_3.zip` (va adjunto).
- **Mi otro módulo:** "Planos" (`automa_planos` v1.7.0), el que tú hiciste para mandar planos a firma desde planos@automaproyecto.com. **No lo modifiques.** Recorridos solo llama a su acción `automa_planos.action_enviar_firma`.
- **Código fuente:** GitHub `mauriciomasri/mauriciomasri`, rama `claude/odoo-system-designs-ikp2i6`, carpeta `recorridos/odoo/automa_recorridos`.
- **App de técnicos:** https://mauriciomasri.github.io/mauriciomasri/recorridos/app/ (se conecta con el enlace que genera Odoo).

## Qué hacer

1. **Instalar:** Aplicaciones → Importar módulo → `recorridos_v1_9_3.zip` → Importar.
   - Es normal que salgan avisos de "External ID not found" al importar.
   - Si sale un error en rojo, cópialo completo y no sigas.
2. **Limpiar pruebas:** en Recorridos → Obras, borra las obras **Trg** y **Yjj**. Se van con sus recorridos.
3. **Correos de recorridos:**
   - En Recorridos → Conectar app de técnicos → "Avisar por correo a", deja mi usuario.
   - En mi usuario → Preferencias, revisa que Notificaciones esté en "Por correo".
4. **Probar la firma con una orden de prueba:**
   - Crea o usa una cotización de prueba cuyo cliente tenga **mi correo** (maurimasri@gmail.com). **No uses un cliente real.**
   - En la pestaña Planos, sube un PDF con descripción "Prueba firma".
   - Guarda y pica **Mandar a firmar**.
   - Revisa que:
     - en el módulo Planos se creó el registro "Obra - Prueba firma" en Enviado;
     - el correo de firma salió desde planos@automaproyecto.com;
     - la firma cae bien en cada página (posición de firma del módulo Planos).
   - Firma desde el correo.
   - Vuelve a la orden: la columna Firma debe decir **Firmado** y **Ver firmado** debe descargar el PDF firmado.
5. **Probar un recorrido:**
   - Abre la app desde el enlace de Conectar app de técnicos.
   - Entra a Planos de obras, abre el plano de prueba, marca 2 círculos y pica Guardar.
   - Revisa que me llegó el correo "Nuevo recorrido: …".
   - Abre el mismo plano otra vez: debe ofrecer "Partir del último recorrido".
6. **Borrar lo de prueba** al final: la cotización, la obra y el registro en Planos.

## Reglas

- **No cambies el código de Recorridos en mi Odoo con Studio:** se perdería al actualizar.
- Si algo falla, anota en qué paso falló, el mensaje de error completo y una captura. Yo se lo paso a Claude Code para corregirlo en el código.
- **No envíes nada a clientes reales.**

## Qué me devuelves

Una lista de los pasos 1–6, cada uno con ✅ o ❌, y en cada ❌ el error y la captura.
