// Estilo claro v7: node render7.mjs slides.json saida/
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
const slides = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const out = process.argv[3];
const profile = JSON.parse(fs.readFileSync('perfil.json', 'utf8'));
fs.mkdirSync(out, { recursive: true });
const b64 = (f, t) => `data:${t};base64,${fs.readFileSync(path.resolve(f)).toString('base64')}`;
const font = f => b64(path.join('fontes', f), 'font/ttf');
const AV = b64('fotos/exemplo-usuario-1.jpg', 'image/jpeg');
const hl = t => t.replace(/\*\*(.+?)\*\*/g, '<mark>$1</mark>');
const CSS = `
@font-face{font-family:B;font-weight:800;src:url('${font('bricolage-800.ttf')}')}
@font-face{font-family:J;font-weight:400 800;src:url('${font('jakarta.ttf')}')}
:root{--ink:#0F172A;--mut:#64748B;--y:#FFD23F;--line:#E8EAEE}
*{margin:0;box-sizing:border-box}
body{width:1080px;height:1350px;overflow:hidden;background:#fff;color:var(--ink);font-family:J,sans-serif;position:relative}
.head{position:absolute;top:52px;left:56px;right:56px;display:flex;align-items:center;gap:20px}
.av{width:92px;height:92px;border-radius:50%;overflow:hidden;position:relative;box-shadow:0 0 0 4px #fff,0 0 0 8px var(--ink)}
.av img{position:absolute;left:-64px;top:-40px;transform-origin:64px 40px;transform:scale(.72)}
.nm{font:800 38px B}.hd{font-size:27px;color:var(--mut)}
.pg{margin-left:auto;font-weight:800;font-size:26px;color:var(--mut)}
h1,h2{font-family:B;font-weight:800;letter-spacing:-1.5px}
mark{background:var(--y);color:var(--ink);padding:0 10px;border-radius:12px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.chip{display:inline-block;background:var(--y);color:var(--ink);font-weight:800;font-size:26px;letter-spacing:2px;padding:12px 26px;border-radius:99px;text-transform:uppercase}
.foot{position:absolute;left:56px;right:56px;bottom:50px;display:flex;align-items:center}
.pd{display:flex;gap:10px}.pd i{width:16px;height:16px;border-radius:50%;background:#D5D9E0}.pd i.on{background:var(--ink);width:50px;border-radius:10px}
.sw{margin-left:auto;display:flex;align-items:center;gap:14px;font:800 30px B}
.sw b{width:68px;height:68px;border-radius:50%;background:var(--ink);color:#fff;display:grid;place-items:center;font-size:34px}
.step{display:flex;gap:30px;align-items:center;padding:34px 0;border-bottom:3px solid var(--line)}
.step:last-child{border:0}.step .n{flex:none;width:100px;height:100px;border-radius:50%;background:var(--ink);color:var(--y);display:grid;place-items:center;font:800 54px B}
.step h3{font:800 54px/1.05 B;letter-spacing:-1px}.step p{font-size:32px;color:var(--mut);margin-top:8px;line-height:1.3}
.opt{flex:1;border-radius:44px;padding:44px 36px;border:5px solid var(--ink);text-align:center}
.opt b{display:block;font:800 150px/1 B}.opt span{font:800 48px B}
`;
const mk = (s, i, n) => {
  const head = `<div class="head"><div class="av"><img src="${AV}"></div><div><div class="nm">${profile.name}</div><div class="hd">${profile.handle}</div></div><div class="pg">${i + 1}/${n}</div></div>`;
  const foot = `<div class="foot"><div class="pd">${slides.map((_, k) => `<i class="${k === i ? 'on' : ''}"></i>`).join('')}</div>${i < n - 1 ? '<div class="sw">Arrasta <b>→</b></div>' : ''}</div>`;
  let body = '';
  if (s.type === 'cover') body = `<div style="position:absolute;left:56px;right:56px;top:190px;height:720px;border-radius:52px;background:url('${b64(s.photo, 'image/jpeg')}') ${s.pos || 'center 25%'}/cover"></div>
<div style="position:absolute;left:88px;top:840px"><span class="chip">${s.chip}</span></div>
<h1 style="position:absolute;left:56px;right:56px;top:945px;font-size:80px;line-height:1.04">${hl(s.title)}</h1>`;
  else if (s.type === 'big') body = `<h1 style="position:absolute;left:56px;right:56px;top:300px;font-size:100px;line-height:1.05">${hl(s.title)}</h1>
<p style="position:absolute;left:56px;right:56px;top:800px;font-size:44px;color:var(--mut);line-height:1.4">${s.text}</p>`;
  else if (s.type === 'steps') body = `<h2 style="position:absolute;left:56px;right:56px;top:230px;font-size:84px;line-height:1.05">${hl(s.title)}</h2>
<div style="position:absolute;left:56px;right:56px;top:460px">${s.items.map((t, k) => `<div class="step"><div class="n">${k + 1}</div><div><h3>${t[0]}</h3><p>${t[1]}</p></div></div>`).join('')}</div>`;
  else if (s.type === 'poll') body = `<h2 style="position:absolute;left:56px;right:56px;top:260px;font-size:88px;line-height:1.05">${hl(s.title)}</h2>
<div style="position:absolute;left:56px;right:56px;top:640px;display:flex;gap:30px"><div class="opt" style="background:var(--y)"><b>A</b><span>${s.a}</span></div><div class="opt"><b>B</b><span>${s.b}</span></div></div>
<p style="position:absolute;left:56px;right:56px;top:1050px;font:800 46px B;text-align:center">💬 Comenta <mark>A</mark> ou <mark>B</mark> aqui embaixo</p>`;
  else if (s.type === 'cta') body = `<div style="position:absolute;left:56px;right:56px;top:190px;height:470px;border-radius:52px;background:url('${b64(s.photo, 'image/jpeg')}') ${s.pos || 'center 25%'}/cover"></div>
<h1 style="position:absolute;left:56px;right:56px;top:700px;font-size:80px;line-height:1.05">${hl(s.title)}</h1>
<div style="position:absolute;left:56px;top:960px;background:var(--ink);color:#fff;font:800 46px B;padding:26px 50px;border-radius:99px">${s.cta} →</div>
<div style="position:absolute;left:56px;top:1100px;font:800 34px B;color:var(--mut)">🔖 Salva para consultar   ·   📤 Manda para um amigo</div>`;
  return `<!doctype html><meta charset=utf-8><style>${CSS}</style><body>${head}${body}${foot}</body>`;
};
const br = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const pg = await br.newPage({ viewport: { width: 1080, height: 1350 } });
for (const [i, s] of slides.entries()) {
  await pg.setContent(mk(s, i, slides.length));
  await pg.evaluate(() => document.fonts.ready);
  await pg.screenshot({ path: `${out}/slide-${String(i + 1).padStart(2, '0')}.png` });
}
await br.close();
