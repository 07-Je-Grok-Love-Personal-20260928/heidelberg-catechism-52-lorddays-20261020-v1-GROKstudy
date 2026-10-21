from common import *
tools='<div class="btns" style="margin-top:14px"><button class="btn" id="reciteBtn">🙈 背诵模式（点击答案显示）</button><button class="btn" id="supBtn">🔢 隐藏/显示脚注编号</button><button class="btn" onclick="window.print()">🖨️ 打印</button></div>'
def intro(ps): return ''.join(f'<p>{p}</p>' for p in ps)
# HC
b=[f'<section class="hero reveal"><span class="chip i">📜 干净阅读版 · 背诵版</span><h1>海德堡要理问答（全文）</h1><p class="lead">52 主日 · 129 问，全文一字不改地引自 <a href="{CCI}/books/book-of-praise/confessions/heidelberg-catechism" target="_blank" rel="noopener">ccifellowship.org</a>。可开启背诵模式遮住答案自测。</p>{tools}</section>']
b.append(f'<section class="sec"><h2 id="intro"><span class="ico">ℹ️</span>简介（ccifellowship.org 原文）</h2><div class="card reading">{intro(D["hc_intro"])}</div></section>')
cur=None; cursub=None
def subrange(top,sub):
    ns=[l['n'] for l in D['hc'] if l['crumbs'][:1]==[top] and l['crumbs'][1:2]==[sub]]
    return ns[0],ns[-1]
for ld in D['hc']:
    n=ld['n']; p=part(n); top=(ld['crumbs'][0] if ld['crumbs'] else '引言'); sub=ld['crumbs'][1] if len(ld['crumbs'])>1 else None
    if top!=cur:
        cur=top; cursub=None; b.append(f'<h2 id="p{n}" data-toc="{esc(part_label(p[0]))}" style="margin-top:40px;color:{p[2]}"><span class="ico">{PARTS[["i","m","d","g"].index(p[0])][1]}</span>{esc(top)}<span class="small muted">　{esc(part_label(p[0]).split("（")[1].rstrip("）"))}</span></h2>')
    if sub!=cursub:
        cursub=sub
        if sub:
            s_,e_=subrange(top,sub); ic=SUBI.get(sub,'📌')
            b.append(f'<h3 id="sub{n}" data-lv="2" data-nonum data-toc="{ic} {esc(sub)}（主日{s_}{"–"+str(e_) if e_!=s_ else ""}）" class="subhd" style="color:{p[2]}">{ic} {esc(sub)}<span class="small muted">　主日 {s_}{"–"+str(e_) if e_!=s_ else ""}</span></h3>')
    lv=3 if sub else 2
    b.append(f'<section class="sec" style="margin:18px 0"><h3 id="ld{n}" data-lv="{lv}" data-fix="{n}" data-toc="{esc(ld_label(n))}" style="color:{p[2]}">{LDI[n]} 主日 {n} · {esc(N[n]["t"])} <a class="small" href="../ld/{n:02d}.html">→ 深度解析</a></h3>'+''.join(qa_html(q,p[2],lv=lv+1) for q in ld['qas'])+'</section>')
page('texts/hc.html','海德堡要理问答 全文阅读版',''.join(b),'海德堡要理问答129问全文 干净阅读背诵版')
# BC
b=[f'<section class="hero reveal"><span class="chip d">🛡️ 干净阅读版</span><h1>比利时信条（全文 37 条）</h1><p class="lead">又名《真基督教信条》，1561 年德布利（Guido de Brès）著。全文一字不改地引自 <a href="{CCI}/books/book-of-praise/confessions/the-belgic-confession" target="_blank" rel="noopener">ccifellowship.org</a>。</p>{tools}</section>']
b.append(f'<section class="sec"><h2 id="intro"><span class="ico">ℹ️</span>简介（ccifellowship.org 原文）</h2><div class="card reading">{intro(D["bc_intro"])}</div></section>')
groups=[(1,1,'论神'),(2,7,'论启示与圣经'),(8,11,'论三位一体'),(12,13,'论创造与护理'),(14,15,'论人与罪'),(16,17,'论拣选与应许'),(18,21,'论基督'),(22,26,'论救恩'),(27,32,'论教会'),(33,35,'论圣礼'),(36,36,'论政府'),(37,37,'论末后审判')]
cols=['var(--intro)','var(--deliv)','var(--intro)','var(--gold)','var(--misery)','var(--gold)','var(--deliv)','var(--grat)','var(--deliv)','var(--grat)','var(--gold)','var(--misery)']
for gi,(s,e,t) in enumerate(groups):
    gi_ic=BCG[gi][3]
    b.append(f'<section class="sec"><h2 id="g{s}" data-toc="{gi_ic} {t}（第{s}{"–"+str(e) if e!=s else ""}条）" style="color:{cols[gi]}"><span class="ico">{gi_ic}</span>{t}<span class="small muted">　第{s}{"–"+str(e) if e!=s else ""}条 · 本站分组</span></h2><div class="reading">')
    for k in range(s,e+1):
        a=BC[k]; refs=''.join(f'<li>{esc(r)}</li>' for r in a['refs'])
        b.append(f'<div class="art reveal" id="bc{k}" data-lv="2" data-fix="{k}" data-toc="{bc_icon(k)} {esc(art_short(a['title']))}" style="--c:{cols[gi]}"><div class="tools" style="float:right"><button class="btn" data-speak style="padding:2px 8px">🔊</button></div><h3>{esc(a["title"])}</h3>{"".join(f"<p>{x}</p>" for x in a["paras"])}'+(f'<details class="small muted"><summary>📖 经文出处（{len(a["refs"])}）</summary><ol>{refs}</ol></details>' if refs else '')+f'<p class="src"><a href="{a["url"]}" target="_blank" rel="noopener">原文出处</a></p></div>')
    b.append('</div></section>')
