from common import *
import svgs
def ldgrid_groups():
    out=[]
    for k,pn,a,b,t in GROUPS:
        out.append(f'<div class="grp" style="--k:{min(b-a+1,6)}"><h3 id="grp{a}" data-toc="{part(a)[3]} {pn} · {t}（主日{a}{"–"+str(b) if b!=a else ""}）" style="color:{part(a)[2]}">{part(a)[3]} {pn} · {t}<span class="small muted">　主日 {a}{"–"+str(b) if b!=a else ""}</span></h3><div class="ldgrid">')
        for n in range(a,b+1):
            ld=D['hc'][n-1];p=part(n);qa,qb=qrange(ld)
            out.append(f'<a class="ld reveal" data-ld-card="{n}" data-p="{p[0]}" href="ld/{n:02d}.html" style="--c:{p[2]}"><div class="n">{LDI[n]} 主日 {n} · Q{qa}{"–"+str(qb) if qb!=qa else ""}</div><div class="t">{esc(N[n]["t"])}</div><div class="k">{esc(N[n]["k"])}</div><div class="rv" aria-hidden="true"><b>💎 论题</b><br>{esc(re.sub(r"[*=~_:!]{2}","",T[n][0]))}</div></a>')
        out.append('</div></div>')
    return '<div class="grps">'+''.join(out)+'</div>'
def ldgrid_mini(pre=''):
    out=['<div class="ldgrid mini">']
    for ld in D['hc']:
        n=ld['n'];p=part(n)
        out.append(f'<a class="ld" data-ld-card="{n}" data-p="{p[0]}" href="{pre}ld/{n:02d}.html" style="--c:{p[2]}" title="{esc(N[n]["k"])}"><span class="n">{LDI[n]} {n}</span><span class="t">{esc(N[n]["t"])}</span></a>')
    out.append('</div>'); return ''.join(out)
