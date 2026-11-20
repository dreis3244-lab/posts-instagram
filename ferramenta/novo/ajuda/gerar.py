import os,base64
from playwright.sync_api import sync_playwright
HERE=os.path.dirname(os.path.abspath(__file__)); FOT=os.path.join(HERE,'..','..','fotos')
def b64(p): return 'data:image/jpeg;base64,'+base64.b64encode(open(os.path.join(FOT,p+'-image.jpg'),'rb').read()).decode()
CSS='''*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;background:#0B0F1A;font-family:Poppins,sans-serif;color:#fff;overflow:hidden;position:relative}
.bg{position:absolute;inset:0;background:radial-gradient(900px 700px at 85% 10%,#1E3470 0%,rgba(11,15,26,0) 70%),radial-gradient(700px 600px at 0% 100%,#3A2A08 0%,rgba(11,15,26,0) 70%)}
.top{position:absolute;left:80px;right:80px;top:64px;display:flex;justify-content:space-between;font-size:26px;font-weight:500;color:#8E96AD;letter-spacing:2px}
.g{color:#F5B83D}.h{position:absolute;left:80px;right:80px;font-weight:800;line-height:1.02;letter-spacing:-2px}
.p{position:absolute;left:80px;right:80px;font-size:40px;font-weight:500;line-height:1.35;color:#D5D9E6}
.num{position:absolute;left:60px;top:140px;font-size:360px;font-weight:800;line-height:.8;letter-spacing:-8px;color:transparent;-webkit-text-stroke:5px #F5B83D}
.note{position:absolute;left:80px;right:80px;bottom:90px;padding:26px 32px;border-radius:26px;background:rgba(245,184,61,.12);border:1.5px solid rgba(245,184,61,.5);font-size:29px;line-height:1.35;color:#F3D9A0}
.pill{position:absolute;right:80px;bottom:70px;background:#F5B83D;color:#0B0F1A;font-weight:700;font-size:26px;letter-spacing:3px;padding:20px 38px;border-radius:99px}
.ph{position:absolute;border-radius:36px;box-shadow:0 30px 80px rgba(0,0,0,.6);border:3px solid rgba(255,255,255,.18)}'''
def wrap(x): return '<html><head><meta charset="utf-8"><style>%s</style></head><body><div class="bg"></div>%s</body></html>'%(CSS,x)
def top(n): return '<div class="top"><span>@diegoreisads</span><span>%02d / 06</span></div>'%n
def cover(foto,tag,title,sub):
    return wrap(top(1)+'<img class="ph" src="%s" style="right:70px;top:130px;width:420px;height:630px;transform:rotate(3deg)">'%b64(foto)+
     '<div style="position:absolute;left:80px;top:150px;background:#F5B83D;color:#0B0F1A;font-weight:800;font-size:26px;letter-spacing:3px;padding:12px 24px;border-radius:12px">%s</div>'%tag+
     '<div class="h" style="top:810px;font-size:96px">%s</div>'%title+
     '<div class="p" style="top:1170px;font-size:34px;width:700px">%s</div>'%sub+
     '<div class="pill" style="bottom:62px">DESLIZE →</div>')
def step(n,total,title,body,note=None):
    return wrap(top(n)+'<div class="num">%02d</div>'%(n-1)+'<div class="h" style="top:520px;font-size:84px">%s</div>'%title+
     '<div class="p" style="top:%dpx">%s</div>'%(760,body)+
     ('<div class="note">%s</div>'%note if note else ''))
def final(txt,foto):
    return wrap(top(6)+'<div class="h" style="top:170px;font-size:100px">%s</div>'%txt+
     '<svg style="position:absolute;left:80px;top:700px" width="200" height="260" viewBox="0 0 24 30"><path d="M3 1h18v27l-9-6.5L3 28z" fill="#F5B83D"/></svg>'+
     '<div class="p" style="left:340px;top:720px;font-size:46px;font-weight:700;color:#fff">Salva para consultar depois.</div>'+
     '<div class="p" style="left:340px;top:870px;font-size:40px">E manda para quem precisa ver isso.</div>'+
     '<div style="position:absolute;left:80px;bottom:70px;font-size:34px;font-weight:700">@diegoreisads</div>'+
     '<img class="ph" src="%s" style="right:70px;bottom:60px;width:200px;height:300px">'%b64(foto))
