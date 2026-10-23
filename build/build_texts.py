from common import *
tools='<div class="btns" style="margin-top:14px"><button class="btn" id="reciteBtn">🙈 背诵模式（点击答案显示）</button><button class="btn" id="supBtn">🔢 隐藏/显示脚注编号</button><button class="btn" onclick="window.print()">🖨️ 打印</button><button class="btn" id="readAll">🎧 连续朗读</button></div>'
def intro(ps): return ''.join(f'<p>{p}</p>' for p in ps)
# HC — v7: split into 5 reading volumes (each ≈ 1/5 of the DOM) + a light hub + opt-in single-page full text
VOLS=[(1,10,'💜 安慰 · 愁苦 · 中保与父神','引言 · 第一部 · 第二部（救赎之道、父神）'),(11,22,'✝️ 子神与圣灵','第二部 · 使徒信经（子神、圣灵）'),
      (23,31,'💧 称义与圣礼','第二部 · 称义 · 圣言与圣礼 · 洗礼 · 圣餐'),(32,44,'📜 感恩与十诫','第三部 · 归正 · 十诫'),(45,52,'🙏 祷告','第三部 · 主祷文')]
LDQ={ld['n']:[qnum(q) for q in ld['qas']] for ld in D['hc']}
def vol_of(n): return next(i for i,(s_,e_,_,_) in enumerate(VOLS,1) if s_<=n<=e_)
def qrange(s_,e_): return LDQ[s_][0],LDQ[e_][-1]
def subrange(top,sub):
    ns=[l['n'] for l in D['hc'] if l['crumbs'][:1]==[top] and l['crumbs'][1:2]==[sub]]
    return ns[0],ns[-1]
def hc_body(lds,cv=True):
    b=[];cur=None;cursub=None
    for ld in lds:
        n=ld['n']; p=part(n); top=(ld['crumbs'][0] if ld['crumbs'] else '引言'); sub=ld['crumbs'][1] if len(ld['crumbs'])>1 else None
        if top!=cur:
            cur=top; cursub=None; b.append(f'<h2 id="p{n}" data-toc="{esc(part_label(p[0]))}" style="margin-top:40px;color:{p[2]}"><span class="ico">{PARTS[["i","m","d","g"].index(p[0])][1]}</span>{esc(top)}<span class="small muted">　{esc(part_label(p[0]).split("（")[1].rstrip("）"))}</span></h2>')
        if sub!=cursub:
            cursub=sub
            if sub:
                s_,e_=subrange(top,sub); ic=SUBI.get(sub,'📌')
                b.append(f'<h3 id="sub{n}" data-lv="2" data-nonum data-toc="{ic} {esc(sub)}（主日{s_}{"–"+str(e_) if e_!=s_ else ""}）" class="subhd" style="color:{p[2]}">{ic} {esc(sub)}<span class="small muted">　主日 {s_}{"–"+str(e_) if e_!=s_ else ""}</span></h3>')
        lv=3 if sub else 2
        b.append(f'<section class="sec{"" if cv else " ncv"}" style="margin:18px 0"><h3 id="ld{n}" data-lv="{lv}" data-fix="{n}" data-toc="{esc(ld_label(n))}" style="color:{p[2]}">{LDI[n]} 主日 {n} · {esc(N[n]["t"])} <a class="small" href="../ld/{n:02d}.html">→ 深度解析</a></h3>'+''.join(qa_html(q,p[2],lv=lv+1) for q in ld['qas'])+'</section>')
    return ''.join(b)
def volnav(cur):
    out=[]
    for i,(s_,e_,t,d) in enumerate(VOLS,1):
        q0,q1=qrange(s_,e_)
        out.append(f'<a class="hcv{" on" if i==cur else ""}" href="hc-{i}.html"{" aria-current=page" if i==cur else ""}><b>卷{i}</b><span>{t}</span><small>主日 {s_}–{e_} · 问 {q0}–{q1}</small></a>')
    return '<nav class="hcvol" aria-label="要理问答分卷">'+''.join(out)+'<a class="hcv all" href="hc-all.html"><b>📄</b><span>单页全文</span><small>打印 · 页内搜索</small></a></nav>'
hero=lambda sub: f'<section class="hero reveal"><span class="chip i">📜 干净阅读版 · 背诵版</span><h1>海德堡要理问答（全文）{sub}</h1><p class="lead">52 主日 · 129 问，全文一字不改地引自 <a href="{CCI}/books/book-of-praise/confessions/heidelberg-catechism" target="_blank" rel="noopener">ccifellowship.org</a>。可开启背诵模式遮住答案自测。</p>{tools}</section>'
for i,(s_,e_,t,d) in enumerate(VOLS,1):
    lds=[ld for ld in D['hc'] if s_<=ld['n']<=e_]; q0,q1=qrange(s_,e_)
    pv=f'<a class="btn" id="prevLd" href="hc-{i-1}.html">◀ 卷{i-1} {VOLS[i-2][2]}</a>' if i>1 else '<a class="btn" href="hc.html">◀ 分卷目录</a>'
    nx=f'<a class="btn pri" id="nextLd" href="hc-{i+1}.html">卷{i+1} {VOLS[i][2]} ▶</a>' if i<len(VOLS) else '<a class="btn pri" href="hc.html">分卷目录 ▶</a>'
    body=hero(f'<span class="small muted"> · 卷{i}/5</span>')+volnav(i)+f'<p class="small muted" style="margin:6px 2px 0">{d} · 主日 {s_}–{e_} · 问 {q0}–{q1}（v7 起分卷加载，翻页更顺；需要整本打印或 Ctrl+F 全文搜索请用“单页全文”）</p>'+hc_body(lds,cv=False)+f'<div class="btns" style="justify-content:space-between;margin:28px 0 8px">{pv}{nx}</div>'
    page(f'texts/hc-{i}.html',f'海德堡要理问答 卷{i}（主日{s_}–{e_}）',body,f'海德堡要理问答 主日{s_}–{e_} 问{q0}–{q1} 原文 背诵版')
