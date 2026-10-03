// Modelo claro: node render2.mjs slides.json saida/ [perfil.json]
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const slides = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const out = process.argv[3];
const profile = JSON.parse(fs.readFileSync(process.argv[4] || 'perfil.json', 'utf8'));
fs.mkdirSync(out, { recursive: true });

const img = f => `data:image/jpeg;base64,${fs.readFileSync(path.resolve(f)).toString('base64')}`;
const hl = t => t.replace(/\*\*(.+?)\*\*/g, '<mark>$1</mark>');

const font = f => `data:font/ttf;base64,${fs.readFileSync(path.resolve('fontes', f)).toString('base64')}`;
const CSS = `
@font-face{font-family:'Bricolage Grotesque';font-weight:800;src:url('${font('bricolage-800.ttf')}')}
@font-face{font-family:'Plus Jakarta Sans';font-weight:400 800;src:url('${font('jakarta.ttf')}')}
:root{--ink:#0E1116;--mut:#5B6270;--bg:#F7F5F0;--acc:#FF4D1C;--soft:#FFE6DC}
*{margin:0;box-sizing:border-box}
body{width:1080px;height:1350px;overflow:hidden;background:var(--bg);color:var(--ink);
font-family:'Plus Jakarta Sans',sans-serif;position:relative;padding:72px}
.head{display:flex;align-items:center;gap:22px}
.av{width:84px;height:84px;border-radius:50%;background:var(--ink);color:#fff;display:grid;place-items:center;
font:800 32px 'Bricolage Grotesque';box-shadow:0 0 0 5px var(--bg),0 0 0 9px var(--acc)}
.nm{font:800 36px 'Bricolage Grotesque'}.hd{font-size:26px;color:var(--mut);margin-top:2px}
.pg{margin-left:auto;font-size:26px;color:var(--mut);font-weight:700}
h1{font:800 94px/1.02 'Bricolage Grotesque';letter-spacing:-2px}
h2{font:800 76px/1.06 'Bricolage Grotesque';letter-spacing:-1.5px}
mark{background:linear-gradient(transparent 58%,var(--acc) 58%);color:inherit;padding:0 4px}
p{font-size:42px;line-height:1.42;color:var(--mut);margin-top:36px}
.chip{align-self:flex-start;display:inline-block;background:var(--ink);color:#fff;font-weight:700;font-size:26px;letter-spacing:3px;
padding:14px 26px;border-radius:99px;text-transform:uppercase}
.num{font:800 220px/0.9 'Bricolage Grotesque';color:var(--acc);letter-spacing:-8px}
.bar{position:absolute;left:72px;right:72px;bottom:70px;display:flex;gap:10px;align-items:center}
.bar i{flex:1;height:8px;border-radius:9px;background:#DDD8CE}.bar i.on{background:var(--ink)}
.bar b{margin-left:22px;font-size:28px;white-space:nowrap}
.main{position:absolute;left:72px;right:72px;top:210px;bottom:160px;display:flex;flex-direction:column;justify-content:center}
.card{background:var(--acc);color:#fff;border-radius:44px;padding:44px 50px;font:800 52px/1.1 'Bricolage Grotesque'}
.ph{width:100%;height:640px;border-radius:44px;background-size:cover;background-position:center 30%;margin-bottom:44px}
.btn{display:inline-block;background:var(--acc);color:#fff;border-radius:99px;padding:22px 44px;font:800 44px 'Bricolage Grotesque';margin-top:34px}
.orb{position:absolute;right:-140px;top:-140px;width:460px;height:460px;border-radius:50%;background:var(--soft);z-index:0}
.head,.main,.bar{z-index:2}
`;

const body = (s, i, n) => {
  const head = `<div class="head"><div class="av">DR</div><div><div class="nm">${profile.name}</div><div class="hd">${profile.handle}</div></div><div class="pg">${i + 1}/${n}</div></div>`;
  const bar = `<div class="bar">${slides.map((_, k) => `<i class="${k <= i ? 'on' : ''}"></i>`).join('')}<b>${i < n - 1 ? 'Arrasta →' : 'Salva 🔖'}</b></div>`;
  let main = '';
  if (s.type === 'cover') main = `<span class="chip">${s.chip}</span><h1 style="margin-top:44px">${hl(s.title)}</h1>${s.text ? `<p>${s.text}</p>` : ''}<div class="card" style="margin-top:56px">${s.teaser}</div>`;
  else if (s.type === 'photo') main = `<div class="ph" style="background-image:url('${img(s.photo)}');background-position:${s.pos || 'center 30%'}"></div><h2 style="font-size:64px">${hl(s.title)}</h2><div><span class="btn">${s.cta}</span></div>`;
  else main = `${s.num ? `<div class="num">${s.num}</div>` : ''}<h2 style="margin-top:${s.num ? 30 : 0}px">${hl(s.title)}</h2>${s.text ? `<p>${s.text}</p>` : ''}`;
  return `<!doctype html><html><head><meta charset="utf-8"><style>${CSS}</style></head><body><div class="orb"></div>${head}<div class="main">${main}</div>${bar}</body></html>`;
};

const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const pg = await b.newPage({ viewport: { width: 1080, height: 1350 } });
for (const [i, s] of slides.entries()) {
  await pg.setContent(body(s, i, slides.length), );
  await pg.evaluate(() => document.fonts.ready);
  await pg.screenshot({ path: `${out}/slide-${String(i + 1).padStart(2, '0')}.png` });
}
await b.close();
