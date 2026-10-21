from common import *
def plain(s): return re.sub(r'<sup>.*?</sup>','',s).replace('<','\u003c') if False else re.sub('<[^>]+>','',re.sub(r'<sup>.*?</sup>','',s))
idx=[]
for ld in D['hc']:
    for q in ld['qas']:
        idx.append(dict(k='海德堡',t=f'{LDI[ld["n"]]} 主日{ld["n"]} · {q["q"]}',x=plain(' '.join(q['a'])),u=f'ld/{ld["n"]:02d}.html#q{qnum(q)}'))
    no=N[ld['n']]
    idx.append(dict(k='解读',t=f'{ld_label(ld["n"])}（本站解读）',x=' '.join([re.sub(r'[*=~_:!]{2}','',T[ld['n']][0]),no['k'],no['big'],no['cov'],no['why'],no['hard']]),u=f'ld/{ld["n"]:02d}.html'))
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
V5=[('GitHub Pages','https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/'),('Surge','https://heidelberg-catechism-52-lorddays-20261021-v5-grokstudy.surge.sh'),('Netlify','https://heidelberg-catechism-52-lorddays-20261021-v5-grokstudy.netlify.app')]
V4=[('GitHub Pages（与 v5 同一地址，现显示最新版）','https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/'),('Surge','https://heidelberg-catechism-52-lorddays-20261021-v4-grokser.surge.sh'),('Netlify','https://heidelberg-catechism-52-lorddays-20261021-v4-grokser.netlify.app')]
V3=[('GitHub Pages（与 v5 同一地址，现显示最新版）','https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/'),('Surge','https://heidelberg-catechism-52-lorddays-20261020-v3-grokser.surge.sh'),('Netlify','https://heidelberg-catechism-52-lorddays-20261020-v3-grokser.netlify.app')]
V2=[('GitHub Pages（与 v5 同一地址，现显示最新版）','https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/'),('Surge','https://heidelberg-catechism-52-lorddays-20261020-v2-grokser.surge.sh'),('Netlify','https://heidelberg-catechism-52-lorddays-20261020-v2-grokser.netlify.app')]
REL='https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/'
v3changes=['⚡ 流畅度重构：毛玻璃 backdrop-filter 只保留在顶栏、悬浮按钮与提示条；卡片改为“伪玻璃”渐变；背景改为预模糊的径向渐变云层，只用 transform 漂移（不再对大面积元素做 filter:blur 动画）；各 section 使用 content-visibility:auto；目录高亮改用 IntersectionObserver，进度条使用 CSS scroll-timeline（不支持时用 rAF）；所有监听器 passive；支持 prefers-reduced-motion。',
'↔️ 左侧目录可拖动右边缘调整宽度（220px – min(640px, 70vw)），支持鼠标、触屏与键盘方向键，宽度保存在本机；双击把手恢复默认；长标题单行省略并带悬停提示。',
'📑 目录改为三级编号树：一级“一、二、三”，二级“1. 2.”，三级“1.1”；每级可折叠，提供“全部展开 / 全部折叠”，滚动时自动展开并高亮当前所在小节。',
'🖍️ 新增笔记标记系统：高亮、粗体金、蓝实线（定义）、橙波浪线（难点）、红虚线（对比/错误立场）、红字（警示）、经文标签；五类提示框：核心 · 难点 · 易错 · 金句 · 记忆钩。顶栏 🖍️ 或 M 键一键显示/隐藏。原文只包标签，文字一字不改（校验 0 差异）。',
'💎 每个主日新增“精华速览”：五问提要（论题 · 为什么 · 写了什么 · 怎么活 · 圣经与圣约）、逐字金句、易错提醒，以及“关联星图”（各问与关键词、比利时信条、多特信经、威斯敏斯特的连线动画）和 52 主日位置条。',
'📊 新增图表：首页 129 问三部分比例条、52 主日问答数柱状图（可点击）；对比页“覆盖度图”；原文中心卡片进度条；动画只用 transform / stroke-dashoffset。',
'🧭 结构收紧：顶栏导航精简为 8 项（修复约 1024px 宽度时最后一项被截断），新增“原文中心”汇总四部原文；52 主日总览按 17 个主题分组；主日页重排为 精华 → 原文 → 整体 → 局部 → 对照 → 应用（分页签）→ 记忆 → 延伸。',
'✅ 校验：原文逐字比对 0 差异（含金句）；375 / 768 / 1440 全部页面无横向溢出；Playwright 测试目录拖动与折叠；截图全部重拍（v3-*）。']
v4changes=['🏷️ 统一的“主日图标 + 标题”总表：52 个主日各有专属图标与具体标题（如“✝️ 主日1 · 唯一的安慰”“🪞 主日2 · 律法照出我的愁苦”），全站共用——原文阅读版目录、侧栏 52 主日速览、总览、主日页标题与翻页、速记卡片/口诀表/测验、搜索结果。',
'📑 原文目录重做：要理问答为 部（💜引言 / 💔第一部 / ✝️第二部 / 🌿第三部）→ 主题（🩸子神和我们的得赎、🕊️圣灵神和我们的成圣、⚖️称义、📖圣言与圣礼、💧洗礼、🍞圣餐、🪨十诫、🙏祷告）→ 主日（编号＝主日号）→ 问 的四级可折叠树，不再出现“1. 主日1”或重复的部名；比利时信条按 12 个主题分组，37 条用原文条目标题＋图标＋条号；多特信经四项各配图标，条目用原文标题，错谬反驳单独标注。',
'🧭 侧栏“52 个主日速览”改为按四部分组、带编号与图标，与页内目录同步；在主日页自动展开并高亮当前主日。',
'🖍️ 标记增加：全部 129 问都有原文关键短语标记（共 215 处，原文文字不变）；术语词表扩充，每段最多 4 处。',
'💎 每个主日新增“核心经文”（各问第一条经文出处，取自原文脚注）与“承上启下”链条（上一主日 → 本主日 → 下一主日）。',
'🎮 新互动：🧩 拖动排序挑战（按住拖动或 ↑↓，FLIP 动画）、✍️ 填空背诵（由标记短语自动生成并判分）、🎲 “这一问属于哪个主日？”归属挑战（得分与最佳连对）、可点击的关联星图（节点跳到对应问答 / 信条 / 搜索）、总览卡片悬停显示论题。',
'📊 新图表：各问经文出处数量条形图（可点击）、比利时信条 37 条 12 主题环形图（可点击扇区）、速记中心学习进度环与四部分进度条、首页数字滚动计数；动画以 transform / opacity 为主（进度环与星图连线是一次性的 stroke 描边动画）。',
'✅ 校验：原文逐字 0 差异；全部页面 375 / 768 / 1024 / 1440 无溢出；Playwright 目录 + 互动测试全部通过；v3 → v4 性能对比见 README。']
v5changes=['⏳ 历史时间线扩充到 36 个事件，分为五个时期（背景 / 普法尔茨 / 尼德兰 / 多特 / 传承），新增苏黎世辩论、重洗派、加尔文《教会法令》、特伦托会议、《苏黎世协议》、圣像破坏、八十年战争、《誓绝法案》、十二年停战、奥尔登巴内费尔特、威斯特伐利亚、1834 分离运动、北美改革宗教会等；每个事件尽量附上相关主日链接。',
'🎚️ 时间线概览条（36 个圆点依次弹出，点击跳到事件；大圆点＝与主日相关）＋“时期”筛选按钮，筛选会同步淡化地图上的地点。',
'🗺️ 地图升级：21 个地点（新增马尔堡、特伦托、安特卫普、伦敦），按时期着色，弹窗列出相关主日；21 张地点卡片可“在地图上查看”（飞到该地并打开弹窗）；4 条路线可开关（乌尔西努求学、要理问答北传、比利时信条之路、新增“圣餐之争”路线）。',
'🏞️ 区域文化：六个舞台卡片（选帝侯普法尔茨、瑞士城市共和国、萨克森、南尼德兰、荷兰共和国、流亡社区），每张列出政体 / 语言或宗教 / 经济 / 与信条的关系。',
'🔭 每个主日新增“从整体到局部：六级缩放”——圣经大戏（创造 / 堕落 / 救赎 / 完成 / 回应）→ 圣约阶段 → 教义主题 → 要理问答的部与主题 → 本主日 → 各问，逐级展开动画；以及“八个视角罗盘”（整本圣经、圣约、圣经画面、指向基督、历史背景、核心要点、难点、应用），点击翻开一句话并跳到详解。',
'🧩 圣经页新增“52 主日 × 圣经大戏”教义主题矩阵（13 个教义主题 × 5 幕，点击进入主日）；与主日页的缩放使用同一张映射表。',
'⚖️ 对比页新增：“三个处境 → 三份文件”问题—文件—回答流程（说明为什么是三份而不是一份）；可点击的三圆维恩图（独有重点 / 两两共同 / 共同核心）；“抗辩派五条 vs 多特 vs 海德堡 vs 比利时”对照表。',
'🎧 连续朗读播放器：主日页与原文阅读版一键“连续朗读”，底部播放条支持 上一段 / 播放暂停 / 下一段 / 语速 / 进度，当前朗读的问答高亮并自动滚动到视野内（使用浏览器自带语音，效果取决于系统中文语音）。',
'✅ 校验：原文逐字 0 差异；全部页面 375 / 768 / 1024 / 1440 无溢出；Playwright 测试（新增地图飞行、时期筛选、朗读播放器、缩放与罗盘测试）；v4 → v5 性能对比见 README。']
lnk=lambda L:''.join(f'<li>{esc(t)}：<a href="{u}" target="_blank" rel="noopener">{u}</a></li>' for t,u in L)
ch=f'''<section class="hero reveal"><span class="chip g">🆕 版本记录</span><h1>更新记录 Changelog</h1><p class="lead">当前版本：<b class="key">{VERSION}</b> · {DATE}</p></section>'''
ch+=sec('v5','🚀','v5 · 2026-10-21',f'<div class="card pan core reveal"><ul class="clean">{"".join(f"<li>{esc(x)}</li>" for x in v5changes)}</ul><h3>🌐 v5 部署</h3><ul class="clean">{lnk(V5)}<li>Release：<a href="{REL}v5">{REL}v5</a></li></ul></div>')
ch+=sec('v4','📦','v4 · 2026-10-21',f'<div class="card pan why reveal"><ul class="clean">{"".join(f"<li>{esc(x)}</li>" for x in v4changes)}</ul><h3>🌐 v4 部署（保留）</h3><ul class="clean">{lnk(V4)}<li>Release：<a href="{REL}v4">{REL}v4</a></li></ul></div>')
ch+=sec('v3','📦','v3 · 2026-10-20',f'<div class="card pan why reveal"><ul class="clean">{"".join(f"<li>{esc(x)}</li>" for x in v3changes)}</ul><h3>🌐 v3 部署（保留）</h3><ul class="clean">{lnk(V3)}<li>Release：<a href="{REL}v3">{REL}v3</a></li></ul></div>')
ch+=sec('v2','📦','v2 · 2026-10-20',f'<div class="card pan why reveal"><ul class="clean">{"".join(f"<li>{esc(x)}</li>" for x in v2changes)}</ul><h3>🌐 v2 部署（保留）</h3><ul class="clean">{lnk(V2)}<li>Release：<a href="{REL}v2">{REL}v2</a></li></ul></div>')
ch+=sec('v1','📦','v1 · 2026-10-20',f'<div class="card pan why reveal"><ul class="clean"><li>首版：52 主日深度解析页、四部全文阅读/背诵版、圣经与圣约、历史地理（时间线、地图）、信条对比、速记中心、资料页。</li><li>全部原文由程序从 ccifellowship.org 抓取并逐字校验。</li></ul><h3>🌐 v1 部署（保留不动）</h3><ul class="clean">{lnk(V1)}<li>Release：<a href="{REL}v1">{REL}v1</a></li></ul></div>')
ch+=sec('repo','📂','源码',f'<div class="card reveal"><p><a href="https://github.com/07-Je-Grok-Love-Personal-20260928/{REPO}">github.com/07-Je-Grok-Love-Personal-20260928/{REPO}</a></p></div>')
page('changelog.html','更新记录',ch,'版本更新记录')
json.dump(dict(V1=V1,V2=V2,V3=V3,V4=V4,V5=V5,changes=v2changes,changes_v3=v3changes,changes_v4=v4changes,changes_v5=v5changes),open(ROOT+'/build/versions.json','w'),ensure_ascii=False,indent=1)
print('v3 pages done', len(idx))