# single-page full text (opt-in)
b=[hero('<span class="small muted"> · 单页全文</span>'),volnav(0),f'<section class="sec"><h2 id="intro"><span class="ico">ℹ️</span>简介（ccifellowship.org 原文）</h2><div class="card reading">{intro(D["hc_intro"])}</div></section>',hc_body(D['hc'])]
page('texts/hc-all.html','海德堡要理问答 单页全文',''.join(b),'海德堡要理问答129问全文 单页版（打印/全文搜索）')
# hub: light page + redirect of legacy deep links (#q60, #ld11, #sub34, #p32) to the right volume before first paint
qv={q:vol_of(n) for n,qs in LDQ.items() for q in qs}
QV=''.join(str(qv[q]) for q in range(1,130)); LV=''.join(str(vol_of(n)) for n in range(1,53))
REDIR=f'<script>(function(){{var h=location.hash,m=/^#(q|ld|sub|p)(\\d+)$/.exec(h);if(!m)return;var k=+m[2],v=m[1]=="q"?"{QV}"[k-1]:"{LV}"[k-1];if(v)location.replace("hc-"+v+".html"+h)}})()</script>'
grid=''.join(f'<a class="ldc" href="hc-{vol_of(n)}.html#ld{n}" title="{esc(N[n]["t"])}" style="--c:{part(n)[2]}"><b>{n}</b><span>{LDI[n]}</span></a>' for n in range(1,53))
vc=''.join(f'<a class="card lift reveal volcard" href="hc-{i}.html" style="--c:{part(s_)[2]}"><span class="vno">卷{i}</span><h3 id="vol{i}" style="color:{part(s_)[2]}">{t}</h3><p class="small muted" style="margin:0">{d}</p><p class="small" style="margin:.5em 0 0">主日 {s_}–{e_} · 问 {qrange(s_,e_)[0]}–{qrange(s_,e_)[1]} · {sum(len(LDQ[n]) for n in range(s_,e_+1))} 问</p><svg viewBox="0 0 520 10" style="width:100%;height:10px;margin-top:8px" aria-hidden="true"><rect width="520" height="10" rx="5" fill="currentColor" opacity=".08"/><rect x="{(s_-1)/52*520:.0f}" width="{(e_-s_+1)/52*520:.0f}" height="10" rx="5" fill="{part(s_)[2]}"/></svg></a>' for i,(s_,e_,t,d) in enumerate(VOLS,1))
hub=[f'<section class="hero reveal"><span class="chip i">📜 干净阅读版 · 背诵版</span><h1>海德堡要理问答（全文）</h1><p class="lead">52 主日 · 129 问，全文一字不改地引自 <a href="{CCI}/books/book-of-praise/confessions/heidelberg-catechism" target="_blank" rel="noopener">ccifellowship.org</a>。v7 起按内容分为 <b>5 卷</b>阅读（每卷只加载约五分之一，滚动更顺）；也可打开 <a href="hc-all.html">📄 单页全文</a> 打印或全文搜索。</p></section>',
     sec('vols','📚','分卷阅读',f'<div class="grid g2">{vc}<a class="card lift reveal volcard" href="hc-all.html" style="--c:var(--gold)"><span class="vno">全</span><h3 id="vol-all" style="color:var(--gold)">📄 单页全文</h3><p class="small muted" style="margin:0">129 问一页呈现：适合打印、Ctrl+F 页内搜索、连续朗读全书</p></a></div>'),
     sec('jump','🔢','按主日直达',f'<div class="ldjump">{grid}</div><p class="small muted">颜色：💜 引言 · 💔 愁苦 · ✝️ 得救 · 🌿 感恩。旧链接（如 hc.html#q60）会自动转到对应分卷。</p>'),
     f'<section class="sec"><h2 id="intro"><span class="ico">ℹ️</span>简介（ccifellowship.org 原文）</h2><div class="card reading">{intro(D["hc_intro"])}</div></section>']
page('texts/hc.html','海德堡要理问答 全文阅读版（分卷）',''.join(hub),'海德堡要理问答129问全文 干净阅读背诵版 分卷',head=REDIR)
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
        b.append(f'<div class="art reveal" id="cd{rid}" data-lv="2" '+(f'data-nonum data-toc="❌ {s["title"].split("教义")[0]}错谬反驳（{len(a["paras"])} 段）"' if isrej else f'data-fix="{a["n"]}" data-toc="{CDI[s["sec"]]} {esc(art_short(a["title"]))}"')+f' style="--c:{"var(--misery)" if isrej else c}{";border-style:dashed" if isrej else ""}">'+(f'<h3 id="rej-{s["sec"]}">❌ 错谬反驳</h3>' if isrej else f'<h3>{esc(a["title"])}</h3>')+''.join(f'<p>{x}</p>' for x in a['paras'])+(f'<details class="small muted"><summary>📖 经文出处</summary><ol>{refs}</ol></details>' if refs else '')+f'<p class="src"><a href="{a["url"]}" target="_blank" rel="noopener">原文出处</a></p></div>')
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