def xheat():
    """v6: cross-reference heatmap — 52 LDs x (questions, Belgic, Dort, WSC)."""
    rows=[('问答','--intro',lambda n,ld:len(ld['qas'])),('比利时','--deliv',lambda n,ld:len(N[n]['bc'])),('多特','--grat',lambda n,ld:len(N[n]['cd'])),('威斯敏斯特','--gold',lambda n,ld:len(N[n]['wsc']))]
    cw,ch,lx=13,20,76; W=lx+52*cw+4; H=len(rows)*(ch+4)+26
    o=[f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="52 主日交叉引用热力图" style="width:100%;min-width:640px;height:auto">']
    for r,(lab,var,f) in enumerate(rows):
        vals=[f(ld['n'],ld) for ld in D['hc']]; mx=max(vals) or 1; y=r*(ch+4)
        o.append(f'<text x="0" y="{y+14}" style="fill:var(--fg);font-size:12px">{lab}</text>')
        for i,(ld,v) in enumerate(zip(D['hc'],vals)):
            op=0.08 if v==0 else round(.25+.75*v/mx,2)
            o.append(f'<a href="ld/{ld["n"]:02d}.html"><rect x="{lx+i*cw}" y="{y}" width="{cw-2}" height="{ch}" rx="3" style="fill:var({var});opacity:{op}"><title>主日{ld["n"]} {esc(N[ld["n"]]["t"])}：{lab} {v}</title></rect></a>')
    yb=len(rows)*(ch+4)+14
    for i in range(0,52,4): o.append(f'<text x="{lx+i*cw}" y="{yb}" style="fill:var(--muted);font-size:10px">{i+1}</text>')
    o.append('</svg>'); return ''.join(o)
def ldgrid(pre=''):
    out=['<div class="ldgrid">']
    for ld in D['hc']:
        n=ld['n'];p=part(n);a,b=qrange(ld)
        out.append(f'<a class="ld reveal" data-ld-card="{n}" data-p="{p[0]}" href="{pre}ld/{n:02d}.html" style="--c:{p[2]}"><div class="n">{LDI[n]} 主日 {n} · Q{a}{"–"+str(b) if b!=a else ""}</div><div class="t">{esc(N[n]["t"])}</div><div class="k">{esc(N[n]["k"])}</div><div class="rv" aria-hidden="true"><b>💎 论题</b><br>{esc(re.sub(r"[*=~_:!]{2}","",T[n][0]))}</div></a>')
    out.append('</div>'); return ''.join(out)
# ---------------- INDEX
legend='<div class="tags" style="display:flex;flex-wrap:wrap;gap:8px"><span class="chip i">💜 引言（紫）</span><span class="chip m">💔 罪与愁苦（红）</span><span class="chip d">✝️ 得救（蓝）</span><span class="chip g">🌿 感恩（绿）</span><span class="chip" style="border-color:var(--hard)">⚠️ 难点（橙色斜纹）</span><span class="chip" style="border-color:var(--key)">🔑 重点（黄色高亮）</span></div>'
idx=f'''<section class="hero reveal"><div class="tags"><span class="chip i">🇩🇪 Heidelberg · 1563</span><span class="chip d">⛪ 欧陆改革宗 · 三项联合信条</span><span class="chip g">🧠 速记 · 背诵 · 测验</span></div>
<h1>《海德堡要理问答》<br>52 主日全景深度解析</h1>
<p class="lead">从<mark>整本圣经</mark>与<mark>圣约神学</mark>的高度俯瞰，再逐主日深入<mark>真实背景、逻辑、难点与应用</mark>。全部信条与信经原文<b class="key">一字不改</b>引自 ccifellowship.org《中国改革宗敬拜手册》，并与比利时信条、多特信经交叉对照。</p>
<div class="kpi"><div><b>52</b>主日</div><div><b>129</b>问答</div><div><b>37</b>比利时信条</div><div><b>4</b>多特信经·项</div><div><b>3</b>普世信经</div><div><b>57</b>篇延伸证道</div></div>
<div class="btns" style="margin-top:20px"><a class="btn pri" href="ld/01.html">🚀 从主日1开始</a><a class="btn" href="bible.html">🌍 先看整本圣经</a><a class="btn" href="history.html">🗺️ 历史与地图</a><a class="btn" href="memory.html">🧠 速记中心</a></div></section>'''
idx+=sec('legend','🎨','图例：颜色记忆法 + 笔记标记（全站统一）',f'''<div class="grid g2"><div class="card reveal"><h3 id="lg-color">🌈 四色 = 四部分</h3>{legend}<p style="margin-top:10px">一句话记住全书：<span class="mn" style="display:inline-block;padding:4px 12px;font-size:20px">1 安慰 → 3 罪 → 27 恩 → 21 谢</span></p><p class="small muted">主日数：引言 1 + 愁苦 3 + 得救 27 + 感恩 21 = 52；“得救”27 个主日 = 中保 2（5–6）+ 信心与使徒信经 16（7–22）+ 称义 2（23–24）+ 圣言·圣礼·钥匙 7（25–31）。</p></div>
<div class="card reveal"><h3 id="lg-marks">🖍️ 笔记标记</h3>{legend_html(False)}<p class="small muted" style="margin:8px 0 0">三层含义与示例见 <a href="memory.html#marks">速记中心 · 标记图例</a>。</p><h3 id="lg-theme" style="margin-top:14px">🎨 五套配色（自动保存）</h3><div class="thstrip">{theme_buttons()}</div></div></div>''')
idx+=sec('essence','💎','全书精华：一个论题 · 三个部分',f'''{callout('core','核心','《海德堡要理问答》的总论题是<span class="mk-k">“唯一的安慰”</span>：“或生或死，我的身体和灵魂都<span class="mk-b">不属于我自己</span>，而属于我信实的救主耶稣基督”（第1问）。全书按<span class="mk-u">罪（愁苦）→ 恩（得救）→ 谢（感恩）</span>展开，大致对应罗马书 1:18–3:20 / 3:21–11 章 / 12–16 章的次序。')}
{callout('gold','金句',f'“{esc(T[1][2])}”<span class="src">　—— 原文第1问（逐字）</span>')}
{callout('trap','易错','把“感恩”理解为<span class="mk-r">赚取救恩的条件</span>：第三部的好行为是<span class="mk-u">得救的果子</span>而非根据（参第86、91问）。')}
{callout('hook','记忆钩','三件事：<b>罪多大 → 怎得救 → 怎感谢</b>（第2问）——<b>镜子 · 救主 · 生活</b>。')}
<div class="grid" style="margin-top:14px;grid-template-columns:1fr"><div class="card reveal"><h3 id="ch-parts">📊 129 问的三部分比例</h3><div class="chart">{svgs.parts_stack()}</div><p class="small muted">得救部分占 57%：要理问答把最多篇幅放在“基督为我做了什么”。</p></div>
<div class="card reveal"><h3 id="ch-bars">📈 每个主日的问答数</h3><div class="chart mm"><div style="min-width:560px">{svgs.q_bars()}</div></div><p class="small muted">柱子可点击直达该主日；颜色＝所属部分。最长的是主日 16（第40–44问：受死、埋葬、下到阴间）共 5 问。</p></div></div>''')
idx+=sec('drama','🎭','整本圣经的四幕剧',f'<div class="card reveal mm">{svgs.drama()}</div><p class="muted small">要理问答不是零散的教义清单，而是把“创造—堕落—救赎—完成”的圣经大故事，转化为一个人“或生或死”的安慰。</p>')
idx+=sec('tri','🌈','三重结构：罪 · 恩 · 谢（对应罗马书）',f'<div class="card reveal mm">{svgs.tri()}</div>')
idx+=sec('mindmap','🧭','思维导图：52 主日的骨架（可点击）',f'<div class="card reveal mm" style="color:var(--fg)">{svgs.mindmap()}</div>')
idx+=sec('three','🏛️','三大支柱：信经 · 十诫 · 主祷文','''<div class="grid">
<div class="card pan why reveal lift"><h3>📜 使徒信经 → 信什么</h3><p>主日 7–22（第 23–58 问）：按三位一体分为父与创造、子与救赎、圣灵与成圣。</p></div>
<div class="card pan core reveal lift"><h3>⚖️ 十诫 → 怎样活</h3><p>主日 34–44（第 92–115 问）：律法的第三功用——蒙恩者感恩生活的准则。</p></div>
<div class="card pan cov reveal lift"><h3>🙏 主祷文 → 怎样求</h3><p>主日 45–52（第 116–129 问）：祷告是“感恩中最重要的一部分”（第116问）。</p></div></div>
<p class="muted small">此外，圣言与圣礼（主日 25–31）把“信”连于教会生活：讲道、洗礼、圣餐、天国钥匙。古代教会的教理问答传统即以“信经—十诫—主祷文”为三大纲，海德堡继承而以“安慰”统摄。</p>''')
idx+=sec('all52','📅','52 主日一览（颜色＝所属部分）',f'<p class="muted small">✅ 绿框＝已学完（存于本机）。悬停看口诀；论题与分组见 <a href="lorddays.html">52 主日总览</a>。</p>{ldgrid_mini()}')
idx+=sec('path','🛤️','建议学习路径','''<div class="grid g4">
<a class="card lift reveal" href="bible.html"><h3>① 🌍 整体</h3><p class="muted">圣经神学、圣约神学、多视角</p></a>
<a class="card lift reveal" href="history.html"><h3>② 🗺️ 背景</h3><p class="muted">时间线、故事线、地图、文化</p></a>
<a class="card lift reveal" href="lorddays.html"><h3>③ 🔍 逐主日</h3><p class="muted">原文、逻辑链、难点、应用</p></a>
<a class="card lift reveal" href="compare.html"><h3>④ ⚖️ 对比</h3><p class="muted">三项联合信条与三大信经</p></a>
<a class="card lift reveal" href="memory.html"><h3>⑤ 🧠 记忆</h3><p class="muted">口诀、129 张卡片、测验</p></a>
<a class="card lift reveal" href="texts/hc.html"><h3>⑥ 📜 背诵</h3><p class="muted">干净阅读版 + 背诵模式</p></a></div>''')
page('index.html','首页',idx,'海德堡要理问答52主日深度解析：圣经神学、圣约神学、历史地理、三项联合信条原文与对比')
# ---------------- BIBLE
bib=f'''<section class="hero reveal"><span class="chip i">🌍 跳出局部 · 先看整体</span><h1>整本圣经 × 圣约神学 × 多视角</h1><p class="lead">在进入 129 个问答之前，先站到救赎历史的山顶：要理问答的每一问，都是圣经大故事中的一个坐标。</p></section>'''
bib+=sec('story','📖','一、圣经的大故事（Biblical Theology）',f'''<div class="card reveal mm">{svgs.drama()}</div><div class="grid g2" style="margin-top:16px">
<div class="card pan big reveal"><h3>🌅 创造：神的国度与形像</h3><p>神从无中藉圣言创造万有，造人有他的形像（第6问），在乐园中与人相交。人被赋予“治理”的使命，以敬拜和顺服反映神的荣耀。<b class="key">要理问答：主日3、9、10。</b></p></div>
<div class="card pan err reveal"><h3>🍎 堕落：背约与咒诅</h3><p>亚当作为全人类的盟约元首背叛（第7问），罪责与败坏传给众人。律法如镜子照出这一现实（主日2）。神的公义必须对罪施行刑罚（主日4）。</p></div>
<div class="card pan why reveal"><h3>✝️ 救赎：从乐园的应许到十字架与五旬节</h3><p>第19问是全书最“圣经神学”的一问：福音“在乐园中首先启示”，藉族长、先知宣告，以献祭和律法仪式预表，最后在爱子身上成全。基督作为真神真人的中保（主日5–6），以先知、祭司、君王三职（主日12）完成救赎；圣灵把救恩施行出来（主日20–31）。</p></div>
<div class="card pan core reveal"><h3>👑 完成：复活、审判、永生</h3><p>基督再来审判（主日19）、身体复活与永生（主日22）、国度完全（第123问）。整本要理问答以“阿们”（第129问）作结——神的应许比我的感觉更确实。</p></div></div>''')
LAD='<div class="cov-mobile"><div class="tl"><div class="ev reveal" style="--c:var(--gold)"><div class="card" style="padding:12px 14px"><b style="color:var(--gold)">🔺 救赎之约</b><div class="small">三一神永恒的定旨：父拣选 · 子担保 · 圣灵施行</div></div></div><div class="ev reveal" style="--c:var(--intro)"><div class="card" style="padding:12px 14px"><b style="color:var(--intro)">🌳 创造中的约（行为之约/生命之约）</b><div class="small">亚当为全人类盟约元首，要求完全顺服</div></div></div><div class="ev reveal" style="--c:var(--misery)"><div class="card" style="padding:12px 14px"><b style="color:var(--misery)">💔 背约堕落（创3）</b><div class="small">罪与愁苦——HC 主日2–4</div></div></div><div class="ev reveal" style="--c:var(--deliv)"><div class="card" style="padding:12px 14px"><b style="color:var(--deliv)">✝️ 恩典之约（创3:15 女人的后裔）</b><div class="small">一约多施行，本质合一</div></div></div><div class="ev reveal" style="--c:var(--deliv)"><div class="card" style="padding:12px 14px"><b style="color:var(--deliv)">🌈 挪亚之约</b><div class="small">保守世界，为救赎历史预备舞台</div></div></div><div class="ev reveal" style="--c:var(--deliv)"><div class="card" style="padding:12px 14px"><b style="color:var(--deliv)">⭐ 亚伯拉罕之约</b><div class="small">“我要作你和你后裔的神”；割礼 → 洗礼（HC 第74问）</div></div></div><div class="ev reveal" style="--c:var(--deliv)"><div class="card" style="padding:12px 14px"><b style="color:var(--deliv)">⛰️ 西奈之约</b><div class="small">律法给蒙救赎的百姓（HC 主日34 序言）</div></div></div><div class="ev reveal" style="--c:var(--deliv)"><div class="card" style="padding:12px 14px"><b style="color:var(--deliv)">👑 大卫之约</b><div class="small">永远的君王与国度</div></div></div><div class="ev reveal" style="--c:var(--key)"><div class="card" style="padding:12px 14px"><b style="color:var(--key)">🩸 新约：基督——唯一中保</b><div class="small">HC 主日5–19</div></div></div><div class="ev reveal" style="--c:var(--deliv)"><div class="card" style="padding:12px 14px"><b style="color:var(--deliv)">🕊️ 圣灵施行</b><div class="small">信心 · 称义 · 圣礼 · 教会——HC 主日20–31</div></div></div><div class="ev reveal" style="--c:var(--grat)"><div class="card" style="padding:12px 14px"><b style="color:var(--grat)">🌿 盟约的回应</b><div class="small">感恩 · 十诫 · 祷告——HC 主日32–52</div></div></div><div class="ev reveal" style="--c:var(--gold)"><div class="card" style="padding:12px 14px"><b style="color:var(--gold)">🏙️ 新天新地</b><div class="small">“神的帐幕在人间”（启21:3）</div></div></div></div></div>'
cov='''<div class="mermaid">flowchart TD
P["🔺 救赎之约（三一神永恒的定旨）<br/>父拣选 · 子担保 · 圣灵施行"]:::g --> W["🌳 创造中的约（行为之约/生命之约）<br/>亚当为盟约元首 · 完全顺服"]:::i
W -->|"背约堕落 创3"| F["💔 罪与愁苦<br/>HC 主日2–4"]:::m
F -->|"创3:15 女人的后裔"| G["✝️ 恩典之约（一约多施行）"]:::d
G --> N1["🌈 挪亚之约：保守世界"]:::d
G --> A["⭐ 亚伯拉罕之约：我要作你和你后裔的神<br/>割礼 → 洗礼（HC 第74问）"]:::d
G --> M["⛰️ 西奈之约：律法为蒙救赎者的生活准则<br/>（HC 主日34序言）"]:::d
G --> Dv["👑 大卫之约：永远的君王"]:::d
A --> C
M --> C
Dv --> C["🩸 新约：基督——唯一中保<br/>HC 主日5–19"]:::y
C --> S["🕊️ 圣灵施行：信心·称义·圣礼·教会<br/>HC 主日20–31"]:::d
S --> T["🌿 盟约的回应：感恩·十诫·祷告<br/>HC 主日32–52"]:::gr
T --> E["🏙️ 新天新地：神的帐幕在人间 启21:3"]:::g
classDef g fill:#f59e0b33,stroke:#f59e0b
classDef i fill:#a78bfa33,stroke:#a78bfa
classDef m fill:#fb718533,stroke:#fb7185
classDef d fill:#60a5fa33,stroke:#60a5fa
classDef y fill:#facc1544,stroke:#facc15
classDef gr fill:#34d39933,stroke:#34d399
</div>'''
def acts_matrix():
    head='<tr><th>教义主题 ＼ 圣经大戏</th>'+''.join(f'<th class="ac-{k}">{i} {t}<br><span class="small muted">{sum(1 for n in range(1,53) if ld_act(n)==k)} 个主日</span></th>' for k,i,t in ACTS)+'</tr>'
    rows=''
    for a,b,t in LOCI:
        rows+=f'<tr><th>{t}<br><span class="small muted">主日{a}{"–"+str(b) if b!=a else ""}</span></th>'
        for k,_,_ in ACTS:
            cs=''.join(f'<a class="chip {part(n)[0]}" href="ld/{n:02d}.html" title="{esc(ld_label(n))}">{LDI[n]} {n}</a>' for n in range(a,b+1) if ld_act(n)==k)
            rows+=f'<td class="{"has" if cs else ""}">{cs}</td>'
        rows+='</tr>'
    return f'<div class="tbl actm reveal"><table><thead>{head}</thead><tbody>{rows}</tbody></table></div><p class="small muted">每个主日按其主要重心归入一幕（学习分类，并非唯一的划分）：例如主日19（再来审判）与主日22（复活永生）指向“完成”，主日9–10（创造与护理）属于“创造”，第三部感恩（32–52）是蒙恩者的“回应”。点击芯片即进入该主日；同样的映射也出现在每个主日页的“六级缩放”中。</p>'
bib+=sec('acts','🧩','52 主日 × 圣经大戏：教义主题矩阵',acts_matrix())
bib+=sec('covenant','🤝','二、圣约神学（Covenant Theology）','<div class="cov-desktop">'+cov+'</div>'+LAD+f'''<div class="grid g2" style="margin-top:16px">
<div class="card pan cov reveal"><h3>📌 海德堡要理问答本身的“盟约”语言</h3><ul class="clean"><li>第74问：婴孩“与父母同属于神的圣约和教会”——“割礼已被洗礼所取代”。</li><li>第82问：不信者领圣餐是“亵渎神的圣约”。</li><li>第103问：安息日聚会“与会众一同求告与我们立约的神”。</li><li>主日1 的“属于”（belonging）本身就是盟约关系的语言。</li></ul><p class="small muted">（引语出自本站所引 ccifellowship.org 原文。）</p></div>
<div class="card pan why reveal"><h3>🧑‍🏫 历史：乌尔西努与俄利维亚努是盟约神学的先驱</h3><p>乌尔西努在为海德堡做准备的《大要理问答》（Catechesis maior，1562）中已用“自然之约/创造之约”与“恩典之约”的框架；俄利维亚努后来著《论神与选民之间恩典之约的本质》（De substantia foederis gratuiti, 1585）。因此，海德堡虽然没有系统展开盟约教义，却是在盟约神学的土壤中写成的。</p></div>
<div class="card pan hard reveal"><h3>⚠️ 欧陆改革宗内部的细微差异（难点）</h3><p>威斯敏斯特信仰告白第7章明言“行为之约”（WSC第12问称“生命之约”）。欧陆改革宗各宗派在用语上有差别：一些加拿大改革宗（CanRC）神学家偏好“创造之约/恩宠之约”的说法；美国更正改革宗（PRCA）强调盟约是神与选民之间的“团契关系”，不以“条件”视之；URCNA 等则多接受“行为之约—恩典之约”的传统表述。三者都承认：亚当是全人类的元首、救恩唯独出于恩典、基督是恩典之约唯一的中保。</p></div>
<div class="card reveal"><h3>🏴 威斯敏斯特对照（英文原文，opc.org）</h3><blockquote lang="en" class="small" style="border-left:3px solid var(--gold);padding-left:10px">{esc(WSC_EN[12])}</blockquote><blockquote lang="en" class="small" style="border-left:3px solid var(--gold);padding-left:10px">{esc(WSC_EN[20])}</blockquote><p class="small muted">来源：<a href="https://opc.org/sc.html" target="_blank" rel="noopener">The Orthodox Presbyterian Church · Shorter Catechism</a></p></div></div>''')
angles=[('🏛️','历史视角','1563 年普法尔茨的政治与信仰处境：在路德宗、罗马教与改革宗之间寻求圣经的合一。','history.html'),
('🧱','系统神学视角','神论、人论、基督论、救恩论、教会论、圣礼论、末世论、伦理学——全部在 129 问中出现。','compare.html#matrix'),
('📖','圣经神学视角','从乐园到新天新地的救赎历史线（第19问）。','#story'),
('🤝','圣约神学视角','神与他百姓之间的盟约关系：应许、记号、要求、福分。','#covenant'),
('💗','教牧/经验视角','以“安慰”为钥匙：教义是为了使人“或生或死”都得安慰（第1问）。','ld/01.html'),
('⛪','礼仪/敬拜视角','52 主日的划分本是为下午崇拜讲道；圣礼与主祷文直接塑造敬拜。','ld/25.html'),
('🛡️','护教/论辩视角','面对罗马教（第80问）、重洗派（第74问）、路德宗（第47–48问）、反三一论者（主日8）。','compare.html'),
('🏫','教育视角','“用于教导年轻人，也为牧师和教师提供教义指南”——教会、家庭、学校三位一体的盟约教育。','memory.html')]
bib+=sec('angles','🔭','三、八个视角看同一部要理问答','<div class="grid">'+''.join(f'<a class="card lift reveal" href="{h}"><h3>{i} {t}</h3><p class="muted">{esc(d)}</p></a>' for i,t,d,h in angles)+'</div>')
bib+=sec('core','💎','四、本质核心：一句话、三件事、一位基督','''<div class="card reveal"><p class="mn">“我的身体和灵魂都不属于我自己，而属于我信实的救主耶稣基督。”（第1问）</p><ol class="core"><li><b>罪</b>：我必须知道我的罪恶和愁苦有多么深重（第2问）。</li><li><b>恩</b>：我怎样才能得救，并脱离这一切的罪恶和愁苦——唯独藉着真心信靠耶稣基督（第60问）。</li><li><b>谢</b>：我当如何为这样的拯救而感谢神——以真归正、遵行十诫、恒切祷告。</li></ol><p>全书的中心不是一个概念，而是一位位格：<span class="key">耶稣基督，真神真人，唯一的中保</span>。要理问答的“安慰”是客观的（基督已成就）、个人的（“我”）、群体的（“我们的父”）、末世的（“阿们”）。</p></div>''')
page('bible.html','圣经神学与圣约神学',bib,'从整本圣经与圣约神学看海德堡要理问答')
# ---------------- LORDDAYS
lds=f'''<section class="hero reveal"><span class="chip">📅 52 主日 · 129 问</span><h1>52 主日总览</h1><p class="lead">已学完 <b id="progressCount" class="key">0</b> / 52</p><div style="height:10px;border-radius:10px;background:var(--card2);overflow:hidden"><div id="progressBar" style="height:100%;width:100%;transform:scaleX(0);transform-origin:0 50%;background:linear-gradient(90deg,var(--intro),var(--deliv),var(--grat));transition:transform 1s"></div></div>
<div class="btns" style="margin-top:14px"><button class="btn pri" data-part="all">全部</button><button class="btn" data-part="i">💜 引言</button><button class="btn" data-part="m">💔 愁苦</button><button class="btn" data-part="d">✝️ 得救</button><button class="btn" data-part="g">🌿 感恩</button></div>
<input id="ldFilter" class="tocsearch" style="margin-top:12px;font-size:16px" placeholder="🔍 输入关键词或主日编号（如：圣餐、称义、12）"></section>'''
lds+=sec('grid','🗂️','全部主日（按 17 个主题分组）',ldgrid_groups())
rows=''.join(f'<tr><td><a href="ld/{ld["n"]:02d}.html">{LDI[ld["n"]]} 主日{ld["n"]}</a></td><td>Q{qrange(ld)[0]}–{qrange(ld)[1]}</td><td><span class="chip {part(ld["n"])[0]}">{part(ld["n"])[1]}</span></td><td>{esc(" › ".join(ld["crumbs"][1:]) or "—")}</td><td>{"、".join(str(x) for x in N[ld["n"]]["bc"]) or "—"}</td><td>{len(N[ld["n"]]["cd"]) or "—"}</td><td>{"、".join(str(x) for x in N[ld["n"]]["wsc"]) or "—"}</td></tr>' for ld in D['hc'])
lds+=sec('heat','🔥','交叉引用热力图：哪些主日与其他信条联系最密',f'<div class="card reveal"><div class="chart mm">{xheat()}</div><p class="small muted" style="margin:6px 0 0">颜色越深＝本站为该主日列出的对照越多（比利时信条条数 / 多特信经段落 / 威斯敏斯特问数）；点击格子进入主日。</p></div>')
lds+=sec('table','📊','总表：结构与信条对照',f'<div class="tbl"><table><thead><tr><th>主日</th><th>问答</th><th>部分</th><th>子目</th><th>比利时信条</th><th>多特</th><th>WSC</th></tr></thead><tbody>{rows}</tbody></table></div>')
page('lorddays.html','52主日总览',lds,'海德堡要理问答52主日总览')
print('pages part1 done')
