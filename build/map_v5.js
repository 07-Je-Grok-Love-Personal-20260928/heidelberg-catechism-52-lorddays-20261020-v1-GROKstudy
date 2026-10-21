const m=L.map('map',{scrollWheelZoom:false}).setView([50.2,7.0],5);window.hcMap=m;
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:18,attribution:'&copy; OpenStreetMap contributors'}).addTo(m);
L.circle([49.35,8.2],{radius:70000,color:'#60a5fa',fillOpacity:.12,weight:1}).addTo(m).bindTooltip('选帝侯普法尔茨（Kurpfalz，示意）');
L.circle([51.9,5.0],{radius:110000,color:'#34d399',fillOpacity:.08,weight:1}).addTo(m).bindTooltip('北尼德兰 / 荷兰共和国（示意）');
L.circle([50.6,3.6],{radius:60000,color:'#fb7185',fillOpacity:.08,weight:1}).addTo(m).bindTooltip('南尼德兰（今比利时一带，示意）');
const MK=P.map(p=>{const links=p[5].map(x=>'<a href="ld/'+String(x[0]).padStart(2,'0')+'.html">'+x[1]+'</a>').join('<br>');return L.circleMarker([p[0],p[1]],{radius:9,color:'#fff',weight:2,fillColor:EH[p[3]],fillOpacity:.95}).addTo(m).bindPopup('<b>'+p[2]+'</b><br>'+p[4]+(links?'<hr style="margin:6px 0">📅 相关主日：<br>'+links:''))});
window.hcMK=MK;
const R={u:L.polyline([[51.1079,17.0385],[51.8664,12.6485],[47.3769,8.5417],[49.4094,8.6947]],{color:'#a78bfa',dashArray:'6 8'}).bindTooltip('乌尔西努：布雷斯劳 → 维滕堡 → 苏黎世 → 海德堡'),
h:L.polyline([[49.4094,8.6947],[51.6586,6.6175],[53.3672,7.2057],[51.8133,4.6901]],{color:'#34d399',weight:3}).bindTooltip('要理问答传入尼德兰之路'),
b:L.polyline([[50.6056,3.3878],[51.2194,4.4025],[53.3672,7.2057],[51.8133,4.6901]],{color:'#fb7185',weight:3,dashArray:'4 6'}).bindTooltip('比利时信条之路'),
s:L.polyline([[50.81,8.7708],[47.3769,8.5417],[46.2044,6.1432],[49.4094,8.6947]],{color:'#fbbf24',weight:2,dashArray:'2 6'}).bindTooltip('圣餐之争：马尔堡 → 苏黎世/日内瓦 → 海德堡')};
Object.values(R).forEach(r=>r.addTo(m));
document.querySelectorAll('[data-route]').forEach(b=>b.addEventListener('click',()=>{const r=R[b.dataset.route];if(m.hasLayer(r)){m.removeLayer(r);b.classList.remove('pri')}else{r.addTo(m);b.classList.add('pri');m.fitBounds(r.getBounds(),{padding:[30,30]})}}));
window.hcMapEra=e=>MK.forEach((k,i)=>{const on=e==='all'||P[i][3]===e;k.setStyle({opacity:on?1:.15,fillOpacity:on?.95:.12})});
window.hcFly=i=>{m.flyTo([P[i][0],P[i][1]],7,{duration:.8});MK[i].openPopup()};
document.dispatchEvent(new Event('hcmap'));
