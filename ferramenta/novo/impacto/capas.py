import os
from playwright.sync_api import sync_playwright
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'capas'); os.makedirs(OUT,exist_ok=True)
B='*{margin:0;padding:0;box-sizing:border-box}body{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:Poppins,sans-serif}'
A='''<style>%s body{background:#FFD400;color:#0A0A0A}
.tape{position:absolute;left:-100px;right:-100px;height:90px;background:repeating-linear-gradient(-45deg,#0A0A0A 0 40px,#FFD400 40px 80px);}
.t{position:absolute;left:70px;right:70px;font-weight:900;letter-spacing:-5px;line-height:.9}
.tag{position:absolute;left:70px;top:150px;background:#0A0A0A;color:#FFD400;font-weight:800;font-size:34px;padding:14px 28px;letter-spacing:3px}
</style><div class="tape" style="top:60px"></div><div class="tag">ATENÇÃO, VENDEDOR</div>
<div class="t" style="top:260px;font-size:205px">PARE DE<br>POSTAR</div>
<div class="t" style="top:700px;font-size:160px;background:#0A0A0A;color:#FFD400;padding:10px 24px 26px;left:70px;right:auto;transform:rotate(-2deg)">PRODUTO<br>ASSIM.</div>
<div style="position:absolute;left:70px;bottom:190px;font-size:40px;font-weight:700;width:760px;line-height:1.25">O erro que faz seu vídeo ter 200 views e zero venda.</div>
<div class="tape" style="bottom:60px"></div>'''%B
Bh='''<style>%s body{background:#0B0B0F;color:#fff}
.k{position:absolute;left:70px;font-weight:800;letter-spacing:-3px;line-height:1.05}
.bar{display:inline-block;background:#fff;height:.82em;vertical-align:-.08em;border-radius:6px}
</style>
<div style="position:absolute;left:70px;top:80px;font-size:28px;color:#FF3B3B;font-weight:800;letter-spacing:4px">● CONFIDENCIAL</div>
<div class="k" style="top:170px;font-size:112px">O verdadeiro motivo de você <span style="color:#FF3B3B">não vender</span> no TikTok Shop é</div>
<div class="k" style="top:790px;font-size:150px;line-height:1.12"><span class="bar" style="width:700px"></span><br><span class="bar" style="width:420px"></span></div>
<div style="position:absolute;left:70px;bottom:200px;font-size:38px;font-weight:600;color:#C9CBD6;width:840px;line-height:1.3">Quase ninguém fala disso. Eu mostro no slide 4.</div>
<div style="position:absolute;right:70px;bottom:70px;background:#FF3B3B;font-weight:800;font-size:28px;padding:20px 38px;border-radius:99px;letter-spacing:3px">DESLIZE →</div>'''%B
C='''<style>%s body{background:#111;color:#fff}
.ph{position:absolute;top:330px;width:440px;height:760px;border-radius:50px;border:6px solid #333;background:#1b1b22;overflow:hidden}
.pr{position:absolute;left:50%%;top:60px;transform:translateX(-50%%);width:240px;height:240px;border-radius:40px;background:linear-gradient(135deg,#7EC8FF,#2B6BFF);display:flex;align-items:center;justify-content:center;font-size:110px}
</style>
<div style="position:absolute;left:0;right:0;top:70px;text-align:center;font-size:96px;font-weight:900;letter-spacing:-3px;line-height:1">MESMO PRODUTO.</div>
<div style="position:absolute;left:0;right:0;top:175px;text-align:center;font-size:96px;font-weight:900;letter-spacing:-3px;line-height:1;color:#FFD400">RESULTADO OPOSTO.</div>
<div class="ph" style="left:70px;border-color:#2EE66B"><div class="pr">🧴</div><div style="position:absolute;top:340px;left:0;right:0;text-align:center;font-size:150px;font-weight:900;color:#2EE66B">1.284</div><div style="position:absolute;top:520px;left:0;right:0;text-align:center;font-size:34px;font-weight:700;color:#2EE66B;letter-spacing:3px">VENDAS</div><div style="position:absolute;bottom:40px;left:0;right:0;text-align:center;font-size:40px">✓</div></div>
<div class="ph" style="right:70px;border-color:#FF3B3B"><div class="pr" style="filter:grayscale(1);opacity:.6">🧴</div><div style="position:absolute;top:340px;left:0;right:0;text-align:center;font-size:150px;font-weight:900;color:#FF3B3B">0</div><div style="position:absolute;top:520px;left:0;right:0;text-align:center;font-size:34px;font-weight:700;color:#FF3B3B;letter-spacing:3px">VENDAS</div><div style="position:absolute;bottom:40px;left:0;right:0;text-align:center;font-size:40px">✕</div></div>
<div style="position:absolute;left:0;right:0;top:1150px;text-align:center;font-size:46px;font-weight:700">A diferença não é o produto.</div>
<div style="position:absolute;left:0;right:0;top:1215px;text-align:center;font-size:34px;color:#FFD400;font-weight:700;letter-spacing:3px">DESLIZE PARA VER →</div>'''%B
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
    for n,h in (('A-alerta',A),('B-censurado',Bh),('C-contraste',C)):
        pg.set_content('<html><head><meta charset="utf-8"></head><body>%s</body></html>'%h); pg.wait_for_timeout(300)
        pg.screenshot(path='%s/capa-%s.jpg'%(OUT,n),type='jpeg',quality=93)
    b.close()
