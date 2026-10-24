/* v8 service worker — instant repeat loads + offline reading. Cache: hc-v9-7de41a7586 */
const V="hc-v9-7de41a7586",CORE=["./", "index.html", "lorddays.html", "texts/hc.html", "texts/index.html", "memory.html", "assets/js/app.js"];
self.addEventListener("install",e=>{e.waitUntil(caches.open(V).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting()))});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k.startsWith("hc-")&&k!==V).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
const put=(c,r,res)=>{if(res&&res.ok&&(res.type==="basic"||res.type==="cors"))c.put(r,res.clone()).catch(()=>{});return res};
self.addEventListener("fetch",e=>{const r=e.request;if(r.method!=="GET")return;const u=new URL(r.url);
 const same=u.origin===location.origin,cdn=/^(cdn\.jsdelivr\.net)$/.test(u.hostname);
 if(!same&&!cdn)return; // map tiles etc. go straight to the network
 if(same&&u.search&&r.mode==="navigate")return; // ?full / ?lite / test switches bypass the cache
 e.respondWith(caches.open(V).then(async c=>{const hit=await c.match(r,{ignoreVary:true});
  if(cdn&&hit)return hit; // versioned CDN files: cache-first
  const net=fetch(r).then(res=>put(c,r,res));
  if(hit){e.waitUntil(net.catch(()=>{}));return hit} // stale-while-revalidate
  try{return await net}catch(err){if(r.mode==="navigate"){const o=await c.match("index.html");if(o)return o}throw err}}))});
