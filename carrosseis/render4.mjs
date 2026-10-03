// Modelo v4: node render4.mjs slides.json saida/
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const slides = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const out = process.argv[3];
const profile = JSON.parse(fs.readFileSync('perfil.json', 'utf8'));
fs.mkdirSync(out, { recursive: true });
const b64 = (f, t) => `data:${t};base64,${fs.readFileSync(path.resolve(f)).toString('base64')}`;
const font = f => b64(path.join('fontes', f), 'font/ttf');
const hl = t => t.replace(/\*\*(.+?)\*\*/g, '<mark>$1</mark>');
const AV = b64('fotos/exemplo-usuario-1.jpg', 'image/jpeg');

const CSS = `
@font-face{font-family:B;font-weight:800;src:url('${font('bricolage-800.ttf')}')}
@font-face{font-family:J;font-weight:400 800;src:url('${font('jakarta.ttf')}')}
:root{--ink:#0F1B33;--cream:#FBF6EA;--y:#FFC93C;--mut:#5C6577}
*{margin:0;box-sizing:border-box}
body{width:1080px;height:1350px;overflow:hidden;background:var(--cream);color:var(--ink);font-family:J,sans-serif;position:relative}
.dots{position:absolute;inset:0;background:radial-gradient(rgba(15,27,51,.13) 2.5px,transparent 2.5px) 0 0/34px 34px;
-webkit-mask-image:linear-gradient(160deg,#000 0%,transparent 55%);mask-image:linear-gradient(160deg,#000 0%,transparent 55%)}
.blob{position:absolute;right:-180px;top:-120px;width:620px;height:620px;border-radius:50%;background:var(--y);opacity:.9}
.head{position:absolute;top:56px;left:64px;right:64px;display:flex;align-items:center;gap:22px;z-index:6}
.av{width:88px;height:88px;border-radius:50%;overflow:hidden;position:relative;box-shadow:0 0 0 5px var(--cream),0 0 0 9px var(--ink)}
.av img{position:absolute;left:-64px;top:-40px;transform-origin:64px 40px;transform:scale(.68)}
.nm{font:800 36px B}.hd{font-size:26px;color:var(--mut)}
.pg{margin-left:auto;background:var(--ink);color:#fff;font-weight:800;font-size:26px;padding:10px 22px;border-radius:99px}
h1,h2{font-family:B;font-weight:800;letter-spacing:-2px}
mark{background:var(--y);color:var(--ink);padding:0 12px;border-radius:14px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.chip{display:inline-block;border:4px solid var(--ink);font-weight:800;font-size:26px;letter-spacing:3px;padding:10px 24px;border-radius:99px;text-transform:uppercase;background:#fff}
.foot{position:absolute;left:64px;right:64px;bottom:60px;display:flex;align-items:center;z-index:6}
.pd{display:flex;gap:12px}.pd i{width:20px;height:20px;border-radius:50%;background:#D9D2BE}.pd i.on{background:var(--ink);width:56px;border-radius:12px}
.sw{margin-left:auto;display:flex;align-items:center;gap:16px;font:800 30px B}
.sw b{width:72px;height:72px;border-radius:50%;background:var(--ink);color:var(--y);display:grid;place-items:center;font-size:38px}
.tile{position:absolute;width:420px;height:260px;border-radius:44px;display:grid;place-items:center;font:800 76px B;box-shadow:10px 14px 0 var(--ink);border:6px solid var(--ink);white-space:nowrap}
.vs{position:absolute;width:170px;height:170px;border-radius:50%;background:var(--y);border:6px solid var(--ink);display:grid;place-items:center;font:800 70px B;z-index:3;box-shadow:6px 8px 0 var(--ink)}
.card{display:flex;gap:34px;align-items:center;background:#fff;border:5px solid var(--ink);border-radius:40px;padding:34px 38px;box-shadow:10px 12px 0 var(--ink);margin-bottom:34px}
.card .n{flex:none;width:130px;height:130px;border-radius:34px;background:var(--y);border:5px solid var(--ink);display:grid;place-items:center;font:800 78px B}
.card h3{font:800 54px/1.05 B;letter-spacing:-1px}.card p{font-size:32px;color:var(--mut);margin-top:10px;line-height:1.3}
.bigq{font:800 340px/0.7 B;color:var(--y);-webkit-text-stroke:6px var(--ink)}
.days{display:flex;gap:16px;margin-top:50px}.days div{flex:1;height:150px;border:5px solid var(--ink);border-radius:30px;background:#fff;display:grid;place-items:center;font:800 56px B;box-shadow:6px 8px 0 var(--ink)}
.days div:nth-child(odd){background:var(--y)}
`;