page('texts/bc.html','比利时信条 全文阅读版',''.join(b),'比利时信条37条全文')
# CD
b=[f'<section class="hero reveal"><span class="chip g">🌷 干净阅读版</span><h1>多特信经（全文）</h1><p class="lead">又称《反对抗辩派的五大点》，1618–1619 年多特大会采纳。全文一字不改地引自 <a href="{CCI}/books/book-of-praise/confessions/canons-of-dort" target="_blank" rel="noopener">ccifellowship.org</a>。</p>{tools}</section>']
b.append(f'<section class="sec"><h2 id="intro"><span class="ico">ℹ️</span>简介（ccifellowship.org 原文）</h2><div class="card reading">{intro(D["cd_intro"])}</div><p class="small muted">注：ccifellowship.org 的多特信经页面包含四项（五点）教义的正面条文与“错谬反驳”，未收录多特信经的“结论”（Conclusion）部分，故本站亦未收录，以免以非该站文本冒充原文。</p></section>')
ccol={'section1':'var(--intro)','section2':'var(--misery)','section3-4':'var(--deliv)','section5':'var(--grat)'}
for s in D['cd']:
    c=ccol[s['sec']]
    b.append(f'<section class="sec"><h2 id="{s["sec"]}" data-toc="{CDI[s["sec"]]} {esc(s["title"])}" style="color:{c}"><span class="ico">{CDI[s["sec"]]}</span>{esc(s["title"])}</h2><div class="reading">')
    for a in s['arts']:
        rid=f'{s["sec"]}-{a["n"]}'; refs=''.join(f'<li>{esc(r)}</li>' for r in a['refs'])
        isrej=a['title']=='错谬反驳'
        b.append(f'<div class="art reveal" id="cd{rid}" data-lv="2" '+(f'data-nonum data-toc="❌ 错谬反驳（{len(a["paras"])} 段）"' if isrej else f'data-fix="{a["n"]}" data-toc="{CDI[s["sec"]]} {esc(art_short(a["title"]))}"')+f' style="--c:{"var(--misery)" if isrej else c}{";border-style:dashed" if isrej else ""}">'+(f'<h3 id="rej-{s["sec"]}">❌ 错谬反驳</h3>' if isrej else f'<h3>{esc(a["title"])}</h3>')+''.join(f'<p>{x}</p>' for x in a['paras'])+(f'<details class="small muted"><summary>📖 经文出处</summary><ol>{refs}</ol></details>' if refs else '')+f'<p class="src"><a href="{a["url"]}" target="_blank" rel="noopener">原文出处</a></p></div>')
    b.append('</div></section>')
