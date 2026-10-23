from common import *
import svgs
# ---------------- HISTORY
from history_data import *
people=[('frederick.jpg','腓德烈三世（虔诚者）Frederick III','1515–1576 · 普法尔茨选帝侯','委托编写要理问答；在 1566 年奥格斯堡议会冒着失去帝国法律保护的危险为其辩护。'),
('ursinus.jpg','乌尔西努 Zacharias Ursinus','1534–1583 · 布雷斯劳 → 维滕堡 → 苏黎世 → 海德堡','主要起草者，墨兰顿的学生，后接受改革宗圣餐观；其要理问答讲义是最重要的注释。'),
('olevian.jpg','俄利维亚努 Caspar Olevianus','1536–1587 · 特里尔 → 日内瓦 → 海德堡 → 赫博恩','宫廷牧师，参与编写并推动教会纪律；盟约神学先驱。'),
('hc1563.jpg','1563 年初版书影','Heidelberger Katechismus','德文初版，正式名称为《教理问答或基督教教导》，用于普法尔茨的教会和学校。'),
('dort.jpg','多特大会 Synod of Dort','1618–1619 · 多德雷赫特','回应抗辩派，采纳多特信经，确认三项联合信条的地位。'),
('castle.jpg','海德堡城堡与内卡河谷','Heidelberg · Kurpfalz','选帝侯宫廷所在地，莱茵—内卡地区的政治与学术中心。')]
pp='<div class="grid g2">'+''.join(f'<div class="card person reveal lift"><img src="assets/img/{i[:-4]}-192.webp" srcset="assets/img/{i[:-4]}-192.webp 192w, assets/img/{i[:-4]}-640.webp 640w" sizes="(max-width:420px) 92vw, 96px" alt="{esc(t)}" width="96" height="120" loading="lazy" decoding="async"><div><h3 style="margin:0">{esc(t)}</h3><div class="small muted">{esc(s)}</div><p style="margin:.4em 0 0">{esc(d)}</p></div></div>' for i,t,s,d in people)+'</div><p class="small muted">图片来自 Wikimedia Commons（公有领域；城堡夜景 CC BY 4.0, Schlurcher），见 <a href="sources.html#credits">资料与致谢</a>。</p>'
his=f'''<section class="hero reveal"><span class="chip d">🗺️ 时间线 · 故事线 · 地理 · 文化</span><h1>真实的历史舞台</h1><p class="lead">一部要理问答，诞生于莱茵—内卡河谷的选帝侯宫廷；一部信条，写于南尼德兰的逼迫与火刑之下；一部信经，定于荷兰共和国的国际大会。三条线最终在多德雷赫特汇合。</p></section>'''
lanes=[('📜 海德堡要理问答','var(--deliv)',[('1559','海德堡圣餐争论'),('1559–61','腓德烈三世研读圣经，选择改革宗'),('1562','乌尔西努等起草'),('1563','海德堡要理问答 · 52 主日')]),
('🛡️ 比利时信条','var(--intro)',[('1561','德布利在南尼德兰写成信条'),('1566','安特卫普会议修订；达斯努斯荷兰文译要理问答'),('1571','埃姆登总会：采纳 BC + HC')]),
('🌷 多特信经','var(--grat)',[('1610','抗辩派《抗辩书》五条'),('1618–19','多特大会'),('1619','多特信经；确认 BC 与 HC')])]
story='<div class="card reveal story">'+'<div class="lanes">'+''.join(f'<div class="lane" style="--c:{c}"><b class="lt">{t}</b>'+''.join(f'<div class="sn"><span class="yr">{y}</span>{esc(x)}</div>' for y,x in ev)+'</div>' for t,c,ev in lanes)+'</div><div class="merge">⭐ 三项联合信条：HC · BC · CD —— 圣职签署 · 教会合一</div></div>'
his+=sec('story','📚','故事线：三部信条如何汇成“三项联合信条”',story)
def gantt():
    """v6: era Gantt band (log-ish compressed axis: 1380-1650 linear, after 1650 compressed)."""
    import re as _r
    def X(y): return 90+(y-1380)*2.2 if y<=1650 else 90+270*2.2+(y-1650)*0.35
    W=int(X(2025))+10
    o=[f'<svg viewBox="0 0 {W} 150" role="img" aria-label="五个时期甘特图" style="width:100%;min-width:620px;height:auto">']
    for i,(k,lab,var) in enumerate(ERAS):
        ys=[int(x) for x in _r.findall(r'1[3-9]\d\d|20\d\d',lab)]; a=ys[0]; b=ys[1] if len(ys)>1 else 2025
        y=8+i*26; o.append(f'<rect x="{X(a):.0f}" y="{y}" width="{max(X(b)-X(a),6):.0f}" height="18" rx="9" style="fill:{var};opacity:.85"><title>{esc(lab)}</title></rect><text x="{X(a)-6:.0f}" y="{y+13}" text-anchor="end" style="fill:var(--fg);font-size:11px">{esc(lab.split(" ")[0])}</text>'+(f'<text x="{X(a)+8:.0f}" y="{y+13}" style="fill:var(--ink);font-size:11px;font-weight:700">{esc(" ".join(lab.split(" ")[1:]))}</text>' if X(b)-X(a)>190 else f'<text x="{X(b)+6:.0f}" y="{y+13}" style="fill:var(--fg);font-size:11px;font-weight:700">{esc(" ".join(lab.split(" ")[1:]))}</text>'))
    for yv in [1400,1450,1500,1550,1600,1650,1800,2000]:
        o.append(f'<line x1="{X(yv):.0f}" x2="{X(yv):.0f}" y1="2" y2="136" style="stroke:var(--bd)"/><text x="{X(yv):.0f}" y="148" text-anchor="middle" style="fill:var(--muted);font-size:10px">{yv}</text>')
    o.append('</svg>'); return ''.join(o)