const mk = (s, i, n) => {
  const head = `<div class="head"><div class="av"><img src="${AV}"></div><div><div class="nm">${profile.name}</div><div class="hd">${profile.handle}</div></div><div class="pg">${i + 1}/${n}</div></div>`;
  const foot = `<div class="foot"><div class="pd">${slides.map((_, k) => `<i class="${k === i ? 'on' : ''}"></i>`).join('')}</div>${i < n - 1 ? '<div class="sw">Arrasta <b>→</b></div>' : ''}</div>`;
  let inner = '', extra = '<div class="dots"></div>';
  if (s.type === 'cover') {
    extra += '<div class="blob"></div>';
    inner = `<div style="position:absolute;left:64px;top:210px"><span class="chip">${s.chip}</span></div>
<div class="tile" style="left:64px;top:310px;transform:rotate(-6deg);background:#fff;color:#EE4D2D;font-size:66px;padding-right:50px">🛍️ ${s.a}</div>
<div class="vs" style="left:462px;top:262px">VS</div>
<div class="tile" style="right:64px;top:380px;transform:rotate(5deg);background:#0b0b0f;color:#fff;font-size:58px;padding-left:40px;text-shadow:-4px -3px 0 #25F4EE,4px 3px 0 #FE2C55">${s.b}</div>
<h1 style="position:absolute;left:64px;right:64px;top:700px;font-size:112px;line-height:1.08">${hl(s.title)}</h1>
<p style="position:absolute;left:64px;right:64px;top:1030px;font-size:40px;color:var(--mut);line-height:1.35">${s.text}</p>`;
  } else if (s.type === 'cards') {
    inner = `<h2 style="position:absolute;left:64px;right:64px;top:230px;font-size:86px;line-height:1.05">${hl(s.title)}</h2>
<div style="position:absolute;left:64px;right:84px;top:400px">${s.items.map((t, k) => `<div class="card"><div class="n">${k + 1}</div><div><h3>${t[0]}</h3><p>${t[1]}</p></div></div>`).join('')}</div>`;
  } else if (s.type === 'quote') {
    inner = `<div class="bigq" style="position:absolute;left:64px;top:240px">“</div>
<h2 style="position:absolute;left:64px;right:64px;top:480px;font-size:104px;line-height:1.08">${hl(s.title)}</h2>
<p style="position:absolute;left:64px;right:64px;top:850px;font-size:44px;color:var(--mut);line-height:1.4">${s.text}</p>`;
  } else if (s.type === 'days') {
    inner = `<h2 style="position:absolute;left:64px;right:64px;top:230px;font-size:84px;line-height:1.1">${hl(s.title)}</h2>
<p style="position:absolute;left:64px;right:64px;top:520px;font-size:42px;color:var(--mut);line-height:1.4">${s.text}</p>
<div class="days" style="position:absolute;left:64px;right:64px;top:760px">${[1, 2, 3, 4, 5, 6, 7].map(d => `<div>${d}</div>`).join('')}</div>
<p style="position:absolute;left:64px;top:1000px;font:800 38px B;color:var(--ink)">dias de teste → decide com dado</p>`;
  } else if (s.type === 'photo') {
    extra = `<div style="position:absolute;inset:0;background:url('${b64(s.photo, 'image/jpeg')}') ${s.pos || 'center 30%'}/cover"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,27,51,.25) 0%,rgba(15,27,51,.35) 35%,rgba(15,27,51,.96) 78%)"></div>`;
    inner = `<h2 style="position:absolute;left:64px;right:64px;top:740px;font-size:92px;line-height:1.06;color:#fff">${hl(s.title)}</h2>
<p style="position:absolute;left:64px;right:64px;top:1005px;font-size:36px;color:#e8ecf5">${s.text}</p>
<div style="position:absolute;left:64px;top:1090px;background:var(--y);color:var(--ink);font:800 48px B;padding:26px 50px;border-radius:99px;border:5px solid #fff">${s.cta} →</div>`;
  }
  const f = s.type === 'photo' ? foot.replace(/background:#D9D2BE/g, '') : foot;
  return `<!doctype html><meta charset=utf-8><style>${CSS}${s.type === 'photo' ? '.pd i{background:#ffffff66}.pd i.on{background:#fff}.sw,.nm{color:#fff}.hd{color:#dfe5f2}' : ''}</style><body>${extra}${head}${inner}${f}</body>`;
};

const br = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const pg = await br.newPage({ viewport: { width: 1080, height: 1350 } });
for (const [i, s] of slides.entries()) {
  await pg.setContent(mk(s, i, slides.length));
  await pg.evaluate(() => document.fonts.ready);
  await pg.screenshot({ path: `${out}/slide-${String(i + 1).padStart(2, '0')}.png` });
}
await br.close();