page('texts/cd.html','多特信经 全文阅读版',''.join(b),'多特信经全文')
# creeds
cc={'apostles-creed':('var(--gold)','约公元400年（罗马教会信经，可追溯更早）','西方教会洗礼认信','🕊️'),'nicene-creed':('var(--deliv)','325 尼西亚 / 381 君士坦丁堡','驳斥亚流主义，确立子与圣灵的神性','🔥'),'athanasian-creed':('var(--intro)','约6世纪上半叶（西方）','三位一体与基督神人二性的精确表述','👑')}
b=[f'<section class="hero reveal"><span class="chip">⛪ 三大普世信经 · 背诵版</span><h1>使徒信经 · 尼西亚信经 · 亚他那修信经</h1><p class="lead">信经正文与简介一字不改地引自 <a href="{CCI}/books/book-of-praise/creeds" target="_blank" rel="noopener">ccifellowship.org · 普世信经</a>。</p><div class="btns" style="margin-top:14px"><button class="btn" onclick="window.print()">🖨️ 打印</button></div></section>',
   f'<section class="sec"><h2 id="intro"><span class="ico">ℹ️</span>普世信经简介（原文）</h2><div class="card reading">{intro(D["creeds_intro"])}</div></section>']
for cr in D['creeds']:
    c,date,aim,ic=cc[cr['slug']]
    b.append(f'<section class="sec"><h2 id="{cr["slug"]}" style="color:{c}"><span class="ico">{ic}</span>{esc(cr["title"])}</h2><div class="tags" style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:10px"><span class="chip">🗓️ {date}</span><span class="chip">🎯 {aim}</span></div>'
             f'<div class="creed reveal" data-speakbox style="border-color:color-mix(in srgb,{c} 45%,var(--bd))"><div style="float:right"><button class="btn" data-speak style="padding:2px 10px">🔊 朗读</button></div>{"".join(f"<p>{x}</p>" for x in cr["text"])}</div>'
             f'<details class="card" style="margin-top:12px"><summary style="cursor:pointer">ℹ️ 关于{esc(cr["title"])}（ccifellowship.org 简介原文）</summary><div class="reading" style="font-size:16px">{intro(cr["intro"])}</div></details><p class="src">原文：<a href="{cr["url"]}" target="_blank" rel="noopener">{cr["url"]}</a></p></section>')
page('texts/creeds.html','三大普世信经',''.join(b),'使徒信经 尼西亚信经 亚他那修信经 原文')
hub=f'''<section class="hero reveal"><span class="chip i">📜 原文中心</span><h1>三项联合信条 + 三大普世信经</h1><p class="lead">全部原文一字不改地引自 <a href="{CCI}/books/book-of-praise" target="_blank" rel="noopener">ccifellowship.org《中国改革宗敬拜手册》</a>。阅读版带背诵模式、朗读、脚注开关；笔记标记可用 🖍️ 按钮或 M 键关闭。</p></section>'''
cards=[('hc.html','📜','海德堡要理问答','1563 · 52 主日 · 129 问','“安慰”的教理问答：罪 · 恩 · 谢','var(--deliv)',129),
('bc.html','🛡️','比利时信条','1561 · 37 条','受逼迫教会向君王的公开认信','var(--intro)',37),
('cd.html','🌷','多特信经','1618–1619 · 四项（五点）','回应抗辩派：恩典的教义','var(--grat)',sum(len(x['arts']) for x in D['cd'])),
('creeds.html','⛪','三大普世信经','使徒 · 尼西亚 · 亚他那修','与历代众圣徒同一信仰','var(--gold)',3)]
mx=129
hub+=sec('forms','📚','原文目录','<div class="grid g2">'+''.join(f'<a class="card lift reveal" href="{h}" style="border-top:4px solid {c}"><h3 id="hub-{h[:-5]}" style="color:{c}">{i} {t}</h3><p class="small muted" style="margin:0">{d}</p><p style="margin:.4em 0">{x}</p><svg viewBox="0 0 300 14" style="width:100%;height:14px"><rect width="300" height="14" rx="7" fill="currentColor" opacity=".08"/><g class="barx" style="transform-box:fill-box"><rect width="{max(n/mx*300,14):.0f}" height="14" rx="7" fill="{c}"/></g></svg><p class="small muted" style="margin:.2em 0 0">{n} 个条目</p></a>' for h,i,t,d,x,c,n in cards)+'</div>')
hub+=sec('how','🧭','怎样使用阅读版','<div class="card reveal"><ol class="core"><li>先读 <b>海德堡要理问答</b> 的一个主日，再点“→ 深度解析”看解读。</li><li>对照页中的 <b>比利时信条</b> 条文看同一教义的“公开认信”表达。</li><li>遇到拣选、恩典、坚忍等问题，查 <b>多特信经</b> 的正面条文与“错谬反驳”。</li><li>用 <b>背诵模式</b>（R 键）遮住答案自测；用 🔊 朗读辅助记忆。</li></ol></div>')
page('texts/index.html','原文中心',hub,'三项联合信条与普世信经原文中心')
print('texts done')
