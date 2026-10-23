# v8 · 笔记标记系统 (marks.html): legend with focus filter, meaning table, live demo, site-wide usage chart. Runs after all content pages.
from common import *
import glob
ROWS=[('mk-k','荧光底 + 粗体','核心词句','答案主干、要背的那半句','<span class="mk-k">唯一的安慰</span>'),
('mk-b','金色粗体','重点','论题关键词、结构关键词','<span class="mk-b">三重职分</span>'),
('mk-g','绿色粗体','恩典 · 应许','安慰、赦罪、白白的恩典','<span class="mk-g">白白</span>'),
('mk-r','红色粗体','警示','审判、咒诅、严重后果','<span class="mk-r">永远的刑罚</span>'),
('mk-u','蓝色实线','术语 / 定义','必须能下定义的词','<span class="mk-u">称义</span>'),
('mk-w','橙色波浪线','难点','需要停下来想的地方','<span class="mk-w">降在阴间</span>'),
('mk-d','红色虚线','对比 / 错误立场','被反驳的观点','<span class="mk-d">变质说</span>'),
('mk-bg','淡紫底纹','并列要点','几个并列项、结构词','<span class="mk-bg">先知 · 祭司 · 君王</span>'),
('mk-p','紫色人物','人物','历史人物','<span class="mk-p">乌尔西努</span>'),
('mk-l','青色点线','地点','历史 / 圣经地点','<span class="mk-l">海德堡</span>'),
('mk-t','时间徽章','年代','关键年份','<span class="mk-t">1563年</span>'),
('mk-ref','经文药丸','经文出处','可点击查经','<span class="mk-ref">罗8:28</span>')]
NAMES={c:n for c,_,n,_,_ in ROWS}
def counts():
    tot={c:0 for c,*_ in ROWS}; pages=0
    for f in glob.glob(os.path.join(SITE,'**','*.html'),recursive=True):
        if f.endswith('marks.html'): continue
        s=open(f).read(); pages+=1
        for c in tot: tot[c]+=len(re.findall(r'class="'+re.escape(c)+r'"',s))
    return tot,pages
def chart(tot):
    rows=sorted(tot.items(),key=lambda x:-x[1]); mx=max(v for _,v in rows) or 1; W=600; rh=30; H=len(rows)*rh+8
    o=[f'<svg class="bars" viewBox="0 0 {W} {H}" role="img" aria-label="全站各类标记数量" style="width:100%;height:auto">']
    for i,(c,v) in enumerate(rows):
        y=i*rh+4; w=(W-210)*v/mx
        o.append(f'<g class="mkbar {c}"><text x="104" y="{y+18}" text-anchor="end" style="fill:var(--fg);font-size:13px">{NAMES[c]}</text><rect class="bar-grow" x="112" y="{y+4}" width="{max(w,3):.0f}" height="18" rx="9" style="fill:var(--mkc);--i:{i}"/><text x="{118+w:.0f}" y="{y+18}" style="fill:var(--fg);font-size:13px;font-weight:800">{v:,}</text></g>')
    o.append('</svg>'); return ''.join(o)
