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

// ===== modo foto (style:'foto'): foto do Diego em TODOS os slides, sem cortar as horizontais =====
function drawFotoLand(c,sl,i,n,k,last,tags){
  const im=IMGS[k];c.save();c.filter='blur(36px)';cover(c,im,-60,-60,W+120,H+120,50,30,1);c.restore();c.fillStyle='#0f172ab8';c.fillRect(0,0,W,H);
  header(c,i,n,true);if(i===0){const bk=brandsOf(sl,window.CURINFO);brandChip(c,bk,W-M,188,112)}
  const bx=containBox(im,W-2*M,560);const px=M+(W-2*M-bx.w)/2,py=236;c.save();rr(c,px,py,bx.w,bx.h,30);c.clip();c.drawImage(im,px,py,bx.w,bx.h);c.restore();
  const maxW=W-2*M;const f=fit(c,sl.t||'',{max:last?70:76,min:50,wt:600,maxW,maxLines:3});
  const bl=sl.b?wrap(c,sl.b,`400 34px ${F}`,maxW).slice(0,2):[];
  const th=f.L.length*f.s*1.24,bh=bl.length*48,ch=sl.follow?96:0;const total=(sl.k?44:0)+th+(bl.length?bh+16:0)+ch;
  let y=Math.max(py+bx.h+30,H-130-total);if(sl.k){c.fillStyle='#ffd257';c.font=`600 25px ${F}`;c.letterSpacing='4px';c.fillText(sl.k.toUpperCase(),M,y+26);c.letterSpacing='0px';y+=44}
  y=drawRich(c,f,M,y,1.24,'#ffffff')+8;
  if(bl.length){c.fillStyle='#ffffffdd';c.font=`400 34px ${F}`;for(const ln of bl){c.fillText(ln,M,y+32);y+=48}y+=10}
  if(sl.follow){y+=14;engageRow(c,M,y,true)}
  footer(c,i,n,true)}
window.drawSlide=async function(canvas,sl,i,n,info){
  window.CURINFO=info;canvas.width=W;canvas.height=H;const c=canvas.getContext('2d');c.fillStyle='#ffffff';c.fillRect(0,0,W,H);c.textBaseline='alphabetic';
  const last0=i===n-1,isCover0=i===0;const P=info.photos||[];
  if(info.mode==='foto'){if(fullOK(P[0]))drawFull(c,sl,i,n,P[0],last0,info.tags);else drawFotoLand(c,sl,i,n,P[0],last0,info.tags);return}
  if((isCover0||last0)&&info.mode==='full'&&fullOK(P[0])){drawFull(c,sl,i,n,P[0],last0,info.tags);return}
  if(info.mode==='cri'&&isCover0){drawCriCover(c,sl,i,n,info);return}
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
  if(showPhoto){const ph=Math.min(room,600);if(info.mode==='cri')illoCard(c,sl.ic||'bag',M,bottom-ph,W-2*M,ph);else photoIn(c,[P[0]],M,bottom-ph,W-2*M,ph)}
  if(side){const bx=sideBx;const px0=W-M-bx.w;c.save();rr(c,px0,250+dy,bx.w,bx.h,30);c.clip();c.drawImage(IMGS[P[0]],px0,250+dy,bx.w,bx.h);c.restore()}
  if(sl.src){c.fillStyle=GREY;c.font=`400 22px ${F}`;c.fillText(sl.src,M,H-140)}
  footer(c,i,n)}

