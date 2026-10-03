// Estilo oficial (igual aos modelos do Diego): node render8.mjs slides.json saida/
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
const slides = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const out = process.argv[3];
const P = JSON.parse(fs.readFileSync('perfil.json', 'utf8'));
fs.mkdirSync(out, { recursive: true });
const MIME = { '.webp': 'image/webp', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg' };
const b64 = (f, t) => `data:${MIME[path.extname(f).toLowerCase()] || t};base64,${fs.readFileSync(path.resolve(f)).toString('base64')}`;
const font = f => b64(path.join('fontes', f), 'font/ttf');
const AV = b64('fotos/avatar-ref.jpg', 'image/jpeg');
const hl = t => t.replace(/\*\*(.+?)\*\*/g, '<mark>$1</mark>');
const BADGE = `<svg width="40" height="40" viewBox="0 0 24 24" style="margin-left:10px;vertical-align:-6px"><path fill="#1D9BF0" d="M12 1l2.6 1.9 3.2-.1 1 3 2.6 1.9-1 3.1 1 3-2.6 1.9-1 3-3.2-.1L12 23l-2.6-1.9-3.2.1-1-3L2.6 16.3l1-3-1-3.1 2.6-1.9 1-3 3.2.1z"/><path fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" d="M7.8 12.2l3 3 5.4-6"/></svg>`;
const CSS = `
@font-face{font-family:P;font-weight:400;src:url('${font('poppins-400.ttf')}')}
@font-face{font-family:P;font-weight:600;src:url('${font('poppins-600.ttf')}')}
@font-face{font-family:P;font-weight:700;src:url('${font('poppins-700.ttf')}')}
:root{--ink:#0F1B33;--gold:#B7791F;--hi:#FDE9A8;--btn:#FFD65C}
*{margin:0;box-sizing:border-box}
body{width:1080px;height:1350px;overflow:hidden;background:#fff;color:var(--ink);font-family:P,sans-serif;position:relative}
.head{text-shadow:0 2px 12px rgba(0,0,0,.45);position:absolute;top:44px;left:68px;right:72px;display:flex;align-items:center;gap:20px;z-index:5}
.av{width:124px;height:124px;border-radius:50%;overflow:hidden;position:relative;flex:none}
.av img{position:absolute;left:-68px;top:-44px}
.nm{font-weight:700;font-size:44px;line-height:1.1}.hd{font-size:34px;color:#6b7385;line-height:1.3}
.pg{margin-left:auto;font-size:32px;color:#6b7385;align-self:flex-start;margin-top:30px}
mark{background:var(--hi);color:var(--ink);font-weight:700;padding:0 10px;border-radius:14px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.eb{font-weight:700;font-size:27px;letter-spacing:5px;text-transform:uppercase;color:var(--gold)}
h1{font-weight:700;line-height:1.25;letter-spacing:-1px}
.foot{position:absolute;left:72px;right:72px;bottom:50px;display:flex;align-items:center;z-index:5}
.pd{display:flex;gap:18px}.pd i{width:22px;height:22px;border-radius:50%;background:#E2E6EE}.pd i.on{background:var(--ink)}
.sw{margin-left:auto;font-size:32px;color:#6b7385;font-weight:600}
.src{position:absolute;left:72px;bottom:130px;font-size:25px;color:#7b8394}
.row{display:flex;gap:34px;align-items:center;margin-bottom:56px}
.row .n{flex:none;width:80px;height:80px;border-radius:50%;border:5px solid #D6A537;color:var(--gold);display:grid;place-items:center;font-weight:700;font-size:38px}
.row p{font-size:44px;line-height:1.3;font-weight:400}
`;
const DARK = `<style>.nm{color:#fff}.hd{color:#E4E8F1}.pg{color:#cdd3e1}.pd i{background:#ffffff55}.pd i.on{background:#fff}.sw{color:#dfe4ee}</style>`;
const mk = (s, i, n) => {
  const head = `<div class="head"><div class="av"><img src="${AV}"></div><div><div class="nm">${P.name}${P.verified ? BADGE : ''}</div><div class="hd">${P.handle} · agora</div></div><div class="pg">${i + 1}/${n}</div></div>`;
  const foot = `<div class="foot"><div class="pd">${slides.map((_, k) => `<i class="${k === i ? 'on' : ''}"></i>`).join('')}</div>${i < n - 1 ? '<div class="sw">Arrasta &nbsp;→</div>' : ''}</div>`;
  const photo = `<div style="position:absolute;inset:0;background:url('${s.photo ? b64(s.photo, 'image/jpeg') : ''}') ${s.pos || 'center 25%'}/cover"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,27,51,.35) 0%,rgba(15,27,51,.05) 22%,rgba(15,27,51,.55) 52%,rgba(15,27,51,.97) 78%)"></div>`;
  let b = '', extra = '';
  if (s.type === 'cover') { extra = DARK; b = `${photo}${s.live ? '<div style="position:absolute;right:72px;top:216px;background:#fff;border-radius:99px;padding:14px 26px;font-weight:700;font-size:28px;letter-spacing:2px;display:flex;align-items:center;gap:12px;z-index:4"><span style="width:30px;height:30px;border-radius:50%;background:#E5322D;display:inline-block"></span>AO VIVO</div>' : ''}
<div class="eb" style="position:absolute;left:72px;top:800px;color:#F2C14E;z-index:3">${s.eyebrow}</div>
<h1 style="position:absolute;left:72px;right:60px;top:850px;font-size:78px;font-weight:600;color:#fff;z-index:3">${hl(s.title)}</h1>
<p style="position:absolute;left:72px;right:72px;top:1150px;font-size:38px;color:#E1E6F0;z-index:3">${s.text || ''}</p>`; }
  else if (s.type === 'big') b = `<div class="eb" style="position:absolute;left:72px;top:330px">${s.eyebrow}</div>
<h1 style="position:absolute;left:72px;right:72px;top:390px;font-size:92px">${hl(s.title)}</h1>
<p style="position:absolute;left:72px;right:72px;top:700px;font-size:46px;line-height:1.5;color:#475569">${s.text}</p>`;
  else if (s.type === 'list') b = `<div class="eb" style="position:absolute;left:72px;top:236px">${s.eyebrow}</div>
<h1 style="position:absolute;left:72px;right:72px;top:290px;font-size:84px">${hl(s.title)}</h1>
<div style="position:absolute;left:72px;right:60px;top:560px">${s.items.map((t, k) => `<div class="row"><div class="n">${k + 1}</div><p>${t}</p></div>`).join('')}</div>${s.src ? `<div class="src">${s.src}</div>` : ''}`;
  else if (s.type === 'ask') b = `<div class="eb" style="position:absolute;left:72px;top:330px">${s.eyebrow}</div>
<h1 style="position:absolute;left:72px;right:72px;top:390px;font-size:88px">${hl(s.title)}</h1>
<div style="position:absolute;left:72px;right:72px;top:760px;display:flex;gap:26px">${s.options.map((t, k) => `<div style="flex:1;border:5px solid #D6A537;border-radius:36px;padding:34px 20px;text-align:center"><div style="font-size:72px;font-weight:700;color:var(--gold)">${k + 1}</div><div style="font-size:34px;line-height:1.3;margin-top:8px">${t}</div></div>`).join('')}</div>
<p style="position:absolute;left:72px;right:72px;top:1080px;font-size:44px;font-weight:600">💬 Comenta o número aqui embaixo 👇</p>`;
  else if (s.type === 'cta') { extra = DARK; b = `${photo}
<h1 style="position:absolute;left:72px;right:60px;top:735px;font-size:84px;font-weight:600;color:#fff;z-index:3">${hl(s.title)}</h1>
<p style="position:absolute;left:72px;right:72px;top:965px;font-size:33px;color:#E1E6F0;z-index:3">${s.text}</p>
<div style="position:absolute;left:72px;top:1030px;background:var(--btn);color:var(--ink);font-size:44px;padding:26px 54px;border-radius:99px;z-index:3">Comente <b>${s.keyword}</b> &nbsp;→</div>
<div style="position:absolute;left:72px;top:1155px;display:flex;gap:18px;z-index:3;font-weight:700;font-size:34px;color:#fff">${['<span style="color:#FFD65C">♥</span> Curta', '🔖 Salve', `＋ Siga ${P.handle}`].map(t => `<div style="border:2px solid #ffffff55;background:#ffffff1c;border-radius:99px;padding:18px 34px">${t}</div>`).join('')}</div>`; }
  return `<!doctype html><meta charset=utf-8><style>${CSS}</style>${extra}<body>${b}${head}${foot}</body>`;
};
const br = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const pg = await br.newPage({ viewport: { width: 1080, height: 1350 } });
for (const [i, s] of slides.entries()) {
  await pg.setContent(mk(s, i, slides.length));
  await pg.evaluate(() => document.fonts.ready);
  await pg.screenshot({ path: `${out}/slide-${String(i + 1).padStart(2, '0')}.png` });
}
await br.close();
