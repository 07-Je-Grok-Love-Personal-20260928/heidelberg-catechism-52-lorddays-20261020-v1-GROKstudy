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
V9=[('GitHub Pages','https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/'),('Surge','https://heidelberg-catechism-52-lorddays-20261024-v9-grokstudy.surge.sh'),('Netlify','https://heidelberg-catechism-52-lorddays-20261024-v9-grokstudy.netlify.app')]
V8=[('GitHub Pages（与 v9 同一地址，现显示最新版）','https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/'),('Surge','https://heidelberg-catechism-52-lorddays-20261023-v8-grokstudy.surge.sh'),('Netlify','https://heidelberg-catechism-52-lorddays-20261023-v8-grokstudy.netlify.app')]
V7=[('GitHub Pages（与 v9 同一地址，现显示最新版）','https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/'),('Surge','https://heidelberg-catechism-52-lorddays-20261023-v7-grokstudy.surge.sh'),('Netlify','https://heidelberg-catechism-52-lorddays-20261023-v7-grokstudy.netlify.app')]
V6=[('GitHub Pages（与 v9 同一地址，现显示最新版）','https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/'),('Surge','https://heidelberg-catechism-52-lorddays-20261021-v6-grokstudy.surge.sh'),('Netlify','https://heidelberg-catechism-52-lorddays-20261021-v6-grokstudy.netlify.app')]
V5=[('GitHub Pages（与 v9 同一地址，现显示最新版）','https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/'),('Surge','https://heidelberg-catechism-52-lorddays-20261021-v5-grokstudy.surge.sh'),('Netlify','https://heidelberg-catechism-52-lorddays-20261021-v5-grokstudy.netlify.app')]
V4=[('GitHub Pages（与 v9 同一地址，现显示最新版）','https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/'),('Surge','https://heidelberg-catechism-52-lorddays-20261021-v4-grokser.surge.sh'),('Netlify','https://heidelberg-catechism-52-lorddays-20261021-v4-grokser.netlify.app')]
V3=[('GitHub Pages（与 v9 同一地址，现显示最新版）','https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/'),('Surge','https://heidelberg-catechism-52-lorddays-20261020-v3-grokser.surge.sh'),('Netlify','https://heidelberg-catechism-52-lorddays-20261020-v3-grokser.netlify.app')]
V2=[('GitHub Pages（与 v9 同一地址，现显示最新版）','https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/'),('Surge','https://heidelberg-catechism-52-lorddays-20261020-v2-grokser.surge.sh'),('Netlify','https://heidelberg-catechism-52-lorddays-20261020-v2-grokser.netlify.app')]
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
v9changes=[
'☁️ 流畅度（重点）：逐帧剖析真实卡顿来源后对症处理——① 滚动期间放一层透明“滚动护罩”，静止的鼠标不再触发悬停样式与提示气泡的重算（替代 v8 对整个 main 切换 pointer-events 带来的整树样式重算）；② “滚动结束”改为 380 ms 真正静止后才算（scrollend 在滚轮两格之间也会触发），图表展开、路线描线等动画不会在手势中途启动；③ 滚动一开始就把正在播放的路线动画直接定格到终点；④ 空闲时按“离视口最近者优先”逐段预排版 content-visibility 区块（地图区块除外），快速滚动时不再临时排版整段；⑤ 背景云层漂移在滚动时暂停；⑥ 所有监听均为 passive，动画只用 transform / opacity。前后对比见 README 的 perf6 表。',
'🎨 新增五套主题（共十套）：🌸 樱花粉霞 · 🍋 柠檬薄荷 · 🔥 暮光琥珀（深色）· 🌠 极光青紫（深色）· 🖋️ 水墨朱砂。选择器改为双列色板预览（底色 / 卡片 / “Aa” 字色 / 两个强调色），一键切换并带淡入过渡（尊重“减少动态效果”），自动保存，首屏绘制前应用（无闪烁）；十套主题的正文、弱化文字、强调色与荧光底全部通过 WCAG AA（contrast.py 0 失败）；地图、图表、标记颜色随主题变化（深色主题自动换深色底图）。',
'🖍️ 笔记标记 3.0：荧光笔改为“马克笔”斜切笔触；重点粗体加柔和下辉光；定义 = 实线、难点 = 波浪线、对比 = 虚线、经文 = 双下划线，线粗与间距重新调校；新增“着重号”（字下圆点，用于要义里最该背的关键词：;;词;;）；提示框加渐变底色与图标圆章。M 键开关、三层图例照常。',
'✒️ 中文排版：标点挤压（text-spacing-trim）、中西文自动间距（text-autospace）、标题均衡换行、段落避免孤字（text-wrap: pretty）、严格断行；正文行高 1.9、问答答句行长限制约 42 字；h4 加菱形引导符，标题层级更分明。',
'📊 新图表：52 主日总览页新增“核心词分布”堆叠条形图（22 个教义词在三大部分中的出现次数，按原文统计）；每个主日新增“🔑 关键词 × 问答”矩阵（每个关键词在本主日各问答中出现几次，圆点大小 = 次数）。',
'✂️ 内容提炼：解说与要义重复的句子判定门槛从 0.62 降到 0.55，主日页更紧凑；原文一字未动。',
'🔬 v9 收尾剖析（逐帧 trace）：① 预排版改为“排版一次后交还 content-visibility:auto”——布局结果保留，离屏时仍跳过绘制与分层（此前一直保持可见，长页面的 Layerize 变为 3–4 倍，移动端地图集只有 53–54 fps）；预排版在空闲期限内成批完成。② 移动端（lite）标题下划线改为静态，不再用 transform 过渡（移动端地图集 Layerize 540 → 80 ms）。③ 修正背景云层“滚动时暂停”的选择器优先级（v8 起实际上从未暂停）。结果：24 个“页面 × 设备”组合在 6× CPU 降速下全部 ≥ 58 fps（v8 同法测量：15 个低于 58，最低 42.9）。',
 '✅ 校验：原文逐字 0 差异；和合本经文 0 差异；十套主题 × 375 / 768 / 1024 / 1440 四个宽度无横向溢出；v8 Playwright 测试与目录测试通过。']