// ===== modo criativo (style:'cri'): sem fotos no começo/meio, ilustrações vetoriais; foto só no último slide =====
const CORAL='#f97316',PINK='#db2777';
function heart(c,x,y,s,col){c.save();c.translate(x,y);c.scale(s,s);c.fillStyle=col;c.beginPath();c.moveTo(0,14);c.bezierCurveTo(-26,-4,-14,-22,0,-9);c.bezierCurveTo(14,-22,26,-4,0,14);c.fill();c.restore()}
function sparkle(c,x,y,r,col){c.save();c.fillStyle=col;c.translate(x,y);c.beginPath();for(let k=0;k<8;k++){const a=k*Math.PI/4,q=k%2?r*.28:r;c.lineTo(Math.cos(a-Math.PI/2)*q,Math.sin(a-Math.PI/2)*q)}c.closePath();c.fill();c.restore()}
function ill(c,kind,cx,cy,s,dark){const k=s/400;c.save();c.translate(cx,cy);c.scale(k,k);c.lineJoin='round';c.lineCap='round';
  const body=dark?'#f8fafc':INK,line=dark?'#f8fafc':INK;
  const D={
  live(){rr(c,-110,-190,220,380,36);c.fillStyle=body;c.fill();const g=c.createLinearGradient(-100,-180,100,180);g.addColorStop(0,'#fbbf24');g.addColorStop(.55,CORAL);g.addColorStop(1,PINK);rr(c,-96,-176,192,352,26);c.fillStyle=g;c.fill();
    rr(c,-80,-156,92,32,16);c.fillStyle='#ef4444';c.fill();c.fillStyle='#fff';c.beginPath();c.arc(-62,-140,6,0,7);c.fill();c.font=`700 15px ${F}`;c.textBaseline='middle';c.fillText('AO VIVO',-50,-139);c.textBaseline='alphabetic';
    rr(c,-80,56,160,102,20);c.fillStyle='#fff';c.fill();rr(c,-68,68,64,64,14);c.fillStyle=GOLD;c.fill();c.fillStyle='#cbd5e1';rr(c,2,74,62,10,5);c.fill();rr(c,2,94,44,10,5);c.fill();rr(c,2,116,62,18,9);c.fillStyle=INK;c.fill();
    heart(c,150,-70,1.5,PINK);heart(c,128,-10,1,'#fb7185');heart(c,172,30,1.1,'#fbbf24');
    rr(c,-210,20,110,64,28);c.fillStyle='#fff';c.fill();c.fillStyle=INK;for(let j=0;j<3;j++){c.beginPath();c.arc(-182+j*28,52,6,0,7);c.fill()}
    sparkle(c,-150,-120,22,GOLD);},
  bag(){c.strokeStyle=line;c.lineWidth=20;c.beginPath();c.arc(0,-50,62,Math.PI,0);c.stroke();rr(c,-130,-50,260,240,30);c.fillStyle=GOLD;c.fill();c.lineWidth=12;c.strokeStyle=INK;c.stroke();
    c.fillStyle=INK;c.beginPath();c.arc(-44,18,10,0,7);c.fill();c.beginPath();c.arc(44,18,10,0,7);c.fill();c.lineWidth=12;c.beginPath();c.arc(0,42,40,.15*Math.PI,.85*Math.PI);c.stroke();
    sparkle(c,160,-110,28,CORAL);sparkle(c,-170,-90,18,dark?'#fff':GOLD);sparkle(c,150,120,14,PINK)},
  chat(){rr(c,-190,-150,250,130,44);c.fillStyle=dark?'#f8fafc':INK;c.fill();c.beginPath();c.moveTo(-150,-30);c.lineTo(-160,20);c.lineTo(-100,-22);c.closePath();c.fill();c.fillStyle=dark?INK:'#fff';for(let j=0;j<3;j++){c.beginPath();c.arc(-100+j*38,-85,11,0,7);c.fill()}
    rr(c,-60,20,250,130,44);c.fillStyle=GOLD;c.fill();c.beginPath();c.moveTo(150,140);c.lineTo(165,190);c.lineTo(100,148);c.closePath();c.fill();c.fillStyle=INK;rr(c,-24,60,170,14,7);c.fill();rr(c,-24,92,120,14,7);c.fill();heart(c,170,-90,1.6,PINK);sparkle(c,-150,110,20,CORAL)},
  bars(){c.fillStyle='#fde9a6';rr(c,-150,50,76,110,16);c.fill();c.fillStyle=GOLD;rr(c,-38,-20,76,180,16);c.fill();c.fillStyle=CORAL;rr(c,74,-110,76,270,16);c.fill();
    c.strokeStyle=line;c.lineWidth=16;c.beginPath();c.moveTo(-160,-10);c.lineTo(-50,-70);c.lineTo(10,-40);c.lineTo(150,-170);c.stroke();c.beginPath();c.moveTo(105,-172);c.lineTo(152,-172);c.lineTo(152,-125);c.stroke();c.lineWidth=10;c.beginPath();c.moveTo(-170,176);c.lineTo(170,176);c.stroke();sparkle(c,-130,-130,22,GOLD)},
  bulb(){c.fillStyle=GOLD;c.beginPath();c.arc(0,-40,100,0,7);c.fill();rr(c,-44,40,88,22,10);c.fillStyle=body;c.fill();rr(c,-34,68,68,20,10);c.fill();rr(c,-22,92,44,16,8);c.fill();c.strokeStyle=line;c.lineWidth=14;for(let a=-60;a<=240;a+=45){if(a>10&&a<170)continue;const r=Math.PI*a/180;c.beginPath();c.moveTo(Math.cos(r)*135,-40+Math.sin(r)*135);c.lineTo(Math.cos(r)*170,-40+Math.sin(r)*170);c.stroke()}},
  play(){const g=c.createLinearGradient(-140,-140,140,140);g.addColorStop(0,'#fbbf24');g.addColorStop(.55,CORAL);g.addColorStop(1,PINK);c.fillStyle=g;c.beginPath();c.arc(0,0,150,0,7);c.fill();c.fillStyle='#fff';c.beginPath();c.moveTo(-40,-70);c.lineTo(-40,70);c.lineTo(72,0);c.closePath();c.fill();c.strokeStyle=dark?'#ffffff55':'#0f172a22';c.lineWidth=10;c.beginPath();c.arc(0,0,185,0,7);c.stroke();heart(c,140,-150,1.3,PINK);sparkle(c,-160,130,22,GOLD)},
  check(){rr(c,-120,-150,240,320,28);c.fillStyle='#fff';c.fill();c.strokeStyle=INK;c.lineWidth=12;c.stroke();rr(c,-52,-176,104,50,16);c.fillStyle=INK;c.fill();
    for(let j=0;j<3;j++){const y=-70+j*76;c.beginPath();c.arc(-62,y,22,0,7);c.fillStyle=GOLD;c.fill();c.strokeStyle='#fff';c.lineWidth=8;c.beginPath();c.moveTo(-72,y);c.lineTo(-64,y+8);c.lineTo(-50,y-8);c.stroke();c.fillStyle='#cbd5e1';rr(c,-24,y-8,90,16,8);c.fill()}},
  box(){c.fillStyle='#fcd34d';rr(c,-130,-60,260,220,20);c.fill();c.fillStyle='#f59e0b';rr(c,-26,-60,52,220,6);c.fill();c.fillStyle='#fbbf24';rr(c,-145,-120,290,70,16);c.fill();c.fillStyle='#f59e0b';rr(c,-26,-120,52,70,6);c.fill();c.strokeStyle=INK;c.lineWidth=12;rr(c,-130,-60,260,220,20);c.stroke();rr(c,-145,-120,290,70,16);c.stroke();
    sparkle(c,150,-150,26,CORAL);sparkle(c,-160,-140,18,GOLD)},
  target(){const rs=[160,110,60],cl=['#fff',CORAL,'#fff'];rs.forEach((r,j)=>{c.fillStyle=cl[j];c.beginPath();c.arc(0,10,r,0,7);c.fill();c.strokeStyle=INK;c.lineWidth=12;c.stroke()});c.fillStyle=INK;c.beginPath();c.arc(0,10,18,0,7);c.fill();
    c.strokeStyle=line;c.lineWidth=14;c.beginPath();c.moveTo(150,-140);c.lineTo(8,2);c.stroke();c.beginPath();c.moveTo(150,-140);c.lineTo(100,-150);c.moveTo(150,-140);c.lineTo(160,-92);c.stroke();sparkle(c,-170,-130,20,GOLD)},
  cap(){c.fillStyle=body;c.beginPath();c.moveTo(0,-120);c.lineTo(190,-40);c.lineTo(0,40);c.lineTo(-190,-40);c.closePath();c.fill();c.fillStyle=GOLD;c.beginPath();c.moveTo(-110,10);c.lineTo(-110,90);c.quadraticCurveTo(0,160,110,90);c.lineTo(110,10);c.lineTo(0,56);c.closePath();c.fill();c.strokeStyle=GOLD;c.lineWidth=12;c.beginPath();c.moveTo(170,-30);c.lineTo(170,90);c.stroke();c.fillStyle=CORAL;c.beginPath();c.arc(170,100,18,0,7);c.fill();sparkle(c,-150,-140,24,GOLD);sparkle(c,150,-130,16,CORAL);heart(c,-170,100,1.2,PINK)}
  };(D[kind]||D.bag)();c.restore()}
