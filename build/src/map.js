/* v8 · map.js — self-hosted MapLibre GL live maps with a no-blank fallback chain.
   Layers (bottom→top): ① site-hosted Natural Earth vector base (always present, works offline / anywhere the site loads)
   ② online raster: Esri → CARTO → OSM (first reachable wins; auto-switch on tile errors) ③ regions / routes / HTML markers.
   No WebGL or engine failure → the build-time SVG illustration stays visible. At most 3 live maps exist at once. */
(()=>{
const S=document.currentScript,ROOT=(S&&S.dataset.root)||'',Q=location.search,D=document,R=D.documentElement;
const boxes=[...D.querySelectorAll('.lmap[data-map]')];if(!boxes.length)return;
const $=(s,c)=>(c||D).querySelector(s),cv=n=>getComputedStyle(R).getPropertyValue(n).trim()||'#888';
const PROV=[
 {id:'esri',name:'Esri 街道图',url:'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',attr:'Tiles © <a href="https://www.esri.com/" target="_blank" rel="noopener">Esri</a> — Esri, HERE, Garmin, © OpenStreetMap contributors',max:18},
 {id:'carto',name:'CARTO Voyager',url:'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}.png',sub:['a','b','c','d'],attr:'© <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a> contributors © <a href="https://carto.com/attributions" target="_blank" rel="noopener">CARTO</a>',max:19},
 {id:'osm',name:'OpenStreetMap',url:'https://tile.openstreetmap.org/{z}/{x}/{y}.png',attr:'© <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a> contributors',max:19}];
const SAT={id:'sat',name:'Esri 卫星影像',url:'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',attr:'Imagery © <a href="https://www.esri.com/" target="_blank" rel="noopener">Esri</a>, Maxar, Earthstar Geographics',max:18};
const tiles=p=>p.sub?p.sub.map(s=>p.url.replace('{s}',s)):[p.url];
const NE='地理底图 © <a href="https://www.naturalearthdata.com/" target="_blank" rel="noopener">Natural Earth</a>（公有领域）';
const status=(b,t,s)=>{const e=$('.lm-st',b);if(e){e.textContent=t;e.dataset.s=s||''}b.dataset.state=s||''};
const hasGL=()=>{if(/[?&]maptest=nogl/.test(Q))return false;try{const c=D.createElement('canvas');return!!(c.getContext('webgl2')||c.getContext('webgl'))}catch(e){return false}};
let libP,baseP;
const loadLib=()=>libP||(libP=new Promise((res,rej)=>{
 if(/[?&]maptest=nolib/.test(Q))return rej(Error('test: library blocked'));
 if(window.maplibregl)return res(window.maplibregl);
 const l=D.createElement('link');l.rel='stylesheet';l.href=ROOT+'assets/vendor/maplibre-gl.css';D.head.appendChild(l);
 const s=D.createElement('script');s.src=ROOT+'assets/vendor/maplibre-gl.js';s.async=true;
 s.onload=()=>window.maplibregl?res(window.maplibregl):rej(Error('no maplibregl'));s.onerror=()=>rej(Error('engine failed to load'));D.head.appendChild(s);
 setTimeout(()=>rej(Error('engine timeout')),20000)}));
const loadBase=()=>baseP||(baseP=fetch(ROOT+'assets/geo/base.json').then(r=>{if(!r.ok)throw Error('base '+r.status);return r.json()}));
/* --- tile provider probe: all in parallel, highest-priority success wins; result cached for the session --- */
const SK='hc-tiles-v8',bad=new Set(JSON.parse(sessionStorage.getItem(SK+'-bad')||'[]'));
const probe1=(p,ms)=>new Promise(r=>{const i=new Image();let done=0;const f=v=>{if(!done){done=1;r(v)}};i.onload=()=>f(true);i.onerror=()=>f(false);setTimeout(()=>f(false),ms);
 i.src=tiles(p)[0].replace('{z}','3').replace('{x}','4').replace('{y}','2')+(p.url.includes('?')?'&':'?')+'_='+Math.floor(Date.now()/36e5)});
let provP;
const pickProv=()=>provP||(provP=(async()=>{
 if(/[?&]maptest=local/.test(Q))return null;
 const c=sessionStorage.getItem(SK);if(c&&!bad.has(c))return PROV.find(p=>p.id===c)||null;
 const pr=PROV.map(p=>bad.has(p.id)?Promise.resolve(false):probe1(p,6000));
 for(let i=0;i<PROV.length;i++){if(await pr[i]){sessionStorage.setItem(SK,PROV[i].id);return PROV[i]}}
 return null})());
const markBad=id=>{bad.add(id);sessionStorage.setItem(SK+'-bad',JSON.stringify([...bad]));sessionStorage.removeItem(SK);provP=null};
/* --- geometry helpers --- */
const circle=([lon,lat],km,n=64)=>{const out=[];for(let i=0;i<=n;i++){const a=i/n*2*Math.PI;out.push([lon+km/111.32/Math.cos(lat*Math.PI/180)*Math.cos(a),lat+km/110.57*Math.sin(a)])}return out};
const my=l=>Math.log(Math.tan(Math.PI/4+l*Math.PI/360)),iy=y=>(2*Math.atan(Math.exp(y))-Math.PI/2)*180/Math.PI;
const curve=(pts,bend=.16)=>{const o=[];for(let i=0;i<pts.length-1;i++){const[x1,y1]=[pts[i][0],my(pts[i][1])*57.3],[x2,y2]=[pts[i+1][0],my(pts[i+1][1])*57.3];
 const cx=(x1+x2)/2+(y2-y1)*bend,cy=(y1+y2)/2-(x2-x1)*bend;for(let t=0;t<=1.0001;t+=1/24){const a=(1-t)*(1-t),b=2*(1-t)*t,c=t*t;o.push([a*x1+b*cx+c*x2,iy((a*y1+b*cy+c*y2)/57.3)])}}return o};
const DASH={solid:null,dash:[2.2,1.6],dot:[.4,1.4]};
const themeDark=()=>/^(night|forest|grape|ember|aurora)$/.test(R.dataset.theme||'night');
const baseLayers=()=>[
 {id:'bg',type:'background',paint:{'background-color':cv('--sea2')}},
 {id:'w',type:'fill',source:'base',filter:['==',['get','k'],'w'],paint:{'fill-color':cv('--land1')}},
 {id:'l',type:'fill',source:'base',filter:['==',['get','k'],'l'],paint:{'fill-color':cv('--land1'),'fill-outline-color':cv('--land2')}},
 {id:'a',type:'fill',source:'base',filter:['==',['get','k'],'a'],paint:{'fill-color':cv('--sea1')}},
 {id:'r',type:'line',source:'base',filter:['==',['get','k'],'r'],paint:{'line-color':cv('--river'),'line-width':['interpolate',['linear'],['zoom'],3,.6,8,2.2]}},
 {id:'b',type:'line',source:'base',filter:['==',['get','k'],'b'],paint:{'line-color':cv('--muted'),'line-opacity':.35,'line-width':.7,'line-dasharray':[3,2]}}];
const rasPaint=()=>themeDark()?{'raster-brightness-max':.82,'raster-saturation':-.15,'raster-contrast':.05}:{'raster-saturation':-.05};
const live=new Map();let useOrder=[];
function build(box){
 const id=box.dataset.map,def=JSON.parse($('#md-'+id).textContent),inner=$('.lm-in',box),bar=box.nextElementSibling&&box.nextElementSibling.classList.contains('lmbar')?box.nextElementSibling:null;
 const st={id,box,def,mode:(bar&&bar.dataset.mode)||'auto',prov:null,errs:0,oks:0,off:new Set(),markers:[]};live.set(box,st);
 if(!hasGL()){status(box,'🖼️ 示意图模式：此浏览器不支持 WebGL，已显示同一幅示意图','fallback');box.classList.add('fail');return}
 status(box,'⏳ 正在加载站内地图引擎…','loading');
 Promise.all([loadLib(),loadBase()]).then(([gl,base])=>{
  if(!live.has(box))return;
  const[x0,y0,x1,y1]=def.bbox;
  const m=new gl.Map({container:inner,style:{version:8,sources:{base:{type:'geojson',data:base,attribution:NE}},layers:baseLayers()},
   bounds:[[x0,y0],[x1,y1]],fitBoundsOptions:{padding:18},attributionControl:{compact:true},cooperativeGestures:true,dragRotate:false,pitchWithRotate:false,maxZoom:15,minZoom:1,renderWorldCopies:false,fadeDuration:0,
   locale:{'CooperativeGesturesHandler.WindowsHelpText':'按住 Ctrl 并滚动滚轮以缩放地图','CooperativeGesturesHandler.MacHelpText':'按住 ⌘ 并滚动以缩放地图','CooperativeGesturesHandler.MobileHelpText':'请用双指移动地图','NavigationControl.ZoomIn':'放大','NavigationControl.ZoomOut':'缩小','AttributionControl.ToggleAttribution':'地图来源'}});
  st.m=m;m.touchZoomRotate.disableRotation();m.addControl(new gl.NavigationControl({showCompass:false}),'top-right');m.addControl(new gl.ScaleControl({unit:'metric'}),'bottom-left');
  m.on('error',e=>{if(e&&e.sourceId==='ras'){st.errs++;if(st.errs>=8&&st.oks<2)rasFail(st)}});
  m.on('data',e=>{if(e.sourceId==='ras'&&e.tile&&e.dataType==='source')st.oks++});
  m.on('load',()=>{overlays(st,gl);['dragstart','zoomstart'].forEach(ev=>m.on(ev,e=>{if(e.originalEvent)st.touched=1}));if(window.ResizeObserver){let rw=inner.clientWidth;new ResizeObserver(()=>{if(!st.m||Math.abs(inner.clientWidth-rw)<4)return;rw=inner.clientWidth;m.resize();if(!st.touched)m.fitBounds([[x0,y0],[x1,y1]],{padding:12,duration:0})}).observe(inner)}box.classList.add('ok');box.classList.remove('fail');setMode(st,st.mode)});
 }).catch(err=>{status(box,'🖼️ 示意图模式：实时地图引擎未能加载（'+(err&&err.message||err)+'），已显示同一幅示意图','fallback');box.classList.add('fail')});
}
function overlays(st,gl){
 const{m,def}=st;
 m.addSource('reg',{type:'geojson',data:{type:'FeatureCollection',features:def.regions.map(r=>({type:'Feature',properties:{c:cv(r.cv)},geometry:{type:'Polygon',coordinates:[circle(r.c,r.km)]}}))}});
 m.addLayer({id:'reg-f',type:'fill',source:'reg',paint:{'fill-color':['get','c'],'fill-opacity':.16}});
 m.addLayer({id:'reg-l',type:'line',source:'reg',paint:{'line-color':['get','c'],'line-width':1.5,'line-dasharray':[2,2]}});
 const P=Object.fromEntries(def.places.map(p=>[p.k,p]));
 const rf=def.routes.map(r=>({type:'Feature',properties:{k:r.k,c:cv(r.cv),s:r.s},geometry:{type:'LineString',coordinates:curve(r.pts.map(k=>P[k].c))}}));
 const wf=[];if(def.world_pts.length){const h=[8.69,49.41];def.world_pts.forEach((w,i)=>wf.push({type:'Feature',properties:{k:'_w',c:cv('--teal')},geometry:{type:'LineString',coordinates:curve([h,w.c],.2)}}))}
 st.rfc={type:'FeatureCollection',features:rf};m.addSource('rt',{type:'geojson',data:st.rfc});
 if(wf.length){m.addSource('rtw',{type:'geojson',data:{type:'FeatureCollection',features:wf}});m.addLayer({id:'rt-w',type:'line',source:'rtw',maxzoom:3.6,layout:{'line-cap':'round'},paint:{'line-color':['get','c'],'line-width':2,'line-opacity':.7,'line-dasharray':[.1,2.2]}})}
 m.addLayer({id:'rt-glow',type:'line',source:'rt',layout:{'line-cap':'round','line-join':'round'},paint:{'line-color':['get','c'],'line-width':9,'line-opacity':.18}});
 for(const s in DASH){const L={id:'rt-'+s,type:'line',source:'rt',filter:['==',['get','s'],s],layout:{'line-cap':'round','line-join':'round'},paint:{'line-color':['get','c'],'line-width':3.2}};if(DASH[s])L.paint['line-dasharray']=DASH[s];m.addLayer(L)}
 const mk=(p,c,i,small)=>{const e=D.createElement('button');e.type='button';e.className='mkr'+(small?' s':'');e.style.setProperty('--c',c);e.innerHTML='<b>'+(i||'')+'</b><span>'+p.n+'</span>';e.title=p.n+(p.y?' · '+p.y:'');e.setAttribute('aria-label',e.title);
  const pop=new gl.Popup({offset:16,closeButton:true,maxWidth:'280px'}).setHTML('<div class="mpop"><b>'+(i?i+'. ':'')+p.n+'</b>'+(p.en?' <span class="en">'+p.en+'</span>':'')+(p.y?'<span class="yr">'+p.y+'</span>':'')+'<p>'+p.d+'</p></div>');
  const M=new gl.Marker({element:e,anchor:'center'}).setLngLat(p.c).setPopup(pop).addTo(m);e.addEventListener('click',()=>window.hcHL&&p.k&&window.hcHL(def.id,p.k,0));return M};
 st.markers=def.places.map(p=>{const M=mk(p,cv(p.cv),p.i);M._k=p.k;return M});
 st.wmk=def.world_pts.map(w=>mk(w,cv('--teal'),'',1));
 st.syncWorld=()=>{const z=m.getZoom();st.wmk.forEach(M=>M.getElement().style.display=z<3.6?'':'none')};if(st.wmk.length){m.on('zoomend',st.syncWorld);st.syncWorld()}
 applyRoutes(st);eraApply(st);
 st.m.on('moveend',()=>declutter(st));declutter(st);
 const at=st.box.querySelector('.maplibregl-ctrl-attrib');if(at)at.classList.remove('maplibregl-compact-show');
}
const declutter=st=>{const m=st.m;if(!m)return;const all=[...st.markers,...(st.wmk||[])].filter(M=>M.getElement().style.display!=='none');const pts=all.map(M=>m.project(M.getLngLat()));
 const occ=pts.map(p=>[p.x-11,p.y-11,p.x+11,p.y+11]);const W=st.box.clientWidth,H=st.box.clientHeight;
 all.forEach((M,i)=>{const e=M.getElement(),sp=e.querySelector('span');if(!sp)return;const p=pts[i],w=[...sp.textContent].reduce((a,c)=>a+(c.charCodeAt(0)>255?12:7),12),b=[p.x+13,p.y-9,p.x+13+w,p.y+9];
  const bad=b[2]>W||p.x<0||p.y<0||p.y>H||occ.some((q,j)=>j!==i&&!(b[2]<q[0]||q[2]<b[0]||b[3]<q[1]||q[3]<b[1]));e.classList.toggle('nolab',bad);if(!bad)occ.push(b)})};
const applyRoutes=st=>{if(!st.m||!st.m.getLayer('rt-solid'))return;const f=st.off.size?['!',['in',['get','k'],['literal',[...st.off]]]]:null;['rt-glow','rt-solid','rt-dash','rt-dot'].forEach(l=>{const base=l==='rt-glow'?null:['==',['get','s'],l.slice(3)];st.m.setFilter(l,f&&base?['all',base,f]:(f||base))})};
function setRas(st,p){const m=st.m;if(m.getLayer('ras'))m.removeLayer('ras');if(m.getSource('ras'))m.removeSource('ras');st.errs=0;st.oks=0;st.prov=p;
 if(!p)return;m.addSource('ras',{type:'raster',tiles:tiles(p),tileSize:256,maxzoom:p.max,attribution:p.attr+' · '+NE});m.addLayer({id:'ras',type:'raster',source:'ras',paint:rasPaint()},'reg-f')}
function rasFail(st){const p=st.prov;if(!p)return;if(p.id==='sat'){setRas(st,null);status(st.box,'🎨 卫星影像暂不可用 → 已切换为站内主题底图','local');return}
 markBad(p.id);const nx=PROV.find(q=>!bad.has(q.id));if(nx&&st.mode==='auto'){setRas(st,nx);status(st.box,'🔁 '+p.name+' 加载失败 → 改用 '+nx.name,'raster:'+nx.id)}else{setRas(st,null);status(st.box,'🎨 在线底图均不可用 → 已切换为站内主题底图（离线可用）','local')}}
async function setMode(st,mode){st.mode=mode;const b=st.box.nextElementSibling;if(b&&b.classList.contains('lmbar')){b.dataset.mode=mode;b.querySelectorAll('[data-ml]').forEach(x=>x.classList.toggle('on',x.dataset.ml===mode))}
 if(!st.m)return;
 if(mode==='local'){setRas(st,null);status(st.box,'🎨 站内主题底图 · Natural Earth（无需外网）','local');return}
 if(mode==='sat'){setRas(st,SAT);status(st.box,'🛰️ '+SAT.name,'raster:sat');return}
 status(st.box,'🎨 站内底图已就绪 · 正在连接在线街道图…','local');const p=await pickProv();if(st.mode!=='auto'||!st.m)return;
 if(p){setRas(st,p);status(st.box,'🗺️ 在线底图：'+p.name+'（失败时自动回退）','raster:'+p.id)}else{setRas(st,null);status(st.box,'🎨 在线底图不可达 → 站内主题底图（Natural Earth，离线可用）','local')}}
function drop(box){const st=live.get(box);if(!st)return;try{st.m&&st.m.remove()}catch(e){}live.delete(box);$('.lm-in',box).innerHTML='';box.classList.remove('ok','fail');status(box,'🗺️ 已暂停以节省内存，滚动回来即重新加载','idle')}
/* --- lazy create, keep ≤3 alive (least-recently-visible dropped) --- */
/* v8 perf: never construct a WebGL map while the page is scrolling — wait until scrolling settles (450 ms), then build one map per idle slot */
let lastSc=0,tq=0;addEventListener('scroll',()=>{lastSc=performance.now()},{passive:true});
const ric=window.requestIdleCallback||(f=>setTimeout(f,60));
function queue(){if(tq)return;tq=setTimeout(pump,120)}
function pump(){tq=0;const wait=450-(performance.now()-lastSc);if(wait>0){tq=setTimeout(pump,wait+20);return}
 const b=useOrder.slice().reverse().find(x=>vis.has(x)&&!live.has(x));if(!b)return;ric(()=>{if(performance.now()-lastSc<400){queue();return}if(vis.has(b)&&!live.has(b))build(b);queue()},{timeout:1200})}
const vis=new Set();
const io=new IntersectionObserver(es=>{es.forEach(e=>{const b=e.target;if(e.isIntersecting){vis.add(b);useOrder=useOrder.filter(x=>x!==b);useOrder.push(b);if(!live.has(b))queue(b)}else vis.delete(b)});
 while(live.size>3){const old=useOrder.find(b=>live.has(b)&&!vis.has(b));if(!old)break;useOrder=useOrder.filter(x=>x!==old);drop(old)}},{rootMargin:'250px 0px'});
boxes.forEach(b=>io.observe(b));
const stOf=id=>[...live.values()].find(s=>s.id===id);
/* --- controls & cross-talk with the concept map --- */
D.addEventListener('click',e=>{const t=e.target.closest('.lmbar [data-ml],.lmbar [data-mfit],.lmbar [data-mworld]');if(!t)return;const box=t.closest('.lmbar').previousElementSibling,st=live.get(box);
 if(t.dataset.ml){if(st)setMode(st,t.dataset.ml);else t.closest('.lmbar').dataset.mode=t.dataset.ml;return}
 if(!st||!st.m)return;const[x0,y0,x1,y1]=st.def.bbox;if(t.hasAttribute('data-mworld'))st.m.fitBounds([[-125,-40],[150,62]],{padding:10,duration:900});else st.m.fitBounds([[x0,y0],[x1,y1]],{padding:18,duration:700})});
addEventListener('hcplace',e=>{const{map,key}=e.detail,st=stOf(map);if(!st||!st.m)return;const M=st.markers.find(x=>x._k===key);if(!M)return;st.markers.forEach(x=>x.getPopup().isOpen()&&x.togglePopup());
 st.m.flyTo({center:M.getLngLat(),zoom:Math.max(st.m.getZoom(),6),speed:1.4});M.togglePopup();st.box.scrollIntoView({block:'nearest',behavior:'smooth'})});
addEventListener('hcroute',e=>{const{map,key,on}=e.detail,st=stOf(map);const box=boxes.find(b=>b.dataset.map===map);const s=st||{off:new Set()};if(st){on?st.off.delete(key):st.off.add(key);applyRoutes(st)}});
addEventListener('hcplay',e=>{const st=stOf(e.detail.map);if(!st||!st.m||!st.rfc)return;const gl=window.maplibregl;const fs=st.rfc.features.filter(f=>f.properties.k!=='_w'&&!st.off.has(f.properties.k));const path=fs.flatMap(f=>f.geometry.coordinates);if(!path.length)return;
 const el=D.createElement('div');el.className='mdot';const M=new gl.Marker({element:el}).setLngLat(path[0]).addTo(st.m);const t0=performance.now(),dur=Math.min(9000,1200*fs.length+1500);
 const step=t=>{const p=Math.min(1,(t-t0)/dur);M.setLngLat(path[Math.min(path.length-1,Math.floor(p*(path.length-1)))]);if(p<1)requestAnimationFrame(step);else setTimeout(()=>M.remove(),900)};requestAnimationFrame(step)});
addEventListener('hcera',e=>{const st=stOf(e.detail.map);const era=e.detail.era;window._hcEra=era;if(!st)return;eraApply(st)});
const eraApply=st=>{const era=window._hcEra||'all';const P=Object.fromEntries(st.def.places.map(p=>[p.k,p]));st.markers.forEach(M=>M.getElement().classList.toggle('dim',era!=='all'&&P[M._k].era!==era))};
/* theme change → recolour every live map */
new MutationObserver(()=>{live.forEach(st=>{const m=st.m;if(!m||!m.isStyleLoaded())return;baseLayers().forEach(L=>{for(const k in L.paint)if(!/dasharray/.test(k))m.setPaintProperty(L.id,k,L.paint[k])});if(m.getLayer('ras')){const p=rasPaint();['raster-brightness-max','raster-saturation','raster-contrast'].forEach(k=>m.setPaintProperty('ras',k,p[k]===undefined?(k==='raster-brightness-max'?1:0):p[k]))}
 const P=Object.fromEntries(st.def.places.map(p=>[p.k,p]));st.markers.forEach(M=>M.getElement().style.setProperty('--c',cv(P[M._k].cv)))})}).observe(R,{attributes:true,attributeFilter:['data-theme']});
window.hcMaps={live,stOf,PROV,status:()=>boxes.map(b=>({id:b.dataset.map,state:b.dataset.state||'',ok:b.classList.contains('ok'),fail:b.classList.contains('fail')}))};
})();
