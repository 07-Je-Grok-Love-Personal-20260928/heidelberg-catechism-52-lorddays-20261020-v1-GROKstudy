from common import *
def sec(id,ico,title,inner): return f'<section class="sec"><h2 id="{id}"><span class="ico">{ico}</span>{title}</h2>{inner}</section>'
def plain(s): return re.sub(r'<sup>.*?</sup>','',s).replace('<','\u003c') if False else re.sub('<[^>]+>','',re.sub(r'<sup>.*?</sup>','',s))
idx=[]
for ld in D['hc']:
    for q in ld['qas']:
        idx.append(dict(k='海德堡',t=f'主日{ld["n"]} · {q["q"]}',x=plain(' '.join(q['a'])),u=f'ld/{ld["n"]:02d}.html#q{qnum(q)}'))
    no=N[ld['n']]
    idx.append(dict(k='解读',t=f'主日{ld["n"]} · {no["t"]}（本站解读）',x=' '.join([no['k'],no['big'],no['cov'],no['why'],no['hard']]),u=f'ld/{ld["n"]:02d}.html'))
for a in D['bc']: idx.append(dict(k='比利时信条',t=a['title'],x=plain(' '.join(a['paras'])),u=f'texts/bc.html#bc{a["n"]}'))
for s in D['cd']:
    for a in s['arts']: idx.append(dict(k='多特信经',t=f'{s["title"]} · {a["title"]}',x=plain(' '.join(a['paras'])),u=f'texts/cd.html#cd{s["sec"]}-{a["n"]}'))
