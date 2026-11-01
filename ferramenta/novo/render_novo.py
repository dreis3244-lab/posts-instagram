import sys,json,os,re,base64,html,pathlib
from playwright.sync_api import sync_playwright
S=str(pathlib.Path(__file__).resolve().parent.parent)+'/'
def uri(f,m):return f'data:{m};base64,'+base64.b64encode(open(f,'rb').read()).decode()
def rich(t):
    t=html.escape(t or '').replace('\n','<br>')
    t=re.sub(r'\*([^*]+)\*',r'<b>\1</b>',t);t=re.sub(r'\^([^^]+)\^',r'<mark>\1</mark>',t);return t
def foto(p):return uri(S+'fotos/%s-image.jpg'%p,'image/jpeg')
LOGO={k:uri(S+'logos/%s.png'%k,'image/png') for k in ('ia','shopee','tiktok')}
AVA=foto('007e7f9b')
CSS='''
@font-face{font-family:P;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf);font-weight:700}
@font-face{font-family:P;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf);font-weight:500}
@font-face{font-family:P;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Regular.ttf);font-weight:400}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1350px;font-family:P,Inter,sans-serif;overflow:hidden;position:relative}
.s{position:absolute;inset:0;padding:84px 72px;display:flex;flex-direction:column}
.k{font-weight:700;font-size:30px;letter-spacing:5px;text-transform:uppercase}
.t{font-weight:700;line-height:1.04;letter-spacing:-2px}
.b{font-weight:500;font-size:46px;line-height:1.35}
.mid{justify-content:center;padding-bottom:170px}
.src{position:absolute;left:72px;right:72px;bottom:150px;font-size:24px;opacity:.7;font-weight:500}
.dots{position:absolute;left:72px;bottom:62px;display:flex;gap:12px}.dots i{width:14px;height:14px;border-radius:50%}
.sw{position:absolute;right:72px;bottom:50px;font-weight:700;font-size:30px;letter-spacing:2px}
.logos{display:flex;gap:16px}.logos img{height:54px}
.who{display:flex;align-items:center;gap:20px;font-weight:700;font-size:30px}
.who img{width:76px;height:76px;border-radius:50%;object-fit:cover;object-position:50% 22%}
.item{display:flex;align-items:center;gap:30px;margin-bottom:26px}
.ph{position:absolute;right:0;bottom:0}
.ph img{display:block;height:var(--ph,820px);width:auto}
'''
# estilos: cada um define cores + decoracoes
ST={
'neon':'''body{background:#07070a;color:#fff}
.bg{position:absolute;inset:0;background:radial-gradient(900px 700px at 100% 0,#c6ff3d33,transparent 60%)}
.k{color:#c6ff3d}.t{color:#fff;text-transform:none}mark{background:none;color:#c6ff3d}.t b{color:#c6ff3d}
.b{color:#d7d7de}.num{position:absolute;right:56px;top:40px;font-size:300px;font-weight:700;color:#ffffff0d;line-height:1}
.dots i{background:#ffffff33}.dots i.on{background:#c6ff3d;width:44px;border-radius:8px}.sw{color:#c6ff3d}
.card{background:#14141a;border:2px solid #2a2a33;border-radius:36px;padding:34px 40px}
.card .a{font-weight:700;font-size:60px;color:#c6ff3d;min-width:230px;letter-spacing:-1px}.card .x{font-size:36px;font-weight:500;color:#e8e8ee;line-height:1.25}
.btn{display:inline-block;background:#c6ff3d;color:#07070a;font-weight:700;font-size:44px;padding:28px 54px;border-radius:100px}
.ph img{border-radius:40px 0 0 0;border:3px solid #c6ff3d55;border-right:0;border-bottom:0}''',
'edit':'''body{background:#f3eee3;color:#111}
.k{color:#111;background:#ffd23f;display:inline-block;padding:10px 20px;border:3px solid #111;align-self:flex-start;transform:rotate(-2deg)}
.t{color:#111;letter-spacing:-3px}mark{background:#ff4d2e;color:#fff;padding:0 14px;border-radius:10px;box-decoration-break:clone;-webkit-box-decoration-break:clone}.t b{text-decoration:underline;text-decoration-thickness:10px;text-decoration-color:#ffd23f;text-underline-offset:6px}
.b{color:#2b2b2b}.num{position:absolute;right:60px;top:60px;font-size:150px;font-weight:700;color:#111;line-height:1;-webkit-text-stroke:0}
.dots i{background:#11111133;border:2px solid #111}.dots i.on{background:#111}.sw{color:#111}
.card{background:#fff;border:4px solid #111;border-radius:28px;padding:30px 36px;box-shadow:12px 12px 0 #111}
.card .a{font-weight:700;font-size:58px;color:#ff4d2e;min-width:230px;letter-spacing:-1px}.card .x{font-size:36px;font-weight:500;line-height:1.25}
.btn{display:inline-block;background:#ff4d2e;color:#fff;border:4px solid #111;box-shadow:10px 10px 0 #111;font-weight:700;font-size:44px;padding:26px 50px;border-radius:20px}
.ph img{border:4px solid #111;border-radius:30px 0 0 0;box-shadow:-12px -12px 0 #ffd23f;border-right:0;border-bottom:0}.who{color:#111}''',
'grad':'''body{background:linear-gradient(155deg,#2b0a6b 0%,#7a1fa2 48%,#ff5a36 100%);color:#fff}
.k{color:#ffe27a}.t{color:#fff}mark{background:#ffe27a;color:#2b0a6b;padding:0 14px;border-radius:14px;box-decoration-break:clone;-webkit-box-decoration-break:clone}.t b{color:#ffe27a}
.b{color:#ffffffeb}.num{position:absolute;right:56px;top:40px;font-size:300px;font-weight:700;color:#ffffff14;line-height:1}
.dots i{background:#ffffff55}.dots i.on{background:#fff;width:44px;border-radius:8px}.sw{color:#fff}
.card{background:#ffffff1f;border:2px solid #ffffff44;border-radius:36px;padding:34px 40px;backdrop-filter:blur(8px)}
.card .a{font-weight:700;font-size:60px;color:#ffe27a;min-width:230px;letter-spacing:-1px}.card .x{font-size:36px;font-weight:500;line-height:1.25}
.btn{display:inline-block;background:#fff;color:#2b0a6b;font-weight:700;font-size:44px;padding:28px 54px;border-radius:100px}
.ph img{border-radius:44px 0 0 0;border:3px solid #ffffff66;border-right:0;border-bottom:0}'''}
def dots(i,n,sw=True):return '<div class=dots>'+''.join('<i class="%s"></i>'%('on' if j==i else '') for j in range(n))+'</div><div class=sw>%s</div>'%('ARRASTE &rarr;' if (i<n-1 and sw) else '')
def slide(s,i,n,photo,logos):
    num='<div class=num>%02d</div>'%(i+1) if i>0 else ''
    d=dots(i,n,photo is None);size=lambda L:max(78,min(150,int(2200/ (max(L,12)**.62*1.0))))
    if i==0:
        t=s.get('t','');fs=100 if len(t)<60 else 88 if len(t)<85 else 78
        lg=''.join('<img src="%s">'%LOGO[k] for k in logos)
        return f'<div class=bg></div><div class=s style="padding-bottom:84px"><div class=who><img src="{AVA}">Diego Reis</div><div style="height:50px"></div><div class=k>{html.escape(s.get("k",""))}</div><div style="height:28px"></div><div class=t style="font-size:{fs}px;max-width:920px;position:relative;z-index:2">{rich(t)}</div><div style="height:28px"></div><div class=b style="max-width:600px;font-size:38px;position:relative;z-index:2">{rich(s.get("b",""))}</div><div class=logos style="margin-top:auto;margin-bottom:60px">{lg}</div></div>'+(f'<div class=ph style="--ph:640px"><img src="{photo}"></div>' if photo else '')+d
    if s.get('l')=='list':
        its=''.join(f'<div class="card item"><div class=a>{html.escape(x["a"])}</div><div class=x>{rich(x["t"])}</div></div>' for x in s['items'])
        src=f'<div class=src>{html.escape(s["src"])}</div>' if s.get('src') else ''
        return f'<div class=bg></div>{num}<div class="s mid"><div class=k>{html.escape(s.get("k",""))}</div><div style="height:26px"></div><div class=t style="font-size:92px;margin-bottom:50px">{rich(s["t"])}</div>{its}</div>{src}{d}'
    if s.get('l')=='enquete':
        opts=''.join(f'<div class="card item"><div class=a>{o[0]}</div><div class=x>{rich(o[2:].strip(" )-:"))}</div></div>' for o in s['b'].split('\n') if o.strip())
        return f'<div class=bg></div>{num}<div class="s mid"><div class=k>{html.escape(s.get("k",""))}</div><div style="height:26px"></div><div class=t style="font-size:100px;margin-bottom:50px">{rich(s["t"])}</div>{opts}</div>{d}'
    if s.get('follow'):
        c=s.get('cta','');cb=f'<div style="margin-top:40px"><span class=btn>Comente {html.escape(c.upper())}</span></div>' if c else ''
        return f'<div class=bg></div><div class=s><div class=who><img src="{AVA}">@diegoreisads</div><div style="height:90px"></div><div class=t style="font-size:104px;position:relative;z-index:2;max-width:940px">{rich(s["t"])}</div><div style="height:30px"></div><div class=b style="max-width:{900 if photo is None else 600}px;position:relative;z-index:2">{rich(s.get("b",""))}</div>{cb}</div>'+(f'<div class=ph style="--ph:600px"><img src="{photo}"></div>' if photo else '')+d
    t=s['t'];fs=116 if len(t)<40 else 100 if len(t)<75 else 86
    src=f'<div class=src>{html.escape(s["src"])}</div>' if s.get('src') else ''
    return f'<div class=bg></div>{num}<div class="s mid"><div class=k>{html.escape(s.get("k",""))}</div><div style="height:30px"></div><div class=t style="font-size:{fs}px">{rich(t)}</div><div style="height:44px"></div><div class=b>{rich(s.get("b",""))}</div></div>{src}{d}'
def main(jf,out,styles):
    jobs=json.load(open(jf))
    with sync_playwright() as p:
        b=p.chromium.launch();pg=b.new_page(viewport={'width':1080,'height':1350})
        for st in styles:
            for j in jobs:
                n=len(j['slides']);f=f'{out}/{st}/{j["slug"]}';os.makedirs(f,exist_ok=True)
                for i,s in enumerate(j['slides']):
                    ph=None
                    if i==0 and j.get('capa'):ph=foto(j['capa'])
                    if i==n-1 and j.get('fim'):ph=foto(j['fim'])
                    h=f'<html><head><meta charset=utf-8><style>{CSS}{ST[st]}</style></head><body>{slide(s,i,n,ph,j.get("logos",[]))}</body></html>'
                    pg.set_content(h);pg.wait_for_timeout(120)
                    pg.screenshot(path=f'{f}/slide-{i+1:02d}.jpg',type='jpeg',quality=93)
