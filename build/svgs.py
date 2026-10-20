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
