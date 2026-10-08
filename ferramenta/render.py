import base64,os,io,sys,json,shutil,re
import pathlib;S=str(pathlib.Path(__file__).resolve().parent)+'/'
L=24
from PIL import Image
POOL=['007e7f9b','0a31043d','2867957f','80bd0a6c','92d4b8f2','34db03c1','3a08c192','c585f51c','98e4ab95','56ec158c','f71430f4','9124974e','32849d64','c03b6113','920ef168','f8ecfdb1','6c5df8bd','56f1beea','48537888','e0d76cec','0f6039f9','3255574b','4e125ccb','a8499a1c']
UP=S+'fotos/'
files=[UP+p+'-image.jpg' for p in POOL]
PYD={'0f6039f9':45,'3255574b':45,'4e125ccb':45,'a8499a1c':50,'92d4b8f2':8,'98e4ab95':8,'32849d64':8,'34b8c541':45,'fe8c4d87':45,'406352b7':35,'0a31043d':40,'34db03c1':40,'56ec158c':40,'c03b6113':40,'2867957f':40,'f8ecfdb1':35,'10497d86':30,'7bc86e39':30}
from playwright.sync_api import sync_playwright
def b64png(f):return 'data:image/png;base64,'+base64.b64encode(open(f,'rb').read()).decode()
def b64(f):
    im=Image.open(f).convert('RGB');im.thumbnail((1700,1700));b=io.BytesIO();im.save(b,'JPEG',quality=90);return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
TIK=['tiktok-26x','novidade-live','3-erros-tiktok','novidade-moda','5-videos','novidade-ia-no-tiktok','black-friday']
SHO=['novidade-shopee','shopee-kits','shopee-produto','shopee-instagram']
def cat(slug):
    if slug.startswith('instagram'):return 'insta'
    if any(slug.startswith(x) for x in TIK):return 'tiktok'
    if any(slug.startswith(x) for x in SHO):return 'shopee'
    if slug.startswith('ia-') or slug.startswith('5-prompts'):return 'ia'
    return 'gold'
BADGE={'minha-historia':'+20 MIL|ALUNOS','por-que-ensino-live':'+20 MIL|ALUNOS','quem-eu-ajudo':'+20 MIL|ALUNOS'}
im0=Image.open(''+UP+'007e7f9b-image.jpg').convert('RGB').crop((300,270,650,620)).resize((400,400));bb=io.BytesIO();im0.save(bb,'JPEG',quality=92);AV='data:image/jpeg;base64,'+base64.b64encode(bb.getvalue()).decode()

PORT=[j for j,p in enumerate(POOL) if p not in ('80bd0a6c','56f1beea') and (lambda im:im.size[1]/im.size[0]>=1.3)(Image.open(UP+p+'-image.jpg'))]
ST={'a':0,'p':0,'K':-1}
def nxt(port):
    if port:
        v=PORT[ST['p']%len(PORT)];ST['p']+=3;return v
    v=ST['a']%L;ST['a']+=1;return v
def tags_for(slug):
    t=[]
    if 'live' in slug or slug.startswith('checklist'):t.append('live')
    if any(k in slug for k in ('tiktok','shopee','instagram','moda','black','5-videos')):t.append('shop')
    if slug.startswith('ia-') or slug.startswith('5-prompts') or 'novidade-ia' in slug:t.append('ia')
    return t[:2]
def brands_for(slug):
    b=[]
    if 'tiktok' in slug or any(k in slug for k in ('moda','5-videos')):b.append('tiktok')
    if 'shopee' in slug:b.append('shopee')
    if slug.startswith('ia-') or slug.startswith('5-prompts') or 'novidade-ia' in slug or '-ia-' in slug:b.append('ia')
    return b[:2]
def INFO(K,i,N,slug):
    full=(i==0 and K%2==0) or (i==N-1)
    if full:return {'mode':'full','photos':[nxt(True)],'tags':tags_for(slug),'brands':brands_for(slug)}
    if i==0:return {'mode':'clean','photos':[nxt(False)],'tags':tags_for(slug),'brands':brands_for(slug)}
    return {'mode':'clean','photos':[nxt(False)],'tags':[]}

HANDLE=sys.argv[1];jf=sys.argv[2];outroot=sys.argv[3];only=sys.argv[4].split(',') if len(sys.argv)>4 else None
jobs=json.load(open(jf))
def sub(x):
    if isinstance(x,str):return x.replace('@diegoreisads','@'+HANDLE).replace('{H}',HANDLE)
    if isinstance(x,list):return [sub(i) for i in x]
    if isinstance(x,dict):return {k:sub(v) for k,v in x.items()}
    return x
with sync_playwright() as p:
    b=p.chromium.launch();errs=[]
    pg=b.new_page(viewport={'width':1200,'height':1000});pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.set_content('<canvas id=c></canvas>');pg.add_script_tag(path=S+'engine3.js')
    pg.evaluate('(d)=>{window.PY=d;window.HANDLE=%s}'%json.dumps(HANDLE),[PYD.get(p,25) for p in POOL])
    pg.evaluate("async(u)=>{window.AVATAR=await new Promise(r=>{const i=new Image();i.onload=()=>r(i);i.src=u})}",AV)
    pg.evaluate("async(u)=>{window.LOGOS={};for(const k in u){LOGOS[k]=await new Promise(r=>{const i=new Image();i.onload=()=>r(i);i.src=u[k]})}}",{k:b64png(f'{S}logos/{k}.png') for k in ('ia','shopee','tiktok')})
    pg.evaluate("async(u)=>{window.IMGS=await Promise.all(u.map(s=>new Promise(r=>{const i=new Image();i.onload=()=>r(i);i.src=s})))}",[b64(f) for f in files])
    K=0
    for j in jobs:
        K+=1;slug=j['slug']
        if only and slug not in only:continue
        slides=sub(j['slides']);N=len(slides);cap=sub(j['cap'])
        folder=f"{outroot}/{j['d']+'/' if j.get('d') else ''}{j['n']}-{slug}";os.makedirs(folder,exist_ok=True)
        for i,s in enumerate(slides):
            dd=pg.evaluate("""async([s,i,n,info])=>{const c=document.getElementById('c');await drawSlide(c,s,i,n,info);return c.toDataURL('image/jpeg',0.93)}""",[s,i,N,INFO(K,i,N,slug)])
            open(f'{folder}/slide-{i+1:02d}.jpg','wb').write(base64.b64decode(dd.split(',')[1]))
        open(f'{folder}/legenda.txt','w').write(cap+'\n');print(slug,N)
    print(errs)
