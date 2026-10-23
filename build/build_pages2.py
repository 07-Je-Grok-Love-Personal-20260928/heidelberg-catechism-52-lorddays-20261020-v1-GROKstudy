from common import *
import svgs
# ---------------- COMPARE
cmp_rows=[('📅 年代','1563','1561（多特大会 1619 年修订确认）','1618–1619'),
('📍 地点','德国 · 海德堡（选帝侯普法尔茨）','南尼德兰（今比利时）· 图尔奈一带','荷兰共和国 · 多德雷赫特'),
('✍️ 作者','乌尔西努为主，俄利维亚努与海德堡神学教师协作；腓德烈三世委托','德布利（Guido de Brès），殉道者','国际性大会（荷兰及外国改革宗教会代表）'),
('📚 文体','要理问答（问答体，第一人称“我”）','信仰告白（条文体，“我们相信”）','教会法规性决议（正面条文 + 错谬反驳）'),
('👥 读者','年轻人、家庭、学校、牧师讲道','逼迫者（腓利二世）与政府、世人','教会的牧者与神学家'),
('🎯 目的','教导与安慰；促进普法尔茨的信仰合一','护教：证明改革宗是守法的、合乎圣经的真基督教','裁决阿米念主义争论，维护恩典教义'),
('🧱 结构','引言 + 愁苦 / 拯救 / 感恩 · 52主日 129问','37 条：神 → 圣经 → 三一 → 创造 → 罪 → 基督 → 救恩 → 教会 → 圣礼 → 政府 → 末世','五项（四部分）教义：拣选、救赎、败坏与归正、坚忍'),
('🎨 语气','温暖、教牧、个人、敬拜性','庄重、宣告性、殉道者的勇气','精确、论辩、教牧（如第一项第14条“如何教导拣选”）'),
('⚔️ 主要对手','罗马教（弥撒）、重洗派（婴儿洗）、路德宗（基督论/圣餐）','罗马教、重洗派、古代异端','抗辩派（阿米念主义）、伯拉纠主义'),
('💎 核心钥匙','安慰：我属于基督','真教会：圣经·三一·基督·教会的标记','恩典：救恩全然出于神的主权恩典'),
('🔗 与普世信经','主日7–22 逐句讲解使徒信经','第9条明确接受三大信经','以三一神的恩典作为前提，不另立信经')]
ct='<div class="tbl"><table><thead><tr><th>维度</th><th>📜 海德堡要理问答</th><th>🛡️ 比利时信条</th><th>🌷 多特信经</th></tr></thead><tbody>'+''.join(f'<tr><td><b>{a}</b></td><td>{esc(b)}</td><td>{esc(c)}</td><td>{esc(d)}</td></tr>' for a,b,c,d in cmp_rows)+'</tbody></table></div>'
matrix=[('圣经与启示','主日6（第19问）、主日25','第2–7条','—','WCF 1'),('三位一体','主日8','第8–11条','—','WSC 6'),('创造与护理','主日9–10','第12–13条','第一项第6条','WSC 9–11'),('人与罪','主日2–4','第14–15条','第三、四项第1–4条','WSC 13–19'),('拣选','（第54问“蒙选”）','第16条','第一项全部','WCF 3'),('基督的位格','主日5–6、13–14','第18–19条','第二项第4条','WSC 21–22'),('基督的工作/代赎','主日11–19','第20–21条','第二项全部','WSC 23–28'),('信心与称义','主日7、23–24','第22–24条','第三、四项第14条','WSC 33、86'),('归正/成圣','主日32–33','第24条','第三、四项第11–12条','WSC 35、87'),('坚忍与确据','主日1、52','（第24条）','第五项全部','WCF 17–18'),('教会','主日21、31','第27–32条','（第一项第7条：蒙拣选者）','WCF 25'),('圣礼','主日25–30','第33–35条','—','WSC 91–97'),('律法与伦理','主日34–44','第25条','第三、四项第5条','WSC 39–82'),('政府','（第104问）','第36条','—','WCF 23'),('末世','主日19、22','第37条','—','WSC 37–38')]
mt='<div class="tbl"><table><thead><tr><th>教义主题</th><th>海德堡要理问答</th><th>比利时信条</th><th>多特信经</th><th>威斯敏斯特参照</th></tr></thead><tbody>'+''.join(f'<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td><td>{d}</td><td class="muted">{e}</td></tr>' for a,b,c,d,e in matrix)+'</tbody></table></div>'
creed_rows=[('📅 年代','约公元 400 年定型（源头更早）','325 尼西亚 / 381 君士坦丁堡','约 6 世纪上半叶'),('🌍 地区','西方（罗马）教会','东西方教会共同（西方加“和子”）','西方教会'),('🎯 问题','简要总结使徒的教导，用于洗礼认信','驳斥亚流主义：子“与父同质”，扩充圣灵论','精确表述三位一体与基督神人二性'),('🧱 结构','三段：父、子、圣灵 + 教会与末世','三段：父、子、圣灵 + 教会','两部分：三一论（第3–28点）、基督论（第29–43点）'),('💎 关键词','我信……','受生却非被造，与父同质','一体三位，三位一体；其位格不紊，其本质不分'),('🔗 在海德堡中','主日7–22 逐句讲解（第23问全文引用）','主日8、13（独生子）、20（圣灵）','主日8（三一）、主日6、14、18（二性）')]
crt='<div class="tbl"><table><thead><tr><th>维度</th><th>🕊️ 使徒信经</th><th>🔥 尼西亚信经</th><th>👑 亚他那修信经</th></tr></thead><tbody>'+''.join(f'<tr><td><b>{a}</b></td><td>{esc(b)}</td><td>{esc(c)}</td><td>{esc(d)}</td></tr>' for a,b,c,d in creed_rows)+'</tbody></table></div>'
cp=f'''<section class="hero reveal"><span class="chip">⚖️ 深度对比</span><h1>三项联合信条 · 三大普世信经</h1><p class="lead">同一信仰，三种声音：<mark>要理问答教导心</mark>，<mark>信条宣告真理</mark>，<mark>信经守护恩典</mark>。</p></section>'''
COV=[('圣经与启示',2,6,0),('三位一体',1,4,0),('创造与护理',2,2,1),('人与罪',3,2,4),('拣选',.5,1,18),('基督的位格',4,2,1),('基督的工作/代赎',9,2,9),('信心与称义',3,3,1),('归正/成圣',2,1,2),('坚忍与确据',2,1,15),('教会',2,6,1),('圣礼',6,3,0),('律法与伦理',11,1,1),('政府',.5,1,0),('末世',2,1,0)]
def covchart():
    mx=18; out=['<div class="card reveal covc"><div class="legend" style="margin-bottom:10px"><span class="it"><i style="width:14px;height:8px;border-radius:4px;background:var(--deliv);display:inline-block"></i>海德堡（主日数）</span><span class="it"><i style="width:14px;height:8px;border-radius:4px;background:var(--intro);display:inline-block"></i>比利时信条（条数）</span><span class="it"><i style="width:14px;height:8px;border-radius:4px;background:var(--grat);display:inline-block"></i>多特信经（正面条文数）</span></div>']
    for t,h,b,c in COV:
        bars=''.join(f'<div style="display:flex;align-items:center;gap:6px;height:12px"><span class="barx" style="display:block;height:9px;border-radius:5px;width:{max(v/mx*86,0.8):.1f}%;background:{col};transition-delay:{i*80}ms"></span><span class="small muted" style="font-size:11px;line-height:1">{("≈" if v==.5 else "")+(str(int(v)) if v>=1 else ("½" if v else "0"))}</span></div>' for i,(v,col) in enumerate([(h,'var(--deliv)'),(b,'var(--intro)'),(c,'var(--grat)')]))
        out.append(f'<div style="display:grid;grid-template-columns:minmax(80px,8em) 1fr;gap:10px;align-items:center;padding:6px 0;border-bottom:1px dashed var(--bd)"><b class="small">{t}</b><div>{bars}</div></div>')
    out.append('<p class="small muted" style="margin:8px 0 0">数据依据下方“教义主题对照矩阵”统计（½ = 仅在个别问答中提及）。一眼可见：<span class="mk-k">海德堡</span>重在基督的工作与感恩生活，<span class="mk-k">比利时信条</span>重在圣经、三一与教会，<span class="mk-k">多特信经</span>集中火力于拣选与坚忍——三者互补而非重复。</p></div>')
    return ''.join(out)
