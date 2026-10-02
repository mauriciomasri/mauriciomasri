// Guarda la app en el celular para que funcione sin internet.
// La página se busca primero en internet (para recibir actualizaciones) y, si no hay señal,
// se usa la copia guardada. Al cambiar cualquier archivo de la app, sube VERSION.
const VERSION = "recorridos-v17";
const FILES = [
  "./",
  "index.html",
  "manifest.webmanifest",
  "logo.png",
  "lib/pdf.min.js",
  "lib/pdf.worker.min.js",
  "lib/pdf-lib.min.js",
  "fonts/barlow-latin-400-normal.woff2",
  "fonts/barlow-latin-600-normal.woff2",
  "fonts/barlow-latin-700-normal.woff2",
  "fonts/barlow-condensed-latin-600-normal.woff2",
  "fonts/barlow-condensed-latin-700-normal.woff2",
  "icons/icon-180.png",
  "icons/icon-192.png",
  "icons/icon-512.png",
  "icons/icon-512-maskable.png",
];

self.addEventListener("install", e => {
  e.waitUntil(caches.open(VERSION).then(c => c.addAll(FILES.map(f => new Request(f, { cache: "reload" })))).then(() => self.skipWaiting()));
});

self.addEventListener("activate", e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== VERSION).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", e => {
  const req = e.request;
  if (req.method !== "GET") return;
  if (req.mode === "navigate") {
    // Primero internet (con límite de 4 s), luego la copia guardada.
    e.respondWith((async () => {
      try {
        const ctrl = new AbortController(); const t = setTimeout(() => ctrl.abort(), 4000);
        const res = await fetch(req, { cache: "no-store", signal: ctrl.signal }); clearTimeout(t);
        if (res.ok) (await caches.open(VERSION)).put("index.html", res.clone());
        return res;
      } catch (err) {
        return (await caches.match("index.html")) || (await caches.match("./")) || Response.error();
      }
    })());
    return;
  }
  e.respondWith(caches.match(req, { ignoreSearch: true }).then(hit => hit || fetch(req)));
});
