from common import *
from notes4 import X
from notes7 import E
import svgs, random
def strip_tags(s): return re.sub('<[^>]+>','',s)
def first(s,k=1):
    parts=[x for x in re.split(r'(?<=[。！？])',s) if x.strip()]
    return ''.join(parts[:k])
def kwmark(s,kws):
    for k in kws:
        if k and k in s: s=s.replace(esc(k),f'<span class="mk-b">{esc(k)}</span>',1)
    return s
def _sents(x): return [y for y in re.split(r'(?<=[。！？；])',x) if y.strip()]
def _bg(x): x=re.sub(r'[^\u4e00-\u9fff]','',re.sub(r'[=*_~!]','',x)); return {x[i:i+2] for i in range(len(x)-1)}
DSTAT=[0,0]
def distill(no,st,ch,th,trap,ex=()):
    """v6: drop a commentary sentence when >=62% of its content already appears in a sentence shown elsewhere on the page."""
    shown=[z for z in (_bg(y) for t in [th,trap]+list(no['core'])+list(no['app'][:1])+list(ex) for y in _sents(t)) if z]
    out={}
    for k,v in [('big',no['big']),('cov',no['cov']),('story',st),('christ',ch),('why',no['why']),('hard',no['hard'])]:
        keep=[]
        for y in _sents(v):
            a=_bg(y); DSTAT[0]+=1
            if (len(a)>=8 or len(a)<8 and any(a==b for b in shown)) and any(len(a&b)/len(a)>=.62 for b in shown): DSTAT[1]+=1; continue
            keep.append(y); shown.append(a)
        out[k]=''.join(keep).strip()
    return out
