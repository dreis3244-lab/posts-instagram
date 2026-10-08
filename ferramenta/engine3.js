// Motor v3 — estilo post limpo: fundo branco, letra fina, uma cor de destaque (dourado)
const W=1080,H=1350,M=72;
const F="Poppins,'Liberation Sans',sans-serif";
const INK='#0f172a',GREY='#64748b',LINE='#e2e8f0',GOLD='#d9a21b',GOLDD='#a9760a',MARK='#fde9a6';
window.IMGS=[];
function rr(c,x,y,w,h,r){c.beginPath();c.moveTo(x+r,y);c.arcTo(x+w,y,x+w,y+h,r);c.arcTo(x+w,y+h,x,y+h,r);c.arcTo(x,y+h,x,y,r);c.arcTo(x,y,x+w,y,r);c.closePath()}
function cover(c,im,x,y,w,h,px=50,py=25,z=1){const s=Math.max(w/im.width,h/im.height)*z,dw=im.width*s,dh=im.height*s;const ox=x-(dw-w)*px/100,oy=y-(dh-h)*py/100;c.save();c.beginPath();c.rect(x,y,w,h);c.clip();c.drawImage(im,ox,oy,dw,dh);c.restore()}
function photo(c,i,x,y,w,h,py=25){const im=IMGS[i];if(!im)return;c.save();rr(c,x,y,w,h,30);c.clip();cover(c,im,x,y,w,h,50,(window.PY&&window.PY[i]!=null)?window.PY[i]:py);c.restore()}
function verified(c,x,y,r){c.save();c.fillStyle='#1d9bf0';c.beginPath();for(let k=0;k<16;k++){const a=k*Math.PI/8,q=k%2?r*.86:r;c.lineTo(x+Math.cos(a)*q,y+Math.sin(a)*q)}c.closePath();c.fill();c.strokeStyle='#fff';c.lineWidth=r*.2;c.lineCap='round';c.lineJoin='round';c.beginPath();c.moveTo(x-r*.42,y+r*.02);c.lineTo(x-r*.1,y+r*.36);c.lineTo(x+r*.45,y-r*.32);c.stroke();c.restore()}
function avatar(c,cx,cy,r){c.save();c.beginPath();c.arc(cx,cy,r,0,7);c.clip();if(window.AVATAR)c.drawImage(window.AVATAR,cx-r,cy-r,r*2,r*2);c.restore()}
function header(c,i,n,dark){avatar(c,M+58,106,56);{const g=c.createLinearGradient(M-10,170,M+126,40);g.addColorStop(0,'#fbbf24');g.addColorStop(.5,'#f97316');g.addColorStop(1,'#db2777');c.strokeStyle=g;c.lineWidth=7;c.beginPath();c.arc(M+58,106,59,0,7);c.stroke()}c.textBaseline='alphabetic';c.fillStyle=dark?'#fff':INK;c.font=`700 44px ${F}`;c.fillText('Diego Reis',M+140,100);const nw=c.measureText('Diego Reis').width;verified(c,M+140+nw+30,86,17);
  c.fillStyle=dark?'#ffffffbb':GREY;c.font=`400 32px ${F}`;c.fillText('@'+(window.HANDLE||'diegoreisads')+'  ·  agora',M+140,146);
  c.textAlign='right';c.font=`400 28px ${F}`;c.fillText(`${i+1}/${n}`,W-M,104);c.textAlign='left'}
function footer(c,i,n,dark){const y=H-72;for(let k=0;k<n;k++){c.fillStyle=k===i?(dark?'#fff':INK):(dark?'#ffffff55':LINE);c.beginPath();c.arc(M+8+k*30,y,k===i?7:6,0,7);c.fill()}
  if(i<n-1){c.fillStyle=dark?'#ffffffcc':GREY;c.font=`500 28px ${F}`;c.textAlign='right';c.fillText('Arrasta  →',W-M,y+10);c.textAlign='left'}}
// texto rico: *destaque* e ^destaque^ = negrito com marca-texto dourada
function tok(t){const out=[];const re=/(\*[^*]+\*|\^[^^]+\^)/g;let last=0,m;const push=(s,hl)=>{if(!s)return;const ps=s.split(/(\s+)/);let first=true;for(const p of ps){if(!p)continue;if(/^\s+$/.test(p)){out.push({sp:true});continue}out.push({w:p,hl})}};
  while((m=re.exec(t))){push(t.slice(last,m.index),0);push(m[0].slice(1,-1),1);last=m.index+m[0].length}push(t.slice(last),0);
  // cola pontuação: palavra sem espaço antes
  const res=[];let gap=true;for(const o of out){if(o.sp){gap=true;continue}o.glue=!gap&&res.length>0;res.push(o);gap=false}
  return res}
