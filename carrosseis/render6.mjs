// Estilo "criador": node render6.mjs slides.json saida/
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
const hl = t => t.replace(/\*\*(.+?)\*\*/g, '<em>$1</em>').replace(/__(.+?)__/g, '<u>$1</u>');
const CSS = `
@font-face{font-family:A;src:url('${font('anton.ttf')}')}
@font-face{font-family:J;font-weight:400 800;src:url('${font('jakarta.ttf')}')}
:root{--o:#FF6A2B;--c:#25F4EE}
*{margin:0;box-sizing:border-box}
body{width:1080px;height:1350px;overflow:hidden;background:#0A0A0C;color:#fff;font-family:J,sans-serif;position:relative}
.bg{position:absolute;inset:0;background-size:cover}
.sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,10,12,.05) 0%,rgba(10,10,12,.1) 40%,rgba(10,10,12,.92) 72%,#0A0A0C 100%)}
.top{text-shadow:0 2px 10px rgba(0,0,0,.7);position:absolute;top:50px;left:60px;right:60px;display:flex;align-items:center;gap:18px;z-index:5}
.av{width:70px;height:70px;border-radius:50%;overflow:hidden;position:relative;border:3px solid #fff}
.av img{position:absolute;left:-64px;top:-40px;transform-origin:64px 40px;transform:scale(.55)}
.nm{font-weight:800;font-size:28px}.hd{font-size:22px;opacity:.75}
.tag{margin-left:auto;font-size:22px;font-weight:800;letter-spacing:3px;opacity:.85}
h1{font-family:A;font-weight:400;text-transform:uppercase;line-height:1.02;letter-spacing:0}
em{font-style:normal;color:var(--o)}u{text-decoration:none;color:var(--c)}
.foot{position:absolute;left:60px;right:60px;bottom:48px;display:flex;justify-content:space-between;font-size:24px;font-weight:800;letter-spacing:2px;z-index:5}
.row{display:flex;align-items:center;gap:26px;background:#16161a;border:2px solid #26262c;border-radius:30px;padding:30px 34px;margin-bottom:26px}
.ic{width:100px;height:100px;border-radius:26px;display:grid;place-items:center;font-size:54px;flex:none}
.row b{font:400 50px/1 A;text-transform:uppercase;display:block}.row span{font-size:28px;color:#a4a4ad}
`;
const mk = (s, i, n) => {
  const top = `<div class="top"><div class="av"><img src="${AV}"></div><div><div class="nm">${profile.name}</div><div class="hd">${profile.handle}</div></div><div class="tag">${s.tag || ''}</div></div>`;
  const foot = `<div class="foot"><span>${profile.handle.toUpperCase()}</span><span>${i < n - 1 ? 'ARRASTA →' : ''} ${i + 1}/${n}</span></div>`;
  let body = '';
  if (s.type === 'cover') body = `<div class="bg" style="background-image:url('${b64(s.photo, 'image/jpeg')}');background-position:${s.pos || 'center 20%'}"></div><div class="sh"></div>
<h1 style="position:absolute;left:60px;right:60px;top:790px;font-size:128px">${hl(s.title)}</h1>
<p style="position:absolute;left:60px;right:60px;top:1130px;font-size:34px;color:#d5d5dc;line-height:1.35">${s.text}</p>`;
  else if (s.type === 'list') body = `<h1 style="position:absolute;left:60px;right:60px;top:200px;font-size:110px">${hl(s.title)}</h1>
<div style="position:absolute;left:60px;right:60px;top:560px">${s.items.map(t => `<div class="row"><div class="ic" style="background:${t[3]}">${t[0]}</div><div><b>${t[1]}</b><span>${t[2]}</span></div></div>`).join('')}</div>`;
  return `<!doctype html><meta charset=utf-8><style>${CSS}</style><body>${body}${top}${foot}</body>`;
};
const br = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const pg = await br.newPage({ viewport: { width: 1080, height: 1350 } });
for (const [i, s] of slides.entries()) {
  await pg.setContent(mk(s, i, slides.length));
  await pg.evaluate(() => document.fonts.ready);
  await pg.screenshot({ path: `${out}/slide-${String(i + 1).padStart(2, '0')}.png` });
}
await br.close();
