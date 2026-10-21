from common import *
def mindmap():
    # horizontal tree: root -> 4 parts -> groups
    W,H=1200,820
    parts=[('i','引言','主日1','#a78bfa'),('m','第一部 罪与愁苦','主日2–4','#fb7185'),('d','第二部 得救','主日5–31','#60a5fa'),('g','第三部 感恩','主日32–52','#34d399')]
    gs=GROUPS; rows=len(gs); y0=40; dy=(H-80)/(rows-1)
    out=[f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="海德堡要理问答结构思维导图" xmlns="http://www.w3.org/2000/svg"><defs><filter id="gl"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>']
    rx,ry=110,H/2
    gy=[y0+i*dy for i in range(rows)]
    py={}
    for k,_,_,_ in parts:
        ys=[gy[i] for i,g in enumerate(gs) if g[0]==k]; py[k]=sum(ys)/len(ys)
    px=420; gx=720
    for k,t,r,c in parts:
        out.append(f'<path d="M{rx+90},{ry} C{rx+190},{ry} {px-140},{py[k]} {px-90},{py[k]}" stroke="{c}" stroke-width="4" fill="none" opacity=".8"><animate attributeName="stroke-dasharray" from="0,1200" to="1200,0" dur="1.6s" fill="freeze"/></path>')
    for i,g in enumerate(gs):
        c=[p[3] for p in parts if p[0]==g[0]][0]
        out.append(f'<path d="M{px+90},{py[g[0]]} C{px+170},{py[g[0]]} {gx-120},{gy[i]} {gx-10},{gy[i]}" stroke="{c}" stroke-width="2.2" fill="none" opacity=".7"><animate attributeName="stroke-dasharray" from="0,900" to="900,0" dur="2.2s" fill="freeze"/></path>')
    out.append(f'<g filter="url(#gl)"><rect x="{rx-100}" y="{ry-48}" width="200" height="96" rx="24" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/></g><text x="{rx}" y="{ry-8}" text-anchor="middle" fill="#fde68a" font-size="22" font-weight="900">海德堡要理问答</text><text x="{rx}" y="{ry+22}" text-anchor="middle" fill="#e2e8f0" font-size="15">1563 · 52主日 · 129问</text>')
    for k,t,r,c in parts:
        out.append(f'<rect x="{px-90}" y="{py[k]-30}" width="180" height="60" rx="18" fill="{c}" opacity=".95"/><text x="{px}" y="{py[k]-4}" text-anchor="middle" fill="#0b1020" font-size="17" font-weight="900">{t}</text><text x="{px}" y="{py[k]+18}" text-anchor="middle" fill="#0b1020" font-size="13">{r}</text>')
    for i,g in enumerate(gs):
        c=[p[3] for p in parts if p[0]==g[0]][0]
        rng=f'主日{g[2]}' if g[2]==g[3] else f'主日{g[2]}–{g[3]}'
        out.append(f'<a href="ld/{g[2]:02d}.html"><rect x="{gx-10}" y="{gy[i]-19}" width="460" height="38" rx="12" fill="{c}" fill-opacity=".16" stroke="{c}" stroke-opacity=".7"/><text x="{gx+8}" y="{gy[i]+6}" fill="{c}" font-size="15" font-weight="800">{rng}</text><text x="{gx+150}" y="{gy[i]+6}" fill="currentColor" font-size="16">{g[4]}</text></a>')
    out.append('</svg>')
    return ''.join(out)
def drama():
    acts=[('创造','Creation','创1–2','主日3、9–10','#a78bfa','🌅'),('堕落','Fall','创3','主日2–4','#fb7185','🍎'),('救赎','Redemption','创3:15 → 福音书 → 使徒行传','主日5–31','#60a5fa','✝️'),('完成','Consummation','启21–22','主日19、22、52','#34d399','👑')]
    W=1200;H=300;w=260;gap=(W-4*w)/5
    out=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="圣经四幕剧">']
    for i,(z,e,ref,ld,c,ic) in enumerate(acts):
        x=gap+i*(w+gap)
        out.append(f'<g><rect x="{x}" y="40" width="{w}" height="220" rx="28" fill="{c}" fill-opacity=".14" stroke="{c}" stroke-width="2"><animate attributeName="y" values="50;40" dur="{0.6+i*0.2}s" fill="freeze"/></rect><text x="{x+w/2}" y="100" text-anchor="middle" font-size="44">{ic}</text><text x="{x+w/2}" y="150" text-anchor="middle" font-size="30" font-weight="900" fill="{c}">{z}</text><text x="{x+w/2}" y="178" text-anchor="middle" font-size="15" fill="currentColor" opacity=".7">{e}</text><text x="{x+w/2}" y="210" text-anchor="middle" font-size="15" fill="currentColor">{ref}</text><text x="{x+w/2}" y="238" text-anchor="middle" font-size="15" font-weight="800" fill="{c}">要理问答：{ld}</text></g>')
        if i<3:
            ax=x+w+4; out.append(f'<path d="M{ax},150 L{ax+gap-8},150" stroke="currentColor" stroke-width="3" marker-end="url(#ah)" opacity=".6"/>')
    out.insert(1,'<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10z" fill="currentColor"/></marker></defs>')
    out.append('</svg>'); return ''.join(out)
def tri():
    # three-part structure arc (misery-deliverance-gratitude) + Romans mapping
    return '''<svg viewBox="0 0 1200 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="三重结构"><defs><linearGradient id="tg" x1="0" x2="1"><stop offset="0" stop-color="#fb7185"/><stop offset=".5" stop-color="#60a5fa"/><stop offset="1" stop-color="#34d399"/></linearGradient></defs>
<path d="M80,200 Q600,-60 1120,200" stroke="url(#tg)" stroke-width="10" fill="none" stroke-linecap="round"><animate attributeName="stroke-dasharray" from="0,1600" to="1600,0" dur="2s" fill="freeze"/></path>
<circle cx="80" cy="200" r="34" fill="#fb7185"/><text x="80" y="208" text-anchor="middle" font-size="22" font-weight="900" fill="#fff">罪</text>
<circle cx="600" cy="70" r="40" fill="#60a5fa"/><text x="600" y="79" text-anchor="middle" font-size="24" font-weight="900" fill="#fff">恩</text>
<circle cx="1120" cy="200" r="34" fill="#34d399"/><text x="1120" y="208" text-anchor="middle" font-size="22" font-weight="900" fill="#fff">谢</text>
<text x="80" y="252" text-anchor="middle" font-size="16" fill="currentColor">愁苦 Misery · 罗1:18–3:20</text>
<text x="600" y="140" text-anchor="middle" font-size="16" fill="currentColor">拯救 Deliverance · 罗3:21–11:36</text>
<text x="1120" y="252" text-anchor="middle" font-size="16" fill="currentColor">感恩 Gratitude · 罗12–16</text>
<text x="340" y="190" text-anchor="middle" font-size="15" fill="currentColor" opacity=".75">律法照出罪 →</text><text x="860" y="190" text-anchor="middle" font-size="15" fill="currentColor" opacity=".75">→ 十诫与祷告</text></svg>'''

COLS={'i':'#a78bfa','m':'#fb7185','d':'#60a5fa','g':'#34d399'}
def ld_strip(n):
    w=52*12; out=[f'<svg viewBox="0 0 {w} 34" role="img" aria-label="主日{n}在全书52主日中的位置" style="max-height:44px">']
    for i in range(1,53):
        p=part(i)[0]; x=(i-1)*12
        h=26 if i==n else 14; y=30-h
        op='1' if i==n else '.45'
        out.append(f'<rect x="{x+1}" y="{y}" width="10" height="{h}" rx="3" fill="{COLS[p]}" opacity="{op}"><title>主日{i} · {esc(N[i]["t"])}</title></rect>')
    out.append(f'<polygon points="{(n-1)*12+6-5},0 {(n-1)*12+6+5},0 {(n-1)*12+6},4" fill="#fbbf24"/></svg>')
    return ''.join(out)
def ld_constellation(n,ld,no):
    import math
    W,H=560,340; cx,cy=W/2,H/2; p=part(n); col=COLS[p[0]]
    qs=[qnum(q) for q in ld['qas']]
    outer=[(k,'#facc15','../search.html?q='+k) for k in no['kw'][:5]]
    outer+=[(f'比利时{BC[k]["title"][:4]}','#60a5fa',f'#xbc{k}') for k in no['bc'][:3]]
    for s in no['cd'][:2]:
        sec_,st_,arts=parse_cd(s)
        outer.append((('多特'+st_[:3]).replace('第',''),'#34d399','#x-cd'))
    outer+=[(f'WSC {x}','#fbbf24','#x-wsc') for x in no['wsc'][:2]]
    g=[f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="主日{n}关联星图" class="const">']
    g.append(f'<defs><radialGradient id="cg{n}"><stop offset="0" stop-color="{col}" stop-opacity=".95"/><stop offset="1" stop-color="{col}" stop-opacity=".35"/></radialGradient></defs>')
    # orbits
    g.append(f'<ellipse cx="{cx}" cy="{cy}" rx="92" ry="70" fill="none" stroke="currentColor" stroke-opacity=".15" stroke-dasharray="4 6"/><ellipse cx="{cx}" cy="{cy}" rx="225" ry="135" fill="none" stroke="currentColor" stroke-opacity=".12" stroke-dasharray="4 6"/>')
    nodes=[]
    for i,q in enumerate(qs):
        a=-math.pi/2+2*math.pi*i/len(qs); x=cx+92*math.cos(a); y=cy+70*math.sin(a)
        nodes.append(('q',x,y,f'Q{q}',col,f'#q{q}'))
    for i,(t,c,k) in enumerate(outer):
        a=-math.pi/2+2*math.pi*(i+.5)/max(len(outer),1); x=cx+225*math.cos(a); y=cy+135*math.sin(a)
        nodes.append(('o',x,y,t,c,k))
    for j,(k,x,y,t,c,h) in enumerate(nodes):
        g.append(f'<line class="draw" x1="{cx:.0f}" y1="{cy:.0f}" x2="{x:.0f}" y2="{y:.0f}" stroke="{c}" stroke-opacity=".55" stroke-width="{2 if k=="q" else 1.4}" style="transition-delay:{j*60}ms"/>')
    g.append(f'<circle cx="{cx}" cy="{cy}" r="44" fill="url(#cg{n})"/><text x="{cx}" y="{cy-6}" text-anchor="middle" font-size="13" fill="#0b1020" font-weight="800">主日</text><text x="{cx}" y="{cy+18}" text-anchor="middle" font-size="26" fill="#0b1020" font-weight="900">{n}</text>')
    for k,x,y,t,c,h in nodes:
        g.append(f'<a href="{esc(h)}" class="cn"><title>{esc(t)} — 点击跳转</title><g>')
        if k=='q':
            g.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="19" fill="{c}"/><text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-size="13" font-weight="800" fill="#0b1020">{t}</text>')
        else:
            tw=len(t)*15+18
            g.append(f'<rect x="{x-tw/2:.0f}" y="{y-15:.0f}" width="{tw}" height="30" rx="15" fill="{c}" fill-opacity=".18" stroke="{c}"/><text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-size="14" fill="currentColor">{esc(t)}</text>')
        g.append('</g></a>')
    g.append('</svg>')
    return ''.join(g)
def q_bars():
    """52 bars: number of Q&As per Lord's Day, colored by part, animated growth"""
    W,H=52*16+40,200; out=[f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="每个主日的问答数量">']
    mx=max(len(ld['qas']) for ld in D['hc'])
    for y in range(0,mx+1):
        yy=170-y*150/mx
        out.append(f'<line x1="30" x2="{W}" y1="{yy:.0f}" y2="{yy:.0f}" stroke="currentColor" stroke-opacity=".08"/><text x="22" y="{yy+4:.0f}" font-size="13" text-anchor="end" fill="currentColor" opacity=".6">{y}</text>')
    for i,ld in enumerate(D['hc']):
        n=ld['n']; c=len(ld['qas']); h=c*150/mx; x=34+i*16
        out.append(f'<a href="ld/{n:02d}.html"><rect class="bar-grow" style="transition-delay:{i*18}ms;transform-box:fill-box" x="{x}" y="{170-h:.0f}" width="12" height="{h:.0f}" rx="3" fill="{COLS[part(n)[0]]}"><title>主日{n} · {esc(N[n]["t"])} · {c}问</title></rect></a>')
        if n%4==1 or n==52: out.append(f'<text x="{x+6}" y="190" font-size="13" text-anchor="middle" fill="currentColor" opacity=".7">{n}</text>')
    out.append('</svg>'); return ''.join(out)
def parts_stack():
    parts=[('引言',1,1,2,'i'),('罪与愁苦',3,3,11,'m'),('得救',27,12,85,'d'),('感恩',21,86,129,'g')]
    W=640; out=[f'<svg viewBox="0 0 {W} 150" role="img" aria-label="129问在三部分中的分布">']
    x=0; small=0
    for t,lds,a,b,k in parts:
        cnt=b-a+1; w=cnt/129*W
        out.append(f'<g class="barx" style="transform-box:fill-box;transition-delay:{small*150}ms"><rect x="{x:.1f}" y="46" width="{w-2:.1f}" height="48" fill="{COLS[k]}" rx="6"/></g>')
        rng="Q"+str(a)+("–"+str(b) if b!=a else "")
        if w>120:
            out.append(f'<text x="{x+w/2:.0f}" y="77" text-anchor="middle" font-size="18" font-weight="800" fill="#0b1020">{t} {cnt}问</text><text x="{x+w/2:.0f}" y="118" text-anchor="middle" font-size="14" fill="currentColor" opacity=".8">{rng} · {lds} 个主日</text>')
        else:
            lx=4+small*96
            out.append(f'<line x1="{x+w/2:.0f}" y1="46" x2="{lx+20}" y2="28" stroke="{COLS[k]}" stroke-width="1.5"/><text x="{lx}" y="22" font-size="14" font-weight="700" fill="{COLS[k]}">{t} {cnt}问</text>')
            small+=1
        x+=w
    out.append('<text x="4" y="142" font-size="13" fill="currentColor" opacity=".7">引言 Q1–2 · 1 个主日　|　罪与愁苦 Q3–11 · 3 个主日</text></svg>'); return ''.join(out)

def refbars(ld,c):
    qs=[(qnum(q),len(q['refs'])) for q in ld['qas']]; mx=max([v for _,v in qs]+[1])
    rows=''.join(f'<a class="rb" href="#q{n}"><span class="small" style="width:3.2em">Q{n}</span><span class="rbt"><span class="barx" style="width:{max(v/mx*100,3):.0f}%;background:{c};transition-delay:{i*90}ms"></span></span><span class="small muted">{v} 处</span></a>' for i,(n,v) in enumerate(qs))
    return f'<div class="refbars">{rows}</div>'
def bc_donut():
    import math
    R,r=120,72; cx=cy=150; tot=37; a0=-math.pi/2; out=['<svg viewBox="0 0 300 300" role="img" aria-label="比利时信条37条分组" class="donut">']
    cols=['#a78bfa','#60a5fa','#a78bfa','#fbbf24','#fb7185','#fbbf24','#60a5fa','#34d399','#60a5fa','#34d399','#fbbf24','#fb7185']
    for i,(s_,e_,t,ic) in enumerate(BCG):
        n=e_-s_+1; a1=a0+2*math.pi*n/tot-0.015
        p=lambda a,rr:(cx+rr*math.cos(a),cy+rr*math.sin(a))
        x1,y1=p(a0,R);x2,y2=p(a1,R);x3,y3=p(a1,r);x4,y4=p(a0,r); lg=1 if a1-a0>math.pi else 0
        out.append(f'<a href="texts/bc.html#g{s_}" class="seg" style="transition-delay:{i*70}ms"><path d="M{x1:.1f},{y1:.1f} A{R},{R} 0 {lg} 1 {x2:.1f},{y2:.1f} L{x3:.1f},{y3:.1f} A{r},{r} 0 {lg} 0 {x4:.1f},{y4:.1f}Z" fill="{cols[i]}" fill-opacity=".85"><title>{ic} {t}：第{s_}{"–"+str(e_) if e_!=s_ else ""}条（{n} 条）</title></path></a>')
        am=(a0+a1)/2; lx,ly=p(am,(R+r)/2)
        if n>=2: out.append(f'<text x="{lx:.0f}" y="{ly+5:.0f}" text-anchor="middle" font-size="15" pointer-events="none">{ic}</text>')
        a0=a1+0.015
    out.append(f'<text x="{cx}" y="{cy-4}" text-anchor="middle" font-size="34" font-weight="900" fill="currentColor">37</text><text x="{cx}" y="{cy+20}" text-anchor="middle" font-size="14" fill="currentColor" opacity=".7">条 · 12 组</text></svg>')
    return ''.join(out)
