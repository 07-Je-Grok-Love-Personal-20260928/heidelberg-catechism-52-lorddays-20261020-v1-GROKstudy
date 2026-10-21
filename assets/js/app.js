/* v3 · app.js — passive listeners, IntersectionObserver, rAF-batched writes */
(function(){
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const LS={get:(k,d)=>{try{const v=JSON.parse(localStorage.getItem(k));return v===null||v===undefined?d:v}catch(e){return d}},set:(k,v)=>{try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}};
const root=document.documentElement;
function toast(t){let e=$('.toast');if(!e){e=document.createElement('div');e.className='toast';document.body.appendChild(e)}e.textContent=t;requestAnimationFrame(()=>e.classList.add('on'));clearTimeout(e._t);e._t=setTimeout(()=>e.classList.remove('on'),1800)}
window.hcToast=toast;
const ready=f=>document.readyState==='loading'?document.addEventListener('DOMContentLoaded',f):f();
ready(()=>{
 const b=document.body;const mobile=()=>innerWidth<=1024;
 if(new URLSearchParams(location.search).has('cv0'))b.classList.add('cv-off');
 $('#themeBtn')?.addEventListener('click',()=>{const n=root.dataset.theme==='dark'?'light':'dark';root.dataset.theme=n;LS.set('hc-theme',n);toast(n==='dark'?'🌙 深色模式':'☀️ 浅色模式');if(window.mermaid)location.reload()});
 /* ---------- marks toggle ---------- */
 const setMarks=on=>{b.classList.toggle('nomarks',!on);$$('[data-marks]').forEach(x=>x.setAttribute('aria-pressed',on?'true':'false'))};
 setMarks(LS.get('hc-marks',true));
 document.addEventListener('click',e=>{if(!e.target.closest('[data-marks]'))return;const on=b.classList.contains('nomarks');setMarks(on);LS.set('hc-marks',on);toast(on?'🖍️ 已显示笔记标记':'🧽 已隐藏笔记标记（纯净阅读）')});
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
  toc.addEventListener('click',e=>{const tw=e.target.closest('.tw');if(tw){tw.parentElement.parentElement.classList.toggle('closed');return}if(e.target.closest('a')&&mobile())b.classList.remove('toc-open')});
  $('#tocExpand')?.addEventListener('click',()=>$$('li',toc).forEach(li=>li.classList.remove('closed')));
  $('#tocCollapse')?.addEventListener('click',()=>{$$('li',toc).forEach(li=>{if(li.querySelector(':scope>ul'))li.classList.add('closed')});window.hcOpenCur&&hcOpenCur()});
  $('#tocSearch')?.addEventListener('input',e=>{const q=e.target.value.trim();
   $$('li',toc).forEach(li=>{li.style.display=''});
   if(q){$$('li',toc).forEach(li=>{const hit=li.textContent.includes(q);li.style.display=hit?'':'none';if(hit)li.classList.remove('closed')})}
   $$('#gnav a').forEach(a=>a.style.display=!q||a.textContent.includes(q)?'':'none')});
  /* scrollspy via IntersectionObserver (no scroll handler, no layout reads) */
  const vis=new Map();let curIt=null,raf=0;
  const openPath=it=>{let li=it.li.parentElement.closest('li');while(li){li.classList.remove('closed');li.querySelector(':scope>.row>a').classList.add('par');li=li.parentElement.closest('li')}};
  window.hcOpenCur=()=>{if(curIt)openPath(curIt)};
  const apply=()=>{raf=0;let best=null;for(const it of items){if(vis.has(it.h))best=it}if(!best)best=items[0];
   if(!best||best===curIt)return;curIt?.a.classList.remove('on');$$('a.par',toc).forEach(x=>x.classList.remove('par'));
   curIt=best;best.a.classList.add('on');openPath(best);
   if(!b.classList.contains('resizing')){const sc=$('.side .scroll');const ar=best.a.getBoundingClientRect(),sr=sc.getBoundingClientRect();if(ar.top<sr.top+60||ar.bottom>sr.bottom-30)sc.scrollTo({top:sc.scrollTop+ar.top-sr.top-sr.height/3,behavior:'smooth'})}};
  const spy=new IntersectionObserver(es=>{es.forEach(e=>{const r=e.boundingClientRect;if(e.isIntersecting||(r.height>0&&r.bottom<(e.rootBounds?e.rootBounds.top:0)+1))vis.set(e.target,1);else if(r.height>0)vis.delete(e.target)});
   // headings above viewport keep their (negative) top so the last one passed wins
   if(!raf)raf=requestAnimationFrame(apply)},{rootMargin:'-'+(parseInt(getComputedStyle(root).getPropertyValue('--top'))||58)+'px 0px -70% 0px',threshold:0});
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
 const rv=$$('.reveal');
 if(matchMedia('(prefers-reduced-motion: reduce)').matches||!('IntersectionObserver' in window))rv.forEach(e=>e.classList.add('in'));
 else{const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{rootMargin:'0px 0px -6% 0px'});rv.forEach(e=>io.observe(e))}
 /* ---------- tabs ---------- */
 $$('.tabs').forEach(t=>{const bs=$$('button',t),ps=$$(':scope>.tabp',t.parentElement);bs.forEach((x,i)=>x.addEventListener('click',()=>{bs.forEach((y,j)=>y.classList.toggle('on',i===j));ps.forEach((p,j)=>p.classList.toggle('on',i===j))}))});
 /* ---------- recite / footnotes ---------- */
 $('#reciteBtn')?.addEventListener('click',()=>{b.classList.toggle('recite');$$('.qa .a.show').forEach(x=>x.classList.remove('show'));toast(b.classList.contains('recite')?'🙈 背诵模式：点击答案显示':'👀 阅读模式')});
 $('#supBtn')?.addEventListener('click',()=>{b.classList.toggle('nosup');toast(b.classList.contains('nosup')?'已隐藏经文脚注编号':'已显示经文脚注编号')});
 const clean=box=>{const c=box.cloneNode(true);c.querySelectorAll('sup,details,.tools,button').forEach(x=>x.remove());return c.textContent.replace(/\s+\n/g,'\n').trim()};
 document.addEventListener('click',e=>{
  const a=e.target.closest('.qa .a');if(a&&b.classList.contains('recite')){a.classList.toggle('show');return}
  const s=e.target.closest('[data-speak]');if(s){const box=s.closest('.qa,.art,.creed,[data-speakbox]');if(!('speechSynthesis' in window)){toast('此浏览器不支持朗读');return}if(speechSynthesis.speaking){speechSynthesis.cancel();toast('⏹ 已停止');return}const u=new SpeechSynthesisUtterance(clean(box));u.lang='zh-CN';u.rate=.95;speechSynthesis.speak(u);toast('🔊 朗读中…再次点击停止');return}
  const cp=e.target.closest('[data-copy]');if(cp){navigator.clipboard?.writeText(clean(cp.closest('.qa,.art'))).then(()=>toast('📋 已复制'));return}
  const f=e.target.closest('.fc');if(f)f.classList.toggle('flip')});
 /* ---------- quiz ---------- */
 $$('.quiz').forEach(q=>{const ans=+q.dataset.ans;$$('.opt',q).forEach((o,i)=>o.addEventListener('click',()=>{if(q.dataset.done)return;q.dataset.done=1;o.classList.add(i===ans?'ok':'no');$$('.opt',q)[ans].classList.add('ok');const r=$('.res',q);if(r)r.textContent=i===ans?'✅ 答对了！':'❌ 再想想：正确答案已标绿';const sc=LS.get('hc-quiz',{});sc[q.dataset.id]=i===ans;LS.set('hc-quiz',sc)}))});
 /* ---------- done markers ---------- */
 const done=LS.get('hc-done',{});
 $$('[data-ld-card]').forEach(c=>{if(done[c.dataset.ldCard])c.classList.add('done')});
 const db=$('#doneBtn');if(db){const n=db.dataset.ld;const upd=()=>db.textContent=done[n]?'✅ 已学完（点击取消）':'☑️ 标记本主日为已学完';upd();db.addEventListener('click',()=>{done[n]=!done[n];LS.set('hc-done',done);upd();toast(done[n]?'🎉 已记录学习进度':'已取消')})}
 const pc=$('#progressCount');if(pc){const k=Object.values(done).filter(Boolean).length;pc.textContent=k;const bar=$('#progressBar');if(bar)bar.style.transform='scaleX('+(k/52)+')'}
 const tidy=()=>$$('.ldgrid').forEach(g=>{const any=[...g.children].some(c=>c.style.display!=='none');const box=g.closest('.grp')||g;box.style.display=any?'':'none'});
 const lf=$('#ldFilter');if(lf){lf.addEventListener('input',()=>{const q=lf.value.trim();$$('[data-ld-card]').forEach(c=>c.style.display=!q||c.textContent.includes(q)||c.dataset.ldCard===q?'':'none');tidy()})}
 $$('[data-part]').forEach(btn=>btn.addEventListener('click',()=>{const p=btn.dataset.part;$$('[data-part]').forEach(x=>x.classList.toggle('pri',x===btn));$$('[data-ld-card]').forEach(c=>c.style.display=p==='all'||c.dataset.p===p?'':'none');tidy()}));
 $('#shuffleBtn')?.addEventListener('click',()=>{const d=$('#deck');[...d.children].sort(()=>Math.random()-.5).forEach(x=>d.appendChild(x));toast('🔀 已随机打乱')});

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
 /* ---------- v4: count-up KPIs (one rAF loop, text only) ---------- */
 const kp=$$('.kpi b');if(kp.length&&!matchMedia('(prefers-reduced-motion: reduce)').matches){const vals=kp.map(b=>+b.textContent);const kio=new IntersectionObserver(es=>{if(!es.some(e=>e.isIntersecting))return;kio.disconnect();const t0=performance.now();const step=t=>{const p=Math.min(1,(t-t0)/900),e=1-Math.pow(1-p,3);kp.forEach((b,i)=>b.textContent=Math.round(vals[i]*e));if(p<1)requestAnimationFrame(step)};requestAnimationFrame(step)});kio.observe(kp[0])}

 /* ---------- v5: history — era filter, fly-to, scrubber ---------- */
 $$('.erab [data-era]').forEach(btn=>btn.addEventListener('click',()=>{const e=btn.dataset.era;$$('.erab [data-era]').forEach(x=>x.classList.toggle('pri',x===btn));
  $$('#tl .ev, #pcards .pcard').forEach(x=>x.style.display=e==='all'||x.dataset.era===e?'':'none');
  $$('.scrub .dot').forEach(d=>d.classList.toggle('dim',e!=='all'&&d.dataset.era!==e));window.hcMapEra&&hcMapEra(e)}));
 document.addEventListener('click',e=>{const f=e.target.closest('[data-fly]');if(!f)return;const i=+f.dataset.fly;jump($('#map'),false);const go=()=>window.hcFly&&hcFly(i);if(window.hcFly)setTimeout(go,500);else document.addEventListener('hcmap',()=>setTimeout(go,300),{once:true})});

 /* ---------- v5: continuous read-aloud player ---------- */
 (()=>{const items=$$('main .qa:not(.fc .qa), main .art, main .creed').filter(x=>!x.closest('details:not([open])'));
  if(items.length<2||!('speechSynthesis' in window))return;
  const host=$('.hero .btns')||$('.hero');if(!host)return;
  const tb=document.createElement('button');tb.className='btn';tb.id='readAll';tb.innerHTML='🎧 连续朗读';host.appendChild(tb);
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
 /* ---------- keyboard ---------- */
 addEventListener('keydown',e=>{if(e.target.matches('input,textarea')||e.ctrlKey||e.metaKey||e.altKey)return;const k=e.key;if(k==='t')tocBtn?.click();else if(k==='r')$('#reciteBtn')?.click();else if(k==='m')$('#marksBtn')?.click();else if(k==='ArrowLeft'&&$('#prevLd'))location.href=$('#prevLd').href;else if(k==='ArrowRight'&&$('#nextLd'))location.href=$('#nextLd').href});
 $('#topBtn')?.addEventListener('click',()=>scrollTo({top:0,behavior:'smooth'}));
 /* ---------- lazy mermaid ---------- */
 const all=$$('.mermaid');const mms=all.filter(e=>e.offsetParent!==null);all.filter(e=>e.offsetParent===null).forEach(e=>e.classList.remove('mermaid'));
 const loadM=()=>{if(window._mmL)return;window._mmL=1;const s=document.createElement('script');s.src='https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js';s.async=true;s.onload=()=>{mermaid.initialize({startOnLoad:false,theme:root.dataset.theme==='dark'?'dark':'default',securityLevel:'loose',flowchart:{useMaxWidth:true,htmlLabels:true},themeVariables:{fontFamily:'PingFang SC, Microsoft YaHei, Noto Sans SC, sans-serif'}});mermaid.run({nodes:mms}).then(()=>{requestAnimationFrame(()=>{const m=$$('.mermaid svg').map(svg=>{const vb=svg.viewBox&&svg.viewBox.baseVal;return [svg,vb,svg.parentElement.clientWidth]});m.forEach(([svg,vb,cw])=>{if(!vb||!vb.width)return;const need=vb.width*.8;if(cw<need){svg.style.maxWidth='none';svg.style.width=need+'px';svg.style.height=(vb.height*.8)+'px';svg.removeAttribute('height')}})})})};document.head.appendChild(s)};
 if(mms.length){const mio=new IntersectionObserver(es=>{if(es.some(e=>e.isIntersecting)){mio.disconnect();loadM()}},{rootMargin:'600px'});mms.forEach(m=>mio.observe(m))}
 window.hcReady=true;
});
})();
