from common import *
tools='<div class="btns" style="margin-top:14px"><button class="btn" id="reciteBtn">🙈 背诵模式（点击答案显示）</button><button class="btn" id="supBtn">🔢 隐藏/显示脚注编号</button><button class="btn" onclick="window.print()">🖨️ 打印</button></div>'
def intro(ps): return ''.join(f'<p>{p}</p>' for p in ps)
# HC
b=[f'<section class="hero reveal"><span class="chip i">📜 干净阅读版 · 背诵版</span><h1>海德堡要理问答（全文）</h1><p class="lead">52 主日 · 129 问，全文一字不改地引自 <a href="{CCI}/books/book-of-praise/confessions/heidelberg-catechism" target="_blank" rel="noopener">ccifellowship.org</a>。可开启背诵模式遮住答案自测。</p>{tools}</section>']
b.append(f'<section class="sec"><h2 id="intro"><span class="ico">ℹ️</span>简介（ccifellowship.org 原文）</h2><div class="card reading">{intro(D["hc_intro"])}</div></section>')
cur=None
for ld in D['hc']:
    n=ld['n']; p=part(n); top=(ld['crumbs'][0] if ld['crumbs'] else '引言')
    if top!=cur:
        cur=top; b.append(f'<h2 id="p{n}" style="margin-top:40px"><span class="ico">{p[3]}</span>{esc(top)}</h2>')
    sub=(' · '+ld['crumbs'][1]) if len(ld['crumbs'])>1 else ''
    b.append(f'<section class="sec" style="margin:18px 0"><h3 id="ld{n}" data-toc="主日{n}{sub}" style="color:{p[2]}">📅 主日 {n}<span class="muted small">{esc(sub)}</span> <a class="small" href="../ld/{n:02d}.html">→ 深度解析</a></h3>'+''.join(qa_html(q,p[2]) for q in ld['qas'])+'</section>')
page('texts/hc.html','海德堡要理问答 全文阅读版',''.join(b),'海德堡要理问答129问全文 干净阅读背诵版')
# BC
b=[f'<section class="hero reveal"><span class="chip d">🛡️ 干净阅读版</span><h1>比利时信条（全文 37 条）</h1><p class="lead">又名《真基督教信条》，1561 年德布利（Guido de Brès）著。全文一字不改地引自 <a href="{CCI}/books/book-of-praise/confessions/the-belgic-confession" target="_blank" rel="noopener">ccifellowship.org</a>。</p>{tools}</section>']
b.append(f'<section class="sec"><h2 id="intro"><span class="ico">ℹ️</span>简介（ccifellowship.org 原文）</h2><div class="card reading">{intro(D["bc_intro"])}</div></section>')
groups=[(1,1,'论神'),(2,7,'论启示与圣经'),(8,11,'论三位一体'),(12,13,'论创造与护理'),(14,15,'论人与罪'),(16,17,'论拣选与应许'),(18,21,'论基督'),(22,26,'论救恩'),(27,32,'论教会'),(33,35,'论圣礼'),(36,36,'论政府'),(37,37,'论末后审判')]
b.append('<section class="sec"><h2 id="arts"><span class="ico">📜</span>正文</h2><div class="reading">')
cols=['var(--intro)','var(--deliv)','var(--intro)','var(--gold)','var(--misery)','var(--gold)','var(--deliv)','var(--grat)','var(--deliv)','var(--grat)','var(--gold)','var(--misery)']
for gi,(s,e,t) in enumerate(groups):
    b.append(f'<h3 id="g{s}" data-toc="第{s}{"–"+str(e) if e!=s else ""}条 {t}" style="color:{cols[gi]}">🔖 第{s}{"–"+str(e) if e!=s else ""}条 · {t}<span class="small muted">（本站分组）</span></h3>')
    for k in range(s,e+1):
        a=BC[k]; refs=''.join(f'<li>{esc(r)}</li>' for r in a['refs'])
        b.append(f'<div class="art reveal" id="bc{k}" style="--c:{cols[gi]}"><div class="tools" style="float:right"><button class="btn" data-speak style="padding:2px 8px">🔊</button></div><h3>{esc(a["title"])}</h3>{"".join(f"<p>{x}</p>" for x in a["paras"])}'+(f'<details class="small muted"><summary>📖 经文出处（{len(a["refs"])}）</summary><ol>{refs}</ol></details>' if refs else '')+f'<p class="src"><a href="{a["url"]}" target="_blank" rel="noopener">原文出处</a></p></div>')
b.append('</div></section>')
page('texts/bc.html','比利时信条 全文阅读版',''.join(b),'比利时信条37条全文')
# CD
b=[f'<section class="hero reveal"><span class="chip g">🌷 干净阅读版</span><h1>多特信经（全文）</h1><p class="lead">又称《反对抗辩派的五大点》，1618–1619 年多特大会采纳。全文一字不改地引自 <a href="{CCI}/books/book-of-praise/confessions/canons-of-dort" target="_blank" rel="noopener">ccifellowship.org</a>。</p>{tools}</section>']
b.append(f'<section class="sec"><h2 id="intro"><span class="ico">ℹ️</span>简介（ccifellowship.org 原文）</h2><div class="card reading">{intro(D["cd_intro"])}</div><p class="small muted">注：ccifellowship.org 的多特信经页面包含四项（五点）教义的正面条文与“错谬反驳”，未收录多特信经的“结论”（Conclusion）部分，故本站亦未收录，以免以非该站文本冒充原文。</p></section>')
ccol={'section1':'var(--intro)','section2':'var(--misery)','section3-4':'var(--deliv)','section5':'var(--grat)'}
for s in D['cd']:
    c=ccol[s['sec']]
    b.append(f'<section class="sec"><h2 id="{s["sec"]}" style="color:{c}"><span class="ico">🌷</span>{esc(s["title"])}</h2><div class="reading">')
    for a in s['arts']:
        rid=f'{s["sec"]}-{a["n"]}'; refs=''.join(f'<li>{esc(r)}</li>' for r in a['refs'])
        isrej=a['title']=='错谬反驳'
        b.append(f'<div class="art reveal" id="cd{rid}" style="--c:{"var(--misery)" if isrej else c}{";border-style:dashed" if isrej else ""}">'+(f'<h3 id="rej-{s["sec"]}" data-toc="{esc(s["title"][:6])} · 错谬反驳">❌ 错谬反驳</h3>' if isrej else f'<h3>{esc(a["title"])}</h3>')+''.join(f'<p>{x}</p>' for x in a['paras'])+(f'<details class="small muted"><summary>📖 经文出处</summary><ol>{refs}</ol></details>' if refs else '')+f'<p class="src"><a href="{a["url"]}" target="_blank" rel="noopener">原文出处</a></p></div>')
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
print('texts done')
