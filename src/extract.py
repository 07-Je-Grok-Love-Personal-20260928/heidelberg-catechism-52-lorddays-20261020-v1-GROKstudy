from bs4 import BeautifulSoup
import json,re
P=json.load(open('pages.json'))
B='/books/book-of-praise/confessions/'
def soup(k): return BeautifulSoup(open(P[k]).read(),'lxml')
def content(k):
    s=soup(k); c=s.find(id='block-tulip-content')
    for nav in c.find_all('nav'): nav.decompose()
    return s.title.string.split('|')[0].strip(), c
def inner(el):
    for a in el.find_all(True):
        a.attrs={k:v for k,v in a.attrs.items() if k in ('href',)}
        if a.name=='a': a.name='span'; a.attrs={}
    return el.decode_contents().strip()
def refs(c):
    ol=c.find('ol',class_='reference-list')
    return [li.get_text(strip=True) for li in ol.find_all('li')] if ol else []
D={}
# creeds
D['creeds_intro']=[inner(p) for p in content('/books/book-of-praise/creeds')[1].select('.article-body p')]
D['creeds']=[]
for slug in ['apostles-creed','nicene-creed','athanasian-creed']:
    k='/books/book-of-praise/creeds/'+slug; t,c=content(k)
    al=c.find(class_='alert')
    intro=[inner(p) for p in c.select('.article-body > div > p')]
    text=[inner(p) for p in al.find_all('p')] if al else []
    D['creeds'].append(dict(slug=slug,title=t,intro=intro,text=text,url='https://ccifellowship.org'+k))
# HC
hc=[]; t,c=content(B+'heidelberg-catechism'); D['hc_intro']=[inner(p) for p in c.select('.article-body p')]
lds=sorted([k for k in P if re.search(r'lord-day-\d+$',k)],key=lambda k:int(k.split('-')[-1]))
for k in lds:
    n=int(k.split('-')[-1]); t,c=content(k)
    qas=[]
    for h in c.find_all('h4'):
        art=h.find_parent('article')
        q=h.get_text(strip=True)
        ps=[inner(p) for p in art.find_all('p')]
        qas.append(dict(q=q,a=ps,refs=refs(art)))
    # hierarchy titles
    parts=k.replace(B+'heidelberg-catechism','').strip('/').split('/')[:-1]
    crumbs=[]; acc=B+'heidelberg-catechism'
    for pp in parts:
        acc+='/'+pp; crumbs.append(content(acc)[0])
    hc.append(dict(n=n,title=t,crumbs=crumbs,qas=qas,url='https://ccifellowship.org'+k))
D['hc']=hc
# Belgic
t,c=content(B+'the-belgic-confession'); D['bc_intro']=[inner(p) for p in c.select('.article-body p')]
bc=[]
for i in range(1,38):
    k=B+'the-belgic-confession/%d'%i; t,c=content(k)
    bc.append(dict(n=i,title=t,paras=[inner(p) for p in c.select('.article-body p')],refs=refs(c),url='https://ccifellowship.org'+k))
D['bc']=bc
t,c=content(B+'canons-of-dort'); D['cd_intro']=[inner(p) for p in c.select('.article-body p')]
cd=[]
for sec in ['section1','section2','section3-4','section5']:
    st=content(B+'canons-of-dort/'+sec)[0]
    arts=sorted([k for k in P if k.startswith(B+'canons-of-dort/'+sec+'/')],key=lambda k:int(k.split('/')[-1]))
    A=[]
    for k in arts:
        t,c=content(k)
        A.append(dict(n=int(k.split('/')[-1]),title=t,paras=[inner(p) for p in c.select('.article-body p')],refs=refs(c),url='https://ccifellowship.org'+k))
    cd.append(dict(sec=sec,title=st,arts=A))
D['cd']=cd
json.dump(D,open('../data.json','w'),ensure_ascii=False,indent=1)
print(len(hc),sum(len(x['qas']) for x in hc),len(bc),[len(x['arts']) for x in cd],[len(c['text']) for c in D['creeds']])
print([ (x['n'],len(x['qas'])) for x in hc])
print(hc[10]['crumbs'],hc[0]['crumbs'])
