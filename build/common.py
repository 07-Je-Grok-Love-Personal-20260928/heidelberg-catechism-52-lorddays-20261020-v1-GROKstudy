import json,re,html,os,sys
sys.path.insert(0,os.path.dirname(__file__))
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE=os.path.join(ROOT,'site')
D=json.load(open(os.path.join(ROOT,'data.json')))
SER=json.load(open(os.path.join(ROOT,'sermons.json')))
from notes1 import N as _a; from notes2 import N as _b; from notes3 import N as _c
N={**_a,**_b,**_c}
VERSION='v5'; DATE='2026-10-21'
REPO='heidelberg-catechism-52-lorddays-GROKstudy'
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

from notes5 import KQ,T
from bs4 import BeautifulSoup, NavigableString
NAV=[('index.html','🏠','首页'),('bible.html','📖','圣经与圣约'),('history.html','🗺️','历史地理'),('lorddays.html','📅','52主日'),('texts/index.html','📜','原文'),('compare.html','⚖️','对比'),('memory.html','🧠','速记'),('search.html','🔎','搜索')]
GNAV=[('index.html','🏠 首页'),('bible.html','📖 圣经与圣约'),('history.html','🗺️ 历史地理'),('lorddays.html','📅 52主日总览'),('texts/index.html','📜 原文中心'),('texts/hc.html','　📜 海德堡要理问答'),('texts/bc.html','　🛡️ 比利时信条'),('texts/cd.html','　🌷 多特信经'),('texts/creeds.html','　⛪ 三大普世信经'),('compare.html','⚖️ 三项信条对比'),('memory.html','🧠 速记中心'),('search.html','🔎 全文搜索'),('sources.html','🔗 资料与说明'),('changelog.html','🆕 版本更新')]

# ---------- v4: ONE canonical title + icon table for all 52 Lord's Days ----------
LDI={1:'✝️',2:'🪞',3:'🍎',4:'⚖️',5:'🤝',6:'👑',7:'🔑',8:'🔺',9:'🌍',10:'🛡️',11:'🌟',12:'🫒',13:'👶',14:'🌱',15:'🩸',16:'⚰️',17:'🌅',18:'☁️',19:'🏛️',20:'🕊️',21:'⛪',22:'🌄',23:'📜',24:'🎁',25:'📖',26:'💧',27:'👪',28:'🍞',29:'🍷',30:'🚫',31:'🗝️',32:'🌿',33:'🔄',34:'🪨',35:'🗿',36:'🗣️',37:'🤚',38:'🕯️',39:'👨‍👩‍👧',40:'❤️‍🩹',41:'💍',42:'💰',43:'🗨️',44:'💭',45:'🙏',46:'👨‍👧',47:'✨',48:'🏰',49:'🧭',50:'🌾',51:'🤲',52:'⚔️'}
def ld_title(n): return N[n]['t']
def ld_label(n): return f'{LDI[n]} 主日{n} · {N[n]["t"]}'
PARTS=[('i','💜','引言','唯一的安慰',1,1),('m','💔','第一部','罪与愁苦',2,4),('d','✝️','第二部','得救',5,31),('g','🌿','第三部','感恩',32,52)]
def part_label(k):
    for kk,ic,a,b,s,e in PARTS:
        if kk==k: return f'{ic} {a} · {b}（主日{s}–{e}）' if s!=e else f'{ic} {a} · {b}（主日{s}）'
