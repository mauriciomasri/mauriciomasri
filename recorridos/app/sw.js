// Guarda la app completa en el celular para que funcione sin internet.
// Al cambiar cualquier archivo de la app, sube VERSION para que se actualice.
const VERSION = "recorridos-v1";
const FILES = [
  "./",
  "index.html",
  "manifest.webmanifest",
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
  e.waitUntil(caches.open(VERSION).then(c => c.addAll(FILES)).then(() => self.skipWaiting()));
});

self.addEventListener("activate", e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== VERSION).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", e => {
  if (e.request.method !== "GET") return;
  e.respondWith(
    caches.match(e.request, { ignoreSearch: true }).then(hit => hit || fetch(e.request).catch(() =>
      e.request.mode === "navigate" ? caches.match("index.html") : Response.error()))
  );
});
