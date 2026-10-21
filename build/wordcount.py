# counts commentary text (CJK chars + latin words) in <main>, excluding verbatim creed/catechism text, scripts, svg, nav
import sys,glob,os,re,json
from bs4 import BeautifulSoup
ROOT=sys.argv[1]; OUT=sys.argv[2] if len(sys.argv)>2 else None
VERB='.qa .q, .qa .a, .qa .refs, .art, .creed, .reading, blockquote, .co-gold, .fc .b, script, style, svg, .mermaid, #ldgame, .tbl.actm'
def count(t):
    cjk=len(re.findall(r'[\u4e00-\u9fff]',t)); lat=len(re.findall(r'[A-Za-z]+',t)); return cjk+lat
res={}
for f in sorted(glob.glob(ROOT+'/*.html')+glob.glob(ROOT+'/ld/*.html')):
    s=BeautifulSoup(re.sub(r'<(/?)template\b',r'<\1div',open(f).read()),'html.parser'); m=s.select_one('main')
    if not m: continue
    for x in m.select(VERB): x.decompose()
    res[os.path.relpath(f,ROOT)]=count(m.get_text(' '))
ld=sum(v for k,v in res.items() if k.startswith('ld/')); ov={k:res[k] for k in ['index.html','bible.html','history.html','lorddays.html','compare.html','memory.html'] if k in res}
summary=dict(ld_total=ld,ld_avg=round(ld/52),overview=ov,overview_total=sum(ov.values()))
print(json.dumps(summary,ensure_ascii=False))
if OUT: json.dump(dict(summary=summary,pages=res),open(OUT,'w'),ensure_ascii=False,indent=1)