function illoCard(c,kind,x,y,w,h){c.fillStyle='#f5f2ea';rr(c,x,y,w,h,36);c.fill();ill(c,kind,x+w/2,y+h/2,Math.min(h*.86,w*.62),false)}
function drawCriCover(c,sl,i,n,info){let g=c.createLinearGradient(0,0,W,H);g.addColorStop(0,'#0b1220');g.addColorStop(1,'#1e293b');c.fillStyle=g;c.fillRect(0,0,W,H);
  const rg=c.createRadialGradient(W*.7,H*.74,20,W*.7,H*.74,640);rg.addColorStop(0,'#d9a21b70');rg.addColorStop(1,'#d9a21b00');c.fillStyle=rg;c.fillRect(0,0,W,H);
  header(c,i,n,true);const bk=brandsOf(sl,info);if(bk.length)brandChip(c,bk,W-M,188,112);let y=bk.length?330:262;
  if(sl.k){c.fillStyle='#ffd257';c.font=`600 25px ${F}`;c.letterSpacing='4px';c.fillText(sl.k.toUpperCase(),M,y);c.letterSpacing='0px';y+=26}
  const f=fit(c,sl.t||'',{max:92,min:58,wt:600,maxW:W-2*M,maxLines:4});y=drawRich(c,f,M,y+18,1.22,'#ffffff')+14;
  if(sl.b){c.fillStyle='#ffffffcc';c.font=`400 36px ${F}`;for(const ln of wrap(c,sl.b,`400 36px ${F}`,W-2*M).slice(0,2)){c.fillText(ln,M,y+36);y+=50}}
  const top=y+30,bot=H-120,ph=bot-top;ill(c,sl.ic||'live',W/2+40,top+ph/2,Math.min(ph*1.05,660),true);footer(c,i,n,true)}