function layout(c,t,size,wt,maxW,hlWt=700){const ws=tok(t);const sp=size*.28;const lines=[[]];let x=0;
  for(const o of ws){c.font=`${o.hl?hlWt:wt} ${size}px ${F}`;o.mw=c.measureText(o.w).width;const pre=(lines.at(-1).length&&!o.glue)?sp:0;
    if(x+pre+o.mw>maxW&&lines.at(-1).length&&!o.glue){lines.push([]);x=0;o.dx=0}else o.dx=x+pre;x=o.dx+o.mw;lines.at(-1).push(o)}
  return lines}
function fit(c,t,{max,min,wt,maxW,maxLines}){for(let s=max;s>=min;s-=2){const L=layout(c,t,s,wt,maxW);if(L.length<=maxLines&&L.every(l=>l.every(o=>o.mw<=maxW)))return {s,L,wt}}return {s:min,L:layout(c,t,min,wt,maxW),wt}}
function drawRich(c,f,x,y,lh=1.28,color=INK){const {s,L,wt}=f;let yy=y+s;
  for(const line of L){let i=0;while(i<line.length){if(line[i].hl){let j=i;while(j+1<line.length&&line[j+1].hl&&!line[j+1].glue)j++;const x0=x+line[i].dx-8,x1=x+line[j].dx+line[j].mw+8;c.fillStyle=MARK;rr(c,x0,yy-s*.86,x1-x0,s*1.1,10);c.fill();i=j+1}else i++}
    for(const o of line){c.font=`${o.hl?700:wt} ${s}px ${F}`;c.fillStyle=o.hl?INK:color;c.fillText(o.w,x+o.dx,yy)}yy+=s*lh}
  return yy-s*lh+s*.5}

function containBox(im,w,h){const s=Math.min(w/im.width,h/im.height);return {w:im.width*s,h:im.height*s}}
function photoIn(c,idxs,x,y,w,h){c.fillStyle='#f5f2ea';rr(c,x,y,w,h,36);c.fill();const pad=22,gap=20;const n=idxs.length;const sw=(w-2*pad-gap*(n-1))/n,sh=h-2*pad;
  const boxes=idxs.map(k=>containBox(IMGS[k],sw,sh));const tot=boxes.reduce((a,b)=>a+b.w,0)+gap*(n-1);let cx=x+(w-tot)/2;
  idxs.forEach((k,j)=>{const b=boxes[j];const by=y+(h-b.h)/2;c.save();rr(c,cx,by,b.w,b.h,24);c.clip();c.drawImage(IMGS[k],cx,by,b.w,b.h);c.restore();cx+=b.w+gap})}
function fullOK(k){const im=IMGS[k];return im&&im.height/im.width>=1.3}
function drawFull(c,sl,i,n,k,last,tags){cover(c,IMGS[k],0,0,W,H,50,6,1);
  let g=c.createLinearGradient(0,H*.30,0,H);g.addColorStop(0,'#0f172a00');g.addColorStop(.5,'#0f172acc');g.addColorStop(1,'#0f172af2');c.fillStyle=g;c.fillRect(0,0,W,H);
  g=c.createLinearGradient(0,0,0,240);g.addColorStop(0,'#0f172a99');g.addColorStop(1,'#0f172a00');c.fillStyle=g;c.fillRect(0,0,W,240);
  header(c,i,n,true);if(i===0){const bk=brandsOf(sl,window.CURINFO);const lx=brandChip(c,bk,W-M,188,112);tagPills(c,(tags||[]).filter(t=>t==='live'||(!bk.length)),lx-(bk.length?14:0),216,true)}
  const maxW=W-2*M;const f=fit(c,sl.t||'',{max:last?80:88,min:56,wt:500,maxW,maxLines:4});
  const bl=sl.b?wrap(c,sl.b,`400 36px ${F}`,maxW).slice(0,3):[];
  const th=f.L.length*f.s*1.26,bh=bl.length*50,ch=(sl.cta?130:0)+(sl.follow?96:0);const total=(sl.k?44:0)+th+(bl.length?bh+20:0)+ch;
  let y=H-150-total;if(sl.k){c.fillStyle='#ffd257';c.font=`600 25px ${F}`;c.letterSpacing='4px';c.fillText(sl.k.toUpperCase(),M,y+26);c.letterSpacing='0px';y+=44}
  y=drawRich(c,f,M,y,1.26,'#ffffff')+8;
  if(bl.length){c.fillStyle='#ffffffdd';c.font=`400 36px ${F}`;for(const ln of bl){c.fillText(ln,M,y+34);y+=50}y+=10}
  if(sl.cta){y+=14;y+=ctaBtn(c,M,y,sl.cta,true)}
  if(sl.follow){y+=18;engageRow(c,M,y,true)}
  footer(c,i,n,true)}



