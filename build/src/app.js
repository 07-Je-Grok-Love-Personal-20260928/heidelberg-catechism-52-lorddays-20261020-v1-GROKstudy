/* v7 · app.js — passive listeners, IntersectionObserver, NO DOM writes while scrolling, idle-time init */
(function(){
const ROOT=(document.currentScript&&document.currentScript.dataset.root)||'';
const idle=f=>('requestIdleCallback' in window)?requestIdleCallback(()=>f(),{timeout:700}):setTimeout(f,60);
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const LS={get:(k,d)=>{try{const v=JSON.parse(localStorage.getItem(k));return v===null||v===undefined?d:v}catch(e){return d}},set:(k,v)=>{try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}};
const root=document.documentElement;
function toast(t){let e=$('.toast');if(!e){e=document.createElement('div');e.className='toast';document.body.appendChild(e)}e.textContent=t;requestAnimationFrame(()=>e.classList.add('on'));clearTimeout(e._t);e._t=setTimeout(()=>e.classList.remove('on'),1800)}
window.hcToast=toast;
const ready=f=>document.readyState==='loading'?document.addEventListener('DOMContentLoaded',f):f();
ready(()=>{
 const b=document.body;const mobile=()=>innerWidth<=1024;
 if(new URLSearchParams(location.search).has('cv0'))b.classList.add('cv-off');
 /* ---------- v6: theme picker (5 themes, persisted, applied pre-paint by the head script) ---------- */
 const TN={night:'🌌 深夜星空',dawn:'🌅 晨曦米白',forest:'🌲 翡翠森林',grape:'🍇 葡萄紫金',ocean:'🌊 海洋蓝',sakura:'🌸 樱花粉霞',citrus:'🍋 柠檬薄荷',ember:'🔥 暮光琥珀',aurora:'🌠 极光青紫',sumi:'🖋️ 水墨朱砂'};
 const syncTheme=()=>$$('[data-theme-set]').forEach(x=>x.setAttribute('aria-checked',x.dataset.themeSet===root.dataset.theme?'true':'false'));
 const setTheme=t=>{if(!TN[t])return;if(document.startViewTransition&&!matchMedia('(prefers-reduced-motion: reduce)').matches&&!setTheme._vt){setTheme._vt=1;try{document.startViewTransition(()=>setTheme(t)).finished.finally(()=>{setTheme._vt=0})}catch(e){setTheme._vt=0;setTheme(t)}return}root.dataset.theme=t;LS.set('hc-theme',t);syncTheme();const mc=$('meta[name=theme-color]');if(mc)mc.content=getComputedStyle(root).getPropertyValue('--bg').trim();document.dispatchEvent(new CustomEvent('hctheme',{detail:t}));toast('🎨 '+TN[t])};
 window.hcSetTheme=setTheme;syncTheme();
 const thp=$('#thp'),thb=$('#themeBtn');
 thb?.addEventListener('click',e=>{e.stopPropagation();const o=thp.classList.toggle('open');thb.setAttribute('aria-expanded',o)});
 document.addEventListener('click',e=>{const t=e.target.closest('[data-theme-set]');if(t){setTheme(t.dataset.themeSet);if(t.closest('#thp')){thp.classList.remove('open');thb.setAttribute('aria-expanded','false')}return}if(thp&&!e.target.closest('#thp'))thp.classList.remove('open')});
 addEventListener('keydown',e=>{if(e.key==='Escape'&&thp?.classList.contains('open')){thp.classList.remove('open');thb.focus()}});
 /* ---------- v7: one scroll-state helper. During a scroll the ONLY work is a flag + timer; everything else waits for scrollend ---------- */
 const SMIL=[...document.querySelectorAll('svg')].filter(s=>s.querySelector('animateMotion,animate,animateTransform')); const sky=$('.sky');const SC={on:false,t:0,q:[]};const HAS_END='onscrollend' in window;
 const scEnd=()=>{clearTimeout(SC.t);SC.t=0;if(!SC.on)return;SC.on=false;root.classList.remove('scr');const nvc=document.getElementById('navc');if(nvc)nvc.classList.remove('dim');if(sky&&!document.hidden)sky.classList.remove('paused');SMIL.forEach(s=>{try{s.unpauseAnimations()}catch(_){}});const q=SC.q;SC.q=[];q.forEach(f=>f());if(typeof schedPL==='function')setTimeout(schedPL,600)};
 const shield=document.createElement('div');shield.id='scrshield';shield.setAttribute('aria-hidden','true');document.body.appendChild(shield);
 const unshield=()=>root.classList.remove('scr');let px=-1,py=-1;shield.addEventListener('pointermove',e=>{if(px<0){px=e.clientX;py=e.clientY;return}if(Math.abs(e.clientX-px)+Math.abs(e.clientY-py)>4)unshield()},{passive:true});let fw=null;shield.addEventListener('pointerdown',e=>{unshield();fw={x:e.clientX,y:e.clientY,t:performance.now()}},{passive:true});document.addEventListener('click',e=>{const f=fw;fw=null;if(!f||performance.now()-f.t>1500||(e.target!==document.body&&e.target!==root))return;const el=document.elementFromPoint(f.x,f.y);if(el&&el!==document.body&&el!==shield){e.stopPropagation();el.click()}},true);
 const arm=d=>{clearTimeout(SC.t);SC.t=setTimeout(()=>{const q=performance.now()-SC.last;if(q<380)arm(400-q);else scEnd()},d)};
 const onAct=()=>{SC.last=performance.now();if(!SC.on){SC.on=true;px=-1;root.classList.add('scr');document.querySelectorAll('svg.cmap.go:not(.done)').forEach(s=>{s.classList.add('done');try{s.setCurrentTime(60)}catch(_){}});SMIL.forEach(s=>{try{s.pauseAnimations()}catch(_){}});if(sky)sky.classList.add('paused')}arm(HAS_END?700:420)};addEventListener('scroll',onAct,{passive:true});addEventListener('wheel',onAct,{passive:true});addEventListener('touchmove',onAct,{passive:true});
 if(HAS_END)addEventListener('scrollend',()=>arm(160),{passive:true});
 const afterScroll=f=>{if(SC.on){if(!SC.q.includes(f))SC.q.push(f)}else f()};
 /* v9: idle pre-layout — render content-visibility sections one at a time while the reader is NOT scrolling, nearest-below first,
    so a scroll never has to lay out a fresh section mid-gesture (the main source of 40–90 ms frames at 6× CPU) */
 let PL=0;const preLay=()=>{PL=0;const vh=innerHeight;let best=null,bd=1e9;
  for(const s of document.querySelectorAll('main section.sec:not(.ncv)')){
   const r=s.getBoundingClientRect();const d=r.top>=0?r.top:vh*3-r.bottom;if(d<bd){bd=d;best=s}}
  if(!best)return;best.classList.add('ncv');schedPL()};
 const schedPL=()=>{if(PL)return;PL=1;const next=()=>afterScroll(()=>idle(preLay));if('requestIdleCallback' in window)requestIdleCallback(next,{timeout:2000});else setTimeout(next,120)};
addEventListener('load',()=>setTimeout(schedPL,900),{once:true});
 document.addEventListener('visibilitychange',()=>{if(sky)sky.classList.toggle('paused',document.hidden||SC.on)});
 /* ---------- marks toggle ---------- */
 const MKS=['all','core','off'],MKT={all:'🖍️ 标记：全部',core:'⭐ 标记：仅核心（荧光核心词 + 经文）',off:'🧽 标记：关（纯净阅读）'};
 const getMk=()=>root.classList.contains('mkoff')?'off':root.classList.contains('mkcore')?'core':'all';
 const syncMk=m=>{$$('[data-mk-set]').forEach(x=>x.setAttribute('aria-checked',x.dataset.mkSet===m?'true':'false'));$$('[data-marks]').forEach(x=>{x.dataset.mk=m;x.title=MKT[m]+' · M 切换'})};
 const setMarks=(m,say)=>{root.classList.toggle('mkcore',m==='core');root.classList.toggle('mkoff',m==='off');LS.set('hc-marks',m);syncMk(m);if(say)toast(MKT[m])};
 syncMk(getMk());
 document.addEventListener('click',e=>{const s=e.target.closest('[data-mk-set]');if(s){setMarks(s.dataset.mkSet,1);return}if(!e.target.closest('[data-marks]'))return;setMarks(MKS[(MKS.indexOf(getMk())+1)%3],1)});
 /* ---------- anchor jumps that survive content-visibility size estimates ---------- */
 const jump=(el,push)=>{if(!el)return;const far=Math.abs(el.getBoundingClientRect().top)>innerHeight*1.5;el.scrollIntoView({block:'start',behavior:far?'instant':'smooth'});
  if(push)history.pushState(null,'','#'+el.id);let k=0,stable=0;const want=()=>parseFloat(getComputedStyle(el).scrollMarginTop)||0;
  const fix=()=>{const d=el.getBoundingClientRect().top-want();if(Math.abs(d)>3){stable=0;el.scrollIntoView({block:'start',behavior:'instant'})}else stable++;if(stable<2&&k++<12)setTimeout(()=>requestAnimationFrame(fix),far?60:260)};
  setTimeout(()=>requestAnimationFrame(fix),far?30:420)};
 window.hcJump=id=>jump(document.getElementById(id),true);
 document.addEventListener('click',e=>{const a=e.target.closest('a[href^="#"]');if(!a||e.defaultPrevented||e.button||e.metaKey||e.ctrlKey)return;const id=decodeURIComponent(a.getAttribute('href').slice(1));const el=id&&document.getElementById(id);if(!el)return;e.preventDefault();jump(el,true)});
 if(location.hash){const el=document.getElementById(decodeURIComponent(location.hash.slice(1)));if(el)addEventListener('load',()=>jump(el,false),{once:true})}
 /* ---------- hierarchical TOC ---------- */
 const toc=$('#toc');const heads=$$('main [data-lv]');const items=[];
 if(toc&&heads.length){
  const pre=toc.firstElementChild; /* v7: TOC is rendered at build time; JS only hydrates it */
  if(pre){$$('li',toc).forEach(li=>{const a=li.querySelector(':scope>.row>a');const h=document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)));if(h)items.push({h,a,li})})}else{
  const rootUl=document.createElement('ul');const stack=[{lv:0,ul:rootUl,li:null}];
  heads.forEach(h=>{
   const lv=+h.dataset.lv;while(stack.length>1&&stack[stack.length-1].lv>=lv)stack.pop();
   let parent=stack[stack.length-1];
   if(!parent.ul){parent.ul=document.createElement('ul');parent.li.appendChild(parent.ul);const t=document.createElement('button');t.className='tw';t.type='button';t.textContent='▾';t.setAttribute('aria-label','展开/折叠');parent.li.firstChild.prepend(t)}
   const li=document.createElement('li');li.className='l'+lv;
   const row=document.createElement('div');row.className='row';
   const a=document.createElement('a');a.href='#'+h.id;
   let label=h.dataset.toc;if(!label){const c=h.cloneNode(true);const ic=c.querySelector('.ico');const it=ic?ic.textContent.trim()+' ':'';c.querySelectorAll('.ico,.hn,.tools,small,.small,a').forEach(x=>x.remove());label=it+c.textContent.replace(/\s+/g,' ').trim()}
   const no=h.dataset.no&&!h.closest('.qa')?h.dataset.no:'';
   if(no){const s=document.createElement('span');s.className='no';s.textContent=no;a.appendChild(s)}
   a.appendChild(document.createTextNode(label));a.title=(no?no+' ':'')+label;
   row.append(a);li.appendChild(row);parent.ul.appendChild(li);
   stack.push({lv,ul:null,li});items.push({h,a,li});
  });
  toc.appendChild(rootUl);
  // default: L1 open, deeper collapsed (except short lists)
  $$('li',toc).forEach(li=>{if(li.querySelector(':scope>ul')&&!li.classList.contains('l1'))li.classList.add('closed')});
  if(items.length<=14)$$('li',toc).forEach(li=>li.classList.remove('closed'));
  }
  toc.addEventListener('click',e=>{const tw=e.target.closest('.tw');if(tw){tw.parentElement.parentElement.classList.toggle('closed');return}if(e.target.closest('a')&&mobile())b.classList.remove('toc-open')});
  $('#tocExpand')?.addEventListener('click',()=>$$('li',toc).forEach(li=>li.classList.remove('closed')));
  $('#tocCollapse')?.addEventListener('click',()=>{$$('li',toc).forEach(li=>{if(li.querySelector(':scope>ul'))li.classList.add('closed')});window.hcOpenCur&&hcOpenCur()});
  $('#tocSearch')?.addEventListener('input',e=>{const q=e.target.value.trim();
   $$('li',toc).forEach(li=>{li.style.display=''});
   if(q){$$('li',toc).forEach(li=>{const hit=li.textContent.includes(q);li.style.display=hit?'':'none';if(hit)li.classList.remove('closed')})}
   $$('#gnav a').forEach(a=>a.style.display=!q||a.textContent.includes(q)?'':'none')});
  /* scrollspy via IntersectionObserver (no scroll handler, no layout reads) */
  const vis=new Map();let curIt=null,raf=0,parSet=new Set();
  const pathOf=it=>{const p=new Set();let li=it.li.parentElement.closest('li');while(li){p.add(li);li=li.parentElement.closest('li')}return p};
  const lnk=li=>li.querySelector(':scope>.row>a');
  const openPath=it=>{const p=pathOf(it);parSet.forEach(l=>{if(!p.has(l))lnk(l).classList.remove('par')});p.forEach(l=>{if(l.classList.contains('closed'))l.classList.remove('closed');const x=lnk(l);if(!x.classList.contains('par'))x.classList.add('par')});parSet=p};
  window.hcOpenCur=()=>{if(curIt)openPath(curIt)};
  const apply=()=>{raf=0;let best=null;for(const it of items){if(vis.has(it.h))best=it}if(!best)best=items[0];
   if(!best||best===curIt)return;curIt?.a.classList.remove('on');
   curIt=best;best.a.classList.add('on');openPath(best);
   if(!b.classList.contains('resizing')&&!(mobile()&&!b.classList.contains('toc-open'))){const sc=$('.side .scroll');const ar=best.a.getBoundingClientRect(),sr=sc.getBoundingClientRect();if(ar.top<sr.top+60||ar.bottom>sr.bottom-30)sc.scrollTo({top:sc.scrollTop+ar.top-sr.top-sr.height/3,behavior:'smooth'})}};
  const sched=()=>{if(raf)return;raf=1;afterScroll(()=>requestAnimationFrame(apply))};
  const spy=new IntersectionObserver(es=>{es.forEach(e=>{const r=e.boundingClientRect;if(e.isIntersecting||(r.height>0&&r.bottom<(e.rootBounds?e.rootBounds.top:0)+1))vis.set(e.target,1);else if(r.height>0)vis.delete(e.target)});
   // headings above viewport keep their (negative) top so the last one passed wins
   sched()},{rootMargin:'-'+(parseInt(getComputedStyle(root).getPropertyValue('--top'))||58)+'px 0px -70% 0px',threshold:0});
  items.forEach(it=>spy.observe(it.h));
 }
 /* ---------- sidebar toggle + resizer ---------- */
 const tocBtn=$('#tocBtn'),side=$('#side'),rz=$('#resizer');
 if(LS.get('hc-toc-hidden',false)&&!mobile())b.classList.add('toc-hidden');
 tocBtn?.addEventListener('click',()=>{if(mobile())b.classList.toggle('toc-open');else{b.classList.toggle('toc-hidden');LS.set('hc-toc-hidden',b.classList.contains('toc-hidden'))}});
 $('.backdrop')?.addEventListener('click',()=>b.classList.remove('toc-open'));
 $$('#gnav a').forEach(a=>a.addEventListener('click',()=>{if(mobile())b.classList.remove('toc-open')}));
 const MIN=220,maxW=()=>Math.min(640,Math.round(innerWidth*(mobile()?.92:.7))),DEF=300;
 const setW=w=>{w=Math.max(MIN,Math.min(maxW(),Math.round(w)));root.style.setProperty('--side',w+'px');return w};
 if(rz&&side){let sx=0,sw=0,pend=null,fr=0,cur=0;
  rz.addEventListener('pointerdown',e=>{e.preventDefault();rz.setPointerCapture(e.pointerId);sx=e.clientX;sw=side.getBoundingClientRect().width;b.classList.add('resizing')});
  rz.addEventListener('pointermove',e=>{if(!b.classList.contains('resizing'))return;pend=sw+e.clientX-sx;if(!fr)fr=requestAnimationFrame(()=>{fr=0;cur=setW(pend)})});
  const end=e=>{if(!b.classList.contains('resizing'))return;b.classList.remove('resizing');if(cur){LS.set('hc-side-w',cur)}};
  rz.addEventListener('pointerup',end);rz.addEventListener('pointercancel',end);rz.addEventListener('lostpointercapture',end);
  rz.addEventListener('dblclick',()=>{setW(DEF);LS.set('hc-side-w',DEF);toast('↔ 目录宽度已恢复默认')});
  rz.addEventListener('keydown',e=>{if(e.key==='ArrowLeft'||e.key==='ArrowRight'){e.preventDefault();const w=setW(side.getBoundingClientRect().width+(e.key==='ArrowRight'?24:-24));LS.set('hc-side-w',w)}});
  addEventListener('resize',()=>{const w=LS.get('hc-side-w',0);if(w)setW(w)},{passive:true});
 }
 /* ---------- progress bar fallback (no CSS scroll-timeline) ---------- */
 const pr=$('.progress');
 if(pr&&!(window.CSS&&CSS.supports('animation-timeline: scroll()'))){let t=0;addEventListener('scroll',()=>{if(t)return;t=requestAnimationFrame(()=>{t=0;const h=root;pr.style.transform='scaleX('+(h.scrollTop/((h.scrollHeight-h.clientHeight)||1))+')'})},{passive:true})}
 /* ---------- reveal ---------- */
 const rv=$$('.reveal, section.sec');
 const seen=e=>e.classList.add(e.matches('section.sec')?'seen':'in');
 const ANIM='.bar-grow,.barx,.draw,.seg,.dot,.ladder,.parr,.vc,.arc,.cch';const lazyA=e=>e.matches(ANIM)||!!e.querySelector(ANIM);
 if(root.classList.contains('lite')||!('IntersectionObserver' in window))rv.forEach(seen);
 else{const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){const t=e.target;io.unobserve(t);afterScroll(()=>requestAnimationFrame(()=>seen(t)))}}),{rootMargin:'0px 0px -6% 0px'});rv.forEach(e=>lazyA(e)?io.observe(e):seen(e))}
 const clean=box=>{const c=box.cloneNode(true);c.querySelectorAll('sup,details,.tools,button').forEach(x=>x.remove());return c.textContent.replace(/\s+\n/g,'\n').trim()};
 idle(()=>{
 /* ---------- tabs ---------- */
 $$('.tabs').forEach(t=>{const bs=$$('button',t),ps=$$(':scope>.tabp',t.parentElement);bs.forEach((x,i)=>x.addEventListener('click',()=>{bs.forEach((y,j)=>y.classList.toggle('on',i===j));ps.forEach((p,j)=>p.classList.toggle('on',i===j))}))});
 /* ---------- recite / footnotes ---------- */
 $('#reciteBtn')?.addEventListener('click',()=>{b.classList.toggle('recite');$$('.qa .a.show').forEach(x=>x.classList.remove('show'));toast(b.classList.contains('recite')?'🙈 背诵模式：点击答案显示':'👀 阅读模式')});
 $('#supBtn')?.addEventListener('click',()=>{b.classList.toggle('nosup');toast(b.classList.contains('nosup')?'已隐藏经文脚注编号':'已显示经文脚注编号')});
 document.addEventListener('click',e=>{
  const a=e.target.closest('.qa .a');if(a&&b.classList.contains('recite')){a.classList.toggle('show');return}
  const s=e.target.closest('[data-speak]');if(s){const box=s.closest('.qa,.art,.creed,[data-speakbox]');if(!('speechSynthesis' in window)){toast('此浏览器不支持朗读');return}if(speechSynthesis.speaking){speechSynthesis.cancel();toast('⏹ 已停止');return}const u=new SpeechSynthesisUtterance(clean(box));u.lang='zh-CN';u.rate=.95;speechSynthesis.speak(u);toast('🔊 朗读中…再次点击停止');return}
  const cp=e.target.closest('[data-copy]');if(cp){navigator.clipboard?.writeText(clean(cp.closest('.qa,.art'))).then(()=>toast('📋 已复制'));return}
  const f=e.target.closest('.fc');if(f)f.classList.toggle('flip')});
 /* ---------- quiz ---------- */
 document.addEventListener('click',e=>{const o=e.target.closest('.quiz .opt');if(!o)return;const q=o.closest('.quiz');if(q.dataset.done)return;const os=$$('.opt',q),i=os.indexOf(o),ans=+q.dataset.ans;q.dataset.done=1;o.classList.add(i===ans?'ok':'no');os[ans].classList.add('ok');const r=$('.res',q);if(r)r.textContent=i===ans?'✅ 答对了！':'❌ 再想想：正确答案已标绿';const sc=LS.get('hc-quiz',{});sc[q.dataset.id]=i===ans;LS.set('hc-quiz',sc)});
 });
 /* ---------- v6: paginated lists (items live in <template>, only one page is in the DOM) ---------- */
 $$('.paged').forEach(box=>{const tpl=$(':scope>template',box),out=$('.pg-out',box),ctl=$('.pgctl',box),size=+box.dataset.size||12,unit=box.dataset.unit||'';
  const all=[...tpl.content.children];let list=all,pg=0,flt='all';
  const P={all:'全部',i:'💜 引言',m:'💔 愁苦',d:'✝️ 得救',g:'🌿 感恩'};
  ctl.innerHTML=(box.dataset.parts?Object.entries(P).map(([k,v])=>`<button class="btn${k==='all'?' pri':''}" data-pgp="${k}">${v}</button>`).join(''):'')+'<span class="pgn"><button class="btn" data-pgv="-1" aria-label="上一页">◀</button><b class="pgl" aria-live="polite"></b><button class="btn" data-pgv="1" aria-label="下一页">▶</button></span>'+(box.dataset.shuffle?'<button class="btn" data-pgs>🔀 随机打乱</button>':'')+(box.dataset.jump?`<input class="pgj" inputmode="numeric" placeholder="跳到第几${unit}…" aria-label="跳到第几${unit}">`:'');
  const render=()=>{const n=Math.max(1,Math.ceil(list.length/size));pg=Math.min(Math.max(pg,0),n-1);out.replaceChildren(...list.slice(pg*size,pg*size+size).map(x=>document.importNode(x,true)));$('.pgl',ctl).textContent=` ${pg+1} / ${n} 页 · ${list.length} 项 `};
  const filter=k=>{flt=k;list=k==='all'?all:all.filter(x=>x.dataset.p===k);pg=0;$$('[data-pgp]',ctl).forEach(x=>x.classList.toggle('pri',x.dataset.pgp===k));render()};
  ctl.addEventListener('click',e=>{const t=e.target.closest('button');if(!t)return;if(t.dataset.pgp)filter(t.dataset.pgp);else if(t.dataset.pgv){pg+=+t.dataset.pgv;render();const r=box.getBoundingClientRect();if(r.top<0)jump(box,false)}else if(t.hasAttribute('data-pgs')){list=[...list];for(let i=list.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[list[i],list[j]]=[list[j],list[i]]}pg=0;render();toast('🔀 已随机打乱')}});
  $('.pgj',ctl)?.addEventListener('keydown',e=>{if(e.key!=='Enter')return;const v=e.target.value.trim();if(flt!=='all')filter('all');const i=list.findIndex(x=>x.dataset.q===v);if(i<0){toast('没有找到 '+v);return}pg=Math.floor(i/size);render();const el=out.children[i%size];el.classList.add('flash');setTimeout(()=>el.classList.remove('flash'),1600)});
  render()});
 /* ---------- done markers ---------- */
 const done=LS.get('hc-done',{});
 $$('[data-ld-card]').forEach(c=>{if(done[c.dataset.ldCard])c.classList.add('done')});
 const db=$('#doneBtn');if(db){const n=db.dataset.ld;const upd=()=>db.textContent=done[n]?'✅ 已学完（取消）':'☑️ 标记已学完';upd();db.addEventListener('click',()=>{done[n]=!done[n];LS.set('hc-done',done);upd();toast(done[n]?'🎉 已记录学习进度':'已取消')})}
 const pc=$('#progressCount');if(pc){const k=Object.values(done).filter(Boolean).length;pc.textContent=k;const bar=$('#progressBar');if(bar)bar.style.transform='scaleX('+(k/52)+')'}
 const tidy=()=>$$('.ldgrid').forEach(g=>{const any=[...g.children].some(c=>c.style.display!=='none');const box=g.closest('.grp')||g;box.style.display=any?'':'none'});
 const lf=$('#ldFilter');if(lf){lf.addEventListener('input',()=>{const q=lf.value.trim();$$('[data-ld-card]').forEach(c=>c.style.display=!q||c.textContent.includes(q)||c.dataset.ldCard===q?'':'none');tidy()})}
 $$('[data-part]').forEach(btn=>btn.addEventListener('click',()=>{const p=btn.dataset.part;$$('[data-part]').forEach(x=>x.classList.toggle('pri',x===btn));$$('[data-ld-card]').forEach(c=>c.style.display=p==='all'||c.dataset.p===p?'':'none');tidy()}));

 idle(()=>{
 /* ---------- v4: drag-to-order challenge (pointer events + FLIP, transform only) ---------- */
 const flip=(list,fn)=>{const kids=[...list.children];const f=new Map(kids.map(k=>[k,k.getBoundingClientRect().top]));fn();kids.forEach(k=>{const d=f.get(k)-k.getBoundingClientRect().top;if(d&&!k.classList.contains('drag')){k.style.transition='none';k.style.transform=`translate3d(0,${d}px,0)`;requestAnimationFrame(()=>{k.style.transition='transform .22s cubic-bezier(.22,.8,.24,1)';k.style.transform=''})}})};
 $$('.sortbox').forEach(box=>{const list=$('.sortq',box),res=$('.res',box);
  const clear=()=>{$$('li',list).forEach(li=>li.classList.remove('ok','no'));res.textContent=''};
  list.addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;const li=b.closest('li');clear();flip(list,()=>{if(b.hasAttribute('data-up')&&li.previousElementSibling)list.insertBefore(li,li.previousElementSibling);if(b.hasAttribute('data-down')&&li.nextElementSibling)list.insertBefore(li.nextElementSibling,li)})});
  let drag=null,sy=0,base=0;
  list.addEventListener('pointerdown',e=>{const li=e.target.closest('li');if(!li||e.target.closest('button'))return;e.preventDefault();drag=li;li.setPointerCapture(e.pointerId);sy=e.clientY;base=0;li.classList.add('drag');clear()});
  list.addEventListener('pointermove',e=>{if(!drag)return;let dy=e.clientY-sy-base;const pr=drag.previousElementSibling,nx=drag.nextElementSibling;
   if(nx&&dy>nx.offsetHeight/2){const h=nx.offsetHeight+8;flip(list,()=>list.insertBefore(nx,drag));base+=h;dy-=h}
   else if(pr&&dy<-pr.offsetHeight/2){const h=pr.offsetHeight+8;flip(list,()=>list.insertBefore(drag,pr));base-=h;dy+=h}
   drag.style.transform=`translate3d(0,${dy}px,0) scale(1.02)`});
  const up=()=>{if(!drag)return;const d=drag;drag=null;d.classList.remove('drag');d.style.transition='transform .2s';d.style.transform='';setTimeout(()=>d.style.transition='',220)};
  list.addEventListener('pointerup',up);list.addEventListener('pointercancel',up);
  $('[data-sortcheck]',box).addEventListener('click',()=>{const li=$$('li',list);let good=0;const want=li.map(x=>+x.dataset.q).sort((a,b)=>a-b);li.forEach((x,i)=>{const k=+x.dataset.q===want[i];x.classList.toggle('ok',k);x.classList.toggle('no',!k);good+=k});res.textContent=good===li.length?'🎉 完全正确！问题的推进你已经掌握':'还差一点：'+good+' / '+li.length+' 个位置正确'});
  $('[data-sortshuffle]',box).addEventListener('click',()=>{clear();flip(list,()=>{const k=[...list.children];for(let i=k.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[k[i],k[j]]=[k[j],k[i]]}k.forEach(x=>list.appendChild(x))})});
 });
 /* ---------- v4: cloze recite test built from the marked phrases ---------- */
 $$('[data-cloze]').forEach(box=>{const out=$('.clozeout',box),res=$('.res',box);
  const build=()=>{out.textContent='';let n=0;$$('.qa').forEach(qa=>{const a=$('.a',qa);if(!a)return;const c=a.cloneNode(true);c.querySelectorAll('sup').forEach(x=>x.remove());
    c.querySelectorAll('[class^="mk-"]').forEach(sp=>{const t=sp.textContent;const inp=document.createElement('input');inp.className='cz';inp.dataset.ans=t;inp.setAttribute('aria-label','填空');inp.style.width=Math.min(Math.max(t.length*1.05,3),22)+'em';inp.placeholder='（'+t.length+'字）';sp.replaceWith(inp);n++});
    const d=document.createElement('div');d.className='czq';const h=document.createElement('b');h.textContent=qa.querySelector('.qn').textContent+' ';d.append(h,c);out.appendChild(d)});
   res.textContent='共 '+n+' 个空格';const f=$('input',out);f&&f.focus({preventScroll:true})};
  const norm=s=>s.replace(/[\s，。、；：“”‘’！？,.;:!?"'（）()]/g,'');
  $('[data-clozestart]',box).addEventListener('click',build);
  $('[data-clozecheck]',box).addEventListener('click',()=>{const ins=$$('input.cz',out);if(!ins.length)build();let ok=0;$$('input.cz',out).forEach(i=>{const g=norm(i.value)===norm(i.dataset.ans);i.classList.toggle('ok',g);i.classList.toggle('no',!g&&i.value!=='');ok+=g});const t=$$('input.cz',out).length;res.textContent='✅ '+ok+' / '+t+(ok===t?' 全部正确！':'')});
  $('[data-clozeshow]',box).addEventListener('click',()=>{if(!$('input.cz',out))build();$$('input.cz',out).forEach(i=>{if(norm(i.value)!==norm(i.dataset.ans)){i.value=i.dataset.ans;i.classList.add('shown')}})});
  out.addEventListener('keydown',e=>{if(e.key==='Enter'&&e.target.matches('input.cz')){const a=$$('input.cz',out);const i=a.indexOf(e.target);(a[i+1]||a[0]).focus()}});
 });
 });
 /* ---------- v4: "which Lord's Day?" game ---------- */
 const gm=$('#ldgame');if(gm){const Q=JSON.parse($('#ldgame-data').textContent);let sc=0,tot=0,streak=0,best=LS.get('hc-game-best',0);
  const qel=$('.gq',gm),opts=$('.gopts',gm),st=$('.gstat',gm);
  const stat=()=>st.textContent=`得分 ${sc} / ${tot} · 连对 ${streak} · 最佳连对 ${best}`;
  const next=()=>{const it=Q[Math.floor(Math.random()*Q.length)];const ans=it[1];const pool=new Set([ans]);while(pool.size<4){const r=Q[Math.floor(Math.random()*Q.length)][1];if(Math.abs(r-ans)<=6)pool.add(r);else if(Math.random()<.3)pool.add(r)}
   const arr=[...pool].sort(()=>Math.random()-.5);qel.textContent=it[0];opts.textContent='';
   arr.forEach(n=>{const b=document.createElement('button');b.className='opt';b.textContent=LDL[n-1];b.addEventListener('click',()=>{if(opts.dataset.done)return;opts.dataset.done=1;tot++;const g=n===ans;if(g){sc++;streak++;if(streak>best){best=streak;LS.set('hc-game-best',best)}}else streak=0;b.classList.add(g?'ok':'no');[...opts.children][arr.indexOf(ans)].classList.add('ok');stat();setTimeout(()=>{delete opts.dataset.done;next()},g?700:1600)});opts.appendChild(b)});stat()};
  const LDL=JSON.parse($('#ldgame-labels').textContent);next()}
 /* ---------- v4: progress ring + per-part bars ---------- */
 const ring=$('#ring');if(ring){const k=Object.values(done).filter(Boolean).length;const C=2*Math.PI*52;const arc=$('.arc',ring);arc.style.strokeDasharray=C;arc.style.strokeDashoffset=C*(1-k/52);$('.rk',ring).textContent=k;
  $$('[data-pbar]').forEach(b=>{const [a,z]=b.dataset.pbar.split('-').map(Number);let c=0;for(let i=a;i<=z;i++)if(done[i])c++;$('.barx',b).style.transform='scaleX('+(c/(z-a+1))+')';$('.pc',b).textContent=c+' / '+(z-a+1)})}
 idle(()=>{
 /* ---------- v4: count-up KPIs (one rAF loop, text only) ---------- */
 const kp=$$('.kpi b');if(kp.length&&!matchMedia('(prefers-reduced-motion: reduce)').matches){const vals=kp.map(b=>+b.textContent);const kio=new IntersectionObserver(es=>{if(!es.some(e=>e.isIntersecting))return;kio.disconnect();afterScroll(()=>{const t0=performance.now();const step=t=>{const p=SC.on?1:Math.min(1,(t-t0)/900),e=1-Math.pow(1-p,3);kp.forEach((b,i)=>b.textContent=Math.round(vals[i]*e));if(p<1)requestAnimationFrame(step)};requestAnimationFrame(step)})});kio.observe(kp[0])}

 /* ---------- v5: history — era filter, fly-to, scrubber ---------- */
 $$('.erab [data-era]').forEach(btn=>btn.addEventListener('click',()=>{const e=btn.dataset.era;$$('.erab [data-era]').forEach(x=>x.classList.toggle('pri',x===btn));
  $$('#tl .ev, #pcards .pcard').forEach(x=>x.style.display=e==='all'||x.dataset.era===e?'':'none');
  $$('.scrub .dot').forEach(d=>d.classList.toggle('dim',e!=='all'&&d.dataset.era!==e));window.hcMapEra&&hcMapEra(e)}));
 document.addEventListener('click',e=>{const f=e.target.closest('[data-fly]');if(!f)return;const i=+f.dataset.fly;jump($('#map'),false);const go=()=>window.hcFly&&hcFly(i);if(window.hcFly)setTimeout(go,500);else document.addEventListener('hcmap',()=>setTimeout(go,300),{once:true})});

 /* ---------- v5: continuous read-aloud player ---------- */
 (()=>{const items=$$('main .qa:not(.fc .qa), main .art, main .creed').filter(x=>!x.closest('details:not([open])'));
  const rb0=$('#readAll');if(items.length<2||!('speechSynthesis' in window)){if(rb0)rb0.addEventListener('click',()=>toast('此浏览器不支持朗读'));return}
  let tb=$('#readAll');if(!tb){const fab=$('#nvItems')||$('.fab');if(!fab)return;tb=document.createElement('button');tb.className='nb';tb.id='readAll';tb.title='连续朗读';tb.setAttribute('aria-label','连续朗读');tb.textContent='🎧';fab.prepend(tb)}
  const bar=document.createElement('div');bar.id='player';bar.setAttribute('role','region');bar.setAttribute('aria-label','朗读播放器');
  bar.innerHTML='<button data-p="prev" title="上一段" aria-label="上一段">⏮</button><button data-p="play" title="播放/暂停" aria-label="播放/暂停">▶️</button><button data-p="next" title="下一段" aria-label="下一段">⏭</button><span class="pl"></span><select aria-label="语速"><option value=".75">0.75×</option><option value=".95" selected>1×</option><option value="1.2">1.25×</option><option value="1.5">1.5×</option></select><button data-p="stop" title="关闭" aria-label="关闭">✖</button><i class="pbarx"></i>';
  document.body.appendChild(bar);
  let i=0,on=false,tok=0;const lab=$('.pl',bar),pb=$('[data-p=play]',bar),sel=$('select',bar),px=$('.pbarx',bar);
  const name=el=>{const q=$('.qn',el);return q?q.textContent:(el.dataset.toc||el.id||'').slice(0,18)};
  const ui=()=>{lab.textContent=`${name(items[i])} · ${i+1}/${items.length}`;pb.textContent=on?'⏸':'▶️';px.style.transform=`scaleX(${(i+1)/items.length})`;items.forEach((x,k)=>x.classList.toggle('speaking',k===i&&bar.classList.contains('show')))};
  const say=()=>{speechSynthesis.cancel();const my=++tok;const el=items[i];ui();
   const r=el.getBoundingClientRect();if(r.top<70||r.bottom>innerHeight-80)jump(el,false);
   const u=new SpeechSynthesisUtterance(clean(el));u.lang='zh-CN';u.rate=+sel.value;
   u.onend=()=>{if(my!==tok||!on)return;if(i<items.length-1){i++;say()}else{on=false;ui();toast('✅ 朗读完毕')}};
   u.onerror=()=>{if(my===tok){on=false;ui()}};speechSynthesis.speak(u)};
  const open=()=>{bar.classList.add('show');b.classList.add('hasplayer')};
  tb.addEventListener('click',()=>{open();const v=items.findIndex(x=>x.getBoundingClientRect().bottom>80);i=Math.max(0,v);on=true;say()});
  bar.addEventListener('click',e=>{const k=e.target.closest('[data-p]')?.dataset.p;if(!k)return;
   if(k==='play'){on=!on;if(on)say();else{tok++;speechSynthesis.cancel();ui()}}
   if(k==='next'&&i<items.length-1){i++;on?say():ui()}
   if(k==='prev'&&i>0){i--;on?say():ui()}
   if(k==='stop'){on=false;tok++;speechSynthesis.cancel();bar.classList.remove('show');b.classList.remove('hasplayer');ui()}});
  sel.addEventListener('change',()=>{if(on)say()});
  addEventListener('pagehide',()=>speechSynthesis.cancel());
  window.hcPlayer={items,get i(){return i}};
 })();
 /* ---------- v8: floating nav cluster (back · forward · home · prev/next 主日 · top · bottom) ---------- */
 const nv=$('#navc'),nvi=$('#nvItems'),nvt=$('#nvTg'),NAVI=window.navigation;
 const toBottom=()=>{const h=root.scrollHeight;scrollTo({top:h,behavior:Math.abs(h-scrollY)>innerHeight*4?'instant':'smooth'})};
 const toTop=()=>scrollTo({top:0,behavior:scrollY>innerHeight*4?'instant':'smooth'});
 const canBack=()=>NAVI&&'canGoBack' in NAVI?NAVI.canGoBack:(history.length>1||!!document.referrer);
 const canFwd=()=>NAVI&&'canGoForward' in NAVI?NAVI.canGoForward:true;
 const nvSync=()=>{if(!nvi)return;const b=$('[data-nv=back]',nvi),f=$('[data-nv=fwd]',nvi);if(b)b.disabled=!canBack();if(f)f.disabled=!canFwd()};
 const back=()=>{if(canBack())history.back();else location.href=ROOT+'index.html'};
 if(nv){const pv=$('#prevLd'),nx=$('#nextLd');const mk=(a,t,lab,cls)=>{const x=document.createElement('a');x.className='nb ld '+cls;x.href=a.href;x.textContent=t;x.title=lab;x.setAttribute('aria-label',lab);return x};
  const hm=$('[data-nv=home]',nvi);if(pv)hm.after(mk(pv,'‹',' 上一主日 ( , )'.trim()+'：'+pv.textContent.replace(/\s+/g,' ').trim(),'pv'));if(nx)(nvi.querySelector('.pv')||hm).after(mk(nx,'›','下一主日 ( . )：'+nx.textContent.replace(/\s+/g,' ').trim(),'nx'));
  const MOB=matchMedia('(max-width:1024px)');const st=LS.get('hc-navc',null);if(st!==null&&!(MOB.matches&&st))nv.classList.add(st?'open':'shut');nvt.setAttribute('aria-expanded',String(getComputedStyle(nvi).display!=='none'));
  const tg=()=>{const vis=getComputedStyle(nvi).display!=='none';nv.classList.toggle('open',!vis);nv.classList.toggle('shut',vis);nvt.setAttribute('aria-expanded',String(!vis));LS.set('hc-navc',!vis)};
  nvt.addEventListener('click',tg);nv._tg=tg;nvSync();
  nvi.addEventListener('click',e=>{if(MOB.matches&&e.target.closest('a,button')&&nv.classList.contains('open')){nv.classList.remove('open');nvt.setAttribute('aria-expanded','false')}const b=e.target.closest('[data-nv]');if(!b)return;const k=b.dataset.nv;if(k==='back')back();else if(k==='fwd')history.forward();else if(k==='bottom')toBottom();else if(k==='help')help();});
  addEventListener('pageshow',nvSync);NAVI&&NAVI.addEventListener&&NAVI.addEventListener('currententrychange',nvSync);
  let lastY=scrollY;addEventListener('scroll',()=>{if(!SC.on)return;const y=scrollY;if(y>lastY+40&&!nv.classList.contains('dim')){nv.classList.add('dim')}lastY=y},{passive:true});}
 const HELP=[['[ / ]','后退 / 前进'],['H','主页'],['G / Shift+G','到顶部 / 到底部'],[', / .','上一 / 下一主日（← → 亦可）'],['T','目录'],['M','笔记标记：全部 / 仅核心 / 关'],['N','展开 / 收起快捷导航'],['Esc','关闭弹窗 · 取消标记聚焦'],['?','本说明']];
 const help=()=>{let d=$('#kbHelp');if(!d){d=document.createElement('div');d.id='kbHelp';d.className='kbhelp';d.setAttribute('role','dialog');d.setAttribute('aria-label','快捷键');d.innerHTML='<h5>⌨️ 快捷键</h5>'+HELP.map(([k,t])=>'<div><kbd>'+k+'</kbd><span>'+t+'</span></div>').join('')+'<button type="button" class="btn" data-close>关闭</button>';document.body.appendChild(d);d.addEventListener('click',e=>{if(e.target.closest('[data-close]'))d.classList.remove('show')})}d.classList.toggle('show')};
 /* ---------- keyboard ---------- */
 addEventListener('keydown',e=>{if(e.target.matches('input,textarea,select')||e.target.isContentEditable||e.ctrlKey||e.metaKey||e.altKey)return;const k=e.key;
  if(k==='Escape'){$('#kbHelp')?.classList.remove('show');if(root.dataset.mkf){mkFocus(null)}return}
  const go=a=>{const x=$(a);if(x)location.href=x.href};
  if(k==='t')tocBtn?.click();else if(k==='r')$('#reciteBtn')?.click();else if(k==='m')$('#marksBtn')?.click();
  else if(k==='ArrowLeft'||k===',')go('#prevLd');else if(k==='ArrowRight'||k==='.')go('#nextLd');
  else if(k==='[')back();else if(k===']')history.forward();else if(k==='h')location.href=ROOT+'index.html';
  else if(k==='g')toTop();else if(k==='G')toBottom();else if(k==='n')nv?._tg?.();else if(k==='?')help();else return;
 });
 $('#topBtn')?.addEventListener('click',toTop);
 /* ---------- v8: marks — legend focus filter + live counts ---------- */
 const MKN={'mk-k':'核心','mk-b':'重点','mk-g':'恩典','mk-r':'警示','mk-u':'术语','mk-w':'难点','mk-d':'对比','mk-bg':'要点','mk-p':'人物','mk-l':'地点','mk-t':'年代','mk-ref':'经文'};
 const mkFocus=c=>{if(c&&root.dataset.mkf!==c){root.dataset.mkf=c;toast('🔦 聚焦：'+(MKN[c]||c)+' · 其余标记淡化（Esc 取消）')}else{delete root.dataset.mkf;toast('🖍️ 已取消聚焦')}$$('[data-mkf]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.mkf===root.dataset.mkf)))};
 document.addEventListener('click',e=>{const b=e.target.closest('button[data-mkf]');if(b)mkFocus(b.dataset.mkf)});
 /* ---------- v8: concept maps — draw routes once on view, toggle routes, highlight stops (events also drive the live map) ---------- */
 const cms=$$('svg.cmap[data-cm]');
 if(cms.length){const RM=matchMedia('(prefers-reduced-motion: reduce)').matches;
  const play=svg=>{svg.classList.remove('go','done');void svg.getBBox;requestAnimationFrame(()=>{svg.classList.add('go');if(!RM&&!svg.classList.contains('sm'))svg.querySelectorAll('animateMotion').forEach((a,i)=>{try{a.beginElementAt(.35+i*.5)}catch(_){}})})};
  if(RM||!('IntersectionObserver' in window))cms.forEach(s=>s.classList.add('go','done'));
  else{const cio=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){cio.unobserve(e.target);afterScroll(()=>play(e.target))}}),{rootMargin:'0px 0px -12% 0px'});cms.forEach(s=>cio.observe(s))}
  const svgOf=id=>$$('svg.cmap[data-cm="'+id+'"]');
  const hl=(id,k,fly)=>{svgOf(id).forEach(s=>s.querySelectorAll('.pm').forEach(g=>g.classList.toggle('hl',g.dataset.pk===k)));$$('[data-pk^="'+id+':"]').forEach(b=>b.classList.toggle('on',b.dataset.pk===id+':'+k));if(fly)dispatchEvent(new CustomEvent('hcplace',{detail:{map:id,key:k}}))};
  document.addEventListener('click',e=>{
   const p=e.target.closest('button[data-pk]');if(p){const [id,k]=p.dataset.pk.split(':');hl(id,k,1);return}
   const g=e.target.closest('svg.cmap[data-cm] .pm');if(g){const id=g.closest('svg').dataset.cm;hl(id,g.dataset.pk,1);return}
   const r=e.target.closest('button[data-rt]');if(r){const [id,k]=r.dataset.rt.split(':');const on=r.getAttribute('aria-pressed')!=='true';r.setAttribute('aria-pressed',String(on));r.classList.toggle('on',on);svgOf(id).forEach(s=>s.querySelector('.rt[data-rk="'+k+'"]')?.classList.toggle('off',!on));dispatchEvent(new CustomEvent('hcroute',{detail:{map:id,key:k,on}}));return}
   const pl=e.target.closest('button[data-play]');if(pl){svgOf(pl.dataset.play).forEach(play);dispatchEvent(new CustomEvent('hcplay',{detail:{map:pl.dataset.play}}))}});
  window.hcHL=hl}
 /* ---------- lazy mermaid ---------- */
 const all=$$('.mermaid');const mms=all.filter(e=>e.offsetParent!==null);all.filter(e=>e.offsetParent===null).forEach(e=>e.classList.remove('mermaid'));
 const loadM=()=>{if(window._mmL)return;window._mmL=1;const s=document.createElement('script');s.src='https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js';s.async=true;s.onload=()=>{mermaid.initialize({startOnLoad:false,theme:root.dataset.theme==='dark'?'dark':'default',securityLevel:'loose',flowchart:{useMaxWidth:true,htmlLabels:true},themeVariables:{fontFamily:'PingFang SC, Microsoft YaHei, Noto Sans SC, sans-serif'}});mermaid.run({nodes:mms}).then(()=>{requestAnimationFrame(()=>{const m=$$('.mermaid svg').map(svg=>{const vb=svg.viewBox&&svg.viewBox.baseVal;return [svg,vb,svg.parentElement.clientWidth]});m.forEach(([svg,vb,cw])=>{if(!vb||!vb.width)return;const need=vb.width*.8;if(cw<need){svg.style.maxWidth='none';svg.style.width=need+'px';svg.style.height=(vb.height*.8)+'px';svg.removeAttribute('height')}})})})};document.head.appendChild(s)};
 if(mms.length){const mio=new IntersectionObserver(es=>{if(es.some(e=>e.isIntersecting)){mio.disconnect();loadM()}},{rootMargin:'600px'});mms.forEach(m=>mio.observe(m))}
 /* ---------- v7: service worker (instant repeat loads + offline) & hover/touch prefetch fallback ---------- */
 if('serviceWorker' in navigator&&/^https?:/.test(location.protocol)&&!/[?&]nosw/.test(location.search))navigator.serviceWorker.register(new URL(ROOT+'sw.js',location.href)).catch(()=>{});
 if(!(window.HTMLScriptElement&&HTMLScriptElement.supports&&HTMLScriptElement.supports('speculationrules'))){const got=new Set([location.href.split('#')[0]]);
  const pf=e=>{const a=e.target&&e.target.closest&&e.target.closest('a[href]');if(!a||a.target==='_blank'||a.origin!==location.origin||a.hasAttribute('download'))return;const u=a.href.split('#')[0];if(got.has(u))return;got.add(u);
   if(navigator.serviceWorker&&navigator.serviceWorker.controller)fetch(u,{credentials:'same-origin'}).catch(()=>{});else{const l=document.createElement('link');l.rel='prefetch';l.href=u;document.head.appendChild(l)}};
  document.addEventListener('pointerover',pf,{passive:true});document.addEventListener('touchstart',pf,{passive:true});document.addEventListener('focusin',pf)}
 window.hcReady=true;
 });
});
})();
