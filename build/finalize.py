# v7 post-build: (1) inline the (minified) stylesheet into every page → no render-blocking CSS request;
# (2) write sw.js whose cache name is a hash of the whole build (each deploy = fresh cache, old caches deleted).
import os,re,hashlib,json
SITE=os.path.join(os.path.dirname(__file__),'..','site')
css=open(os.path.join(SITE,'assets/css/style.css')).read().strip()
n=0;h=hashlib.sha1()
pages=[]
for d,_,fs in os.walk(SITE):
    for f in sorted(fs):
        p=os.path.join(d,f);rel=os.path.relpath(p,SITE).replace(os.sep,'/')
        if f.endswith('.html'):
            s=open(p).read()
            if 'data-mkc="' in s:   # v7: static per-page mark counts in the legend (no JS, zero CLS)
                from bs4 import BeautifulSoup
                sp=BeautifulSoup(s,'html.parser'); cnt={}
                for el in sp.select('[class*="mk-"]'):
                    if el.find_parent(class_='nomk'): continue
                    for c in el.get('class',[]):
                        if c.startswith('mk-'): cnt[c]=cnt.get(c,0)+1
                s=re.sub(r'<b class="mkn" data-mkc="(mk-[\w]+)"></b>',lambda m:f'<b class="mkn" data-mkc="{m.group(1)}" title="本页 {cnt.get(m.group(1),0)} 处">{cnt.get(m.group(1),0)}</b>',s)
                open(p,'w').write(s)
            s2=re.sub(r'<link rel="stylesheet" href="(?:\.\./)*assets/css/style\.css">',lambda m:'<style>'+css+'</style>',s,count=1)
            if s2!=s: n+=1; open(p,'w').write(s2); s=s2
            pages.append(rel)
        if rel!='sw.js': h.update(rel.encode()); h.update(open(p,'rb').read())
ver='hc-v8-'+h.hexdigest()[:10]
core=['./','index.html','lorddays.html','texts/hc.html','texts/index.html','memory.html','assets/js/app.js']
sw=f'''/* v8 service worker — instant repeat loads + offline reading. Cache: {ver} */
const V="{ver}",CORE={json.dumps(core)};
self.addEventListener("install",e=>{{e.waitUntil(caches.open(V).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting()))}});
self.addEventListener("activate",e=>{{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k.startsWith("hc-")&&k!==V).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))}});
const put=(c,r,res)=>{{if(res&&res.ok&&(res.type==="basic"||res.type==="cors"))c.put(r,res.clone()).catch(()=>{{}});return res}};
self.addEventListener("fetch",e=>{{const r=e.request;if(r.method!=="GET")return;const u=new URL(r.url);
 const same=u.origin===location.origin,cdn=/^(cdn\\.jsdelivr\\.net)$/.test(u.hostname);
 if(!same&&!cdn)return; // map tiles etc. go straight to the network
 if(same&&u.search&&r.mode==="navigate")return; // ?full / ?lite / test switches bypass the cache
 e.respondWith(caches.open(V).then(async c=>{{const hit=await c.match(r,{{ignoreVary:true}});
  if(cdn&&hit)return hit; // versioned CDN files: cache-first
  const net=fetch(r).then(res=>put(c,r,res));
  if(hit){{e.waitUntil(net.catch(()=>{{}}));return hit}} // stale-while-revalidate
  try{{return await net}}catch(err){{if(r.mode==="navigate"){{const o=await c.match("index.html");if(o)return o}}throw err}}}}))}});
'''
open(os.path.join(SITE,'sw.js'),'w').write(sw)
print('inlined css into',n,'pages ·',len(css),'bytes · sw',ver)