SUBI={'子神和我们的得赎':'🩸','圣灵神和我们的成圣':'🕊️','我们得称为义':'⚖️','圣言与圣礼':'📖','圣洗礼':'💧','圣餐':'🍞','十诫':'🪨','祷告':'🙏'}
BCG=[(1,1,'论神','👁️'),(2,7,'论启示与圣经','📖'),(8,11,'论三位一体','🔺'),(12,13,'论创造与护理','🌍'),(14,15,'论人与罪','🍎'),(16,17,'论拣选与应许','🌟'),(18,21,'论基督','✝️'),(22,26,'论救恩','🎁'),(27,32,'论教会','⛪'),(33,35,'论圣礼','💧'),(36,36,'论政府','🏛️'),(37,37,'论末后审判','⚖️')]
def bc_icon(k): return next(i for s,e,t,i in BCG if s<=k<=e)
CDI={'section1':'🌟','section2':'🩸','section3-4':'🔄','section5':'🛡️'}
def art_short(t): return re.sub(r'^第[一二三四五六七八九十]+条\s*','',t)
CN='一二三四五六七八九十'
def cnum(i):
    if i<=10: return CN[i-1]
    if i<20: return '十'+CN[i-11]
    return CN[i//10-1]+'十'+(CN[i%10-1] if i%10 else '')
def sec(id,ico,title,inner,cls=''):
    title=re.sub(r'^[一二三四五六七八九十]+、','',title)
    return f'<section class="sec {cls}"><h2 id="{id}"><span class="ico">{ico}</span>{title}</h2>{inner}</section>'
# ---------- marking system ----------
MD=[(r'\*\*(.+?)\*\*','mk-b'),(r'==(.+?)==','mk-k'),(r'~~(.+?)~~','mk-w'),(r'__(.+?)__','mk-u'),(r'::(.+?)::','mk-d'),(r'!!(.+?)!!','mk-r')]
def md(s):
    s=esc(s)
    for pat,c in MD: s=re.sub(pat,lambda m:f'<span class="{c}">{m.group(1)}</span>',s)
    return s
GLOSS=[(t,'mk-u') for t in ['恩典之约','行为之约','救赎之约','生命之约','盟约元首','盟约记号','盟约','代赎','归算','称义','成圣','重生','中保','三重职分','收养','预定','拣选','圣礼','圣约','道成肉身','神人二性','降在阴间','圣徒相通','天国的钥匙','教会纪律','律法的第三功用','治死旧人','活出新人','真信心','护理','受膏','大先知','大祭司','君王','记号与印记','属灵的同在','代求','再来','身体复活','永生','好行为','悔改','归正']]+\
      [(t,'mk-d') for t in ['罗马天主教','罗马教','特伦托','重洗派','路德宗','路德派','亚米念','阿民念','抗辩派','伯拉纠','苏西尼','亚流','变质说','弥撒','普救论','完美主义','律法主义','反律主义','神秘主义','自由主义','成功神学']]+\
      [(t,'mk-k') for t in ['唯独恩典','唯独信心','唯独基督','唯独圣经','唯一的安慰']]
GRE=re.compile('|'.join(sorted({re.escape(t) for t,_ in GLOSS},key=len,reverse=True)))
GCL=dict(GLOSS)
REFRE=re.compile(r'(?<![\u4e00-\u9fa5])(?:创|出|利|民|申|书|士|得|撒上|撒下|王上|王下|代上|代下|拉|尼|斯|伯|诗|箴|传|歌|赛|耶|哀|结|但|何|珥|摩|俄|拿|弥|鸿|哈|番|该|亚|玛|太|可|路|约|徒|罗|林前|林后|加|弗|腓|西|帖前|帖后|提前|提后|多|门|来|雅|彼前|彼后|约壹|约贰|约叁|犹|启)\s?\d+[:：]\d+(?:[\-–,，]\d+)*')
SKIP_ANC={'sortq','clozebox','qa','reading','creed','fc','verb','co-gold','tbl','chip','mn','src','toc','gnav','nomk','legend','mermaid','tools','opt','ld','tabs'}
def _skip(el):
    for p in el.parents:
        if p.name in ('a','h1','h2','h3','h4','script','style','svg','button','summary','table','blockquote','code','mark'): return True
        c=p.get('class') or []
        if any(x in SKIP_ANC or x.startswith('mk-') for x in c): return True
    return False
def automark(soup):
    main=soup
    for blk in main.select('.pan p, .pan li, .card > p, .card li, .tl .card p, .co'):
        if _skip(blk) and not ('co' in (blk.get('class') or [])): continue
        used=set(); cnt=[0]
        for tn in list(blk.find_all(string=True)):
            if not isinstance(tn,NavigableString) or _skip(tn): continue
            if tn.parent is not blk and any((x.startswith('mk-')) for x in (tn.parent.get('class') or [])): continue
            s=str(tn); out=[]; pos=0; changed=False
            for m in sorted(list(GRE.finditer(s))+list(REFRE.finditer(s)),key=lambda m:m.start()):
                if m.start()<pos: continue
                w=m.group(0)
                if REFRE.fullmatch(w): c='mk-ref'
                else:
                    if w in used or cnt[0]>=4: continue
                    c=GCL[w]; used.add(w); cnt[0]+=1
                out.append(esc(s[pos:m.start()])); out.append(f'<span class="{c}">{esc(w)}</span>'); pos=m.end(); changed=True
            if changed:
                out.append(esc(s[pos:]))
                frag=BeautifulSoup(''.join(out),'html.parser')
                tn.replace_with(frag)
def number(soup):
    els=[]
    for el in soup.find_all(True):
        if el.has_attr('data-lv'): els.append(el); continue
        if el.name in ('h2','h3') and not _noauto(el):
            el['data-lv']='1' if el.name=='h2' else '2'; els.append(el)
    c=[0,0,0,0,0]
    for i,el in enumerate(els):
        lv=int(el['data-lv'])
        if not el.get('id'): el['id']=f's{i}'
        if el.has_attr('data-nonum') and lv>1:
            for j in range(lv-1,5): c[j]=0 if j>=lv else c[j]
            continue
        c[lv-1]+=1
        for j in range(lv,5): c[j]=0
        if el.has_attr('data-fix'): c[lv-1]=int(el['data-fix'])
        if lv==1: no=cnum(c[0])+'、'
        elif el.has_attr('data-fix'): no=f"{c[lv-1]}."
        else: no='.'.join(str(x) for x in c[1:lv])+('.' if lv==2 else '')
        el['data-no']=no
        if el.name in ('h2','h3','h4') and not el.has_attr('data-nonum'):
            hn=soup.new_tag('span',attrs={'class':'hn'}); hn.string=no
            ico=el.find('span',class_='ico',recursive=False)
            if ico: ico.insert_after(hn)
            else: el.insert(0,hn)
def _noauto(el):
    for p in el.parents:
        c=p.get('class') or []
        if p.name in ('header','aside','footer','summary','a','details') or any(x in ('fc','quiz','qa','hero','art','nolv','pager') for x in c): return True
    return False
def post(body):
    soup=BeautifulSoup(body,'html.parser')
    number(soup); automark(soup)
    return str(soup)
LEGEND_ITEMS=[('<span class="mk-k">高亮</span>','核心词句'),('<span class="mk-b">粗体金</span>','重点'),('<span class="mk-u">蓝实线</span>','定义 / 术语'),('<span class="mk-w">橙波浪</span>','难点'),('<span class="mk-d">红虚线</span>','对比 / 错误立场'),('<span class="mk-r">红字</span>','警示'),('<span class="mk-ref">罗8:28</span>','经文')]
def legend_html(full=True):
    it=''.join(f'<span class="it">{a}<span class="muted small">{b}</span></span>' for a,b in LEGEND_ITEMS)
    co=''
    if full:
        co='<div class="grid g4" style="margin-top:10px">'+''.join(f'<div class="co {c} sample" style="margin:0"><b class="lab">{l}</b><span class="small">{d}</span></div>' for c,l,d in [('co-core','核心','一句话论题'),('co-hard','难点','需要细想的地方'),('co-trap','易错','常见误解'),('co-gold','金句','原文中的一句（逐字）'),('co-hook','记忆钩','口诀 / 联想')])+'</div>'
    return f'<div class="legend nomk">{it}<button class="btn" data-marks style="padding:3px 12px;font-size:13px">🖍️ 显示/隐藏标记 (M)</button></div>{co}<p class="small muted" style="margin:8px 0 0">标记只加在样式层：原文引文的文字一字不改，可随时关闭标记。</p>'
def callout(kind,label,html_):
    return f'<div class="co co-{kind} nolv"><b class="lab">{label}</b>{html_}</div>'
def gnav(pre,path):
    out=['<h4>🧭 全站导航</h4><div id="gnav" class="gnav">']
    for h,t in GNAV: out.append(f'<a href="{pre}{h}" class="{"on" if h==path else ""}">{t}</a>')
    cur=int(path[3:5]) if path.startswith('ld/') else 0
    out.append(f'</div><details class="ldnav" style="margin:10px 4px"{" open" if cur else ""}><summary class="small muted" style="cursor:pointer">📅 52 个主日速览</summary><div class="gnav">')
    for k,ic,pa,pb,s_,e_ in PARTS:
        out.append(f'<div class="gpart" style="color:{part(s_)[2]}">{esc(part_label(k))}</div>')
        for n in range(s_,e_+1):
            out.append(f'<a href="{pre}ld/{n:02d}.html" class="{"on" if n==cur else ""}" title="{n}. {esc(ld_label(n))}"><span class="no">{n}.</span> {esc(ld_label(n))}</a>')
    out.append('</div></details>')
    return ''.join(out)
def page(path,title,body,desc='',head=''):
    depth=path.count('/'); pre='../'*depth
    sect=path.split('/')[0] if '/' in path else path
    def on(h): return h==path or (h=='texts/index.html' and path.startswith('texts/')) or (h=='lorddays.html' and path.startswith('ld/'))
    navh=''.join(f'<a href="{pre}{h}" class="{"on" if on(h) else ""}" title="{t}"><span>{i}</span><span class="lb">{t}</span></a>' for h,i,t in NAV)
    body=post(body)
    doc=f'''<!doctype html><html lang="zh-Hans" data-theme="dark"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(title)} | 海德堡要理问答 52 主日深度解析</title><meta name="description" content="{esc(desc or title)}"><meta name="theme-color" content="#0a0f1f"><script>try{{var d=document.documentElement,t=JSON.parse(localStorage.getItem("hc-theme"));if(t)d.dataset.theme=t;var w=JSON.parse(localStorage.getItem("hc-side-w"));if(w)d.style.setProperty("--side",w+"px")}}catch(e){{}}</script>
<link rel="icon" href="data:image/svg+xml,{esc(LOGO.replace('class="logo" ','').replace('#','%23'))}">
<link rel="stylesheet" href="{pre}assets/css/style.css">{head}</head><body>
<div class="sky" aria-hidden="true"><i></i><i></i><i></i><i></i></div>
<header class="topbar"><button class="ibtn" id="tocBtn" title="显示/隐藏目录 (T)" aria-label="目录">☰</button><a class="brand" href="{pre}index.html">{LOGO}<b>海德堡要理问答 · 52主日</b></a><nav class="nav">{navh}</nav><a class="vbadge" href="{pre}changelog.html" title="版本更新记录">{VERSION} · {DATE}</a><button class="ibtn" id="marksBtn" data-marks title="显示/隐藏笔记标记 (M)" aria-label="标记" aria-pressed="true">🖍️</button><button class="ibtn" id="themeBtn" title="切换深浅色" aria-label="主题">🌓</button></header>
<div class="progress"></div><div class="backdrop"></div>
<div class="layout"><aside class="side" id="side"><div class="scroll"><input id="tocSearch" class="tocsearch" placeholder="🔍 过滤目录…" aria-label="过滤目录"><h4>📑 本页目录</h4><div class="tocbar"><button id="tocExpand" title="全部展开">⊞ 全部展开</button><button id="tocCollapse" title="全部折叠">⊟ 全部折叠</button></div><nav id="toc" class="toc" aria-label="本页目录"></nav><hr style="border:none;border-top:1px solid var(--bd);margin:14px 0">{gnav(pre,path)}<hr style="border:none;border-top:1px solid var(--bd);margin:14px 0"><h4>🖍️ 标记图例</h4><div class="legend-mini">{''.join(f'<span>{a}</span>' for a,b in LEGEND_ITEMS)}</div></div><div class="resizer" id="resizer" role="separator" aria-orientation="vertical" aria-label="拖动调整目录宽度" tabindex="0" title="拖动调整宽度（双击恢复默认）"></div></aside>
<main id="main"><div class="wrap">{body}
<footer class="foot">📚 信条、信经原文一字不改地引自 <a href="{CCI}/books/book-of-praise">基督教华人网络团契 ccifellowship.org《中国改革宗敬拜手册》(2015)</a>，版权归原出版委员会所有，此处仅作学习引用并逐条注明出处。解读部分为本站原创学习笔记（未经神学家审阅），持守欧陆改革宗三项联合信条。· <a href="{pre}sources.html">资料与说明</a> · <a href="{pre}changelog.html">版本 {VERSION} · {DATE}</a> · <a href="https://github.com/07-Je-Grok-Love-Personal-20260928/{REPO}">GitHub 源码</a></footer>
</div></main></div>
<div class="fab"><button class="ibtn" id="topBtn" title="回到顶部" aria-label="回到顶部">⬆</button></div>
<script src="{pre}assets/js/app.js" defer></script></body></html>'''
    fp=os.path.join(SITE,path); os.makedirs(os.path.dirname(fp),exist_ok=True)
    open(fp,'w').write(doc)
def mark_answer(n,paras):
    ps=list(paras)
    for ph,t in KQ.get(n,[]):
        for i,p in enumerate(ps):
            j=p.find(ph)
            if j>=0:
                ps[i]=p[:j]+f'<span class="mk-{t}">{ph}</span>'+p[j+len(ph):]; break
        else: raise SystemExit(f'KQ miss Q{n}: {ph}')
    return ps
def qa_html(q,c,anchor=True,tools=True,lv=None,marks=True):
    n=qnum(q)
    qtext=esc(q['q'])
    ps=mark_answer(n,q['a']) if marks else q['a']
    a=''.join(f'<p>{p}</p>' for p in ps)
    refs=''.join(f'<li>{esc(r)}</li>' for r in q['refs'])
    rd=f'<details><summary>📖 经文出处（{len(q["refs"])}）</summary><ol class="refs">{refs}</ol></details>' if q['refs'] else ''
    t='<div class="tools"><button data-speak title="朗读">🔊</button><button data-copy title="复制">📋</button></div>' if tools else ''
    short=re.sub(r'^\d+[．.]\s*问：','',q['q'])
    lva=f' data-lv="{lv}" data-toc="Q{n} {esc(short)}"' if lv else ''
    return f'<div class="qa reveal" id="q{n}" style="--c:{c}"{lva}>{t}<div class="q"><span class="qn">Q{n}</span><span>{qtext}</span></div><div class="a">{a}</div>{rd}</div>'

# ===== v5: canonical whole-Bible mapping (study labels, not confessional text) =====
ACTS=[('cr','🌅','创造'),('fa','🍎','堕落'),('re','✝️','救赎'),('co','👑','完成'),('rs','🙌','回应')]
def ld_act(n):
    if n==1: return 're'
    if n<=4: return 'fa'
    if n in (9,10): return 'cr'
    if n in (19,22): return 'co'
    if n<=31: return 're'
    return 'rs'
def ld_cov(n):
    if n==1: return '恩典之约的总纲：我属于信实的救主'
    if n<=4: return '工作之约（生命之约）被违背：律法显明罪'
    if n<=7: return '恩典之约的中保与接受（真信心）'
    if n<=10: return '三一神：创造与护理之约的主'
    if n<=19: return '恩典之约的中保：基督的位格与职分、降卑与升高'
    if n<=22: return '圣灵施行恩典之约：教会、赦罪、复活与永生'
    if n<=24: return '恩典之约的福益：唯独因信称义'
    if n<=30: return '恩典之约的记号与印证：圣礼'
    if n==31: return '恩典之约群体的秩序：天国的钥匙'
    if n<=44: return '恩典之约中的感恩生活：十诫（律法第三功用）'
    return '恩典之约中的感恩生活：祷告与主祷文'
LOCI=[(1,1,'📖 序论（安慰）'),(2,4,'🧍 人论 · 罪论'),(5,7,'🌉 救恩论（中保与信心）'),(8,10,'👑 神论（三一 · 创造 · 护理）'),(11,19,'✝️ 基督论'),(20,20,'🕊️ 圣灵论'),(21,21,'⛪ 教会论'),(22,22,'⏳ 末世论'),(23,24,'⚖️ 救恩论（称义）'),(25,30,'🍞 圣礼论'),(31,31,'🗝️ 教会论（纪律）'),(32,44,'📜 伦理（十诫）'),(45,52,'🙏 祷告')]
def ld_locus(n): return next(t for a,b,t in LOCI if a<=n<=b)
