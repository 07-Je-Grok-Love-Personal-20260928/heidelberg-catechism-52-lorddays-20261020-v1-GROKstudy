# v6: render every <div class="mermaid"> to static SVG at build time (no CDN, no runtime JS),
# colours mapped to CSS variables so the diagrams follow all 5 themes.
import glob,re,json,os
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from common import SITE,HEXVAR
MJS='/tmp/lh/node_modules/mermaid/dist/mermaid.min.js'
PH={'#010101':'var(--card2)','#020202':'var(--fg)','#030303':'var(--bd)','#040404':'var(--muted)','#050505':'var(--card)','#060606':'var(--bg2)','#070707':'var(--card)'}
TV=dict(fontFamily='PingFang SC, Microsoft YaHei, Noto Sans SC, sans-serif',primaryColor='#010101',primaryTextColor='#020202',primaryBorderColor='#030303',
        lineColor='#040404',secondaryColor='#050505',tertiaryColor='#060606',textColor='#020202',mainBkg='#010101',nodeBorder='#030303',
        clusterBkg='#060606',clusterBorder='#030303',edgeLabelBackground='#070707',titleColor='#020202',nodeTextColor='#020202')
def recolor(svg):
    def h8(m):
        h=m.group(1).lower();a=int(m.group(2),16)*100//255
        return f'color-mix(in srgb,{HEXVAR[h]} {a}%,transparent)' if h in HEXVAR else m.group(0)
    svg=re.sub(r'(#[0-9a-fA-F]{6})([0-9a-fA-F]{2})\b',h8,svg)
    for k,v in PH.items(): svg=re.sub(k,v,svg,flags=re.I)
    svg=re.sub(r'#[0-9a-fA-F]{6}\b',lambda m:HEXVAR.get(m.group(0).lower(),m.group(0)),svg)
    return svg
def main():
    files=[f for f in glob.glob(SITE+'/**/*.html',recursive=True) if 'class="mermaid"' in open(f).read()]
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':1400,'height':900})
        pg.set_content('<html><body><div id="o"></div></body></html>'); pg.add_script_tag(path=MJS)
        pg.evaluate('tv=>mermaid.initialize({startOnLoad:false,theme:"base",securityLevel:"loose",flowchart:{useMaxWidth:true,htmlLabels:false},themeVariables:tv})',TV)
        n=0
        for f in files:
            s=BeautifulSoup(open(f),'html.parser')
            for i,d in enumerate(s.select('div.mermaid')):
                import html as _h
                src=_h.unescape(re.sub(r'<br\s*/?>','<br/>',d.decode_contents()))
                svg=pg.evaluate('async([id,src])=>{const r=await mermaid.render(id,src);return r.svg}',[f'mm{os.path.basename(f)[:-5]}{i}',src])
                svg=recolor(svg)
                new=BeautifulSoup(f'<div class="mermaid-static" role="img" aria-label="流程图">{svg}</div>','html.parser')
                d.replace_with(new); n+=1
            open(f,'w').write(str(s))
        b.close()
    print('mermaid prerendered',n,'in',[os.path.relpath(f,SITE) for f in files])
main()
