import json,re,html,os,sys
sys.path.insert(0,os.path.dirname(__file__))
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE=os.path.join(ROOT,'site')
D=json.load(open(os.path.join(ROOT,'data.json')))
SER=json.load(open(os.path.join(ROOT,'sermons.json')))
from notes1 import N as _a; from notes2 import N as _b; from notes3 import N as _c
N={**_a,**_b,**_c}
VERSION='v1'; DATE='2026-10-20'
REPO='heidelberg-catechism-52-lorddays-20261020-v1-GROKstudy'
CCI='https://ccifellowship.org'
def esc(s): return html.escape(s,quote=True)
def part(n):
    if n==1: return ('i','引言','var(--intro)','💜')
    if n<=4: return ('m','第一部 罪与愁苦','var(--misery)','💔')
    if n<=31: return ('d','第二部 得救','var(--deliv)','✝️')
    return ('g','第三部 感恩','var(--grat)','🌿')
GROUPS=[('i','引言',1,1,'唯一的安慰'),('m','第一部',2,2,'律法的镜子'),('m','第一部',3,3,'创造与堕落'),('m','第一部',4,4,'神的公义'),
 ('d','第二部',5,7,'中保与真信心'),('d','第二部',8,8,'三位一体'),('d','第二部',9,10,'父神与创造'),('d','第二部',11,19,'子神与救赎'),('d','第二部',20,22,'圣灵与成圣'),
 ('d','第二部',23,24,'因信称义'),('d','第二部',25,25,'圣言与圣礼'),('d','第二部',26,27,'圣洗礼'),('d','第二部',28,30,'圣餐'),('d','第二部',31,31,'天国钥匙'),
 ('g','第三部',32,33,'感恩与归正'),('g','第三部',34,44,'十诫'),('g','第三部',45,52,'主祷文')]
def qnum(q): return int(re.match(r'(\d+)',q['q']).group(1))
def qrange(ld):
    ns=[qnum(q) for q in ld['qas']]; return (ns[0],ns[-1])
BC={a['n']:a for a in D['bc']}
CDS={s['sec']:s for s in D['cd']}
SECMAP=[('第三、四项','section3-4'),('第一项','section1'),('第二项','section2'),('第五项','section5')]
def parse_cd(s):
    sec=None
    for k,v in SECMAP:
        if s.startswith(k): sec=v;break
    arts=CDS[sec]['arts']; res=[]
    rest=s.split('教义',1)[1]
    m=re.findall(r'第([\d、\-]+)条',rest.replace('错谬反驳第','X'))
    for grp in m:
        for piece in grp.split('、'):
            if '-' in piece:
                a,b=piece.split('-'); res+=list(range(int(a),int(b)+1))
            else: res.append(int(piece))
    found=[a for a in arts if a['n'] in res and a['title']!='错谬反驳']
    if '错谬反驳' in rest:
        found+= [a for a in arts if a['title']=='错谬反驳']
    return sec,CDS[sec]['title'],found
WSC_EN={1:"Q. 1. What is the chief end of man? A. Man’s chief end is to glorify God, and to enjoy him forever.",
20:"Q. 20. Did God leave all mankind to perish in the estate of sin and misery? A. God having, out of his mere good pleasure, from all eternity, elected some to everlasting life, did enter into a covenant of grace, to deliver them out of the estate of sin and misery, and to bring them into an estate of salvation by a redeemer.",
33:"Q. 33. What is justification? A. Justification is an act of God’s free grace, wherein he pardoneth all our sins, and accepteth us as righteous in his sight, only for the righteousness of Christ imputed to us, and received by faith alone.",
86:"Q. 86. What is faith in Jesus Christ? A. Faith in Jesus Christ is a saving grace, whereby we receive and rest upon him alone for salvation, as he is offered to us in the gospel.",
92:"Q. 92. What is a sacrament? A. A sacrament is an holy ordinance instituted by Christ; wherein, by sensible signs, Christ, and the benefits of the new covenant, are represented, sealed, and applied to believers.",
12:"Q. 12. What special act of providence did God exercise toward man in the estate wherein he was created? A. When God had created man, he entered into a covenant of life with him, upon condition of perfect obedience; forbidding him to eat of the tree of the knowledge of good and evil, upon pain of death."}
LOGO='<svg class="logo" viewBox="0 0 64 64" aria-hidden="true"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#a78bfa"/><stop offset=".5" stop-color="#60a5fa"/><stop offset="1" stop-color="#34d399"/></linearGradient></defs><rect x="4" y="4" width="56" height="56" rx="16" fill="url(#lg)"/><path d="M32 13v38M20 25h24" stroke="#fff" stroke-width="6" stroke-linecap="round"/><circle cx="32" cy="51" r="0"/></svg>'
NAV=[('index.html','🏠 首页'),('bible.html','📖 圣经与圣约'),('history.html','🗺️ 历史地理'),('lorddays.html','📅 52主日'),('texts/hc.html','📜 要理问答'),('texts/bc.html','🛡️ 比利时信条'),('texts/cd.html','🌷 多特信经'),('texts/creeds.html','⛪ 普世信经'),('compare.html','⚖️ 信条对比'),('memory.html','🧠 速记'),('sources.html','🔗 资料')]
def gnav(pre):
    out=['<h4>🧭 全站导航</h4><div id="gnav" class="toc">']
    for h,t in NAV: out.append(f'<a href="{pre}{h}">{t}</a>')
    out.append('</div><details style="margin:10px 4px"><summary class="small muted" style="cursor:pointer">📅 52 个主日速达</summary><div class="toc">')
    for n in range(1,53):
        p=part(n); out.append(f'<a href="{pre}ld/{n:02d}.html" style="border-left-color:{p[2]}">主日{n} · {esc(N[n]["t"])}</a>')
    out.append('</div></details>')
    return ''.join(out)
