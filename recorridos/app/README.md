# Automa Recorridos (app instalable)

App web que se instala en el celular y funciona **sin internet**.
Los técnicos abren el PDF del plano, encierran cada salida en 🔴 🟡 🟢,
agregan textos y fotos, y envían el PDF marcado por WhatsApp.

## Publicar (GitHub Pages)

1. En GitHub: repo `mauriciomasri` → **Settings → Pages**.
2. *Source*: **Deploy from a branch** → rama con esta carpeta → carpeta **/ (root)** → **Save**.
3. En 1–2 minutos queda en:
   `https://mauriciomasri.github.io/mauriciomasri/recorridos/app/`

## Instalar en el celular (una sola vez, con internet)

- **iPhone (Safari):** abrir el enlace → botón Compartir → **Agregar a inicio**.
- **Android (Chrome):** abrir el enlace → menú ⋮ → **Instalar app**.

Después se abre siempre desde el ícono **Recorridos**, con o sin señal.

## Actualizar la app

`index.html` es la fuente de la app. Después de cualquier cambio sube
`VERSION` en `sw.js` y `APP_VERSION` en `index.html`. Los celulares reciben la
versión nueva la próxima vez que abren la app con internet (se recarga sola).

## Contenido

| Archivo | Qué es |
|---|---|
| `index.html` | La app (portada, resumen, planos marcados y fotos en el PDF) |
| `logo.png` | Logo de Automa para las hojas del PDF |
| `sw.js` | Guarda la app en el celular para usarla sin internet |
| `manifest.webmanifest`, `icons/` | Nombre e ícono al instalarla |
| `lib/` | pdf.js 3.11.174 (Apache-2.0) y pdf-lib 1.17.1 (MIT) |
| `fonts/` | Barlow y Barlow Condensed (SIL OFL) |
