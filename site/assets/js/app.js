(function(){
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const LS={get:(k,d)=>{try{return JSON.parse(localStorage.getItem(k))??d}catch(e){return d}},set:(k,v)=>{try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}};
// theme
const th=LS.get('hc-theme','dark');document.documentElement.dataset.theme=th;
function toast(t){let e=$('.toast');if(!e){e=document.createElement('div');e.className='toast';document.body.appendChild(e)}e.textContent=t;e.classList.add('on');clearTimeout(e._t);e._t=setTimeout(()=>e.classList.remove('on'),1800)}
window.hcToast=toast;
document.addEventListener('DOMContentLoaded',()=>{
 const b=document.body;
 $('#themeBtn')?.addEventListener('click',()=>{const n=document.documentElement.dataset.theme==='dark'?'light':'dark';document.documentElement.dataset.theme=n;LS.set('hc-theme',n);toast(n==='dark'?'🌙 深色模式':'☀️ 浅色模式');if(window.mermaid)location.reload()});
 // TOC
 const toc=$('#toc');const heads=$$('main h2[id], main h3[id]');
 if(toc){heads.forEach(h=>{const a=document.createElement('a');a.href='#'+h.id;a.textContent=h.dataset.toc||h.textContent.replace(/\s+/g,' ').trim();a.className=h.tagName==='H3'?'l3':'l2';toc.appendChild(a)});
  $('#tocSearch')?.addEventListener('input',e=>{const q=e.target.value.trim();$$('#toc a, #gnav a').forEach(a=>a.style.display=!q||a.textContent.includes(q)?'':'none')});}
 const tocBtn=$('#tocBtn');
 if(LS.get('hc-toc-hidden',false)&&innerWidth>1024)b.classList.add('toc-hidden');
 tocBtn?.addEventListener('click',()=>{if(innerWidth<=1024){b.classList.toggle('toc-open')}else{b.classList.toggle('toc-hidden');LS.set('hc-toc-hidden',b.classList.contains('toc-hidden'))}});
 $('.backdrop')?.addEventListener('click',()=>b.classList.remove('toc-open'));
 $$('#toc a, #gnav a').forEach(a=>a.addEventListener('click',()=>{if(innerWidth<=1024)b.classList.remove('toc-open')}));
 // scrollspy + progress
 const pr=$('.progress');const links=$$('#toc a');
 const onScroll=()=>{const h=document.documentElement;const p=h.scrollTop/(h.scrollHeight-h.clientHeight||1);if(pr)pr.style.width=(p*100)+'%';
  let cur=null;for(const x of heads){if(x.getBoundingClientRect().top<120)cur=x;else break}
  links.forEach(a=>a.classList.toggle('on',cur&&a.getAttribute('href')==='#'+cur.id))};
 addEventListener('scroll',onScroll,{passive:true});onScroll();
 // reveal
 const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{rootMargin:'0px 0px -6% 0px'});
 $$('.reveal').forEach(e=>io.observe(e));
 setTimeout(()=>$$('.reveal').forEach(e=>e.classList.add('in')),2500);
 // recite mode
 $('#reciteBtn')?.addEventListener('click',()=>{b.classList.toggle('recite');$$('.qa .a.show').forEach(x=>x.classList.remove('show'));toast(b.classList.contains('recite')?'🙈 背诵模式：点击答案显示':'👀 阅读模式')});
 document.addEventListener('click',e=>{const a=e.target.closest('.qa .a');if(a&&b.classList.contains('recite'))a.classList.toggle('show')});
 $('#supBtn')?.addEventListener('click',()=>{b.classList.toggle('nosup');toast(b.classList.contains('nosup')?'已隐藏经文脚注编号':'已显示经文脚注编号')});
 // speech
 document.addEventListener('click',e=>{const s=e.target.closest('[data-speak]');if(!s)return;const box=s.closest('.qa,.art,.creed,[data-speakbox]');if(!('speechSynthesis' in window)){toast('此浏览器不支持朗读');return}
  if(speechSynthesis.speaking){speechSynthesis.cancel();toast('⏹ 已停止');return}
  const c=box.cloneNode(true);c.querySelectorAll('sup,details,.tools,button').forEach(x=>x.remove());const u=new SpeechSynthesisUtterance(c.innerText);u.lang='zh-CN';u.rate=.95;speechSynthesis.speak(u);toast('🔊 朗读中…再次点击停止')});
 // copy
 document.addEventListener('click',e=>{const s=e.target.closest('[data-copy]');if(!s)return;const box=s.closest('.qa,.art');const c=box.cloneNode(true);c.querySelectorAll('sup,details,.tools,button').forEach(x=>x.remove());navigator.clipboard?.writeText(c.innerText.trim()).then(()=>toast('📋 已复制'))});
 // flashcards
 document.addEventListener('click',e=>{const f=e.target.closest('.fc');if(f)f.classList.toggle('flip')});
 // quiz
 $$('.quiz').forEach(q=>{const ans=+q.dataset.ans;$$('.opt',q).forEach((o,i)=>o.addEventListener('click',()=>{if(q.dataset.done)return;q.dataset.done=1;o.classList.add(i===ans?'ok':'no');$$('.opt',q)[ans].classList.add('ok');const r=$('.res',q);if(r)r.textContent=i===ans?'✅ 答对了！':'❌ 再想想：正确答案已标绿';const sc=LS.get('hc-quiz',{});sc[q.dataset.id]=i===ans;LS.set('hc-quiz',sc)}))});
 // done marker
 const done=LS.get('hc-done',{});
 $$('[data-ld-card]').forEach(c=>{if(done[c.dataset.ldCard])c.classList.add('done')});
 const db=$('#doneBtn');if(db){const n=db.dataset.ld;const upd=()=>db.textContent=done[n]?'✅ 已学完（点击取消）':'☑️ 标记本主日为已学完';upd();db.addEventListener('click',()=>{done[n]=!done[n];LS.set('hc-done',done);upd();toast(done[n]?'🎉 已记录学习进度':'已取消')})}
 const pc=$('#progressCount');if(pc){const k=Object.values(done).filter(Boolean).length;pc.textContent=k;const bar=$('#progressBar');if(bar)bar.style.width=(k/52*100)+'%'}
 // LD filter
 const lf=$('#ldFilter');if(lf){lf.addEventListener('input',()=>{const q=lf.value.trim();$$('[data-ld-card]').forEach(c=>c.style.display=!q||c.textContent.includes(q)||c.dataset.ldCard===q?'':'none')})}
 $$('[data-part]').forEach(btn=>btn.addEventListener('click',()=>{const p=btn.dataset.part;$$('[data-part]').forEach(x=>x.classList.toggle('pri',x===btn));$$('[data-ld-card]').forEach(c=>c.style.display=p==='all'||c.dataset.p===p?'':'none')}));
 // flashcard deck shuffle
 $('#shuffleBtn')?.addEventListener('click',()=>{const d=$('#deck');const ch=[...d.children];ch.sort(()=>Math.random()-.5).forEach(x=>d.appendChild(x));toast('🔀 已随机打乱')});
 // keyboard
 addEventListener('keydown',e=>{if(e.target.matches('input,textarea'))return;if(e.key==='t')tocBtn?.click();if(e.key==='r')$('#reciteBtn')?.click();if(e.key==='ArrowLeft'&&$('#prevLd'))location.href=$('#prevLd').href;if(e.key==='ArrowRight'&&$('#nextLd'))location.href=$('#nextLd').href});
 $('#topBtn')?.addEventListener('click',()=>scrollTo({top:0,behavior:'smooth'}));
 // mermaid
 const mms=$$('.mermaid').filter(e=>e.offsetParent!==null);$$('.mermaid').filter(e=>e.offsetParent===null).forEach(e=>e.classList.remove('mermaid'));
 const loadM=()=>{if(window._mmL)return;window._mmL=1;const s=document.createElement('script');s.src='https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js';s.onload=()=>{mermaid.initialize({startOnLoad:false,theme:document.documentElement.dataset.theme==='dark'?'dark':'default',securityLevel:'loose',flowchart:{useMaxWidth:true,htmlLabels:true},themeVariables:{fontFamily:'PingFang SC, Microsoft YaHei, Noto Sans SC, sans-serif'}});mermaid.run({nodes:mms}).then(()=>{document.querySelectorAll('.mermaid svg').forEach(svg=>{const vb=svg.viewBox&&svg.viewBox.baseVal;if(!vb||!vb.width)return;const box=svg.parentElement;const k=.8;const need=vb.width*k;if(box.clientWidth<need){svg.style.maxWidth='none';svg.style.width=need+'px';svg.style.height=(vb.height*k)+'px';svg.removeAttribute('height')}})})};document.head.appendChild(s)};
 if(mms.length){const mio=new IntersectionObserver(es=>{if(es.some(e=>e.isIntersecting)){mio.disconnect();loadM()}},{rootMargin:'800px'});mms.forEach(m=>mio.observe(m))}
});
})();