cp+=sec('table','📊','一、三项联合信条总对比',ct)
cp+=sec('coverage','📈','覆盖度图：同一教义，三份文件各用多少篇幅',covchart())
cp+=sec('bcgroups','🍩','比利时信条 37 条的 12 个主题（点击扇区跳到原文）',f'<div class="grid g2"><div class="card reveal"><div class="chart" style="max-width:340px;margin:auto">{svgs.bc_donut()}</div></div><div class="card reveal"><ul class="clean">'+''.join(f'<li>{ic} <a href="texts/bc.html#g{s_}">{t}</a>：第{s_}{"–"+str(e_) if e_!=s_ else ""}条（{e_-s_+1} 条）</li>' for s_,e_,t,ic in BCG)+'</ul><p class="small muted">分组为本站学习用划分；条文标题与正文见原文中心。</p></div></div>')
cp+=sec('why3','❓','二、为什么需要三份，而不是一份？','''<div class="grid g2">
<div class="card pan core reveal"><h3>① 三个处境，三种文体</h3><p>问答体用第一人称安慰与教导（海德堡）；公开告白向君王申明信仰（比利时信条）；会议裁决处理改革宗内部的抗辩派争论（多特信经）。处境细节见下一节。</p></div>
<div class="card pan cov reveal"><h3>② 互相补充，形成完整的教义版图</h3><p>海德堡对拣选几乎只在第54问点到；比利时信条第16条简要陈述；多特信经则用整整一项展开。反之，多特信经不讨论圣礼与政府，这些由比利时信条与海德堡承担。三者合起来覆盖了从神论到末世论的全部主题。</p></div>
<div class="card pan big reveal"><h3>③ “联合”的意义：跨地域、跨语言的合一</h3><p>一部来自德国、一部来自南尼德兰、一部由国际大会制定，被荷兰改革宗教会共同签署，成为“联合”信条——表明改革宗信仰不是某地的私见，而是大公教会的圣经信仰。</p></div>
<div class="card pan hard reveal"><h3>⚠️ 难点：它们有没有矛盾？</h3><p>没有。多特大会正是以比利时信条与海德堡为准绳审查抗辩派，并确认二者。多特信经并没有增加新教义，而是把前两份已有的恩典教义（如第1、21、54问、比利时信条第14–16条）展开、捍卫。</p></div>
<div class="card pan app reveal"><h3>🌱 应用：怎样一起读？</h3><p>先读海德堡（心）→ 再读比利时信条（骨架）→ 再读多特信经（防线）。每个主日页面都附有交叉对照，方便“一问一条一项”联读。</p></div></div>''')
from compare_v5 import problems, venn, remon
cp+=sec('problems','🧯','三个处境 → 三份文件：各自要解决什么问题',problems())
cp+=sec('venn','⭕','维恩图：独有重点与共同核心（点击区域跳到原文）','<div class="card reveal" style="max-width:640px;margin:auto">'+venn()+'</div>')
cp+=sec('remon','🌪️','抗辩派五条 vs 多特 vs 海德堡 vs 比利时',remon())
cp+=sec('same','🔁','三、相同点与不同点','''<div class="grid g2"><div class="card pan core reveal"><h3>✅ 相同点</h3><ul class="clean"><li>唯独圣经为最高权威（比利时信条第7条）。</li><li>接受三大普世信经（比利时信条第9条；海德堡第23问引用使徒信经）。</li><li>全然败坏、唯独恩典、唯独基督、唯独信心。</li><li>以安慰与确据为教牧目标（海德堡第1问；多特信经第五项）。</li><li>与圣经引证紧密结合（每条附经文）。</li></ul></div>
<div class="card pan err reveal"><h3>↔️ 不同点</h3><ul class="clean"><li>人称：“我”（HC）／“我们”（BC）／会议宣告（CD）。</li><li>范围：HC 与 BC 是全面的；CD 是针对五点的专题性文件。</li><li>语气：HC 温和教牧；BC 庄严护教；CD 精确论辩。</li><li>形式：CD 独有“错谬反驳”部分。</li><li>用途：HC 用于主日讲道与教理班；BC 用于公开认信；CD 用于教义裁定与圣职签署。</li></ul></div></div>''')
cp+=sec('flow','🧩','四、三份信条如何互相支撑（流程图）','''<div class="mermaid">flowchart TB
S["📖 唯独圣经"] --> E["⛪ 三大普世信经<br/>三一论与基督论的大公根基"]
E --> BC["🛡️ 比利时信条 1561<br/>我们相信：完整的教义骨架"]
E --> HC["📜 海德堡要理问答 1563<br/>我的安慰：教导与敬拜"]
BC --> CD["🌷 多特信经 1619<br/>捍卫恩典：拣选·救赎·归正·坚忍"]
HC --> CD
CD --> U["⭐ 三项联合信条<br/>圣职签署 · 教会合一"]
BC --> U
HC --> U
</div>''')
cp+=sec('matrix','🗺️','五、教义主题对照矩阵',mt)
cp+=sec('creeds','⛪','六、三大普世信经对比',crt+'''<div class="grid g2" style="margin-top:16px"><div class="card pan why reveal"><h3>❓ 为什么需要三份信经？</h3><p><b>使徒信经</b>给出最简洁的“信仰骨架”，便于洗礼认信与背诵；<b>尼西亚信经</b>在亚流争论中精确界定子与圣灵的神性（“与父同质”）；<b>亚他那修信经</b>进一步用精细的语言同时防守三一论与基督论两条战线（防形态论、三神论、聂斯脱利、欧迪奇）。三份信经是同一信仰面对逐步加深的异端时的逐步澄清。</p></div>
<div class="card pan cov reveal"><h3>🔗 与三项联合信条的关系</h3><p>比利时信条第9条称这三大信经为“我们甘愿接受”的信经（见 ccifellowship.org 普世信经简介）。海德堡要理问答以使徒信经为第二部的主干。欧陆改革宗并不另创三一论，而是站在大公教会的肩膀上。</p></div></div><p><a class="btn pri" href="texts/creeds.html">📖 阅读三大信经原文</a></p>''')
page('compare.html','三项联合信条与普世信经对比',cp,'三项联合信条深度对比：为什么三份而不是一份')
# ---------------- MEMORY
deck=[]
for ld in D['hc']:
    c=part(ld['n'])[2]
    for q in ld['qas']:
        deck.append(f'<div class="fc" data-p="{part(ld["n"])[0]}" data-q="{qnum(q)}" style="--c:{c}"><div class="in"><div class="f"><div class="small muted">{LDI[ld["n"]]} 主日{ld["n"]} · {esc(N[ld["n"]]["t"])}</div><div class="big">Q{qnum(q)}</div><div>{esc(re.sub(r"^\d+[．.]\s*问：","",q["q"]))}</div></div><div class="b">{"".join(f"<p>{x}</p>" for x in q["a"])}</div></div></div>')
