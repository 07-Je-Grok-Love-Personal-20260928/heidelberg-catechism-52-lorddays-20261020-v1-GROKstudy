# Compare every verbatim block on the built site with the original ccifellowship.org pages (fresh parse of crawled HTML)
import json,glob,re,os
from bs4 import BeautifulSoup
ROOT='/workspace/hc52-20261020'
P=json.load(open(ROOT+'/src/pages.json'))
def norm(s): return re.sub(r'\s+',' ',s).strip()
orig=set()
for k,f in P.items():
    s=BeautifulSoup(open(ROOT+'/src/'+f).read(),'lxml'); c=s.find(id='block-tulip-content')
    if not c: continue
    for nav in c.find_all('nav'): nav.decompose()
    for el in c.find_all(['p','h4','li']): orig.add(norm(el.get_text()))
tot=bad=0; badl=[]
for f in glob.glob(ROOT+'/site/**/*.html',recursive=True):
    s=BeautifulSoup(open(f).read(),'lxml')
    sel=s.select('.qa .q span:not(.qn)')+s.select('.qa .a p')+s.select('.qa ol.refs li')+s.select('.reading .art p:not(.src)')+s.select('.creed p')+s.select('.fc .b p')+s.select('details .reading p')+s.select('.card.reading > p')
    for el in sel:
        t=norm(el.get_text()); tot+=1
        if t not in orig: bad+=1; badl.append((os.path.relpath(f,ROOT),t[:80]))
print('checked',tot,'verbatim blocks; mismatches',bad)
for x in badl[:20]: print(x)
# v3: gold-quote callouts must be exact substrings of an original paragraph
allorig='\n'.join(orig)
gt=gb=0;mk=0
for f in glob.glob(ROOT+'/site/**/*.html',recursive=True):
    s=BeautifulSoup(open(f).read(),'lxml')
    mk+=len(s.select('[class^="mk-"]'))
    for el in s.select('.co-gold:not(.sample)'):
        m=re.search(r'“(.+?)”',el.get_text()); gt+=1
        if not m or m.group(1) not in allorig: gb+=1; print('GOLD MISMATCH',f,m and m.group(1))
print('gold quotes checked',gt,'mismatches',gb,'| mark spans on site',mk)
