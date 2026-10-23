# v8 · build-time map illustrations: real Natural Earth coastlines projected (Web Mercator) into lively inline SVG.
import json,math,os
from shapely.geometry import shape,box,Polygon,MultiPolygon,LineString,MultiLineString,GeometryCollection
from shapely.ops import transform
from common import esc
G=json.load(open(os.path.join(os.path.dirname(__file__),'geo_out','base.json')))['features']
SH=[(f['properties']['k'],shape(f['geometry'])) for f in G]
def my(lat): return math.log(math.tan(math.pi/4+math.radians(lat)/2))
class Proj:
    def __init__(s,bb,W=640):
        s.x0,s.y0,s.x1,s.y1=bb; s.W=W; s.k=W/(s.x1-s.x0)
        s.my1=my(s.y1); s.H=round((s.my1-my(s.y0))*180/math.pi*s.k)
    def __call__(s,lon,lat): return ((lon-s.x0)*s.k, (s.my1-my(lat))*180/math.pi*s.k)
    def km(s,lat,km): return km/111.32/math.cos(math.radians(lat))*s.k*math.cos(math.radians(lat))/math.cos(math.radians(lat))  # px per km along latitude (Mercator scale)
def _rings(g):
    if isinstance(g,Polygon): yield g
    elif hasattr(g,'geoms'):
        for x in g.geoms: yield from _rings(x)
def _lines(g):
    if isinstance(g,LineString): yield g
    elif hasattr(g,'geoms'):
        for x in g.geoms: yield from _lines(x)
def _d(coords,P,close):
    pts=[];last=None
    for lon,lat in coords:
        x,y=P(lon,lat); q=(round(x,1),round(y,1))
        if q!=last: pts.append(q); last=q
    if len(pts)<2: return ''
    return 'M'+' '.join(f'{x:g} {y:g}' for x,y in pts)+('Z' if close else '')
def base_paths(P,world=False):
    pad=(P.x1-P.x0)*.06
    clip=box(P.x0-pad,max(P.y0-pad,-80),P.x1+pad,min(P.y1+pad,80))
    land=[];riv=[];lak=[]
    tol=1.7/P.k   # ~1.7 px (v8 perf)
    for k,g in SH:
        if k not in (('w',) if world else ('l','a','r')) : continue
        if not g.intersects(clip): continue
        h=g.intersection(clip).simplify(tol,preserve_topology=True)
        if k in('l','w','a'):
            for poly in _rings(h):
                if poly.area<(tol*tol*6): continue
                d=_d(poly.exterior.coords,P,True)+''.join(_d(i.coords,P,True) for i in poly.interiors)
                (lak if k=='a' else land).append(d)
        else:
            for ln in _lines(h):
                if ln.length<tol*4: continue
                riv.append(_d(ln.coords,P,False))
    return ''.join(land),''.join(riv),''.join(lak)
def curve(a,b,bend=.16):
    (x1,y1),(x2,y2)=a,b; mx,my_=(x1+x2)/2,(y1+y2)/2; dx,dy=x2-x1,y2-y1
    return (mx-dy*bend, my_+dx*bend)
def route_d(pts):
    d=f'M{pts[0][0]:.1f} {pts[0][1]:.1f}'
    for a,b in zip(pts,pts[1:]):
        c=curve(a,b); d+=f' Q{c[0]:.1f} {c[1]:.1f} {b[0]:.1f} {b[1]:.1f}'
    return d
LAB={'r':(9,4,'start'),'l':(-9,4,'end'),'t':(0,-11,'middle'),'b':(0,18,'middle')}
def tw(t,fs): return sum((fs if ord(ch)>255 else fs*.56) for ch in t)
def lbox(x,y,lp,t,fs):
    dx,dy,an=LAB[lp]; w=tw(t,fs); x0=x+dx if an=='start' else x+dx-w if an=='end' else x+dx-w/2
    return (x0-2,y+dy-fs*.85,x0+w+2,y+dy+fs*.25)
def hit(a,b): return not(a[2]<b[0] or b[2]<a[0] or a[3]<b[1] or b[3]<a[1])
def place_labels(pts,W,H,fs,taken=()):
    """Greedy collision-free label placement. pts: [(key,x,y,label,pref)] → {key:lp or None}."""
    occ=list(taken)+[(x-8,y-8,x+8,y+8) for _,x,y,_,_ in pts]; out={}
    for k,x,y,t,pref in pts:
        for lp in [pref]+[q for q in 'rltb' if q!=pref]:
            bx=lbox(x,y,lp,t,fs)
            if bx[0]<2 or bx[2]>W-2 or bx[1]<26 or bx[3]>H-4: continue
            if any(hit(bx,o) for o in occ if not(abs((o[0]+o[2])/2-x)<.1 and abs((o[1]+o[3])/2-y)<.1)): continue
            out[k]=lp; occ.append(bx); break
        else: out[k]=None
    return out,occ