for c in D['creeds']: idx.append(dict(k='普世信经',t=c['title'],x=plain(' '.join(c['text'])),u=f'texts/creeds.html#{c["slug"]}'))
os.makedirs(SITE+'/assets/data',exist_ok=True)
json.dump(idx,open(SITE+'/assets/data/search.json','w'),ensure_ascii=False,separators=(',',':'))
srch=f'''<section class="hero reveal"><span class="chip">🔎 全文搜索</span><h1>搜索三项联合信条与普世信经</h1><p class="lead">在 129 个问答、37 条比利时信条、多特信经全部条文、三大信经以及本站 52 篇解读中检索。</p>
<input id="q" class="tocsearch" style="font-size:17px;padding:12px 16px;margin-top:10px" placeholder="例如：安慰、称义、圣餐、拣选、阿们" autofocus>
<div class="btns" id="kinds" style="margin-top:10px"></div></section>
<section class="sec"><h2 id="res"><span class="ico">📋</span>结果 <span id="cnt" class="small muted"></span></h2><div id="out" class="grid g2"></div></section>
<script>(function(){{let D=[],kind='全部';const q=document.getElementById('q'),out=document.getElementById('out'),cnt=document.getElementById('cnt'),kd=document.getElementById('kinds');
const esc=s=>s.replace(/[&<>"]/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]));
function hl(t,w){{if(!w)return esc(t);const i=t.indexOf(w);if(i<0)return esc(t.slice(0,120))+'…';const a=Math.max(0,i-50);return(a?'…':'')+esc(t.slice(a,i))+'<mark>'+esc(w)+'</mark>'+esc(t.slice(i+w.length,i+w.length+90))+'…'}}
function run(){{const w=q.value.trim();let r=D.filter(d=>(kind==='全部'||d.k===kind)&&(!w||d.t.includes(w)||d.x.includes(w)));cnt.textContent='共 '+r.length+' 条'+(r.length>80?'（显示前 80 条）':'');
out.innerHTML=r.slice(0,80).map(d=>'<a class="card lift" href="'+d.u+'"><span class="chip">'+d.k+'</span><h3 style="margin:8px 0 4px;font-size:17px">'+(w&&d.t.includes(w)?d.t.split(w).map(esc).join('<mark>'+esc(w)+'</mark>'):esc(d.t))+'</h3><p class="small muted" style="margin:0">'+hl(d.x,w)+'</p></a>').join('')}}
fetch('assets/data/search.json').then(r=>r.json()).then(j=>{{D=j;['全部','海德堡','比利时信条','多特信经','普世信经','解读'].forEach(k=>{{const b=document.createElement('button');b.className='btn'+(k==='全部'?' pri':'');b.textContent=k;b.onclick=()=>{{kind=k;[...kd.children].forEach(x=>x.classList.toggle('pri',x===b));run()}};kd.appendChild(b)}});
const u=new URLSearchParams(location.search).get('q');if(u)q.value=u;run()}});q.addEventListener('input',run)}})()</script>'''
page('search.html','全文搜索',srch,'海德堡要理问答、比利时信条、多特信经、普世信经全文搜索')
V1=[('GitHub Pages（旧仓库名，仓库更名后已失效）','https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-20261020-v1-GROKstudy/'),('Surge','https://heidelberg-catechism-52-lorddays-20261020-v1-grokstudy.surge.sh'),('Netlify','https://heidelberg-catechism-52-lorddays-20261020-v1-grokstudy.netlify.app')]
V2=[('GitHub Pages','https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/'),('Surge','https://heidelberg-catechism-52-lorddays-20261020-v2-grokser.surge.sh'),('Netlify','https://heidelberg-catechism-52-lorddays-20261020-v2-grokser.netlify.app')]
v2changes=['📱 手机端圣约神学流程图改为竖排“盟约阶梯”，平板与桌面仍显示 Mermaid 流程图；其余流程图在手机上按原始比例横向滑动，文字清晰。',
'🪔 52 个主日全部新增“深化”板块：一个圣经画面、如何指向基督、一句祷告、两道小组/家庭讨论题（共 208 条新内容）。',
'🔎 新增全文搜索页：129 问、37 条比利时信条、多特信经全部条文、三大信经与 52 篇解读，可按类别筛选并高亮关键词。',
'🆕 新增版本徽章（顶栏）与本更新记录页。',
'⚡ 性能：脚本 defer；Mermaid 只在图表接近可视区时才加载；地图库 Leaflet 改为按需加载；手机端减少毛玻璃模糊层以提升滚动流畅度；长列表卡片使用 content-visibility；图片标注尺寸并懒加载。',
'🎨 主题在页面渲染前即应用（无闪烁）；表格首列不折行；打印样式优化。',
'🏷️ 仓库更名为 heidelberg-catechism-52-lorddays-GROKstudy（保留全部历史），GitHub Pages 地址随之更新；全站只用相对路径。',
'✅ 原文逐字校验仍为 0 处差异；375 / 768 / 1440 三种宽度的溢出检测重新跑过；截图全部重拍。']
lnk=lambda L:''.join(f'<li>{esc(t)}：<a href="{u}" target="_blank" rel="noopener">{u}</a></li>' for t,u in L)
ch=f'''<section class="hero reveal"><span class="chip g">🆕 版本记录</span><h1>更新记录 Changelog</h1><p class="lead">当前版本：<b class="key">{VERSION}</b> · {DATE}</p></section>'''
ch+=sec('v2','🚀','v2 · 2026-10-20',f'<div class="card pan core reveal"><ul class="clean">{"".join(f"<li>{esc(x)}</li>" for x in v2changes)}</ul><h3>🌐 v2 部署</h3><ul class="clean">{lnk(V2)}</ul></div>')
ch+=sec('v1','📦','v1 · 2026-10-20',f'<div class="card pan why reveal"><ul class="clean"><li>首版：52 主日深度解析页、四部全文阅读/背诵版、圣经与圣约、历史地理（时间线、地图）、信条对比、速记中心、资料页。</li><li>全部原文由程序从 ccifellowship.org 抓取并逐字校验。</li></ul><h3>🌐 v1 部署（保留不动）</h3><ul class="clean">{lnk(V1)}</ul></div>')
ch+=sec('repo','📂','源码',f'<div class="card reveal"><p><a href="https://github.com/07-Je-Grok-Love-Personal-20260928/{REPO}">github.com/07-Je-Grok-Love-Personal-20260928/{REPO}</a></p></div>')
page('changelog.html','更新记录',ch,'版本更新记录')
json.dump(dict(V1=V1,V2=V2,changes=v2changes),open(ROOT+'/build/versions.json','w'),ensure_ascii=False,indent=1)
print('v2 pages done', len(idx))
