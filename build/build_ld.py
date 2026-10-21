from common import *
from notes4 import X
import svgs, random
def strip_tags(s): return re.sub('<[^>]+>','',s)
def first(s,k=1):
    parts=[x for x in re.split(r'(?<=[。！？])',s) if x.strip()]
    return ''.join(parts[:k])
def kwmark(s,kws):
    for k in kws:
        if k and k in s: s=s.replace(esc(k),f'<span class="mk-b">{esc(k)}</span>',1)
    return s
def ld_page(ld):
    n=ld['n']; no=N[n]; p=part(n); c=p[2]; a,b=qrange(ld); th,trap,gold=T[n]
    goldq=next(qnum(q) for q in ld['qas'] if any(gold in x for x in q['a']))
    K=lambda s:kwmark(esc(s),no['kw'])
    crumbs=' › '.join(ld['crumbs']) or '引言'
    qr=f'第{a}{"–"+str(b) if b!=a else ""}问'
    kws=''.join(f'<span class="chip {p[0]}">🔑 {esc(k)}</span>' for k in no['kw'])
    hero=f'''<section class="hero reveal" style="background:linear-gradient(135deg,color-mix(in srgb,{c} 32%,transparent),color-mix(in srgb,{c} 6%,transparent))"><div class="tags"><span class="chip {p[0]}">{p[3]} {esc(p[1])}</span><span class="chip">🧭 {esc(crumbs)}</span><span class="chip">❓ {qr} · 共{len(ld['qas'])}问</span></div>
<h1>{LDI[n]} 主日 {n}　{esc(no['t'])}</h1>{callout('core','核心',md(th))}{callout('hook','记忆钩',f'<b style="font-family:var(--serif);font-size:1.1em">{esc(no["k"])}</b>')}<div class="tags">{kws}</div>
<div class="chart" style="margin-top:14px">{svgs.ld_strip(n)}</div><div class="small muted">全书位置 {n}/52 · {qr}</div>
<div class="btns" style="margin-top:14px"><button class="btn" id="reciteBtn">🙈 背诵模式 (R)</button><button class="btn" id="supBtn">🔢 脚注编号</button><button class="btn" data-marks>🖍️ 标记 (M)</button><button class="btn pri" id="doneBtn" data-ld="{n}">☑️ 标记已学完</button></div>
<details class="small" style="margin-top:12px"><summary style="cursor:pointer">🖍️ 标记图例（点击展开）</summary><div style="margin-top:8px">{legend_html(False)}</div></details></section>'''
    # 1. essence
    keyrefs='　'.join(f'<a href="#q{qnum(q)}" class="chip" style="white-space:nowrap">Q{qnum(q)} · {esc(q["refs"][0].split("；")[0])}</a>' for q in ld['qas'] if q['refs'])+'<span class="src">　（各问第一条经文出处，引自原文脚注）</span>'
    bridge=(f'<a class="node" href="{n-1:02d}.html">⬅ 承接<br><b>{esc(ld_label(n-1))}</b></a>' if n>1 else '<span class="node">🚪 全书开端</span>')+'<span class="arr">➜</span>'+f'<span class="node" style="border-color:{c}"><b>{esc(ld_label(n))}</b><br><span class="small">{esc(no["k"])}</span></span><span class="arr">➜</span>'+(f'<a class="node" href="{n+1:02d}.html">引出 ➡<br><b>{esc(ld_label(n+1))}</b></a>' if n<52 else '<span class="node">🙌 阿们：全书结束</span>')
    rows=[('🎯 论题','core',md(th)),('❓ 为什么','why',K(first(no['why']))),('📌 写了什么','what','；'.join(K(x) for x in no['core'][:2])),('🌱 怎么活','app',K(no['app'][0])),('🤝 圣经·圣约','cov',K(first(no['cov'])))]
    ess=''.join(f'<tr><th>{h}</th><td>{v}</td></tr>' for h,_,v in rows)
    s0=sec('essence','💎',f'精华速览：一页抓住主日{n}',f'''<div class="grid g2"><div class="card reveal"><h3 id="ess-table">五问提要</h3><div class="tbl" style="border:none;background:none"><table style="min-width:0"><tbody>{ess}</tbody></table></div>
{callout('gold','金句',f'“{esc(gold)}”<span class="src">　—— 原文第{goldq}问（逐字）</span>')}{callout('trap','易错',md(trap))}{callout('bible','核心经文',keyrefs)}</div>
<div class="card reveal"><h3 id="ess-map">关联星图</h3><div class="chart">{svgs.ld_constellation(n,ld,no)}</div><p class="small muted" style="margin:6px 0 0">中心为本主日；内圈为各问，外圈为关键词与比利时信条 / 多特信经 / 威斯敏斯特对照。<b>每个节点都可点击</b>跳到对应原文或搜索。</p></div></div>
<div class="card reveal" style="margin-top:14px"><h3 id="ess-bridge">🔗 承上启下：在全书中的位置</h3><div class="chain bridge">{bridge}</div></div>''')
    # 2. text
    chain=[]
    for i,q in enumerate(ld['qas']):
        qt=re.sub(r'^\d+[．.]\s*问：','',q['q'])
        if i: chain.append('<span class="arr">➜</span>')
        chain.append(f'<div class="node" style="--c:{c}"><b>Q{qnum(q)}</b> {esc(qt)}</div>')
    s1=sec('text','📜','原文：中文《海德堡要理问答》',f'<p class="src">以下问答一字不改地引自 <a href="{ld["url"]}" target="_blank" rel="noopener">ccifellowship.org · 主日{n}</a>（上标数字对应经文出处；彩色标记仅为样式，可按 M 关闭）。</p><div class="card reveal nolv" style="margin-bottom:12px"><b class="small muted">🔗 问题推进</b><div class="chain" style="margin-top:6px">{"".join(chain)}</div></div>'+''.join(qa_html(q,c,lv=2) for q in ld['qas']))
    # 3. whole
    st,ch,pr,dq=X[n]
    s2=sec('whole','🌍','整体：圣经神学 · 圣约神学 · 基督中心',f'''<div class="grid g2">
<div class="card pan big reveal"><h3 id="w-bible">📖 整本圣经的视角</h3><p>{K(no['big'])}</p></div>
<div class="card pan cov reveal"><h3 id="w-cov">🤝 圣约神学的视角</h3><p>{K(no['cov'])}</p></div>
<div class="card pan core reveal"><h3 id="w-story">📚 圣经中的一个画面</h3><p>{K(st)}</p></div>
<div class="card pan xref reveal"><h3 id="w-christ">✝️ 如何指向基督</h3><p>{K(ch)}</p></div></div>''')
    # 4. local
    s3=sec('local','🔍','局部：为什么写 · 写了什么 · 难在哪里',f'''<div class="card pan why reveal"><h3 id="why">🏛️ 真实背景：为什么这样写？</h3><p>{K(no['why'])}</p></div><div style="height:14px"></div>
<div class="card pan core reveal"><h3 id="core">📌 核心要点：写了什么？</h3><ol class="core">{"".join(f"<li>{K(x)}</li>" for x in no['core'])}</ol><p class="small muted">（要点为本站概述，原文以上方引文为准。）</p></div><div style="height:14px"></div>
<div class="card pan hard reveal"><h3 id="hard">⚠️ 难点剖析</h3>{callout('hard','难点',K(no['hard']))}</div><div style="height:14px"></div>
<div class="card pan err reveal"><h3 id="err">🛡️ 本主日驳斥或防范的错误</h3>{callout('trap','易错',md(trap))}<div class="tags">{"".join(f'<span class="chip err">❌ {esc(x)}</span>' for x in no['err'])}</div></div>''')
    # 5. xref
    xs=[]
    if no['bc']:
        xs.append('<h3 id="x-bc">🛡️ 比利时信条</h3>')
        for k in no['bc']:
            art=BC[k]; body=''.join(f'<p>{x}</p>' for x in art['paras'])
            xs.append(f'<details class="card" id="xbc{k}" data-lv="3" data-toc="比利时信条 {esc(art["title"])}" style="margin:8px 0"><summary style="cursor:pointer"><b style="color:var(--deliv)">比利时信条 {esc(art["title"])}</b></summary><div class="reading" style="font-size:16px;line-height:1.95;margin-top:8px">{body}</div><p class="src">原文：<a href="{art["url"]}" target="_blank" rel="noopener">{art["url"]}</a> · <a href="../texts/bc.html#bc{k}">在本站阅读版中打开</a></p></details>')
    cds=[]
    for s in no['cd']:
        sec_,st_,arts=parse_cd(s)
        for art in arts:
            body=''.join(f'<p>{x}</p>' for x in art['paras'])
            cds.append(f'<details class="card" id="xcd{sec_}-{art["n"]}" data-lv="3" data-toc="多特 {esc(st_[:6])} · {esc(art["title"])}" style="margin:8px 0"><summary style="cursor:pointer"><b style="color:var(--grat)">多特信经 {esc(st_)} · {esc(art["title"])}</b></summary><div class="reading" style="font-size:16px;line-height:1.95;margin-top:8px">{body}</div><p class="src">原文：<a href="{art["url"]}" target="_blank" rel="noopener">{art["url"]}</a></p></details>')
    if cds: xs.append('<h3 id="x-cd">🌷 多特信经</h3>'+''.join(cds))
    if no['wsc']:
        w='<h3 id="x-wsc">🏴 威斯敏斯特小要理问答</h3><p>长老会改革宗对照：'+'、'.join(f'第{x}问' for x in no['wsc'])+'（英文原文见 <a href="https://opc.org/sc.html" target="_blank" rel="noopener">opc.org/sc.html</a>）</p>'
        for x in no['wsc']:
            if x in WSC_EN: w+=f'<blockquote class="small" style="margin:6px 0;padding:8px 12px;border-left:3px solid var(--gold);background:var(--card2);border-radius:8px" lang="en">{esc(WSC_EN[x])}<br><span class="muted">— Westminster Shorter Catechism, opc.org</span></blockquote>'
        xs.append(w)
    s4=sec('xref','🧩','交叉对照：三项联合信条 + 威斯敏斯特',f'<div class="card pan xref reveal">{"".join(xs) or "<p class=muted>本主日内容主要在要理问答中独立展开。</p>"}</div>')
    # 6. application tabs
    s5=sec('app','🌱','应用与深化',f'''<div class="card pan app reveal"><div class="tabs"><button class="on">✅ 生活应用</button><button>🙏 一句祷告</button><button>💬 小组讨论</button></div>
<div class="tabp on"><ul class="clean">{"".join(f"<li>✅ {K(x)}</li>" for x in no["app"])}</ul></div>
<div class="tabp"><p style="font-family:var(--serif)">{esc(pr)}</p></div>
<div class="tabp"><ol class="clean">{''.join(f"<li>{esc(x)}</li>" for x in dq)}</ol></div></div>''')
    cards=''.join(f'<div class="fc" style="--c:{c}"><div class="in"><div class="f"><div class="small muted">点击翻转</div><div class="big">Q{qnum(q)}</div><div>{esc(re.sub(r"^\d+[．.]\s*问：","",q["q"]))}</div></div><div class="b">{"".join(f"<p>{x}</p>" for x in q["a"])}</div></div></div>' for q in ld['qas'])
    qz=no['quiz']; opts=''.join(f'<button class="opt">{"ABCD"[i]}. {esc(o)}</button>' for i,o in enumerate(qz[1]))
    sortq=''
    if len(ld['qas'])>=2:
        items=[(qnum(q),re.sub(r'^\d+[．.]\s*问：','',q['q'])) for q in ld['qas']]
        rnd=random.Random(n); sh=items[:]
        while sh==items: rnd.shuffle(sh)
        sortq=f'''<h3 id="m-sort">🧩 排序挑战：把本主日的问题排回原来的顺序</h3><div class="card reveal sortbox"><p class="small muted">按住拖动（或用 ↑ ↓ 按钮）调整顺序，再点“检查”。</p><ol class="sortq">{"".join(f'<li data-q="{qn}" style="--c:{c}"><span class="grip" aria-hidden="true">⠿</span><span class="st">{esc(t)}</span><span class="mv"><button type="button" data-up aria-label="上移">↑</button><button type="button" data-down aria-label="下移">↓</button></span></li>' for qn,t in sh)}</ol><div class="btns"><button class="btn pri" data-sortcheck>✅ 检查</button><button class="btn" data-sortshuffle>🔀 重新打乱</button></div><p class="res key"></p></div>'''
    cloze=f'''<h3 id="m-cloze">✍️ 填空背诵：标记的关键短语变成空格</h3><div class="card reveal clozebox" data-cloze><p class="small muted">根据上方原文中的标记短语自动生成（题目来自原文，作答只在本机）。</p><div class="btns"><button class="btn pri" data-clozestart>▶️ 开始填空</button><button class="btn" data-clozecheck>✅ 检查</button><button class="btn" data-clozeshow>👀 显示答案</button></div><div class="clozeout"></div><p class="res key"></p></div>'''
    s6=sec('memo','🧠','记忆：卡片 · 排序 · 填空 · 小测',f'''<h3 id="m-cards">🃏 翻转卡片</h3><div class="grid">{cards}</div>{sortq}{cloze}
<h3 id="m-quiz">🎯 小测验</h3><div class="card quiz reveal" data-ans="{qz[2]}" data-id="ld{n}"><p><b>{esc(qz[0])}</b></p>{opts}<p class="res key"></p></div>''')
    sers=[s for s in SER if s['ld']==n]
    s7=sec('more','🎧','延伸：ccifellowship.org 要理问答证道',f'<div class="card reveal"><ul class="clean">{"".join(f"<li>🗣️ <a href=\"{s["url"]}\" target=\"_blank\" rel=\"noopener\">{esc(s["title"])}</a></li>" for s in sers)}</ul><p class="small muted">证道作者 Clarence Stam（加拿大改革宗教会牧师），中文译本由 ccifellowship.org 提供。</p></div>')
    prev=f'<a id="prevLd" href="{n-1:02d}.html">⬅ {esc(ld_label(n-1))}</a>' if n>1 else '<a href="../lorddays.html">⬅ 52主日总览</a>'
    nxt=f'<a id="nextLd" class="r" href="{n+1:02d}.html">{esc(ld_label(n+1))} ➡</a>' if n<52 else '<a class="r" href="../memory.html">🧠 去速记中心 ➡</a>'
    body=hero+s0+s1+s2+s3+s4+s5+s6+s7+f'<div class="pager">{prev}{nxt}</div>'
    page(f'ld/{n:02d}.html',f'主日{n} {no["t"]}',body,desc=f'海德堡要理问答主日{n}：{no["t"]}——{no["k"]}')
for ld in D['hc']: ld_page(ld)
print('LD pages done')
