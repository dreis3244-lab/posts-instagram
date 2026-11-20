import sys, os
from playwright.sync_api import sync_playwright
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'saida'); os.makedirs(OUT,exist_ok=True)
CSS='''
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;background:#0A0A10;font-family:Poppins,sans-serif;color:#fff;overflow:hidden;position:relative}
.bg{position:absolute;inset:0;background:radial-gradient(900px 700px at 80% 15%,#1B2A5C 0%,rgba(10,10,16,0) 70%),radial-gradient(700px 600px at 0% 100%,#3A2A08 0%,rgba(10,10,16,0) 70%)}
.grain{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:54px 54px}
.top{position:absolute;left:80px;right:80px;top:64px;display:flex;justify-content:space-between;font-size:26px;font-weight:500;color:#8E96AD;letter-spacing:2px}
.g{color:#F5B83D}
.h{position:absolute;left:80px;right:80px;font-weight:800;line-height:1.0;letter-spacing:-2px}
.sub{position:absolute;left:80px;right:80px;font-size:38px;font-weight:500;line-height:1.3;color:#D5D9E6}
.pill{position:absolute;left:80px;bottom:70px;background:#F5B83D;color:#0A0A10;font-weight:700;font-size:26px;letter-spacing:3px;padding:20px 38px;border-radius:99px}
.notif{position:absolute;left:80px;right:80px;height:128px;border-radius:30px;background:rgba(255,255,255,.09);border:1px solid rgba(255,255,255,.16);backdrop-filter:blur(8px);display:flex;align-items:center;gap:26px;padding:0 30px;box-shadow:0 20px 50px rgba(0,0,0,.45)}
.ico{width:72px;height:72px;border-radius:20px;background:#F5B83D;display:flex;align-items:center;justify-content:center;font-size:40px;color:#0A0A10;font-weight:800;flex:none}
.nt{font-size:23px;color:#9AA3BB;font-weight:500}
.nb{font-size:33px;font-weight:700;line-height:1.15}
.nw{margin-left:auto;font-size:22px;color:#9AA3BB}
.big{position:absolute;font-weight:800;line-height:.8;letter-spacing:-8px}
.card{position:absolute;border-radius:34px;padding:40px}
'''
def page(inner): return '<html><head><meta charset="utf-8"><style>%s</style></head><body><div class="bg"></div><div class="grain"></div>%s</body></html>'%(CSS,inner)
def top(n): return '<div class="top"><span>@diegoreisads</span><span>%02d / 06</span></div>'%n
def notif(y,txt,sc,op,rot,t='agora'):
    return '<div class="notif" style="top:%dpx;transform:scale(%s) rotate(%sdeg);opacity:%s"><div class="ico">$</div><div><div class="nt">TikTok Shop</div><div class="nb">%s</div></div><div class="nw">%s</div></div>'%(y,sc,rot,op,txt,t)
S=[]
# 1 capa
S.append(page(top(1)+
 notif(170,'Novo pedido: Garrafa térmica',1,1,-2)+
 notif(330,'Novo pedido: Luminária LED',.97,.85,1.5,'1 min')+
 notif(490,'Novo pedido: Organizador de mesa',.94,.65,-1,'2 min')+
 notif(640,'Novo pedido: Kit de cabos',.91,.42,1.5,'3 min')+
 '<div class="h" style="top:780px;font-size:118px">O celular<br><span class="g">tocando</span><br>o dia todo.</div>'+
 '<div class="sub" style="top:1135px;font-size:34px;width:760px">Não é sorte. São 3 decisões.</div>'+
 '<div class="pill" style="left:auto;right:80px;bottom:62px">DESLIZE →</div>'))
# 2 produto
S.append(page(top(2)+
 '<div class="big" style="left:60px;top:150px;font-size:430px;color:transparent;-webkit-text-stroke:5px #F5B83D">01</div>'+
 '<div class="h" style="top:560px;font-size:84px">Escolha o produto pelo <span class="g">dado</span>, não pelo gosto.</div>'+
 '<div class="card" style="left:80px;top:960px;width:430px;height:280px;background:rgba(255,255,255,.06);border:2px dashed #5B6482"><div style="font-size:26px;color:#8E96AD;font-weight:600">VOCÊ ACHA BONITO</div><div style="font-size:60px;font-weight:800;margin-top:26px;color:#6F7894">✕ Aposta</div></div>'+
 '<div class="card" style="left:570px;top:960px;width:430px;height:280px;background:#F5B83D;color:#0A0A10"><div style="font-size:26px;font-weight:700">JÁ VENDE</div><div style="font-size:60px;font-weight:800;margin-top:26px">✓ Prova</div></div>'))