quiz=''.join(f'<div class="card quiz" data-p="{part(n)[0]}" data-q="{n}" data-ans="{N[n]["quiz"][2]}" data-id="ld{n}"><div class="small muted">{esc(ld_label(n))}</div><p><b>{esc(N[n]["quiz"][0])}</b></p>{"".join(f"<button class=\"opt\">{"ABCD"[i]}. {esc(o)}</button>" for i,o in enumerate(N[n]["quiz"][1]))}<p class="res key"></p></div>' for n in range(1,53))
mrows=''.join(f'<tr><td style="color:{part(n)[2]};font-weight:800">{n}</td><td>{LDI[n]} {esc(N[n]["t"])}</td><td class="key">{esc(N[n]["k"])}</td><td>{"、".join(esc(k) for k in N[n]["kw"])}</td></tr>' for n in range(1,53))
mem=f'''<section class="hero reveal"><span class="chip g">🧠 速记中心</span><h1>快速记住 52 主日</h1><p class="lead">口诀 → 结构 → 卡片 → 测验 → 背诵：五步法。快捷键：<b>T</b> 目录 · <b>R</b> 背诵模式 · <b>←/→</b> 上一/下一主日。</p></section>'''
GD=json.dumps([[re.sub(r'^\d+[．.]\s*问：','',q['q']),ld['n']] for ld in D['hc'] for q in ld['qas']],ensure_ascii=False)
GL=json.dumps([ld_label(n) for n in range(1,53)],ensure_ascii=False)
ring='<svg id="ring" viewBox="0 0 120 120" width="150" height="150"><circle cx="60" cy="60" r="52" fill="none" stroke="currentColor" stroke-opacity=".12" stroke-width="12"/><circle class="arc" cx="60" cy="60" r="52" fill="none" stroke="url(#rg)" stroke-width="12" stroke-linecap="round" stroke-dasharray="327" stroke-dashoffset="327"/><defs><linearGradient id="rg"><stop offset="0" stop-color="#a78bfa"/><stop offset="1" stop-color="#34d399"/></linearGradient></defs><text class="rk" x="60" y="62" text-anchor="middle" font-size="30" font-weight="900" fill="currentColor">0</text><text x="60" y="82" text-anchor="middle" font-size="11" fill="currentColor" opacity=".7">/ 52 已学完</text></svg>'
pbars=''.join(f'<div class="pbar" data-pbar="{s_}-{e_}"><span class="small">{ic} {a} {b}</span><span class="t"><span class="barx" style="background:{part(s_)[2]}"></span></span><span class="pc small muted">0</span></div>' for k,ic,a,b,s_,e_ in PARTS)
mem+=sec('progress','📈','我的学习进度（保存在本机）',f'<div class="card reveal"><div class="ringw">{ring}<div style="flex:1;min-width:220px">{pbars}<p class="small muted">在每个主日页面点“☑️ 标记已学完”即可累计。</p></div></div></div>')
mem+=sec('game','🎲','归属挑战：这一问属于哪个主日？',f'<div class="card reveal" id="ldgame"><p class="gstat small muted"></p><p class="gq"></p><div class="gopts quiz"></div><script type="application/json" id="ldgame-data">{GD}</script><script type="application/json" id="ldgame-labels">{GL}</script></div>')
mem+=sec('marks','🖍️','标记图例：读懂本站的颜色与线条',f'<div class="card reveal">{legend_html(True)}</div>')
mem+=sec('frame','🏗️','第一步：记住骨架（数字记忆）','''<div class="grid g4"><div class="card reveal" style="border-top:4px solid var(--intro)"><h3>💜 1</h3><p>引言：主日 1（Q1–2）安慰与三件事</p></div><div class="card reveal" style="border-top:4px solid var(--misery)"><h3>💔 2–4</h3><p>罪与愁苦：律法 → 堕落 → 公义（Q3–11）</p></div><div class="card reveal" style="border-top:4px solid var(--deliv)"><h3>✝️ 5–31</h3><p>得救：中保 5–6 · 信心 7 · 信经 8–22 · 称义 23–24 · 圣言圣礼 25–30 · 钥匙 31（Q12–85）</p></div><div class="card reveal" style="border-top:4px solid var(--grat)"><h3>🌿 32–52</h3><p>感恩：归正 32–33 · 十诫 34–44 · 主祷文 45–52（Q86–129）</p></div></div>
<div class="card reveal" style="margin-top:14px"><p class="mn">🔢 “1·3·27·21”：一安慰、三愁苦、廿七得救、廿一感恩。</p><p class="mn">🔢 信经 8–22 的“三一三段”：父 9–10 · 子 11–19 · 灵 20–22。</p><p class="mn">🔢 十诫 34–44：每主日约一诫（第3诫加“起誓”主日37，第10诫加律法功用）。</p><p class="mn">🔢 主祷文 45–52：45 总论 · 46 称呼 · 47–52 六个祈求（52 含结语与阿们）。</p></div>''')
mem+=sec('mnemonics','🔑','第二步：52 条口诀表',f'<div class="tbl"><table><thead><tr><th>主日</th><th>主题</th><th>口诀</th><th>关键词</th></tr></thead><tbody>{mrows}</tbody></table></div>')
mem+=sec('cards','🃏','第三步：129 张问答卡片（原文）',f'<div class="paged" data-size="12" data-parts="1" data-shuffle="1" data-jump="1" data-unit="问"><div class="pgctl btns"></div><div class="grid pg-out" id="deck"></div><template>{"".join(deck)}</template></div><p class="small muted">每页 12 张（只渲染当前页，页面更轻快）；可按四部分筛选、随机打乱或输入问号直接跳转。</p>')
mem+=sec('quiz','🎯','第四步：52 题小测验',f'<div class="paged" data-size="8" data-parts="1" data-jump="1" data-unit="主日"><div class="pgctl btns"></div><div class="grid pg-out"></div><template>{quiz}</template></div>')
mem+=sec('recite','🎙️','第五步：背诵与朗读','<div class="card reveal"><p>打开 <a href="texts/hc.html">📜 要理问答全文</a>，点击“背诵模式”遮住答案，逐问回忆后点击答案核对；🔊 按钮可调用浏览器中文语音朗读。<br>建议节奏：<b class="key">每周一个主日</b>（与教会下午崇拜同步），一年一轮；每天复习前一主日的卡片 3 分钟。</p></div>')
page('memory.html','速记中心',mem,'海德堡要理问答记忆法、卡片、测验')
# ---------------- SOURCES
cred=json.load(open(os.path.join(SITE,'assets/img/credits.json')))
cr=''.join(f'<li><b>{k}</b> — <a href="{v["page"]}" target="_blank" rel="noopener">{esc(v["title"])}</a> · {esc(v["license"] or "")} {re.sub("<[^>]+>","",v["artist"] or "")[:80]}</li>' for k,v in cred.items())
links=[('基督教华人网络团契 ccifellowship.org（本站全部信条/信经原文来源）','https://ccifellowship.org/books/book-of-praise'),('信望爱 FHL 线上圣经 · 和合本（v7 经文引语核对）','https://bible.fhl.net/'),('ccifellowship.org · 要理问答证道（Clarence Stam）','https://ccifellowship.org/sermons/heidelberg-catechism'),('洛杉矶改革宗·恩约教会','https://www.ccreformed.org'),('改革宗初学者','https://www.reformedbeginner.net'),('Canadian Reformed Churches','https://canrc.org'),('United Reformed Churches in North America','https://www.urcna.org'),('Heritage Reformed Congregations','https://heritagereformed.com'),('Protestant Reformed Churches in America','https://www.prca.org'),('Orthodox Presbyterian Church（威斯敏斯特准则）','https://opc.org'),('OPC · Westminster Shorter Catechism','https://opc.org/sc.html'),('Canadian Reformed Theological Seminary','https://canadianreformedseminary.ca'),('Westminster Theological Seminary','https://www.wts.edu'),('Covenant / Canadian Reformed Theological Seminary（crts.edu）','https://crts.edu')]
src=f'''<section class="hero reveal"><span class="chip">🔗 资料 · 方法 · 致谢</span><h1>资料来源与校验方法</h1></section>'''
src+=sec('verbatim','✅','一、原文“一字不差”的保证方法','''<div class="card pan core reveal"><ol class="core"><li>用程序抓取 ccifellowship.org《敬拜手册》中“三项联合信条”与“普世信经”的全部页面（共 175 页：海德堡 52 主日、比利时信条 37 条、多特信经 4 项共 63 个条目页、3 篇信经）。</li><li>用 HTML 解析器提取正文节点（问题、答案、条文段落、经文出处列表），只去除链接和样式属性，<b class="key">不做任何文字改动</b>（包括原文中的标点差异，如“51.”与“51．”）。</li><li>由同一份 JSON 数据生成所有页面；构建后再次用程序把站内每段原文与原网页逐字比对。</li><li>本站自行撰写的解读、口诀、要点均标明为解读或概述，与原文在视觉上明确区分。</li></ol><p class="small muted">说明：ccifellowship.org 未收录多特信经的“结论”部分，本站因此未收录，不以其他译本替代。威斯敏斯特小要理问答仅引用 opc.org 的英文原文。原文版权属于《中国改革宗敬拜手册》出版委员会，本站仅作学习引用并逐条注明出处。</p><p class="small muted">v7：学习笔记中带出处的经文引语（119 处）由 <code>build/check_cuv.py</code> 逐条与信望爱（FHL）线上和合本比对（0 处不符）；笔记中引用的要理问答语句也与上方原文逐字对照。经文措辞以和合本为准（如“甚么”）。</p></div>''')
src+=sec('links','🌐','二、参考网站','<div class="card reveal"><ul class="clean">'+''.join(f'<li>🔗 <a href="{u}" target="_blank" rel="noopener">{esc(t)}</a></li>' for t,u in links)+'</ul></div>')
src+=sec('credits','🖼️','三、图片致谢（Wikimedia Commons）',f'<div class="card reveal"><ul class="clean">{cr}</ul><p class="small muted">地图底图 © OpenStreetMap contributors；地图库 Leaflet；流程图 Mermaid。</p></div>')
src+=sec('deploy','🚀','四、部署与源码',f'<div class="card reveal"><p>源码仓库：<a href="https://github.com/07-Je-Grok-Love-Personal-20260928/{REPO}">github.com/07-Je-Grok-Love-Personal-20260928/{REPO}</a></p><p>版本 {VERSION} · 构建日期 {DATE}</p></div>')
page('sources.html','资料与致谢',src,'资料来源')
print('pages part2 done')