def build():
    tot,pages=counts(); total=sum(tot.values())
    kpi=''.join(f'<div><b>{v}</b>{t}</div>' for v,t in [(len(ROWS),'种标记'),(len(CO_KINDS),'种区块'),(4,'个层级'),(pages,'个页面')])
    hero=f'<section class="hero reveal"><span class="chip g">🖍️ 笔记标记 · 阅读即记忆</span><h1>笔记标记系统：一种样式只说一件事</h1><p class="lead">读者的眼睛先抓<span class="mk-k">荧光核心</span>，再看<b>颜色</b>（重点 / 恩典 / 警示），然后看<span class="mk-u">线型</span>（术语 / <span class="mk-w">难点</span> / <span class="mk-d">对比</span>），最后看史地层（<span class="mk-p">人物</span> · <span class="mk-l">地点</span> · <span class="mk-t">年代</span>）。全站共 <b>{total:,}</b> 处标记，均由规则统一生成。</p><div class="kpi">{kpi}</div></section>'
    tbl='<div class="tbl"><table class="mktbl"><thead><tr><th>标记</th><th>样式</th><th>含义</th><th>什么时候用</th><th>聚焦</th></tr></thead><tbody>'+''.join(f'<tr><td class="nw">{ex}</td><td class="nw">{st}</td><td><b>{n}</b></td><td>{w}</td><td><button type="button" class="btn sm" data-mkf="{c}" aria-pressed="false">🔦 只看这类</button></td></tr>' for c,st,n,w,ex in ROWS)+'</tbody></table></div>'
    demo=('<div class="card pan demo">'
      '<p>第1问问的是 <span class="mk-k">生前死后唯一的安慰</span>：我 <b class="mk-b">身体和灵魂</b> 都属于 <span class="mk-b">信实的救主耶稣基督</span>。这安慰 <span class="mk-g">白白</span> 赐下，靠 <span class="mk-u">代赎</span> 而来（<span class="mk-ref">彼前1:18-19</span>），不是靠 <span class="mk-d">功德</span>。</p>'
      '<p>全书三段：<span class="mk-bg">罪与苦 · 救赎 · 感恩</span>。<span class="mk-w">“确据”与“信心”的关系</span> 是难点；忽视罪的严重会落入 <span class="mk-r">轻看审判</span> 的危险。</p>'
      '<p><span class="mk-t">1563年</span>，<span class="mk-p">乌尔西努</span> 在 <span class="mk-l">海德堡</span> 主笔写成要理问答，后经 <span class="mk-l">埃姆登</span> 和 <span class="mk-l">多特</span> 被接受为合一信条。</p></div>')
    cos=''.join(f'<div class="co {k} sample nolv"><b class="lab">{l}</b><span class="small">{d}</span></div>' for k,l,d in CO_KINDS)
    how=('<ol class="steps">'
      '<li><b>第一遍：只看荧光</b>（按 <kbd>M</kbd> 切到“仅核心”）——把每问答案的主干读出来。</li>'
      '<li><b>第二遍：看颜色与线型</b>——蓝线术语要能下定义；橙波浪处停下来想；红虚线说出“我们为什么不这样信”。</li>'
      '<li><b>第三遍：看史地层与区块</b>——人物、地点、年代把教义挂在真实历史上；最后读记忆钩，合上书复述。</li></ol>')
    rules='<ul class="clean"><li>🎯 <b>一种样式只表达一种含义</b>：线型代表语义（实线＝术语、波浪＝难点、虚线＝对比），不再“哪里重要就画哪里”。</li><li>🧮 <b>有上限</b>：每段自动术语标记最多 4 处，史地标记最多 3 处，同一个词只标第一次。</li><li>📜 <b>原文不动</b>：信条原文只加样式标签，文字一字不改（逐字校验 0 差异）。</li><li>🎨 <b>五套配色自动适配</b>，亮色主题下对比度达到 WCAG AA。</li></ul>'
    body=(hero+sec('lg','🧭','图例与聚焦：点击任一行，只突出这一种',legend_html(True))
      +sec('tb','📋','十二种标记：样式 → 含义 → 用法',tbl)
      +sec('demo','🔬','示例：同一段落里的四个层级',callout('core','读法','按 **M** 循环“全部 / 仅核心 / 关”，或点击上表的 🔦 只看某一类，体会每一层各自承担的信息。')+demo)
      +sec('co','🧱','八种区块：一眼知道这段是什么',f'<div class="grid g2">{cos}</div>')
      +sec('stat','📊','全站标记分布',f'<div class="card reveal"><h3 id="stat-bars">各类标记数量（{pages} 个页面合计）</h3>{chart(tot)}</div>')
      +sec('how','🧠','三遍读法：用标记来记忆',how+rules))
    page('marks.html','笔记标记系统',body,'海德堡要理问答学习站的笔记标记系统：图例、含义、用法与全站分布')
    print('marks.html',total,'marks')
if __name__=='__main__': build()