# 3 constancia
cells=''
for r in range(4):
    for c in range(7):
        on = (c==0)
        cells+='<div style="position:absolute;left:%dpx;top:%dpx;width:96px;height:96px;border-radius:24px;background:%s"></div>'%(c*118,r*118,'#F5B83D' if on else 'rgba(255,255,255,.08)')
cells2=''
for r in range(4):
    for c in range(7):
        cells2+='<div style="position:absolute;left:%dpx;top:%dpx;width:96px;height:96px;border-radius:24px;background:#F5B83D"></div>'%(c*118,r*118)
S.append(page(top(3)+
 '<div class="big" style="left:60px;top:150px;font-size:430px;color:transparent;-webkit-text-stroke:5px #F5B83D">02</div>'+
 '<div class="h" style="top:560px;font-size:84px">Quem posta <span class="g">1 vez</span> por semana nunca sai do teste.</div>'+
 '<div style="position:absolute;left:80px;top:960px;transform:scale(.5);transform-origin:top left;width:826px;height:446px">%s</div>'%cells+
 '<div style="position:absolute;left:80px;top:1200px;font-size:26px;color:#8E96AD;font-weight:600;letter-spacing:2px">1 DIA EM 7</div>'+
 '<div style="position:absolute;left:560px;top:960px;transform:scale(.5);transform-origin:top left;width:826px;height:446px">%s</div>'%cells2+
 '<div style="position:absolute;left:560px;top:1200px;font-size:26px;color:#F5B83D;font-weight:700;letter-spacing:2px">TODO DIA</div>'))
# 4 gancho
S.append(page(top(4)+
 '<div class="big" style="left:60px;top:150px;font-size:430px;color:transparent;-webkit-text-stroke:5px #F5B83D">03</div>'+
 '<div class="h" style="top:560px;font-size:84px">Os <span class="g">2 primeiros segundos</span> decidem tudo.</div>'+
 '<div style="position:absolute;left:80px;top:1050px;width:920px;height:22px;border-radius:12px;background:rgba(255,255,255,.12)"></div>'+
 '<div style="position:absolute;left:80px;top:1050px;width:150px;height:22px;border-radius:12px;background:#F5B83D;box-shadow:0 0 40px #F5B83D"></div>'+
 '<div style="position:absolute;left:80px;top:1100px;font-size:30px;font-weight:700;color:#F5B83D">0:00 – 0:02</div>'+
 '<div style="position:absolute;right:80px;top:1100px;font-size:30px;font-weight:500;color:#8E96AD">resto do vídeo</div>'+
 '<div class="sub" style="top:1170px;font-size:34px">Mostre o resultado primeiro. Explique depois.</div>'))
# 5 resultado
bars=''
for i,(h,l) in enumerate([(220,'ALCANCE'),(340,'CLIQUES'),(480,'VENDAS')]):
    bars+='<div style="position:absolute;left:%dpx;bottom:0;width:260px;height:%dpx;border-radius:28px 28px 0 0;background:%s"></div><div style="position:absolute;left:%dpx;bottom:-52px;width:260px;text-align:center;font-size:26px;font-weight:700;letter-spacing:3px;color:%s">%s</div>'%(i*330,h,'#F5B83D' if i==2 else 'rgba(245,184,61,.35)',i*330,'#F5B83D' if i==2 else '#8E96AD',l)
S.append(page(top(5)+
 '<div class="h" style="top:150px;font-size:96px">Aplicando os 3, <span class="g">tudo sobe</span> junto.</div>'+
 '<div style="position:absolute;left:100px;top:600px;width:920px;height:520px">%s</div>'%bars))
# 6 cta
S.append(page(top(6)+
 '<div class="h" style="top:170px;font-size:104px">Quer o passo a passo <span class="g">completo?</span></div>'+
 '<div style="position:absolute;left:80px;top:640px;font-size:44px;font-weight:600;color:#D5D9E6">Comente a palavra</div>'+
 '<div style="position:absolute;left:80px;top:720px;background:#F5B83D;color:#0A0A10;font-size:120px;font-weight:800;letter-spacing:-3px;padding:26px 50px;border-radius:36px">COMEÇAR</div>'+
 '<div class="sub" style="top:1000px;font-size:36px">Eu te mando no direct.</div>'+
 '<div style="position:absolute;left:80px;bottom:70px;font-size:34px;font-weight:700">@diegoreisads</div>'))
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
    for i,h in enumerate(S,1):
        pg.set_content(h); pg.wait_for_timeout(300); pg.screenshot(path='%s/slide-%02d.jpg'%(OUT,i),type='jpeg',quality=93)
    b.close()
