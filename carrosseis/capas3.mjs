import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
const font = f => `data:font/ttf;base64,${fs.readFileSync(path.resolve('fontes', f)).toString('base64')}`;
const img = f => `data:image/jpeg;base64,${fs.readFileSync(path.resolve(f)).toString('base64')}`;
const BASE = `@font-face{font-family:B;font-weight:800;src:url('${font('bricolage-800.ttf')}')}
@font-face{font-family:J;font-weight:400 800;src:url('${font('jakarta.ttf')}')}
*{margin:0;box-sizing:border-box}body{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:J,sans-serif}
.head{position:absolute;top:64px;left:72px;right:72px;display:flex;align-items:center;gap:20px;z-index:5}
.av{width:80px;height:80px;border-radius:50%;display:grid;place-items:center;font:800 30px B}
.nm{font:800 34px B}.hd{font-size:25px;opacity:.75}.pg{margin-left:auto;font-weight:700;font-size:26px;opacity:.8}
h1{font-family:B;font-weight:800;letter-spacing:-2px}`;
const head = (c1, c2) => `<div class="head" style="color:${c1}"><div class="av" style="background:${c2};color:${c1}">DR</div><div><div class="nm">Diego Reis</div><div class="hd">@seu.perfil</div></div><div class="pg">1/6</div></div>`;

// A: escuro + lima + celular ilustrado
const A = `<style>${BASE}
body{background:radial-gradient(900px 700px at 80% 55%,#1c2f6b 0%,#0B0F1A 70%);color:#fff}
h1{position:absolute;left:72px;top:190px;width:640px;font-size:96px;line-height:1}
h1 em{font-style:normal;color:#C6FF3D}
.phone{position:absolute;right:-150px;bottom:-200px;width:560px;height:900px;border-radius:70px;background:#05070d;border:10px solid #2a3350;transform:rotate(-12deg);padding:40px 28px;box-shadow:0 40px 80px #0009}
.n{background:#fff;color:#0B0F1A;border-radius:28px;padding:22px 26px;margin-bottom:22px;font:800 30px B;display:flex;gap:16px;align-items:center}
.n small{display:block;font:500 22px J;color:#667}.dot{width:54px;height:54px;border-radius:16px;background:#C6FF3D;display:grid;place-items:center;font-size:30px}
.tag{position:absolute;left:72px;bottom:150px;background:#C6FF3D;color:#0B0F1A;font:800 44px B;padding:26px 40px;border-radius:24px}
</style>${head('#fff', '#C6FF3D').replace('color:#fff"><div class="av" style="background:#C6FF3D;color:#fff', 'color:#fff"><div class="av" style="background:#C6FF3D;color:#0B0F1A')}
<h1>O que <em>ninguém</em> te conta sobre vender na <em>Shopee</em></h1>
<div class="phone">
<div class="n"><div class="dot">🛍️</div><div>Novo pedido<small>agora</small></div></div>
<div class="n"><div class="dot">📦</div><div>Pedido a caminho<small>há 2 min</small></div></div>
<div class="n"><div class="dot">⭐</div><div>Nova avaliação<small>há 5 min</small></div></div>
<div class="n"><div class="dot">🛍️</div><div>Novo pedido<small>há 8 min</small></div></div></div>
<div class="tag">Arrasta e descobre →</div>`;

// B: foto duotone verde
const B = `<style>${BASE}
body{background:#031a0f;color:#fff}
.ph{position:absolute;inset:0;background:url('${img('fotos/foto-1.jpg')}') center 25%/cover;filter:grayscale(1) contrast(1.15)}
.tint{position:absolute;inset:0;background:linear-gradient(180deg,#00c853aa 0%,#031a0fe6 70%,#031a0f 100%);mix-blend-mode:multiply}
.tint2{position:absolute;inset:0;background:linear-gradient(180deg,rgba(3,26,15,.2),rgba(3,26,15,.95) 80%)}
h1{position:absolute;left:72px;right:72px;bottom:230px;font-size:112px;line-height:.98;text-transform:uppercase}
h1 span{color:#B6FF3B}
.st{position:absolute;right:72px;top:210px;background:#B6FF3B;color:#031a0f;font:800 40px B;padding:20px 34px;border-radius:99px;transform:rotate(6deg)}
.cta{position:absolute;left:72px;bottom:90px;font:800 40px B;color:#B6FF3B}
</style><div class="ph"></div><div class="tint"></div><div class="tint2"></div>${head('#fff', '#B6FF3B').replace('color:#fff"><div class="av" style="background:#B6FF3B;color:#fff', 'color:#fff"><div class="av" style="background:#B6FF3B;color:#031a0f')}
<div class="st">NOVO</div>
<h1>Vender online:<br><span>o que mudou</span><br>em 2026?</h1><div class="cta">Arrasta para o lado →</div>`;

// C: amarelo + stickers
const st = (e, x, y, r, s = 190) => `<div style="position:absolute;left:${x}px;top:${y}px;width:${s}px;height:${s}px;border-radius:50%;background:#fff;display:grid;place-items:center;font-size:${s * .55}px;transform:rotate(${r}deg);box-shadow:8px 10px 0 #111;border:6px solid #111">${e}</div>`;
const C = `<style>${BASE}
body{background:#FFD21F;color:#111}
h1{position:absolute;left:72px;right:72px;top:600px;font-size:112px;line-height:1.28}
h1 span{background:#111;color:#FFD21F;padding:0 18px;border-radius:18px}
.pill{position:absolute;left:72px;bottom:90px;background:#111;color:#fff;font:800 42px B;padding:26px 46px;border-radius:99px}
</style>${head('#111', '#111').replace('class="av" style="background:#111;color:#111"', 'class="av" style="background:#111;color:#FFD21F"')}
${st('🛍️', 90, 230, -10, 230)}${st('📦', 380, 300, 8, 200)}${st('🔥', 650, 220, -6, 220)}${st('📈', 800, 400, 12, 170)}
<h1>Por que <span>tanta gente</span> vende e <span>pouca</span> lucra?</h1>
<div class="pill">Arrasta →</div>`;

const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const pg = await b.newPage({ viewport: { width: 1080, height: 1350 } });
fs.mkdirSync('capas', { recursive: true });
for (const [n, h] of Object.entries({ A, B, C })) {
  await pg.setContent(`<!doctype html><meta charset=utf-8>${h}`);
  await pg.evaluate(() => document.fonts.ready);
  await pg.screenshot({ path: `capas/capa-${n}.png` });
}
await b.close();
