import { chromium } from 'playwright';
import fs from 'fs';

const slides = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const out = process.argv[3];
fs.mkdirSync(out, { recursive: true });

const html = (s, i, n) => `<!doctype html><html><head><meta charset="utf-8"><style>
*{margin:0;box-sizing:border-box}
body{width:1080px;height:1350px;font-family:'DejaVu Sans',sans-serif;color:#fff;
background:${s.bg||'linear-gradient(160deg,#0f0c29,#302b63 60%,#ff3e7f)'};
display:flex;flex-direction:column;justify-content:center;padding:90px;position:relative}
.tag{position:absolute;top:70px;left:90px;font-size:30px;letter-spacing:4px;opacity:.8;text-transform:uppercase}
.num{position:absolute;top:70px;right:90px;font-size:30px;opacity:.8}
h1{font-size:${s.big?96:78}px;line-height:1.12;font-weight:800}
h1 em{font-style:normal;color:#ffd84d}
p{font-size:44px;line-height:1.4;margin-top:50px;opacity:.92}
.foot{position:absolute;bottom:70px;left:90px;font-size:32px;opacity:.85}
</style></head><body>
<div class="tag">${s.tag||'@diegoreisads'}</div><div class="num">${i+1}/${n}</div>
<h1>${s.title}</h1>${s.text?`<p>${s.text}</p>`:''}
<div class="foot">${s.foot||(i<n-1?'Arrasta para o lado →':'')}</div>
</body></html>`;

const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const pg = await b.newPage({ viewport: { width: 1080, height: 1350 } });
for (const [i, s] of slides.entries()) {
  await pg.setContent(html(s, i, slides.length));
  await pg.screenshot({ path: `${out}/slide-${String(i + 1).padStart(2, '0')}.png` });
}
await b.close();
