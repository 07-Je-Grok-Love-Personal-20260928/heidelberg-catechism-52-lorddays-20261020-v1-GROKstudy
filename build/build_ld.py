from common import *
from notes4 import X
def strip_tags(s): return re.sub('<[^>]+>','',s)
def ld_page(ld):
    n=ld['n']; no=N[n]; p=part(n); c=p[2]; a,b=qrange(ld)
    crumbs=' › '.join(ld['crumbs']) or '引言'
    kws=''.join(f'<span class="chip {p[0]}">🔑 {esc(k)}</span>' for k in no['kw'])
    pos=f'<div style="height:8px;border-radius:8px;background:var(--card2);margin-top:16px;overflow:hidden"><div style="width:{n/52*100:.1f}%;height:100%;background:linear-gradient(90deg,var(--intro),{c})"></div></div><div class="small muted" style="margin-top:4px">全书进度 {n}/52 · 第 {a}{"–"+str(b) if b!=a else ""} 问</div>'
    hero=f'''<section class="hero reveal" style="background:linear-gradient(135deg,color-mix(in srgb,{c} 34%,transparent),color-mix(in srgb,{c} 8%,transparent))"><div class="tags"><span class="chip {p[0]}">{p[3]} {esc(p[1])}</span><span class="chip">🧭 {esc(crumbs)}</span><span class="chip">❓ 第{a}{"–"+str(b) if b!=a else ""}问 · 共{len(ld['qas'])}问</span></div>
<h1>主日 {n}　{esc(no['t'])}</h1><div class="mn">🧠 口诀：{esc(no['k'])}</div><div class="tags">{kws}</div>{pos}
<div class="btns" style="margin-top:16px"><button class="btn" id="reciteBtn">🙈 背诵模式 (R)</button><button class="btn" id="supBtn">🔢 隐藏/显示脚注</button><button class="btn pri" id="doneBtn" data-ld="{n}">☑️ 标记已学完</button></div></section>'''
    # logic chain
    chain=[]
    for i,q in enumerate(ld['qas']):
        qt=re.sub(r'^\d+[．.]\s*问：','',q['q'])
        if i: chain.append('<span class="arr">➜</span>')
        chain.append(f'<div class="node" style="--c:{c}"><b>Q{qnum(q)}</b> {esc(qt)}</div>')
    s1=f'<section class="sec"><h2 id="text"><span class="ico">📜</span>原文：中文《海德堡要理问答》</h2><p class="src">以下问答一字不改地引自 <a href="{ld["url"]}" target="_blank" rel="noopener">ccifellowship.org · 主日{n}</a>（脚注数字对应经文出处）。</p>'+''.join(qa_html(q,c) for q in ld['qas'])+'</section>'
    s2=f'<section class="sec"><h2 id="flow"><span class="ico">🔗</span>逻辑链：问题如何一步步推进</h2><div class="card reveal"><div class="chain">{"".join(chain)}</div></div></section>'
    s3=f'''<section class="sec"><h2 id="whole"><span class="ico">🌍</span>先看整体：圣经神学与圣约神学</h2><div class="grid g2">
<div class="card pan big reveal"><h3>📖 整本圣经的视角</h3><p>{esc(no['big'])}</p></div>
<div class="card pan cov reveal"><h3>🤝 圣约神学的视角</h3><p>{esc(no['cov'])}</p></div></div></section>'''
    s4=f'''<section class="sec"><h2 id="local"><span class="ico">🔍</span>再看局部：背景、要点、难点</h2>
<div class="card pan why reveal"><h3 id="why">🏛️ 真实背景：为什么这样写？</h3><p>{esc(no['why'])}</p></div><div style="height:16px"></div>
<div class="card pan core reveal"><h3 id="core">💎 核心要点：写了什么？</h3><ol class="core">{"".join(f"<li>{esc(x)}</li>" for x in no['core'])}</ol><p class="small muted">（要点为本站概述，原文以上方引文为准。）</p></div><div style="height:16px"></div>
<div class="hardbox reveal"><b>⚠️ 难点剖析：</b>{esc(no['hard'])}</div><div style="height:16px"></div>
<div class="card pan err reveal"><h3 id="err">🛡️ 本主日驳斥或防范的错误</h3><div class="tags" style="display:flex;flex-wrap:wrap;gap:8px">{"".join(f'<span class="chip err">❌ {esc(x)}</span>' for x in no['err'])}</div></div></section>'''
    # xref
    xs=[]
    for k in no['bc']:
        art=BC[k]; body=''.join(f'<p>{x}</p>' for x in art['paras'])
        xs.append(f'<details class="card" style="margin:8px 0"><summary style="cursor:pointer"><b style="color:var(--deliv)">🛡️ 比利时信条 {esc(art["title"])}</b></summary><div class="reading" style="font-size:16px;line-height:1.95;margin-top:8px">{body}</div><p class="src">原文：<a href="{art["url"]}" target="_blank" rel="noopener">{art["url"]}</a> · <a href="../texts/bc.html#bc{k}">在本站阅读版中打开</a></p></details>')
    for s in no['cd']:
        sec,st,arts=parse_cd(s)
        for art in arts:
            body=''.join(f'<p>{x}</p>' for x in art['paras'])
            xs.append(f'<details class="card" style="margin:8px 0"><summary style="cursor:pointer"><b style="color:var(--grat)">🌷 多特信经 {esc(st)} · {esc(art["title"])}</b></summary><div class="reading" style="font-size:16px;line-height:1.95;margin-top:8px">{body}</div><p class="src">原文：<a href="{art["url"]}" target="_blank" rel="noopener">{art["url"]}</a></p></details>')
    wsc=''
    if no['wsc']:
        wsc='<p>🏴 <b>威斯敏斯特小要理问答（长老会改革宗）对照：</b>'+'、'.join(f'第{x}问' for x in no['wsc'])+'（英文原文见 <a href="https://opc.org/sc.html" target="_blank" rel="noopener">opc.org/sc.html</a>）</p>'
        for x in no['wsc']:
            if x in WSC_EN: wsc+=f'<blockquote class="small" style="margin:6px 0;padding:8px 12px;border-left:3px solid var(--gold);background:var(--card2);border-radius:8px" lang="en">{esc(WSC_EN[x])}<br><span class="muted">— Westminster Shorter Catechism, opc.org</span></blockquote>'
    s5=f'<section class="sec"><h2 id="xref"><span class="ico">🧩</span>三项联合信条交叉对照（原文可展开）</h2><div class="card pan xref reveal">{"".join(xs) or "<p class=muted>本主日内容主要在要理问答中独立展开。</p>"}{wsc}</div></section>'
    s6=f'<section class="sec"><h2 id="app"><span class="ico">🌱</span>怎么应用？</h2><div class="card pan app reveal"><ul class="clean">{"".join(f"<li>✅ {esc(x)}</li>" for x in no["app"])}</ul></div></section>'
    st,ch,pr,dq=X[n]
    s6b=f'''<section class="sec"><h2 id="deep"><span class="ico">🪔</span>深化：圣经故事 · 基督中心 · 祷告 · 讨论</h2><div class="grid g2">
<div class="card pan big reveal"><h3>📚 圣经中的一个画面</h3><p>{esc(st)}</p></div>
<div class="card pan cov reveal"><h3>✝️ 如何指向基督</h3><p>{esc(ch)}</p></div>
<div class="card pan app reveal"><h3>🙏 一句祷告</h3><p style="font-family:var(--serif)">{esc(pr)}</p></div>
<div class="card pan why reveal"><h3>💬 小组 / 家庭讨论</h3><ol class="clean">{''.join(f"<li>{esc(x)}</li>" for x in dq)}</ol></div></div></section>'''
    # memory
    cards=''.join(f'<div class="fc reveal" style="--c:{c}"><div class="in"><div class="f"><div class="small muted">点击翻转</div><div class="big">Q{qnum(q)}</div><div>{esc(re.sub(r"^\d+[．.]\s*问：","",q["q"]))}</div></div><div class="b">{"".join(f"<p>{x}</p>" for x in q["a"])}</div></div></div>' for q in ld['qas'])
    qz=no['quiz']; opts=''.join(f'<button class="opt">{"ABCD"[i]}. {esc(o)}</button>' for i,o in enumerate(qz[1]))
    s7=f'''<section class="sec"><h2 id="memo"><span class="ico">🧠</span>快速记忆：卡片 + 小测</h2><div class="grid">{cards}</div>
<div class="card quiz reveal" data-ans="{qz[2]}" data-id="ld{n}" style="margin-top:16px"><h3>🎯 小测验</h3><p><b>{esc(qz[0])}</b></p>{opts}<p class="res key"></p></div></section>'''
    sers=[s for s in SER if s['ld']==n]
    s8=f'<section class="sec"><h2 id="more"><span class="ico">🎧</span>延伸阅读：ccifellowship.org 要理问答证道</h2><div class="card reveal"><ul class="clean">{"".join(f"<li>🗣️ <a href=\"{s["url"]}\" target=\"_blank\" rel=\"noopener\">{esc(s["title"])}</a></li>" for s in sers)}</ul><p class="small muted">证道作者 Clarence Stam（加拿大改革宗教会牧师），中文译本由 ccifellowship.org 提供。</p></div></section>'
    prev=f'<a id="prevLd" href="{n-1:02d}.html">⬅ 主日{n-1} · {esc(N[n-1]["t"])}</a>' if n>1 else '<a href="../lorddays.html">⬅ 52主日总览</a>'
    nxt=f'<a id="nextLd" class="r" href="{n+1:02d}.html">主日{n+1} · {esc(N[n+1]["t"])} ➡</a>' if n<52 else '<a class="r" href="../memory.html">🧠 去速记中心 ➡</a>'
    body=hero+s1+s2+s3+s4+s5+s6+s6b+s7+s8+f'<div class="pager">{prev}{nxt}</div>'
    page(f'ld/{n:02d}.html',f'主日{n} {no["t"]}',body,desc=f'海德堡要理问答主日{n}：{no["t"]}——{no["k"]}')
for ld in D['hc']: ld_page(ld)
print('LD pages done')
