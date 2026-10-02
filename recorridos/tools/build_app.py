"""Genera app/index.html (versión instalable sin internet) a partir de recorrido.html."""
import pathlib
base = pathlib.Path(__file__).resolve().parent.parent
s = (base / "recorrido.html").read_text()

def R(o, n, c=1):
    global s
    assert s.count(o) == c, (o[:80], s.count(o))
    s = s.replace(o, n)

# ---- head / fonts ----
R('''<title>Recorrido de Obra Automa</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700&family=Barlow+Condensed:wght@500;600;700&display=swap">
<style>''', '''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,viewport-fit=cover">
<title>Automa Recorridos</title>
<meta name="theme-color" content="#1f4e79">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icons/icon-192.png">
<link rel="apple-touch-icon" href="icons/icon-180.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Recorridos">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<style>
@font-face{font-family:"Barlow";font-weight:400;font-display:swap;src:url(fonts/barlow-latin-400-normal.woff2) format("woff2")}
@font-face{font-family:"Barlow";font-weight:500 600;font-display:swap;src:url(fonts/barlow-latin-600-normal.woff2) format("woff2")}
@font-face{font-family:"Barlow";font-weight:700;font-display:swap;src:url(fonts/barlow-latin-700-normal.woff2) format("woff2")}
@font-face{font-family:"Barlow Condensed";font-weight:500 600;font-display:swap;src:url(fonts/barlow-condensed-latin-600-normal.woff2) format("woff2")}
@font-face{font-family:"Barlow Condensed";font-weight:700;font-display:swap;src:url(fonts/barlow-condensed-latin-700-normal.woff2) format("woff2")}
*{-webkit-tap-highlight-color:transparent}
body{margin:0;-webkit-text-size-adjust:100%;overscroll-behavior:none}''')
R('''</style>

<div class="app">''', '''.top{padding-top:calc(8px + env(safe-area-inset-top,0px))}
.install{border:1px dashed var(--line);border-radius:10px;padding:12px 14px;display:flex;flex-direction:column;gap:6px;font-size:14px;line-height:1.45}
.install b{font-family:var(--f-label);font-size:16px}
.fotos{display:flex;flex-wrap:wrap;gap:8px}
.foto{position:relative;width:76px;height:76px;border-radius:8px;overflow:hidden;border:1px solid var(--line)}
.foto img{width:100%;height:100%;object-fit:cover;display:block}
.foto button{position:absolute;top:2px;right:2px;width:24px;height:24px;border-radius:50%;border:0;background:rgba(0,0,0,.6);color:#fff;font-size:14px;line-height:24px;padding:0}
.addfoto{width:76px;height:76px;border-radius:8px;border:1.5px dashed var(--line);background:var(--bg);display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:12px;font-weight:600;color:var(--muted);gap:2px}
.addfoto span{font-size:22px;line-height:1}
.sheet .stack{display:flex;flex-direction:column;gap:10px}
.sheet .stack .btn{padding:14px;font-size:16px}
</style>
</head>
<body>

<div class="app">''')

# ---- install hint ----
R('''          <button class="linkbtn" id="demoBtn" type="button">Probar con un plano de ejemplo</button>
        </div>''', '''          <button class="linkbtn" id="demoBtn" type="button">Probar con un plano de ejemplo</button>
        </div>
        <div class="install" id="installHint" hidden>
          <b>Instálala para usarla sin internet</b>
          <span id="installTxt"></span>
          <button class="btn primary" id="installBtn" type="button" hidden>Instalar app</button>
        </div>''')

# ---- scripts ----
R('''<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf-lib/1.17.1/pdf-lib.min.js"></script>''', '''<script src="lib/pdf.min.js"></script>
<script src="lib/pdf-lib.min.js"></script>''')
R('pdfjsLib.GlobalWorkerOptions.workerSrc = "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js";',
  'pdfjsLib.GlobalWorkerOptions.workerSrc = "lib/pdf.worker.min.js";')
head, tail = s.rsplit('</script>', 1)
s = head + '''</script>
<script>
if ("serviceWorker" in navigator) addEventListener("load", () => navigator.serviceWorker.register("sw.js").catch(() => {}));
</script>
</body>
</html>''' + tail