his+=sec('timeline','⏳','时间线（1386–2015）：五个时期 · 点击圆点跳转','<div class="card reveal" style="margin-bottom:14px"><h3 id="tl-gantt">📊 五个时期一览（1650 年后轴线压缩）</h3><div class="chart mm">'+gantt()+'</div></div>'+timeline_html())
import mapsvg, build_maps as BM
_LP={'诺伊施塔特':'l','弗兰肯塔尔':'b','瓦朗谢讷':'b','图尔奈':'l','莱顿':'t','阿姆斯特丹':'r','多德雷赫特':'l','安特卫普':'r','韦瑟尔':'r','马尔堡':'r','赫博恩':'t','特里尔':'l','伦敦':'r','埃姆登':'r'}
ERAY={'bg':'1386–1555','pf':'1556–1583','nl':'1561–1581','dt':'1609–1619','lg':'1622–'}
HMAP=dict(id='hist',page='history',ico='🗺️',title='地理：交互地图 + 地点卡片',short='21 个地点',bbox=(-1.5,45.4,18.2,54.4),
  places=[('p%d'%i,t.split(' ')[0],' '.join(t.split(' ')[1:]),lo,la,ERAY[e],d,EC[e][4:-1],_LP.get(t.split(' ')[0],'r'),e) for i,(la,lo,t,e,d,ls) in enumerate(PLACES)],
  routes=[('u','🎓 乌尔西努求学','--intro','dash',['p6','p1','p3','p0'],'布雷斯劳 → 维滕堡 → 苏黎世 → 海德堡'),('h','📜 要理问答北传','--grat','solid',['p0','p16','p17','p19'],'海德堡 → 韦瑟尔 → 埃姆登 → 多特'),
          ('b','🛡️ 比利时信条之路','--misery','dash',['p12','p14','p17','p19'],'图尔奈 → 安特卫普 → 埃姆登 → 多特'),('s','🍞 圣餐之争','--gold','dot',['p2','p3','p4','p0'],'马尔堡 → 苏黎世 / 日内瓦 → 海德堡')],
  regions=[('选帝侯普法尔茨',8.2,49.35,70,'--deliv'),('北尼德兰',5.0,51.9,110,'--grat'),('南尼德兰',3.6,50.6,60,'--misery')],lds=[],culture=[],story=[],
  inset=dict(bbox=(7.7,49.1,9.0,49.75),keys=['p0','p9','p10'],at='br',w=.26,label='海德堡周边'))
_cm=mapsvg.concept(HMAP)
_rtl='<div class="rtl" role="group" aria-label="路线开关">'+''.join(f'<button type="button" class="rtb on" data-rt="hist:{r[0]}" style="--c:var({r[2]})" aria-pressed="true" title="{esc(r[5])}"><i class="sw {r[3]}"></i>{esc(r[1])}</button>' for r in HMAP['routes'])+'<button type="button" class="rtb play" data-play="hist">▶ 播放路线</button></div>'
his+=sec('geo','🗺️','地理：概念图 + 实时地图 + 地点卡片（与主日相连）',callout('geo','地理',md('**三条水流汇向一处**：瑞士的改革宗神学（苏黎世、日内瓦）、萨克森的路德宗传统（维滕堡）与尼德兰的难民教会，在莱茵河—内卡河交汇的==海德堡==相遇，又沿莱茵河北上，在==多特==汇合。'))+
  f'<div id="map" class="mpair"><figure class="mcard cm reveal"><figcaption>🎨 概念示意图 <span class="small muted">· 动画路线 · 编号地点</span></figcaption>{_cm}</figure><figure class="mcard lv"><figcaption>🛰️ 实时交互地图 <span class="small muted">· 拖动 / 双指缩放 · 点击地点</span></figcaption>{BM.live_box(HMAP)}</figure></div>'+_rtl+
  '<p class="small muted">时间线的“时期”按钮会同步淡化两幅地图上不属于该时期的地点；地点卡片的“在地图上查看”会让实时地图飞到该处。更多专题地图见 <a href="maps.html">🗺️ 历史地图集</a> 与 <a href="geo-bible.html">🏜️ 圣经地理</a>。</p>'+BM.mapdef(HMAP)+
  '<h3 id="places">📍 地点卡片（21 处）</h3>'+places_html())
his+=sec('people','👥','四、人物与图像',pp)
his+=sec('culture','🏞️','区域文化：六个舞台',regions_html())
his+='<script>window.hcFly=function(i){window.hcHL&&hcHL("hist","p"+i,1)};window.hcMapEra=function(e){document.querySelectorAll("svg.cmap[data-cm=hist] .pm").forEach(function(g){g.classList.toggle("dim",e!=="all"&&g.dataset.era!==e)});dispatchEvent(new CustomEvent("hcera",{detail:{map:"hist",era:e}}))}</script>'+BM.MAPJS('')
page('history.html','历史、地理与文化',his,'海德堡要理问答的时间线、故事线、地图与文化背景',head='')