function engageRow(c,x,y,dark){const h=76,fg=dark?'#ffffff':INK;const items=[['heart','Curta'],['mark','Salve'],['plus','Siga @'+(window.HANDLE||'diegoreisads')]];c.font=`600 30px ${F}`;let xx=x;
  for(const [ic,lb] of items){const tw=c.measureText(lb).width;const w=tw+44+64;c.fillStyle=dark?'#ffffff1f':'#f1f5f9';rr(c,xx,y,w,h,h/2);c.fill();c.strokeStyle=dark?'#ffffff66':LINE;c.lineWidth=2;rr(c,xx,y,w,h,h/2);c.stroke();
    const cx=xx+44,cy=y+h/2;c.save();c.strokeStyle=dark?'#ffd257':GOLDD;c.fillStyle=dark?'#ffd257':GOLD;c.lineWidth=4;c.lineJoin='round';c.lineCap='round';
    if(ic==='heart'){c.beginPath();c.moveTo(cx,cy+13);c.bezierCurveTo(cx-24,cy-3,cx-14,cy-19,cx,cy-8);c.bezierCurveTo(cx+14,cy-19,cx+24,cy-3,cx,cy+13);c.closePath();c.fill()}
    if(ic==='mark'){c.beginPath();c.moveTo(cx-11,cy-16);c.lineTo(cx+11,cy-16);c.lineTo(cx+11,cy+16);c.lineTo(cx,cy+7);c.lineTo(cx-11,cy+16);c.closePath();c.stroke()}
    if(ic==='plus'){c.beginPath();c.moveTo(cx-14,cy);c.lineTo(cx+14,cy);c.moveTo(cx,cy-14);c.lineTo(cx,cy+14);c.stroke()}
    c.restore();c.fillStyle=fg;c.textBaseline='middle';c.font=`600 30px ${F}`;c.fillText(lb,xx+70,y+h/2+2);c.textBaseline='alphabetic';xx+=w+16}
  return h}
function brandsOf(sl,info){const t=((sl.k||'')+' '+(sl.t||'')).replace(/[*^]/g,'');const b=[];if(/tiktok/i.test(t))b.push('tiktok');if(/shopee/i.test(t))b.push('shopee');if(/\bIA\b/.test(t))b.push('ia');for(const x of (info&&info.brands)||[])if(!b.includes(x))b.push(x);return b.slice(0,2)}
function brandChip(c,keys,rightX,y,h){if(!keys.length||!window.LOGOS)return rightX;const lh=h-20;const ws=keys.map(k=>{const im=LOGOS[k];return im.width/im.height*lh});const w=ws.reduce((a,b)=>a+b,0)+20*2+(keys.length-1)*18;const x=rightX-w;
  c.save();c.shadowColor='#0f172a33';c.shadowBlur=18;c.shadowOffsetY=4;c.fillStyle='#ffffff';rr(c,x,y,w,h,h/2>30?26:h/2);c.fill();c.restore();c.strokeStyle='#e2e8f0';c.lineWidth=2;rr(c,x,y,w,h,h/2>30?26:h/2);c.stroke();
  let xx=x+20;keys.forEach((k,i)=>{c.drawImage(LOGOS[k],xx,y+10,ws[i],lh);xx+=ws[i]+18});return x}