v8changes=['🗺️ 地图重做：去掉不稳定的 Leaflet / OSM CDN，改用站内自托管 MapLibre GL 4.7.1（assets/vendor，BSD-3）＋站内 Natural Earth 底图（assets/geo/base.json，公有领域）。在线瓦片按 Esri 街道图 → CARTO Voyager → OpenStreetMap 顺序并行探测、自动择优、出错自动切换；全部不可达时用站内主题底图（离线可用）；地图引擎或 WebGL 不可用时显示同一幅静态示意图，不会出现空白框。另有卫星图（Esri）与“主题底图”按钮。',
'🎨 每个地图都是“概念示意图 + 实时交互地图”成对出现：示意图（构建时由 Natural Earth 投影生成的 SVG）带渐变陆海、河流、路线描边动画、沿路线移动的光点、编号脉冲标记、指北针、比例尺、密集地区的放大镜插图，标签自动避让；实时地图与之联动（点击地点 / 路线 / ▶ 播放 / 时期筛选两边同步）。',
'🏰 新增“历史地图集”（maps.html）：1563 年普法尔茨、宗教改革的传播、两位作者的人生路线、尼德兰难民之路、多特大会代表 5 个专题，每个都有核心一句、为什么重要、站点卡、地点表、相关主日、文化背景；另有多特代表条形图、改革路线泳道图、专题卡片。',
'📖 新增“圣经地理”（geo-bible.html）：亚伯拉罕之路、出埃及、保罗的旅程 3 张地图，各配经文（已与和合本逐字比对）与要理问答对应问答；地点为传统位置。',
'🏛️ 历史页地图换成同一套成对地图（21 个地点、4 条路线、海德堡周边放大插图），“在地图上查看”与时期筛选同时作用于两张图；13 个主日新增“历史 · 地理”卡片（缩略示意图＋一句关联＋跳到地图）。',
'🧭 右下角导航簇：后退 / 前进 / 主页 / 上一主日 / 下一主日 / 到顶 / 到底 / 快捷键；桌面端竖排展开并为正文让出右侧空间（不遮挡正文），≤1024px 收成一个 🧭 按钮，点开后执行任一操作自动收起；向下滚动时淡化。快捷键 [ ] 后退前进 · H 主页 · G / Shift+G 顶部底部 · , . 上一下一主日 · N 展开收起 · ? 快捷键说明 · Esc 关闭。',
'🖍️ 笔记标记 2.0：新增第 ④ 史地层——人物（紫色粗体）、地点（青色点线）、年代（琥珀色胶囊），历史内容中自动标记（每段最多 3 处）；新增“要点底纹”块；新增 🏛️ 历史、🗺️ 地理两种提示框。新“笔记标记系统”页（marks.html）：12 种标记 × 4 层的图例表、示范段落、8 种提示框、全站各类标记数量图、三遍阅读法；图例每一行可点击“聚焦”（只突出这一种，其余淡化，Esc 取消）；桌面端悬停任一标记显示其含义。',
'🌈 配色更活泼：五套主题都加入陆地 / 海洋 / 河流 / 标记新色变量；卡片顶部渐变色条、标题图标渐变底；地图颜色随主题切换。',
'⚡ 流畅度：实时地图只在进入视野时加载（同时最多 3 个，超出自动释放）；示意图动画只在可见时播放一次；地图引擎与底图按需加载并由 Service Worker 缓存；CLS 保持 0。v7 → v8 性能与 Lighthouse 对比见 README。',
'✅ 校验：原文逐字 0 差异；经文引语与和合本 0 处不符（新增地图集与圣经地理页的引语）；全部页面 × 375 / 768 / 1024 / 1440 × 5 套主题无溢出；Playwright 测试：在线地图、瓦片全部被屏蔽、引擎被屏蔽、无 WebGL 四种情况，以及导航簇（桌面 / 手机）全部通过。']
v7changes=['⚡ 架构级流畅度：原文阅读版拆成 5 卷（每卷约 700–1100 个元素，原单页 3,724 个），旧链接 #q60 / #ld23 自动跳到对应分卷；另保留“全一页”版供打印与 Ctrl+F。',
'⚡ 跨页 View Transitions（原生淡入淡出，顶栏与侧栏保持不动）＋ Speculation Rules 悬停 / 触摸预取与预渲染（不支持的浏览器用 fetch / link prefetch 兜底）。',
'⚡ Service Worker：核心页面预缓存，同源资源 stale-while-revalidate，CDN 缓存优先；二次访问与离线都能秒开（离线回退首页）；?nosw 可关闭。',
'⚡ 关键 CSS 内联到每页（省一次阻塞请求）；目录在构建时生成（不再在加载后插入 → 消除布局偏移）；非关键初始化放进 requestIdleCallback。',
'⚡ 滚动时主线程零工作：滚动监听只设标志；目录高亮只做差异更新并在 scrollend 后执行；数字动画等到滚动停止；整段滚动 DOM 写入 ≤ 20 次。',
'⚡ 背景“浮云”改为单一合成层（1 个元素、2 个径向渐变），滚动中与标签页隐藏时暂停。',
'⚡ 零 CLS：主日页“连续朗读 / 标记已学完”按钮改为静态占位，ld/01 的 CLS 由 0.053 → 0。',
'💎 内容深化：52 个主日都新增“❓ 本主日回答的问题”“💡 为什么重要”“🏃 本周操练”，以及三环“🧬 圣约链：旧约应许 → 在基督里成全 → 今天的教会与我”（附经文）；10 个较薄的主日（9、17、37、39、41、42、43、47、49、50）新增“🔬 深化”。',
'📖 经文核对：本站学习笔记中带出处的 119 处经文引语，逐条与和合本（信望爱 FHL 线上和合本）比对并修正措辞（如“甚么”、赛64:6、太5:22、结36:23、太26:39 的出处等）；学习笔记中引用的要理问答语句也逐字对照原文改正。',
'📊 新可视化：圣经页“圣约链统计”（52 条链引用最多的旧约 / 新约书卷条形图 + 旧约 / 新约比例条）；52 主日总览新增“52 个问题 · 圣约链一览”表；圣约链节点依次淡入（只用 opacity / transform）。',
'🎨 配色细化：五套主题各有焦点环、文字选中色与滚动条颜色；对比度检查扩展到焦点环（≥3:1）与新组件，0 项不达 WCAG AA。',
'🖍️ 标记三态：全部 / ⭐ 仅核心（只留荧光核心词与经文药丸）/ 关；M 键循环；状态在首屏绘制前应用（无闪烁）；主日页原文区新增可展开的本页标记图例，并显示每种标记在本页出现的次数（构建时统计）。',
'🐞 修复：手机上“承上启下 / 问题推进”卡片被拉高到 200px 的空白；构建脚本任何一步失败即停止。',
'✅ 校验：原文逐字 0 差异；4 个宽度无溢出；Playwright 测试；v6 → v7 性能与 Lighthouse 对比见 README。']
v6changes=['⚡ 流畅度重做（针对“页面有些卡顿”）：几乎移除全部 backdrop-filter（仅桌面低 DPR 的顶栏保留，手机 / 高 DPI / 低配设备自动关闭）；移除大阴影、filter 动画与 SVG 内部过渡；背景只剩 2 个可合成图层，滚动中与标签页隐藏时暂停；滚动时不再做淡入；content-visibility 仅用在章节级。',
'⚡ 资源与 DOM：CSS / JS 压缩；人物图改为 webp（192 / 640 两档 + width/height）；Mermaid 流程图构建时预渲染为静态 SVG（不再加载 Mermaid 库）；速记中心 129 张卡片与 52 题小测分页渲染（每页 12 张 / 8 题，可按部分筛选、洗牌、跳转），DOM 从 2566 降到约 950 个元素。',
'🎨 五套配色主题：🌌 深夜星空 · 🌅 晨曦米白 · 🌲 翡翠森林 · 🍇 葡萄紫金 · 🌊 海洋蓝。顶栏 🎨 选择器（首页图例也有色板），自动保存，首屏绘制前应用（无闪烁）；所有图表、地图标记、流程图与标记颜色随主题变化；五套主题正文对比度均达 WCAG AA（实测 13.6–15.9:1）。',
'✂️ 内容提炼：主日页去掉与其他卡片重复的“八个视角罗盘”和“五问提要”；要义清单只出现一次（移到精华区，附数据卡）；易错提示合并为一处；解说中与要义重复的句子自动剔除；重复的提示语缩短。首页 52 主日一览改为紧凑格，对比页合并重复的“文体 / 历史”两条。字数：52 个主日解说 110,782 → 74,688（−32.6%）；概览页 24,716 → 21,416（−13.4%）；原文不计入，且一字未动。',
'🖍️ 笔记标记升级：三层图例（① 核心层：荧光底 + 粗体；② 重点层：金 / 绿 / 红色粗体 = 重点 / 恩典应许 / 警示；③ 语义线：实线 = 定义、波浪线 = 难点、虚线 = 对比 / 错误立场，外加经文药丸）；新增绿色“恩典 · 应许 · 安慰”标记；提示框左侧加粗色条与色块标签；五套主题下颜色统一由变量控制；M 键开关照常。',
'📊 新可视化：52 主日 × 信条交叉引用热力图（52 主日总览）、五个时期甘特图（历史页）、主日数据卡（问答数 / 经文组 / 信条对照 / 关键词），首页主题色板。',
'✅ 校验：原文逐字 0 差异（2094 段 + 53 条金句）；4 个宽度无溢出；Playwright 测试；6× CPU 降速 + 手机仿真滚动帧率与 Lighthouse 的 v5 → v6 对比见 README。']
lnk=lambda L:''.join(f'<li>{esc(t)}：<a href="{u}" target="_blank" rel="noopener">{u}</a></li>' for t,u in L)
ch=f'''<section class="hero reveal"><span class="chip g">🆕 版本记录</span><h1>更新记录 Changelog</h1><p class="lead">当前版本：<b class="key">{VERSION}</b> · {DATE}</p></section>'''
ch+=sec('v9','🚀','v9 · 2026-10-23',f'<div class="card pan core reveal"><ul class="clean">{"".join(f"<li>{esc(x)}</li>" for x in v9changes)}</ul><h3>🌐 v9 部署</h3><ul class="clean">{lnk(V9)}<li>Release：<a href="{REL}v9">{REL}v9</a></li></ul></div>')
ch+=sec('v8','📦','v8 · 2026-10-23',f'<div class="card pan why reveal"><ul class="clean">{"".join(f"<li>{esc(x)}</li>" for x in v8changes)}</ul><h3>🌐 v8 部署（保留）</h3><ul class="clean">{lnk(V8)}<li>Release：<a href="{REL}v8">{REL}v8</a></li></ul></div>')
ch+=sec('v7','📦','v7 · 2026-10-23',f'<div class="card pan why reveal"><ul class="clean">{"".join(f"<li>{esc(x)}</li>" for x in v7changes)}</ul><h3>🌐 v7 部署（保留）</h3><ul class="clean">{lnk(V7)}<li>Release：<a href="{REL}v7">{REL}v7</a></li></ul></div>')
ch+=sec('v6','📦','v6 · 2026-10-21',f'<div class="card pan why reveal"><ul class="clean">{"".join(f"<li>{esc(x)}</li>" for x in v6changes)}</ul><h3>🌐 v6 部署（保留）</h3><ul class="clean">{lnk(V6)}<li>Release：<a href="{REL}v6">{REL}v6</a></li></ul></div>')
ch+=sec('v5','📦','v5 · 2026-10-21',f'<div class="card pan why reveal"><ul class="clean">{"".join(f"<li>{esc(x)}</li>" for x in v5changes)}</ul><h3>🌐 v5 部署（保留）</h3><ul class="clean">{lnk(V5)}<li>Release：<a href="{REL}v5">{REL}v5</a></li></ul></div>')
ch+=sec('v4','📦','v4 · 2026-10-21',f'<div class="card pan why reveal"><ul class="clean">{"".join(f"<li>{esc(x)}</li>" for x in v4changes)}</ul><h3>🌐 v4 部署（保留）</h3><ul class="clean">{lnk(V4)}<li>Release：<a href="{REL}v4">{REL}v4</a></li></ul></div>')
ch+=sec('v3','📦','v3 · 2026-10-20',f'<div class="card pan why reveal"><ul class="clean">{"".join(f"<li>{esc(x)}</li>" for x in v3changes)}</ul><h3>🌐 v3 部署（保留）</h3><ul class="clean">{lnk(V3)}<li>Release：<a href="{REL}v3">{REL}v3</a></li></ul></div>')
ch+=sec('v2','📦','v2 · 2026-10-20',f'<div class="card pan why reveal"><ul class="clean">{"".join(f"<li>{esc(x)}</li>" for x in v2changes)}</ul><h3>🌐 v2 部署（保留）</h3><ul class="clean">{lnk(V2)}<li>Release：<a href="{REL}v2">{REL}v2</a></li></ul></div>')
ch+=sec('v1','📦','v1 · 2026-10-20',f'<div class="card pan why reveal"><ul class="clean"><li>首版：52 主日深度解析页、四部全文阅读/背诵版、圣经与圣约、历史地理（时间线、地图）、信条对比、速记中心、资料页。</li><li>全部原文由程序从 ccifellowship.org 抓取并逐字校验。</li></ul><h3>🌐 v1 部署（保留不动）</h3><ul class="clean">{lnk(V1)}<li>Release：<a href="{REL}v1">{REL}v1</a></li></ul></div>')
ch+=sec('repo','📂','源码',f'<div class="card reveal"><p><a href="https://github.com/07-Je-Grok-Love-Personal-20260928/{REPO}">github.com/07-Je-Grok-Love-Personal-20260928/{REPO}</a></p></div>')
page('changelog.html','更新记录',ch,'版本更新记录')
json.dump(dict(V9=V9,changes_v9=v9changes,V8=V8,changes_v8=v8changes,V1=V1,V2=V2,V3=V3,V4=V4,V5=V5,V6=V6,V7=V7,changes_v7=v7changes,changes_v6=v6changes,changes=v2changes,changes_v3=v3changes,changes_v4=v4changes,changes_v5=v5changes),open(ROOT+'/build/versions.json','w'),ensure_ascii=False,indent=1)
print('v3 pages done', len(idx))