def ld_page(ld):
    n=ld['n']; no=N[n]; p=part(n); c=p[2]; a,b=qrange(ld); th,trap,gold=T[n]
    st,ch,pr,dq=X[n]
    e7=E[n]
    F=distill(no,st,ch,th,trap,[x for x in [e7['so'],e7['do'],e7.get('deep','')]+[a for a,_ in e7['ch']] if x])
    goldq=next(qnum(q) for q in ld['qas'] if any(gold in x for x in q['a']))
    K=lambda s:kwmark(esc(s),no['kw'])
    crumbs=' › '.join(ld['crumbs']) or '引言'
    qr=f'第{a}{"–"+str(b) if b!=a else ""}问'
    kws=''.join(f'<span class="chip {p[0]}">🔑 {esc(k)}</span>' for k in no['kw'])
    hero=f'''<section class="hero reveal" style="background:linear-gradient(135deg,color-mix(in srgb,{c} 32%,transparent),color-mix(in srgb,{c} 6%,transparent))"><div class="tags"><span class="chip {p[0]}">{p[3]} {esc(p[1])}</span><span class="chip">🧭 {esc(crumbs)}</span><span class="chip">❓ {qr} · 共{len(ld['qas'])}问</span></div>
<h1>{LDI[n]} 主日 {n}　{esc(no['t'])}</h1><p class="ldq"><span class="qi" aria-hidden="true">❓</span><span><b>本主日回答：</b>{esc(e7['q'])}</span></p>{callout('core','核心',md(th))}{callout('hook','记忆钩',f'<b style="font-family:var(--serif);font-size:1.1em">{esc(no["k"])}</b>')}<div class="tags">{kws}</div>
<div class="chart" style="margin-top:14px">{svgs.ld_strip(n)}</div><div class="small muted">全书位置 {n}/52 · {qr}</div>
<div class="btns" style="margin-top:14px"><button class="btn" id="reciteBtn">🙈 背诵模式 (R)</button><button class="btn" id="supBtn">🔢 脚注编号</button><button class="btn" data-marks>🖍️ 标记 (M)</button><a class="btn" href="../memory.html#marks" title="标记图例">🗂️ 图例</a><button class="btn" id="readAll">🎧 连续朗读</button><button class="btn pri" id="doneBtn" data-ld="{n}">☑️ 标记已学完</button></div></section>'''
    # 1. essence
    keyrefs='　'.join(f'<a href="#q{qnum(q)}" class="chip" style="white-space:nowrap">Q{qnum(q)} · {esc(q["refs"][0].split("；")[0])}</a>' for q in ld['qas'] if q['refs'])+'<span class="src">　（原文脚注首条）</span>'
    bridge=(f'<a class="node" href="{n-1:02d}.html">⬅ 承接<br><b>{esc(ld_label(n-1))}</b></a>' if n>1 else '<span class="node">🚪 全书开端</span>')+'<span class="arr">➜</span>'+f'<span class="node" style="border-color:{c}"><b>{esc(ld_label(n))}</b><br><span class="small">{esc(no["k"])}</span></span><span class="arr">➜</span>'+(f'<a class="node" href="{n+1:02d}.html">引出 ➡<br><b>{esc(ld_label(n+1))}</b></a>' if n<52 else '<span class="node">🙌 阿们：全书结束</span>')
    nrefs=sum(len(q['refs']) for q in ld['qas']); nx=len(no['bc'])+len(no['cd'])+len(no['wsc'])
    kpi=''.join(f'<div><b>{v}</b>{t}</div>' for v,t in [(len(ld['qas']),'问答'),(nrefs,'经文组'),(nx,'信条对照'),(len(no['kw']),'关键词')])
    wwa=f'<div class="wwa reveal"><div class="w1"><b class="wl">💡 为什么重要</b><p>{K(e7["so"])}</p></div><div class="w2"><b class="wl">🏃 本周操练</b><p>{K(e7["do"])}</p></div></div>'
    s0=sec('essence','💎',f'精华：主日{n}的骨架',wwa+f'''<div class="grid g2"><div class="card reveal"><h3 id="ess-core">📌 要义（本站概述，以原文为准）</h3><ol class="core">{"".join(f"<li>{K(x)}</li>" for x in no['core'])}</ol><div class="kpi mini">{kpi}</div>
{callout('gold','金句',f'“{esc(gold)}”<span class="src">　—— 原文第{goldq}问（逐字）</span>')}{callout('trap','易错',md(trap)+' '+''.join(f'<span class="chip err">❌ {esc(x)}</span>' for x in no['err']))}{callout('bible','核心经文',keyrefs)}</div>
<div class="card reveal"><h3 id="ess-map">关联星图</h3><div class="chart">{svgs.ld_constellation(n,ld,no)}</div><p class="small muted" style="margin:6px 0 0">点节点跳到问答 / 信条；外圈为关键词与比利时信条、多特信经。</p></div></div>
<div class="card reveal" style="margin-top:14px"><h3 id="ess-bridge">🔗 承上启下：在全书中的位置</h3><div class="chain bridge">{bridge}</div></div>''')
    # 2. text
    chain=[]
    for i,q in enumerate(ld['qas']):
        qt=re.sub(r'^\d+[．.]\s*问：','',q['q'])
        if i: chain.append('<span class="arr">➜</span>')
        chain.append(f'<div class="node" style="--c:{c}"><b>Q{qnum(q)}</b> {esc(qt)}</div>')
    s1=sec('text','📜','原文：中文《海德堡要理问答》',f'<p class="src">逐字引自 <a href="{ld["url"]}" target="_blank" rel="noopener">ccifellowship.org · 主日{n}</a>；上标＝经文出处。</p><details class="mklgd card" style="margin:0 0 12px;padding:8px 12px"><summary class="small">🖍️ 本主日笔记标记（数字＝本页出现次数）· 全部 / 仅核心 / 关（M）</summary>'+legend_html(False)+f'</details><div class="card reveal nolv" style="margin-bottom:12px"><b class="small muted">🔗 问题推进</b><div class="chain" style="margin-top:6px">{"".join(chain)}</div></div>'+''.join(qa_html(q,c,lv=2) for q in ld['qas']))
    # 3. whole
    act=ld_act(n)
    acts=''.join(f'<span class="act{" on" if k==act else ""}">{i} {t}</span>' for k,i,t in ACTS)
    qchips=''.join(f'<a class="chip" href="#q{qnum(q)}">Q{qnum(q)}</a>' for q in ld['qas'])
    rungs=[('🌍 圣经大戏',f'<div class="acts">{acts}</div>'),('🤝 圣约阶段',esc(ld_cov(n))),('🏛️ 教义主题',esc(ld_locus(n))),('📘 要理问答',f'{p[3]} {esc(p[1])}'+''.join(f' › {esc(x)}' for x in ld['crumbs'] if not x.startswith('第') or '部' not in x[:4])),('📅 本主日',f'<b>{esc(ld_label(n))}</b> — {esc(no["k"])}'),('❓ 各问',qchips)]
    zoom='<div class="card reveal zoom"><h3 id="w-zoom">🔭 从整体到局部：六级缩放</h3><ol class="ladder">'+''.join(f'<li style="--i:{i}"><span class="rl">{h}</span><span class="rv2">{v}</span></li>' for i,(h,v) in enumerate(rungs))+'</ol></div>'
    W=[('big','w-bible','📖 整本圣经'),('cov','w-cov','🤝 圣约神学'),('story','w-story','📚 圣经画面'),('christ','w-christ','✝️ 指向基督')]
    PC={'big':'big','cov':'cov','story':'core','christ':'xref'}
    wc=''.join(f'<div class="card pan {PC[k]} reveal"><h3 id="{i}">{t}</h3><p>{K(F[k])}</p></div>' for k,i,t in W if F[k])
    CH=[('📜','旧约 · 应许与预表','var(--intro)'),('✝️','基督 · 成全','var(--misery)'),('⛪','今天 · 教会与我','var(--grat)')]
    cch='<div class="card reveal"><h3 id="w-chain">🧬 圣约链：应许 → 成全 → 今天</h3><ol class="cch">'+''.join(f'<li style="--c:{cc};--i:{i}"><span class="ci" aria-hidden="true">{ic}</span><b class="cl">{lab}</b><span class="ct">{K(t)}</span><span class="cr">📖 {esc(r)}</span></li>' for i,((ic,lab,cc),(t,r)) in enumerate(zip(CH,e7['ch'])))+'</ol><p class="small muted" style="margin:8px 0 0">同一位立约的神：旧约的应许在基督里成为“是的”，今天藉圣言与圣礼临到教会（林后1:20）。本站学习笔记。</p></div>'
    s2=sec('whole','🌍','整体：圣经神学 · 圣约神学 · 基督中心',cch+'<div style="height:14px"></div>'+zoom+f'<div style="height:14px"></div><div class="grid g2">{wc}</div>')
    # 4. local
    lc=[]
    if F['why']: lc.append(f'<div class="card pan why reveal"><h3 id="why">🏛️ 背景：为什么这样写？</h3><p>{K(F["why"])}</p></div>')
    if F['hard']: lc.append(f'<div class="card pan hard reveal"><h3 id="hard">⚠️ 难点</h3>{callout("hard","难点",K(F["hard"]))}</div>')
    if e7.get('deep'): lc.append(f'<div class="card pan core reveal" style="grid-column:1/-1"><h3 id="deep">🔬 深化：本主日的关键细节</h3><p>{K(e7["deep"])}</p></div>')
    s3=sec('local','🔍','局部：背景与难点','<div class="grid g2">'+''.join(lc)+'</div>') if lc else ''
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
    cards=''.join(f'<div class="fc" style="--c:{c}"><div class="in"><div class="f"><div class="big">Q{qnum(q)}</div><div>{esc(re.sub(r"^\d+[．.]\s*问：","",q["q"]))}</div></div><div class="b">{"".join(f"<p>{x}</p>" for x in q["a"])}</div></div></div>' for q in ld['qas'])
    qz=no['quiz']; opts=''.join(f'<button class="opt">{"ABCD"[i]}. {esc(o)}</button>' for i,o in enumerate(qz[1]))
    sortq=''
    if len(ld['qas'])>=2:
        items=[(qnum(q),re.sub(r'^\d+[．.]\s*问：','',q['q'])) for q in ld['qas']]
        rnd=random.Random(n); sh=items[:]
        while sh==items: rnd.shuffle(sh)
        sortq=f'''<h3 id="m-sort">🧩 排序挑战：把本主日的问题排回原来的顺序</h3><div class="card reveal sortbox"><p class="small muted">拖动或用 ↑↓ 排序，再点“检查”。</p><ol class="sortq">{"".join(f'<li data-q="{qn}" style="--c:{c}"><span class="grip" aria-hidden="true">⠿</span><span class="st">{esc(t)}</span><span class="mv"><button type="button" data-up aria-label="上移">↑</button><button type="button" data-down aria-label="下移">↓</button></span></li>' for qn,t in sh)}</ol><div class="btns"><button class="btn pri" data-sortcheck>✅ 检查</button><button class="btn" data-sortshuffle>🔀 重新打乱</button></div><p class="res key"></p></div>'''
    cloze=f'''<h3 id="m-cloze">✍️ 填空背诵：标记的关键短语变成空格</h3><div class="card reveal clozebox" data-cloze><p class="small muted">空格取自原文标记短语。</p><div class="btns"><button class="btn pri" data-clozestart>▶️ 开始填空</button><button class="btn" data-clozecheck>✅ 检查</button><button class="btn" data-clozeshow>👀 显示答案</button></div><div class="clozeout"></div><p class="res key"></p></div>'''
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
print("distill dropped sentences:",DSTAT[1],"/",DSTAT[0])