def layer(m,P,uid,small,keys=None,inset=False):
    W,H=P.W,P.H; o=[]
    land,riv,lak=base_paths(P)
    pk={p[0]:p for p in m['places']}; idx={p[0]:i+1 for i,p in enumerate(m['places'])}
    o.append(f'<rect width="{W}" height="{H}" rx="{8 if inset else 14}" style="fill:url(#sg-{uid})"/>')
    if not inset:
        for lon in range(int(P.x0//5*5)+5,int(P.x1)+1,5):
            x,_=P(lon,0); o.append(f'<line class="gr" x1="{x:.0f}" x2="{x:.0f}" y1="0" y2="{H}"/>')
        for lat in range(int(P.y0//5*5)+5,int(P.y1)+1,5):
            _,y=P(0,lat); o.append(f'<line class="gr" x1="0" x2="{W}" y1="{y:.0f}" y2="{y:.0f}"/>')
    o.append(f'<path class="land" d="{land}" style="fill:url(#ld-{uid})"/><path class="lake" d="{lak}"/><path class="riv" d="{riv}"/>')
    regs=[]
    for name,lon,lat,km,c in m.get('regions',[]):
        x,y=P(lon,lat); r=km/111.32*P.k/math.cos(math.radians(lat))
        if x+r<0 or x-r>W or y+r<0 or y-r>H: continue
        o.append(f'<g class="reg" style="--c:var({c})"><ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{r:.0f}" ry="{r:.0f}"/></g>'); regs.append((name,x,y,r,c))
    for i,(rk,lab,c,sty,ks,note) in enumerate(m['routes']):
        pts=[P(pk[k][3],pk[k][4]) for k in ks]; d=route_d(pts)
        o.append(f'<g class="rt {sty}" data-rk="{rk}" style="--c:var({c});--i:{i}"><path class="rt-g" d="{d}"/><path class="rt-l" d="{d}" pathLength="1"'+('' if inset else f' marker-end="url(#ah-{uid})"')+'/>'
                 +('' if small or inset else f'<circle class="rt-dot" r="4.5"><animateMotion dur="{max(3,len(ks)*1.1):.1f}s" begin="indefinite" fill="freeze" path="{d}" calcMode="paced"/></circle>')+'</g>')
    fs=15 if small else 12.5
    sel=[p for p in m['places'] if keys is None or p[0] in keys]
    hide=set(m.get('inset',{}).get('keys',[])) if not inset and m.get('inset') else set()
    cand=[(p[0],*P(p[3],p[4]),p[1],p[8]) for p in sel if p[0] not in hide]
    taken=[] if inset else [(W-70,H-72,W,H),(0,H-34,150,H),(0,0,tw(m['short'],13)+90,30)]
    if not inset and m.get('inset') and not small:
        iw=round(W*m['inset'].get('w',.36)); ih=Proj(m['inset']['bbox'],iw).H
        cx,cy={'tr':(W-iw-10,10),'tl':(10,34),'br':(W-iw-10,H-ih-10),'bl':(10,H-ih-30)}[m['inset'].get('at','tr')]; taken.append((cx-4,cy-4,cx+iw+4,cy+ih+4))
    lps,occ=place_labels(cand,W,H,fs,taken)
    for p in sel:
        k,cn,en,lon,lat,yr,desc,c,lp=p[:9]; x,y=P(lon,lat); era=f' data-era="{p[9]}"' if len(p)>9 else ''
        if not(-5<x<W+5 and -5<y<H+5): continue
        lp2=lps.get(k); lab=''
        if lp2:
            dx,dy,an=LAB[lp2]; lab=f'<text class="pl" x="{x+dx:.1f}" y="{y+dy:.1f}" text-anchor="{an}">{esc(cn)}</text>'
        mini=k in hide
        o.append(f'<g class="pm{" mini" if mini else ""}" data-pk="{k}"{era} style="--c:var({c})"><title>{idx[k]}. {esc(cn)} {esc(en)} · {esc(yr)}：{esc(desc)}</title><circle class="pr" cx="{x:.1f}" cy="{y:.1f}" r="9"/><circle class="pc" cx="{x:.1f}" cy="{y:.1f}" r="{3.5 if mini else 5 if small else 7}"/>'
                 +('' if small or mini else f'<text class="pn" x="{x:.1f}" y="{y+3.2:.1f}" text-anchor="middle">{idx[k]}</text>')+lab+'</g>')
    if not small:
        for name,x,y,r,c in regs:
            t=esc(name.replace('（示意）','')); w=tw(name.replace('（示意）',''),12)
            for ty in (y-r-4,y+r+14,y+4):
                bx=(x-w/2-2,ty-11,x+w/2+2,ty+3)
                if bx[0]<2 or bx[2]>W-2 or bx[1]<26 or bx[3]>H-4 or any(hit(bx,q) for q in occ): continue
                occ.append(bx); o.append(f'<text class="regt" x="{x:.0f}" y="{ty:.0f}" text-anchor="middle" style="--c:var({c})">{t}</text>'); break
    return ''.join(o)
def concept(m,W=640,small=False,uid=None):
    """Lively schematic map: gradient land, animated route drawing, travelling dots, pulsing numbered stops, optional magnified inset."""
    P=Proj(m['bbox'],W); H=P.H; uid=uid or m['id']
    o=[f'<svg class="cmap{" sm" if small else ""}" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(m["title"])}（示意图）" data-cm="{m["id"]}" preserveAspectRatio="xMidYMid meet">',
       f'<defs><linearGradient id="ld-{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" style="stop-color:var(--land1)"/><stop offset="1" style="stop-color:var(--land2)"/></linearGradient>'
       f'<radialGradient id="sg-{uid}" cx=".5" cy=".4" r=".8"><stop offset="0" style="stop-color:var(--sea1)"/><stop offset="1" style="stop-color:var(--sea2)"/></radialGradient>'
       f'<marker id="ah-{uid}" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" style="fill:context-stroke"/></marker></defs>',
       f'<g id="cmg-{uid}" class="cmg">', layer(m,P,uid,small)]
    ins=m.get('inset')
    if ins and not small:
        ib=ins['bbox']; iw=round(W*ins.get('w',.36)); IP=Proj(ib,iw); ih=IP.H
        cx,cy={'tr':(W-iw-10,10),'tl':(10,34),'br':(W-iw-10,H-ih-10),'bl':(10,H-ih-30)}[ins.get('at','tr')]
        a=P(ib[0],ib[3]); b=P(ib[2],ib[1])
        o.append(f'<rect class="insb" x="{a[0]:.0f}" y="{a[1]:.0f}" width="{b[0]-a[0]:.0f}" height="{b[1]-a[1]:.0f}" rx="3"/>'
                 f'<line class="insl" x1="{b[0]:.0f}" y1="{a[1]:.0f}" x2="{cx:.0f}" y2="{cy+ih:.0f}"/><line class="insl" x1="{b[0]:.0f}" y1="{b[1]:.0f}" x2="{cx+iw:.0f}" y2="{cy+ih:.0f}"/>'
                 f'<g class="inset"><rect class="insf" x="{cx-2}" y="{cy-2}" width="{iw+4}" height="{ih+4}" rx="10"/><svg x="{cx}" y="{cy}" width="{iw}" height="{ih}" viewBox="0 0 {iw} {ih}">{layer(m,IP,uid,False,keys=set(ins["keys"]),inset=True)}<text class="cap" x="8" y="18" style="font-size:11.5px">🔍 {esc(ins.get("label","放大"))}</text></svg></g>')
    sx=W-46; o.append(f'<g class="cmp" transform="translate({sx},{H-46})"><circle r="18"/><path d="M0-15L5 0L0 15L-5 0Z"/><text y="-21" text-anchor="middle">N</text></g>')
    km=200 if (P.x1-P.x0)<14 else 500; lat0=(P.y0+P.y1)/2; px=km/111.32*P.k/math.cos(math.radians(lat0))
    o.append(f'<g class="scl" transform="translate(14,{H-16})"><rect width="{px:.0f}" height="5" rx="2"/><text y="-5">{km} km</text></g>')
    o.append(f'<text class="cap" x="14" y="22">{m["ico"]} {esc(m["short"])} · 示意图</text></g></svg>')
    return ''.join(o)
def world_inset(m,W=640):
    P=Proj((-125,-40,150,62),W); land,_,_=base_paths(P,world=True); H=P.H
    o=[f'<svg class="cmap world" viewBox="0 0 {W} {H}" role="img" aria-label="要理问答的全球传播（示意）"><rect width="{W}" height="{H}" rx="14" style="fill:var(--sea2)"/><path class="land" d="{land}" style="fill:var(--land1)"/>']
    hx,hy=P(8.69,49.41)
    o.append(f'<g class="pm" style="--c:var(--deliv)"><circle class="pr" cx="{hx:.0f}" cy="{hy:.0f}" r="9"/><circle class="pc" cx="{hx:.0f}" cy="{hy:.0f}" r="6"/></g>')
    for i,(n,lon,lat,yr,d) in enumerate(m['worldpts']):
        x,y=P(lon,lat); c=curve((hx,hy),(x,y),.22)
        o.append(f'<g class="rt solid" style="--c:var(--teal);--i:{i}"><path class="rt-l" d="M{hx:.0f} {hy:.0f} Q{c[0]:.0f} {c[1]:.0f} {x:.0f} {y:.0f}" pathLength="1"/></g>'
                 f'<g class="pm" style="--c:var(--teal)"><title>{esc(n)} · {esc(yr)}：{esc(d)}</title><circle class="pc" cx="{x:.0f}" cy="{y:.0f}" r="5"/><text class="pl" x="{x+(8 if lon<100 else -8):.0f}" y="{y+4:.0f}" text-anchor="{"start" if lon<100 else "end"}">{esc(n.split("（")[0])} {esc(yr)}</text></g>')
    o.append(f'<text class="cap" x="14" y="22">🌍 从海德堡到全球（示意）</text></svg>')
    return ''.join(o)