# ---- photos in mark sheet ----
R('''        <textarea id="notaIn" placeholder="${isA ? "Ej. caja 5 cm abajo del nivel" : "Opcional"}">${esc(m.nota || "")}</textarea></div>''',
'''        <textarea id="notaIn" placeholder="${isA ? "Ej. caja 5 cm abajo del nivel" : "Opcional"}">${esc(m.nota || "")}</textarea></div>
      <div class="field"><label class="lbl">Fotos</label><div class="fotos" id="fotosBox"></div></div>''')
R('''      bindChips(root, "mot", v => draft.mot = v);
      bindChips(root, "resp", v => draft.resp = v);
      $("okMk").onclick = () => {
        const nota = $("notaIn").value.trim();
        if (draft.mot !== m.mot || draft.resp !== m.resp || nota !== (m.nota || "")) {
          if (!fresh) snapshot();
          m.mot = draft.mot; m.resp = draft.resp; m.nota = nota; changed();
        }
        closeSheet();
      };''', '''      bindChips(root, "mot", v => draft.mot = v);
      bindChips(root, "resp", v => draft.resp = v);
      let fotos = (m.fotos || []).slice();
      const paintFotos = () => {
        $("fotosBox").innerHTML = fotos.map((f, i) => `<div class="foto"><img src="${f}" alt="Foto ${i + 1}"><button type="button" data-i="${i}" aria-label="Quitar foto">×</button></div>`).join("") +
          `<button type="button" class="addfoto" id="addFoto"><span>+</span>Foto</button>`;
        $("fotosBox").querySelectorAll(".foto button").forEach(b => b.onclick = () => { fotos.splice(+b.dataset.i, 1); paintFotos(); });
        $("addFoto").onclick = () => pickPhoto(async f => { try { fotos.push(await shrinkPhoto(f)); paintFotos(); } catch (e) { toast("No se pudo leer la foto"); } });
      };
      paintFotos();
      $("okMk").onclick = () => {
        const nota = $("notaIn").value.trim();
        const fotosChanged = JSON.stringify(fotos) !== JSON.stringify(m.fotos || []);
        if (draft.mot !== m.mot || draft.resp !== m.resp || nota !== (m.nota || "") || fotosChanged) {
          if (!fresh) snapshot();
          m.mot = draft.mot; m.resp = draft.resp; m.nota = nota; m.fotos = fotos; changed();
        }
        closeSheet();
      };''')
R('''  function openTextSheet(m, at) {''', '''  function pickPhoto(cb) {
    const inp = document.createElement("input");
    inp.type = "file"; inp.accept = "image/*";
    inp.onchange = () => { if (inp.files[0]) cb(inp.files[0]); };
    inp.click();
  }
  function shrinkPhoto(file) {
    return new Promise((res, rej) => {
      const url = URL.createObjectURL(file), img = new Image();
      img.onload = () => {
        const k = Math.min(1, 1280 / Math.max(img.width, img.height));
        const c = document.createElement("canvas");
        c.width = Math.round(img.width * k); c.height = Math.round(img.height * k);
        c.getContext("2d").drawImage(img, 0, 0, c.width, c.height);
        URL.revokeObjectURL(url); res(c.toDataURL("image/jpeg", 0.72));
      };
      img.onerror = () => { URL.revokeObjectURL(url); rej(new Error("foto")); };
      img.src = url;
    });
  }
  function openTextSheet(m, at) {''')
R('''${m.n} · ${esc(label(m))}</text></g>`);''', '''${m.n} · ${esc(label(m))}${m.fotos && m.fotos.length ? " 📷" : ""}</text></g>`);''')

# ---- photos in PDF ----
R('''    sp.drawText("Automa · Abre este PDF en la página de recorridos para continuar el siguiente recorrido."''', '''    const conFoto = circ.filter(m => m.fotos && m.fotos.length).sort((a, b) => a.n - b.n);
    let slot = 2, fp = null;
    for (const m of conFoto) {
      for (const f of m.fotos) {
        if (slot === 2) { fp = pdf.addPage([W, H]); slot = 0; fp.drawText(safe(`Fotos - ${S.meta.obra}`), { x: M, y: H - M, size: 14, font }); }
        const img = await pdf.embedJpg(Uint8Array.from(atob(f.split(",")[1]), ch => ch.charCodeAt(0)));
        const boxW = (W - 2 * M - 20) / 2, boxH = H - 2 * M - 50;
        const k = Math.min(boxW / img.width, boxH / img.height);
        const x0 = M + slot * (boxW + 20), y0 = M + 20;
        fp.drawImage(img, { x: x0, y: y0 + (boxH - img.height * k), width: img.width * k, height: img.height * k });
        const c = ST[m.st];
        fp.drawText(safe(`${m.n} · ${c.name}${m.st === "amarillo" && m.mot ? " - " + m.mot : ""}${m.nota ? " - " + m.nota : ""}`).slice(0, 70), { x: x0, y: y0 - 4, size: 9, font, color: rgb(...c.text) });
        slot++;
      }
    }
    sp.drawText("Automa · Abre este PDF en la app Automa Recorridos para continuar el siguiente recorrido."''')