def page(path,title,body,desc='',head=''):
    depth=path.count('/'); pre='../'*depth
    navh=''.join(f'<a href="{pre}{h}" class="{"on" if h==path else ""}">{t}</a>' for h,t in NAV)
    doc=f'''<!doctype html><html lang="zh-Hans" data-theme="dark"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(title)} | 海德堡要理问答 52 主日深度解析</title><meta name="description" content="{esc(desc or title)}"><meta name="theme-color" content="#0b1020">
<link rel="icon" href="data:image/svg+xml,{esc(LOGO.replace('class="logo" ','').replace('#','%23'))}">
<link rel="stylesheet" href="{pre}assets/css/style.css">{head}</head><body>
<div class="bgfx"><i></i><i></i><i></i></div>
<header class="topbar"><button class="ibtn" id="tocBtn" title="显示/隐藏目录 (T)" aria-label="目录">☰</button><a class="brand" href="{pre}index.html">{LOGO}<b>海德堡要理问答 · 52主日</b></a><nav class="nav">{navh}</nav><button class="ibtn" id="themeBtn" title="切换深浅色" aria-label="主题">🌓</button></header>
<div class="progress"></div><div class="backdrop"></div>
<div class="layout"><aside class="side"><input id="tocSearch" class="tocsearch" placeholder="🔍 过滤目录…"><h4>📑 本页目录</h4><div id="toc" class="toc"></div><hr style="border:none;border-top:1px solid var(--bd);margin:14px 0">{gnav(pre)}</aside>
<main><div class="wrap">{body}
<footer class="foot">📚 信条、信经原文一字不改地引自 <a href="{CCI}/books/book-of-praise">基督教华人网络团契 ccifellowship.org《中国改革宗敬拜手册》(2015)</a>，版权归原出版委员会所有，此处仅作学习引用并逐条注明出处。解读部分为本站原创学习笔记，持守欧陆改革宗三项联合信条。· 版本 {VERSION} · {DATE} · <a href="https://github.com/07-Je-Grok-Love-Personal-20260928/{REPO}">GitHub 源码</a></footer>
</div></main></div>
<div class="fab"><button class="ibtn" id="topBtn" title="回到顶部">⬆</button></div>
<script src="{pre}assets/js/app.js"></script></body></html>'''
    fp=os.path.join(SITE,path); os.makedirs(os.path.dirname(fp),exist_ok=True)
    open(fp,'w').write(doc)
def qa_html(q,c,anchor=True,tools=True):
    n=qnum(q)
    qtext=esc(q['q'])
    a=''.join(f'<p>{p}</p>' for p in q['a'])
    refs=''.join(f'<li>{esc(r)}</li>' for r in q['refs'])
    rd=f'<details><summary>📖 经文出处（{len(q["refs"])}）</summary><ol class="refs">{refs}</ol></details>' if q['refs'] else ''
    t='<div class="tools"><button data-speak title="朗读">🔊</button><button data-copy title="复制">📋</button></div>' if tools else ''
    return f'<div class="qa reveal" id="q{n}" style="--c:{c}">{t}<div class="q"><span class="qn">Q{n}</span><span>{qtext}</span></div><div class="a">{a}</div>{rd}</div>'