function tagPills(c,tags,rightX,y,dark){if(!tags||!tags.length)return;let x=rightX;
  for(const t of tags.slice().reverse()){const label={live:'AO VIVO',shop:'SHOP',ia:'IA'}[t];c.font=`700 24px ${F}`;c.letterSpacing='2px';const tw=c.measureText(label).width;const w=tw+30+58,h=56;x-=w;
    c.fillStyle=dark?'#ffffff':INK;rr(c,x,y,w,h,h/2);c.fill();const cx=x+40,cy=y+h/2;c.save();
    if(t==='live'){c.fillStyle='#ef4444';c.beginPath();c.arc(cx,cy,10,0,7);c.fill();c.strokeStyle='#ef444488';c.lineWidth=3;c.beginPath();c.arc(cx,cy,17,0,7);c.stroke()}
    if(t==='shop'){c.strokeStyle=GOLD;c.lineWidth=3.5;c.lineJoin='round';c.beginPath();c.rect(cx-13,cy-6,26,20);c.stroke();c.beginPath();c.arc(cx,cy-6,7,Math.PI,0);c.stroke()}
    if(t==='ia'){c.fillStyle=GOLD;c.translate(cx,cy);c.beginPath();for(let k=0;k<8;k++){const a=k*Math.PI/4,q=k%2?5:15;c.lineTo(Math.cos(a-Math.PI/2)*q,Math.sin(a-Math.PI/2)*q)}c.closePath();c.fill()}
    c.restore();c.fillStyle=dark?INK:'#fff';c.textBaseline='middle';c.fillText(label,x+62,y+h/2+2);c.textBaseline='alphabetic';c.letterSpacing='0px';x-=12}}
function wrap(c,t,font,maxW){c.font=font;const out=[];for(const para of String(t).split('\n')){let line='';for(const w of para.split(/\s+/)){const tt=line?line+' '+w:w;if(c.measureText(tt).width>maxW&&line){out.push(line);line=w}else line=tt}out.push(line)}return out}
function kicker(c,x,y,t){c.fillStyle=GOLDD;c.font=`600 25px ${F}`;c.letterSpacing='4px';c.fillText(t.toUpperCase(),x,y);c.letterSpacing='0px'}
function ctaBtn(c,x,y,word,onDark){const a='Comente ';c.font=`500 34px ${F}`;const w1=c.measureText(a).width;c.font=`700 34px ${F}`;const w2=c.measureText(word.toUpperCase()).width;const w=w1+w2+130,h=88;
  c.fillStyle=onDark?'#ffd257':INK;rr(c,x,y,w,h,h/2);c.fill();c.fillStyle=onDark?INK:'#fff';c.textBaseline='middle';c.font=`500 34px ${F}`;c.fillText(a,x+40,y+h/2+2);c.fillStyle=onDark?INK:'#ffd257';c.font=`700 34px ${F}`;c.fillText(word.toUpperCase(),x+40+w1,y+h/2+2);
  c.fillStyle=onDark?INK:'#fff';c.font=`500 38px ${F}`;c.fillText('→',x+w-70,y+h/2+1);c.textBaseline='alphabetic';return h}
