# Estilo "Estudio": branco/preto/laranja, manchete curta, contador 01 / 04 (baseado nas capas de referencia aprovadas)
import sys,json,os,html,re,base64
from playwright.sync_api import sync_playwright
sys.path.insert(0,os.path.dirname(__file__))
from render_novo import rich,AVA
O='#F26A1B'
def _f(n):return 'data:font/ttf;base64,'+base64.b64encode(open('/usr/share/fonts/truetype/google-fonts/Poppins-%s.ttf'%n,'rb').read()).decode()
CSS='''
@font-face{font-family:P;src:url(@B@);font-weight:700}
@font-face{font-family:P;src:url(@M@);font-weight:500}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1350px;font-family:P,sans-serif;position:relative;overflow:hidden;background:@BG@;color:@FG@}
.h{position:absolute;top:44px;left:0;right:0;text-align:center;font-weight:500;font-size:28px;opacity:.85}
.c{position:absolute;right:60px;bottom:52px;font-weight:500;font-size:28px}
.pill{position:absolute;left:50%;transform:translateX(-50%);bottom:44px;border:3px solid #F26A1B;color:#F26A1B;border-radius:50px;padding:14px 46px;font-weight:500;font-size:26px;letter-spacing:6px}
.w{position:absolute;inset:0;padding:150px 80px 150px;display:flex;flex-direction:column;justify-content:center}
.t{font-weight:700;font-size:96px;line-height:1.02;letter-spacing:-3px}
.t b{color:#F26A1B}mark{background:none;color:#F26A1B}
.k{font-weight:700;font-size:30px;letter-spacing:6px;color:#F26A1B;margin-bottom:30px;text-transform:uppercase}
.b{font-weight:500;font-size:44px;line-height:1.35;margin-top:44px;opacity:.9}
.box{border:4px solid currentColor;border-radius:28px;padding:36px 42px;font-weight:500;font-size:38px;line-height:1.4;margin-top:40px}
.box mark{color:#F26A1B;font-weight:700}
.btn{display:inline-block;background:#F26A1B;color:#fff;font-weight:700;font-size:46px;padding:28px 56px;border-radius:100px;margin-top:50px;align-self:flex-start}
'''
def page(s,i,n,dark):
    bg,fg=('#0b0b0d','#fff') if dark else ('#fff','#111')
    cnt='%02d / %02d'%(i+1,n)
    k=f'<div class=k>{html.escape(s["k"])}</div>' if s.get('k') else ''
    body=f'{k}<div class=t>{rich(s["t"])}</div>'
    if s.get('b'):body+=f'<div class=b>{rich(s["b"])}</div>'
    if s.get('box'):body+=f'<div class=box>{rich(s["box"])}</div>'
    if s.get('cta'):body+=f'<div class=btn>Comente {html.escape(s["cta"].upper())}</div>'
    pill='' if i==n-1 else '<div class=pill>DESLIZE &rarr;</div>'
    return f'<html><head><meta charset=utf-8><style>{CSS.replace('@BG@',bg).replace('@FG@',fg).replace('@B@',_f('Bold')).replace('@M@',_f('Medium'))}</style></head><body><div class=h>@diegoreisads</div><div class=w>{body}</div>{pill}<div class=c>{cnt}</div></body></html>'
def main(jf,out):
    jobs=json.load(open(jf))
    with sync_playwright() as p:
        b=p.chromium.launch();pg=b.new_page(viewport={'width':1080,'height':1350})
        for j in jobs:
            f=f'{out}/{j["slug"]}';os.makedirs(f,exist_ok=True);n=len(j['slides'])
            for i,s in enumerate(j['slides']):
                if s.get('img'):
                    from PIL import Image
                    Image.open(s['img']).convert('RGB').resize((1080,1350),Image.LANCZOS).save(f'{f}/slide-{i+1:02d}.jpg',quality=94);continue
                pg.set_content(page(s,i,n,s.get('dark',False)));pg.wait_for_timeout(120)
                pg.screenshot(path=f'{f}/slide-{i+1:02d}.jpg',type='jpeg',quality=94)
if __name__=='__main__':main(sys.argv[1],sys.argv[2])