# ---- save / share ----
i = s.index('  $("saveBtn").onclick = async () => {'); j = s.index('  /* ---------- demo plan ---------- */')
s = s[:i] + '''  async function makeFile() {
    const bytes = await buildPdf();
    return new File([bytes], fileName(), { type: "application/pdf" });
  }
  function downloadFile(file) {
    const a = document.createElement("a"), url = URL.createObjectURL(file);
    a.href = url; a.download = file.name; document.body.appendChild(a); a.click(); a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 60000);
  }
  $("saveBtn").onclick = async () => {
    if (!S.marks.length) { toast("Aún no hay nada marcado en el plano"); return; }
    if (!S.meta.tecnico) { openMetaSheet(); toast("Pon tu nombre antes de enviar"); return; }
    const btn = $("saveBtn"); btn.disabled = true; btn.textContent = "Generando…";
    let file;
    try { file = await makeFile(); }
    catch (e) { toast("No se pudo generar el PDF. Intenta de nuevo."); return; }
    finally { btn.disabled = false; btn.textContent = "Enviar"; }
    const canShare = !!(navigator.canShare && navigator.canShare({ files: [file] }));
    sheet(`
      <h2>PDF listo</h2>
      <p class="note">${esc(file.name)} · ${(file.size / 1048576).toFixed(1)} MB</p>
      <div class="stack">
        ${canShare ? `<button type="button" class="btn primary" id="shareBtn">Enviar por WhatsApp, correo…</button>` : ""}
        <button type="button" class="btn${canShare ? "" : " primary"}" id="dlBtn">Guardar en el celular</button>
      </div>
      <p class="note">Si no tienes señal, guárdalo y envíalo después. El recorrido también queda guardado en la app.</p>`, () => {
      const sb = $("shareBtn");
      if (sb) sb.onclick = async () => {
        try { await navigator.share({ files: [file], title: file.name }); closeSheet(); toast("Enviado"); }
        catch (e) { if (e && e.name !== "AbortError") toast("No se pudo compartir. Usa Guardar en el celular."); }
      };
      $("dlBtn").onclick = () => { downloadFile(file); closeSheet(); toast("PDF guardado en Descargas"); };
    });
  };

  /* ---------- install hint ---------- */
  const standalone = matchMedia("(display-mode: standalone)").matches || navigator.standalone === true;
  if (!standalone) {
    const ios = /iPhone|iPad|iPod/.test(navigator.userAgent) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);
    $("installTxt").textContent = ios
      ? "En Safari toca el botón Compartir (cuadro con flecha) y luego “Agregar a inicio”. Ábrela siempre desde ese ícono."
      : "En Chrome toca el menú ⋮ y luego “Instalar app” o “Agregar a pantalla principal”. Ábrela siempre desde ese ícono.";
    $("installHint").hidden = false;
    let deferred = null;
    addEventListener("beforeinstallprompt", e => { e.preventDefault(); deferred = e; $("installBtn").hidden = false; });
    $("installBtn").onclick = async () => { if (!deferred) return; deferred.prompt(); await deferred.userChoice.catch(() => {}); deferred = null; $("installBtn").hidden = true; };
  }

''' + s[j:]
R('<button class="btn primary" id="saveBtn" type="button" hidden>Descargar</button>', '<button class="btn primary" id="saveBtn" type="button" hidden>Enviar</button>')
R('<span>Descarga el PDF marcado y mándalo a Mauricio.</span>', '<span>Toca <strong>Enviar</strong> y manda el PDF marcado a Mauricio.</span>')
assert "cdnjs" not in s and "googleapis" not in s and "window.claude" not in s
(base / "app" / "index.html").write_text(s)
print("app/index.html", len(s))