C={
'black-friday-desconto-falso':[
 cover('007e7f9b','BLACK FRIDAY 27/11','Como não cair em <span class="g">desconto falso</span>','Passo a passo antes de comprar.'),
 step(2,6,'Anote o preço <span class="g">hoje</span>','O Procon orienta anotar o preço desde já. No dia da promoção, você compara com o valor real e vê se o desconto existe.','Em 2025, 45,4% dos produtos não tiveram economia real (pesquisa Timelens).'),
 step(3,6,'Compare em <span class="g">vários</span> sites','Pesquise o mesmo produto em lojas, apps e também nas lojas físicas. Se possível, veja o histórico de preço.'),
 step(4,6,'Confira se a loja <span class="g">existe</span>','Veja o cadeado e o https, o CNPJ, o contato e as queixas no Reclame Aqui. Não clique em link de oferta que chegou por mensagem: digite o endereço da loja.'),
 step(5,6,'Pague do jeito <span class="g">seguro</span>','Prefira cartão de crédito, que é mais fácil de contestar, ou cartão virtual. No Pix, confira o nome de quem recebe antes de pagar.'),
 final('Vai comprar na <span class="g">Black Friday</span>?','0f6039f9')],
'ia-video-descobrir':[
 cover('920ef168','NOVIDADE DO TIKTOK','Esse vídeo foi feito com <span class="g">IA</span>? Como descobrir','O TikTok lançou uma ferramenta para isso.'),
 step(2,6,'Olhe o <span class="g">rótulo</span> de IA','O TikTok já identificou e rotulou mais de 5 bilhões de vídeos feitos com IA. Procure o aviso no próprio vídeo.'),
 step(3,6,'Use a <span class="g">Detecção de IA</span>','Fica no Centro de Transparência do TikTok. Você envia a foto ou o vídeo e ela verifica. Dá para usar até sem ter conta.'),
 step(4,6,'Saiba o que ela <span class="g">lê</span>','A ferramenta analisa os metadados C2PA (Content Credentials) e uma marca-d\'água invisível.','Sem sinal digital, não é garantia de que o vídeo é real. Use como mais uma checagem.'),
 step(5,6,'Usaram sua <span class="g">imagem</span> com IA?','Criadores elegíveis podem se cadastrar no Likeness Detection, receber aviso quando a imagem for usada sem consentimento e denunciar.'),
 final('Vale <span class="g">desconfiar</span> antes de compartilhar.','007e7f9b')],
'black-friday-checklist-vendedor':[
 cover('0f6039f9','PARA QUEM VENDE','Vai vender na <span class="g">Black Friday</span>? Ajeite isso hoje','4 pontos que valem antes do dia 27.'),
 step(2,6,'Estoque e <span class="g">agenda</span> de conteúdo','O próprio TikTok Shop orienta o vendedor a garantir estoque e montar uma agenda de conteúdo antes da campanha.'),
 step(3,6,'Pense no <span class="g">frete</span>','Frete grátis é o benefício mais esperado: 79% dos entrevistados da pesquisa da Shopee.','Pesquisa da própria Shopee, com 790 pessoas, sobre intenção de compra.'),
 step(4,6,'Ofereça <span class="g">parcelamento</span>','74% pretendem parcelar as compras nas promoções, segundo a mesma pesquisa.'),
 step(5,6,'Teste uma <span class="g">live</span>','O TikTok Shop diz que as lives são o canal de maior conversão. A média diária de lives cresceu 20 vezes em um ano.'),
 final('Qual desses você <span class="g">ainda não fez</span>?','007e7f9b')],
}
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
    for slug,sl in C.items():
        d=os.path.join(HERE,'saida',slug); os.makedirs(d,exist_ok=True)
        for i,h in enumerate(sl,1):
            pg.set_content(h); pg.wait_for_timeout(250); pg.screenshot(path='%s/slide-%02d.jpg'%(d,i),type='jpeg',quality=93)
    b.close()
