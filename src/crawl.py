import re, os, time, urllib.request, hashlib, json
base="https://ccifellowship.org"
prefixes=["/books/book-of-praise/confessions","/books/book-of-praise/creeds"]
seen=set(); queue=[p for p in prefixes]; pages={}
os.makedirs("pages",exist_ok=True)
while queue:
    p=queue.pop(0)
    if p in seen: continue
    seen.add(p)
    try:
        req=urllib.request.Request(base+p,headers={"User-Agent":"Mozilla/5.0"})
        h=urllib.request.urlopen(req,timeout=30).read().decode("utf-8")
    except Exception as e:
        print("ERR",p,e); continue
    fn="pages/"+p.strip("/").replace("/","__")+".html"
    open(fn,"w").write(h); pages[p]=fn
    for l in re.findall(r'href="(/books/book-of-praise/(?:confessions|creeds)[^"#?]*)"',h):
        if l not in seen: queue.append(l)
json.dump(pages,open("pages.json","w"),indent=1)
print(len(pages))
