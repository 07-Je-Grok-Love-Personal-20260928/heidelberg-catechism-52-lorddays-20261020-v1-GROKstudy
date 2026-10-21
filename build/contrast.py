# WCAG 2.1 contrast for every theme: body text, muted text, accent-coloured text/links, mark colours, ink-on-accent labels
import re,json,sys
css=open('src/style.css').read()
def block(sel):
    i=css.index(sel); j=css.index('}',i); return dict(re.findall(r'--([\w-]+):(#[0-9a-fA-F]{6})',css[i:j]))
base=block(':root{'); T={'night':base}
for t in ['dawn','forest','grape','ocean']: T[t]={**base,**block(f'html[data-theme={t}]')}
def L(h):
    c=[int(h[i:i+2],16)/255 for i in (1,3,5)]; c=[x/12.92 if x<=.03928 else ((x+.055)/1.055)**2.4 for x in c]
    return .2126*c[0]+.7152*c[1]+.0722*c[2]
def cr(a,b):
    la,lb=sorted([L(a),L(b)],reverse=True); return (la+.05)/(lb+.05)
res={};fails=[]
for t,v in T.items():
    r={}
    for surf in ['bg','card','card2','bg2']:
        r[f'fg/{surf}']=cr(v['fg'],v[surf]); r[f'muted/{surf}']=cr(v['muted'],v[surf])
        for acc in ['intro','misery','deliv','grat','gold','hard','key','teal','mk-bold','mk-def','mk-warn','mk-ref','mk-grace']:
            if acc in v: r[f'{acc}/{surf}']=cr(v[acc],v[surf])
    for acc in ['intro','misery','deliv','grat','gold','hard','teal']: r[f'ink/{acc}']=cr(v['ink'],v[acc])
    res[t]={k:round(x,2) for k,x in r.items()}
    for k,x in r.items():
        lim=4.5
        if x<lim: fails.append((t,k,round(x,2)))
    print(t,'fg/card %.1f'%r['fg/card'],'muted/card %.1f'%r['muted/card'],'min accent/card %.2f'%min(x for k,x in r.items() if k.endswith('/card') and not k.startswith(('fg','muted'))),'min ink/accent %.2f'%min(x for k,x in r.items() if k.startswith('ink/')))
print('FAILS',len(fails)); [print(' ',f) for f in fails]
json.dump(res,open('contrast_v6.json','w'),indent=1)