function bigStat(t){if(!t.startsWith('*'))return null;const m=/^\*([+\-]?\d[\d.,]*)\s*(vezes|mil|%)?\*\s*(.*)$/i.exec(t);if(!m)return null;const suf=(m[2]||'').toLowerCase();const big=suf==='vezes'?m[1]+'x':suf==='mil'?m[1]+' mil':suf==='%'?m[1]+'%':m[1];return {big,rest:m[3]}}
window.drawSlide=async function(canvas,sl,i,n,info){
  window.CURINFO=info;canvas.width=W;canvas.height=H;const c=canvas.getContext('2d');c.fillStyle='#ffffff';c.fillRect(0,0,W,H);c.textBaseline='alphabetic';
  const last0=i===n-1,isCover0=i===0;const P=info.photos||[];
  if((isCover0||last0)&&info.mode==='full'&&fullOK(P[0])){drawFull(c,sl,i,n,P[0],last0,info.tags);return}
  header(c,i,n);if(i>0){const bk=brandsOf(sl,null);brandChip(c,bk,W-M,146,100)}const last=i===n-1,isCover=i===0;const bottom=H-150-(sl.src?34:0);
  let y=262;
  if(sl.l==='enquete'){
    if(sl.k){kicker(c,M,y,sl.k);y+=26}
    const f=fit(c,sl.t||'',{max:78,min:56,wt:500,maxW:W-2*M,maxLines:3});y=drawRich(c,f,M,y+16)+34;
    const opts=(sl.b||'').split('\n').filter(Boolean),oh=118,gap=22;
    opts.forEach((o,k)=>{const yy=y+k*(oh+gap);c.strokeStyle=LINE;c.lineWidth=3;rr(c,M,yy,W-2*M,oh,30);c.stroke();
      c.strokeStyle=GOLD;c.lineWidth=3;c.beginPath();c.arc(M+66,yy+oh/2,32,0,7);c.stroke();c.fillStyle=GOLDD;c.font=`700 34px ${F}`;c.textAlign='center';c.textBaseline='middle';c.fillText('ABCD'[k],M+66,yy+oh/2+2);c.textAlign='left';
      c.fillStyle=INK;c.font=`500 40px ${F}`;c.fillText(o,M+130,yy+oh/2+3);c.textBaseline='alphabetic'});
    c.fillStyle=GREY;c.font=`400 28px ${F}`;c.fillText('Comente a letra da sua resposta',M,y+opts.length*(oh+gap)+30);
    footer(c,i,n);return}
  if(sl.l==='chart'){
    if(sl.k){kicker(c,M,y,sl.k);y+=26}
    const f=fit(c,sl.t||'',{max:74,min:52,wt:600,maxW:W-2*M,maxLines:3});y=drawRich(c,f,M,y+16,1.24)+14;
    if(sl.b){c.fillStyle='#475569';c.font=`400 34px ${F}`;for(const ln of wrap(c,sl.b,`400 34px ${F}`,W-2*M).slice(0,2)){c.fillText(ln,M,y+34);y+=46}y+=6}
    const D=sl.data||[];const top=y+26,avail=bottom-top-6;const pitch=Math.min(215,avail/D.length);const mx=Math.max(...D.map(d=>d.v));const bw=W-2*M-260;
    D.forEach((d,k)=>{const yy=top+k*pitch;c.fillStyle='#475569';c.font=`500 34px ${F}`;c.fillText(d.l,M,yy+32);const bh=Math.min(92,pitch-66);const w=Math.max(bh,bw*d.v/mx);
      c.fillStyle=d.hl?GOLD:'#cfd8e3';rr(c,M,yy+48,w,bh,bh/2>22?22:bh/2);c.fill();c.fillStyle=INK;c.font=`700 54px ${F}`;c.textBaseline='middle';c.fillText(d.d||String(d.v),M+w+22,yy+48+bh/2+2);c.textBaseline='alphabetic'});
    if(sl.src){c.fillStyle=GREY;c.font=`400 22px ${F}`;c.fillText(sl.src,M,H-140)}
    footer(c,i,n);return}
  if(sl.l==='list'){
    if(sl.k){kicker(c,M,y,sl.k);y+=26}
    const f=fit(c,sl.t||'',{max:74,min:52,wt:600,maxW:W-2*M,maxLines:3});y=drawRich(c,f,M,y+16,1.24)+22;
    const IT=(sl.items||[]).map(x=>typeof x==='string'?{t:x}:x);const top=y+10,avail=bottom-top;const pitch=Math.min(150,avail/IT.length);
    c.font=`700 30px ${F}`;let bwid=80;IT.forEach((it,k)=>{if(!it.a)it.a=String(k+1);if(it.a.length>2)bwid=Math.max(bwid,c.measureText(it.a).width+44)});const tx=M+bwid+28;
    IT.forEach((it,k)=>{const yy=top+k*pitch,cy=yy+pitch/2-8;const isC=it.a.length<=2;
      c.strokeStyle=GOLD;c.lineWidth=3.5;c.fillStyle=isC?'#fff':'#fff8e0';
      if(isC){c.beginPath();c.arc(M+40,cy,38,0,7);c.stroke();c.fillStyle=GOLDD;c.font=`700 38px ${F}`;c.textAlign='center';c.textBaseline='middle';c.fillText(it.a,M+40,cy+2);c.textAlign='left';c.textBaseline='alphabetic'}
      else{const w=c.measureText(it.a).width+44;rr(c,M,cy-32,bwid,64,32);c.fill();c.stroke();c.fillStyle=GOLDD;c.font=`700 30px ${F}`;c.textAlign='center';c.textBaseline='middle';c.fillText(it.a,M+bwid/2,cy+2);c.textAlign='left';c.textBaseline='alphabetic'}
      const ff=fit(c,it.t,{max:40,min:30,wt:500,maxW:W-M-tx,maxLines:2});const hh=ff.L.length*ff.s*1.28;drawRich(c,ff,tx,cy-hh/2+2,1.28)});
    if(sl.src){c.fillStyle=GREY;c.font=`400 22px ${F}`;c.fillText(sl.src,M,H-140)}
    footer(c,i,n);return}
  if(isCover){
    const y0tag=250;const im0=IMGS[P[0]];const port=false;const PWc=450;const TWc=port?(W-2*M-PWc-44):(W-2*M);y=262;
    if(sl.k){kicker(c,M,y,sl.k);y+=26}
    const f=fit(c,sl.t||'',{max:port?76:88,min:54,wt:500,maxW:TWc,maxLines:port?6:3});y=drawRich(c,f,M,y+18,1.26)+16;
    if(sl.b){c.fillStyle=GREY;c.font=`400 34px ${F}`;for(const ln of wrap(c,sl.b,`400 34px ${F}`,TWc).slice(0,port?5:2)){c.fillText(ln,M,y+34);y+=48}y+=6}
    if(port){const bx=containBox(im0,PWc,Math.min(bottom-262,860));const px0=W-M-bx.w;c.save();rr(c,px0,262,bx.w,bx.h,30);c.clip();c.drawImage(im0,px0,262,bx.w,bx.h);c.restore()}
    else{const top=y+24,ph=Math.max(360,bottom-top);photoIn(c,[P[0]],M,bottom-ph,W-2*M,ph)}
    {const bk=brandsOf(sl,info);const lx=brandChip(c,bk,W-M,188,112);tagPills(c,(info.tags||[]).filter(t=>t==='live'||(!bk.length)),lx-(bk.length?14:0),216,false)}
    footer(c,i,n);return}
  const isBS=!!bigStat(sl.t||'');let side=!!(P[0]!=null&&!last&&i%2===1&&!isBS&&!sl.cta&&IMGS[P[0]]&&IMGS[P[0]].height/IMGS[P[0]].width>=1&&((sl.t||'').length+(sl.b||'').length<=115));const PW=430;let TW=side?(W-2*M-PW-44):(W-2*M);
  const body=(c,dy)=>{c.save();c.translate(0,dy);let y=250;
  const bs=bigStat(sl.t||'');
  if(sl.k){kicker(c,M,y,sl.k);y+=26}
  if(bs){c.font=`700 230px ${F}`;let s=230;while(c.measureText(bs.big).width>TW&&s>120){s-=10;c.font=`700 ${s}px ${F}`}
    c.fillStyle=MARK;rr(c,M-6,y+s*.62,c.measureText(bs.big).width+12,s*.26,10);c.fill();c.fillStyle=INK;c.fillText(bs.big,M,y+s*.98);y+=s*1.1;
    const f=fit(c,bs.rest,{max:66,min:48,wt:600,maxW:TW,maxLines:2});y=drawRich(c,f,M,y,1.22)+20}
  else{const f=fit(c,sl.t||'',{max:last?88:92,min:54,wt:last?500:600,maxW:TW,maxLines:side?5:4});y=drawRich(c,f,M,y+16,1.24)+22}
  if(sl.b){c.fillStyle=GREY;const bf=`400 46px ${F}`;for(const ln of wrap(c,sl.b,bf,TW)){c.font=bf;c.fillStyle='#475569';c.fillText(ln,M,y+46);y+=68}y+=10}
  if(sl.cta){y+=16;y+=ctaBtn(c,M,y,sl.cta)+20}
  if(sl.follow){y+=18;y+=engageRow(c,M,y,false)+20}
  c.restore();return y};
  const sc=document.createElement('canvas');sc.width=W;sc.height=H;let yEnd=body(sc.getContext('2d'),0);if(side&&yEnd>bottom-40){side=false;TW=W-2*M;yEnd=body(sc.getContext('2d'),0)}
  const room0=bottom-(yEnd+30);const showPhoto=(!side&&P[0]!=null&&(last||i%2===1)&&room0>=340);
  const sideBx=side?containBox(IMGS[P[0]],PW,Math.min(bottom-250,780)):null;const dy=side?Math.max(0,Math.min(220,(bottom-250-Math.max(yEnd-250,sideBx.h))*.5)):(showPhoto?0:Math.max(0,Math.min(150,(bottom-yEnd-200)*.45)));const yF=body(c,dy)+dy;
  // foto embaixo se couber
  const room=bottom-(yF+30);
  if(showPhoto){const ph=Math.min(room,600);photoIn(c,[P[0]],M,bottom-ph,W-2*M,ph)}
  if(side){const bx=sideBx;const px0=W-M-bx.w;c.save();rr(c,px0,250+dy,bx.w,bx.h,30);c.clip();c.drawImage(IMGS[P[0]],px0,250+dy,bx.w,bx.h);c.restore()}
  if(sl.src){c.fillStyle=GREY;c.font=`400 22px ${F}`;c.fillText(sl.src,M,H-140)}
  footer(c,i,n)}
