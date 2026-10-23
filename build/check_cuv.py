"""v7: verify scripture quotes in notes7.py against FHL 和合本 (bible.fhl.net, version=unv, gb=1)."""
import json,re,os,urllib.request,urllib.parse,sys
C='cache/cuv.json'; cache=json.load(open(C)) if os.path.exists(C) else {}
def verse(b,c,v):
    k=f'{b}{c}:{v}'
    if k not in cache:
        u='https://bible.fhl.net/json/qb.php?'+urllib.parse.urlencode({'chineses':b,'chap':c,'sec':v,'gb':1,'version':'unv'})
        j=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 (hc52 study; verse check)'}),timeout=30)); cache[k]=j['record'][0]['bible_text'] if j['record'] else ''
    return cache[k]
def text(b,c,a,z): return re.sub(r'（(或|有古卷)[^）]*）','',''.join(verse(b,c,v) for v in range(a,z+1)))
N=lambda s:re.sub(r'[―－\u3000\s，。、；：！？「」『』“”‘’,.;:!?……—\-（）()]','',s)
Q=[ # (quote, book, chap, v1, v2)
('你是属我的','赛',43,1,1),('万不以有罪的为无罪','出',34,6,7),('为女子所生','加',4,4,4),('女人的后裔','创',3,15,15),
('一次交付圣徒的真道','犹',1,3,3),('以色列啊，你要听！耶和华我们神是独一的主','申',6,4,4),
('从前你们的意思是要害我，但神的意思原是好的','创',50,20,20),
('你要给他起名叫耶稣，因他要将自己的百姓从罪恶里救出来','太',1,21,21),('你是我的儿子，我今日生你','诗',2,7,7),
('情愿照你的话成就在我身上','路',1,38,38),('必有童女怀孕生子','赛',7,14,14),('我查不出这人有甚么罪来','路',23,4,4),
('为甚么离弃我','太',27,46,46),('你必不将我的灵魂撇在阴间','诗',16,10,10),('你坐在我的右边，等我使你仇敌作你的脚凳','诗',110,1,1),
('我必将我的灵放在你们里面','结',36,27,27),('我要将我的灵浇灌凡有血气的','珥',2,28,28),('我要把我的教会建造在这磐石上','太',16,18,18),
('我知道我的救赎主活着','伯',19,25,25),('我必在肉体之外得见神','伯',19,26,26),('复活在我，生命也在我','约',11,25,25),
('耶和华我们的义','耶',23,6,6),('所有的义都像污秽的衣服','赛',64,6,6),('我们是无用的仆人','路',17,10,10),
('这应许是给你们和你们的儿女','徒',2,39,39),('不是人手所行的割礼','西',2,11,11),
('这是我的身体，为你们舍的','路',22,19,19),('这杯是用我血所立的新约','路',22,20,20),('耶和华的逾越','出',12,11,11),
('我是真葡萄树','约',15,1,1),('我就是门','约',10,9,9),('我必将大卫家的钥匙放在他肩头上；他开，无人能关','赛',22,22,22),
('我要把天国的钥匙给你','太',16,19,19),('你们要撕裂心肠，不撕裂衣服','珥',2,13,13),('当拜主你的神，单要事奉他','太',4,10,10),
('向耶和华守节','出',32,5,5),('甚么誓都不可起','太',5,34,34),('你们的话，是就说是','太',5,37,37),
('顺从神，不顺从人，是应当的','徒',5,29,29),('当孝敬父母，使你的日子在耶和华你神所赐你的地上得以长久','出',20,12,12),
('向弟兄动怒的，难免受审判','太',5,22,22),('我若讹诈了谁，就还他四倍','路',19,8,8),('你们要呼求我','耶',29,12,12),
('你们奉我的名无论求甚么，我必成就','约',14,13,14),('他岂不是你的父、将你买来的吗','申',32,6,6),('你是我们的父','赛',63,16,16),
('耶和华我们的主啊，你的名在全地何其美','诗',8,1,1),('我要使我的大名显为圣','结',36,23,23),('父啊，愿你荣耀你的名','约',12,28,28),
('我已将你的名显明与他们','约',17,6,6),('我的神啊，我乐意照你的旨意行','诗',40,8,8),('不要成就我的意思，只要成就你的意思','路',22,42,42),
('我就是生命的粮','约',6,35,35),('求你按你的慈爱怜恤我','诗',51,1,1),('我要赦免他们的罪孽','耶',31,34,34),('父啊，赦免他们','路',23,34,34),
('我怎能作这大恶，得罪神呢','创',39,9,9),('我已经为你祈求，叫你不至于失了信心','路',22,32,32),('是的','林后',1,20,20),('阿们','林后',1,20,20),
]
bad=[]
for q,b,c,a,z in Q:
    t=text(b,c,a,z); ok=N(q) in N(t)
    if not ok: bad.append((q,f'{b}{c}:{a}-{z}',t))
json.dump(cache,open(C,'w'),ensure_ascii=False)
for x in bad: print('MISMATCH',x)
print('checked',len(Q),'mismatch',len(bad))
ALLOW={'耶和华拯救':'name gloss (太1:21), not a quote','一次献上':'来10:10 wording, ref range cited 来9:26-28；10:10-14'}
# ---- generic scan: “quote”（Book c:v[-w]） in all notes / page builders ----
import glob
pat=re.compile(r'“([^”]{4,60})”[^“”]{0,6}?[（(\[]\s*([一-龥]{1,3})\s?(\d+)[:：](\d+)(?:[-–](\d+))?')
gb=[];n=0
for f in sorted(glob.glob('notes*.py')+['build_pages.py','build_ld.py','history_data.py']):
    for q,b,c,a,z in pat.findall(open(f).read()):
        c,a=int(c),int(a);z=int(z) if z else a
        try: t=text(b,c,a,z)
        except Exception as e: t='ERR '+str(e)
        n+=1
        if q in ALLOW: continue
        parts=[p for p in re.split(r'……|…',q) if N(p)]
        if not all(N(p) in N(t) for p in parts): gb.append((f,q,f'{b}{c}:{a}-{z}',t))
json.dump(cache,open(C,'w'),ensure_ascii=False)
for x in gb: print('G-MISMATCH',x)
print('generic checked',n,'mismatch',len(gb))
