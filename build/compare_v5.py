from common import *
PROB=[('🔥 1559 海德堡圣餐争论；普法尔茨境内路德宗、腓力派与改革宗并存，需要一份能合一教会、教导孩童与牧者的教材','📘 海德堡要理问答（1563）','用温暖的第一人称问答，以“唯一的安慰”统摄：罪—恩—谢；圣餐上采取改革宗立场（第75–80问），同时避免无谓的论战语气。','texts/hc.html','var(--deliv)'),
('⚔️ 南尼德兰在哈布斯堡统治下受逼迫；改革宗信徒被指控为重洗派式的叛乱者','🛡️ 比利时信条（1561）','以公开信仰告白向君王申明：我们持守大公信仰（三一、基督二性），拒绝重洗派的叛乱主张，尊重政府（第36条），并指明真教会的标记（第29条）。','texts/bc.html','var(--misery)'),
('🌪️ 1610 抗辩派五条：有条件的拣选、普遍救赎、可抗拒的恩典、可能失落的信心','🌷 多特信经（1619）','以“教义—错谬反驳”的结构逐条回应，捍卫恩典的主权；同时带着牧养语气（如第一项教义第16–17条对软弱信徒与夭折婴孩父母的安慰）。','texts/cd.html','var(--grat)')]
def problems():
    h='<div class="pflow">'
    for i,(p,d,a,u,c) in enumerate(PROB):
        h+=f'<div class="prow reveal" style="--c:{c};--i:{i}"><div class="pb pq"><span class="small muted">❓ 问题</span><p>{esc(p)}</p></div><span class="parr" aria-hidden="true">➜</span><a class="pb pd" href="{u}"><b>{d}</b></a><span class="parr" aria-hidden="true">➜</span><div class="pb pa"><span class="small muted">✅ 回答</span><p>{esc(a)}</p></div></div>'
    return h+'</div><p class="small muted">一份文件回答一个处境：教导（HC）、告白（BC）、裁决（CD）。合起来才构成“三项联合信条”——这就是“为什么是三份而不是一份”的历史原因。（本站概述）</p>'
def venn():
    C=[('HC',230,200,'#60a5fa','texts/hc.html'),('BC',370,200,'#fb7185','texts/bc.html'),('CD',300,320,'#34d399','texts/cd.html')]
    L=[(130,150,['📘 HC 独有','个人的安慰','十诫 · 主祷文','问答式教学'],'texts/hc.html'),
       (470,150,['🛡️ BC 独有','圣经正典（第4–7条）','真教会的标记','政府的职分'],'texts/bc.html'),
       (300,440,['🌷 CD 独有','拣选与弃绝的细节','有效恩召','错谬反驳'],'texts/cd.html'),
       (300,120,['HC ∩ BC','使徒信经次序','两项圣礼'],'texts/hc.html#q65'),
       (205,300,['HC ∩ CD','安慰与确据','（Q1 · 第五项）'],'texts/cd.html#section5'),
       (395,300,['BC ∩ CD','拣选（BC16）','败坏（BC14–15）'],'texts/bc.html#bc16'),
       (300,232,['✝️ 共同核心','唯独恩典','唯独基督'],'texts/index.html')]
    s='<svg viewBox="0 0 600 500" class="venn" role="img" aria-label="三项联合信条的独有与共同重点（维恩图）">'
    for k,x,y,c,u in C: s+=f'<a href="{u}"><circle class="vc" cx="{x}" cy="{y}" r="150" fill="{c}" fill-opacity=".16" stroke="{c}" stroke-width="2"/></a>'
    for x,y,ls,u in L:
        s+=f'<a href="{u}" class="vl"><text x="{x}" y="{y}" text-anchor="middle" fill="currentColor">'+''.join(f'<tspan x="{x}" dy="{0 if j==0 else 17}" font-size="{14 if j==0 else 12.5}" font-weight="{800 if j==0 else 400}">{esc(t)}</tspan>' for j,t in enumerate(ls))+'</text></a>'
    return s+'</svg>'
REM=[('① 有条件的拣选','神预见谁会相信而拣选','第一项教义：无条件的拣选','Q54（神拣选的群体）','第16条'),
('② 普遍的救赎','基督为每一个人死，但只有信者得益','第二项教义：基督的死有效地救赎选民','Q37、Q40','第21条'),
('③ 人的败坏 / 信心','人凭自己不能行善（措辞近正统）','第三、四项教义：全然败坏','Q8','第14–15条'),
('④ 可抗拒的恩典','恩典可被抗拒','第三、四项教义：有效恩召、重生','Q21、Q65（圣灵藉福音生信）','第22–24条'),
('⑤ 坚忍未定','真信徒是否会失落尚待考察','第五项教义：圣徒的坚忍','Q1、Q54（我是并永远是）','无专条（参第22–24条）')]
def remon():
    rows=''.join(f'<tr><th>{a}</th><td>{esc(b)}</td><td><a href="texts/cd.html">{esc(c)}</a></td><td>{esc(d)}</td><td>{esc(e)}</td></tr>' for a,b,c,d,e in REM)
    return f'<div class="tbl reveal"><table><thead><tr><th>抗辩派（1610）</th><th>主张（概述）</th><th>🌷 多特的回答</th><th>📘 HC 对应</th><th>🛡️ BC 对应</th></tr></thead><tbody>{rows}</tbody></table></div><p class="small muted">抗辩派条文为本站概述，并非原文引文；对应的问答与条目编号仅供查找，请以原文为准。</p>'
