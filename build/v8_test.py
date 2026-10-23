"""v8 tests: live map (normal / tiles blocked / engine blocked / no WebGL), history fly-to, nav cluster (desktop + mobile)."""
import asyncio,sys,json
from playwright.async_api import async_playwright
BASE=sys.argv[1] if len(sys.argv)>1 else 'http://localhost:8780/'
SHOT=sys.argv[2] if len(sys.argv)>2 else '/tmp/v8'
GL=['--use-gl=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']
TILES='**/{server.arcgisonline.com,*.basemaps.cartocdn.com,tile.openstreetmap.org}/**'
fails=[]
def ok(c,msg):
    print(('PASS ' if c else 'FAIL ')+msg,flush=True)
    if not c: fails.append(msg)
async def map_case(b,name,block=None,q='',shot=None,w=1440,theme='night'):
    c=await b.new_context(viewport={'width':w,'height':900});await c.add_init_script(f"localStorage.setItem('hc-theme',JSON.stringify('{theme}'))")
    pg=await c.new_page();errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    blocked=[0]
    async def ab(r): blocked[0]+=1; await r.abort()
    if block=='tiles':
        for h in ['server.arcgisonline.com','basemaps.cartocdn.com','tile.openstreetmap.org']: await pg.route(f'**/*{h}*/**',ab)
        await pg.route(lambda u:any(h in u for h in ['arcgisonline','cartocdn','openstreetmap.org']),ab)
    if block=='lib': await pg.route('**/maplibre-gl.js',ab)
    await pg.goto(BASE+'maps.html?nosw'+q,wait_until='load')
    await pg.add_style_tag(content='section.sec{content-visibility:visible!important}')
    el=pg.locator('h2#m-pal ~ .mpair').first
    await el.scroll_into_view_if_needed();await pg.wait_for_timeout(9000);await el.scroll_into_view_if_needed();await pg.wait_for_timeout(1200)
    st=await pg.evaluate("hcMaps.status().find(x=>x.id==='pal')")
    fbv=await pg.evaluate("getComputedStyle(document.querySelector('.lmap[data-map=pal] .lm-fb')).visibility")
    can=await pg.evaluate("!!document.querySelector('.lmap[data-map=pal] canvas')")
    badge=await pg.evaluate("document.querySelector('.lmap[data-map=pal] .lm-st').textContent")
    nm=await pg.evaluate("document.querySelectorAll('.lmap[data-map=pal] .mkr').length")
    if shot: await el.screenshot(path=shot)
    await c.close()
    print(f'  [{name}] state={st} fallback_visibility={fbv} canvas={can} markers={nm} blocked_requests={blocked[0]} badge="{badge}" errors={errs[:2]}')
    return st,fbv,can,nm,errs
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=GL)
        st,fbv,can,nm,e=await map_case(b,'online',shot=f'{SHOT}/v8-map-live.png')
        ok(st['ok'] and st['state'].startswith('raster:') and can and nm==12 and fbv=='hidden' and not e,'live map loads with online tiles + 12 markers')
        st,fbv,can,nm,e=await map_case(b,'tiles blocked',block='tiles',shot=f'{SHOT}/v8-map-tiles-blocked.png')
        ok(st['ok'] and st['state']=='local' and can and nm==12,'tiles blocked → site-hosted vector base (no blank)')
        st,fbv,can,nm,e=await map_case(b,'engine blocked',block='lib',shot=f'{SHOT}/v8-map-engine-blocked.png')
        ok(st['fail'] and st['state']=='fallback' and fbv=='visible' and not can,'engine blocked → static illustration visible')
        st,fbv,can,nm,e=await map_case(b,'no webgl',q='&maptest=nogl')
        ok(st['fail'] and fbv=='visible','no WebGL → static illustration visible')
        # history: place card fly-to
        c=await b.new_context(viewport={'width':1280,'height':900});pg=await c.new_page()
        await pg.goto(BASE+'history.html?nosw',wait_until='load');await pg.add_style_tag(content='section.sec{content-visibility:visible!important}')
        await pg.locator('#map').scroll_into_view_if_needed();await pg.wait_for_timeout(8000)
        await pg.locator('[data-fly="19"]').click();await pg.wait_for_timeout(3500)
        pop=await pg.evaluate("(document.querySelector('.lmap[data-map=hist] .maplibregl-popup')||{}).textContent||''")
        hl=await pg.evaluate("!!document.querySelector('svg.cmap[data-cm=hist] .pm.hl[data-pk=p19]')")
        ok('多德雷赫特' in pop and hl,'history: “在地图上查看” flies live map + highlights concept map ('+pop[:20]+')')
        await pg.locator('.erab [data-era=dt]').click();await pg.wait_for_timeout(400)
        dim=await pg.evaluate("[document.querySelectorAll('svg.cmap[data-cm=hist] .pm.dim').length,document.querySelectorAll('.lmap[data-map=hist] .mkr.dim').length]")
        ok(dim[0]>10 and dim[1]>10,f'history: era filter dims both maps {dim}')
        await c.close()
        # nav cluster desktop
        c=await b.new_context(viewport={'width':1440,'height':900});pg=await c.new_page()
        await pg.goto(BASE+'ld/05.html?nosw',wait_until='load');await pg.wait_for_timeout(1200)
        vis=await pg.evaluate("[...document.querySelectorAll('#nvItems > *')].filter(e=>e.offsetParent).map(e=>e.dataset.nv||e.className)")
        ok(len(vis)>=8,f'desktop: cluster expanded {vis}')
        nb=await pg.evaluate("(()=>{const n=document.getElementById('navc').getBoundingClientRect();let hit=0;for(const e of document.querySelectorAll('main p, main li, main h2, main h3, main .card')){const r=e.getBoundingClientRect();if(r.width&&r.right>n.left&&r.left<n.right&&r.bottom>n.top&&r.top<n.bottom){hit++}}return {left:Math.round(n.left),mainRight:Math.round(document.querySelector('.wrap').getBoundingClientRect().right),hit}})()")
        ok(nb['mainRight']<=nb['left'],f'desktop: cluster never overlaps content {nb}')
        await pg.click('[data-nv=bottom]');await pg.wait_for_timeout(2500)
        y=await pg.evaluate("[scrollY,document.documentElement.scrollHeight-innerHeight]");ok(y[0]>=y[1]-5,f'bottom button {y}')
        await pg.click('#topBtn');await pg.wait_for_timeout(2500);y=await pg.evaluate("scrollY");ok(y<5,f'top button {y}')
        await pg.keyboard.press('G');await pg.wait_for_timeout(2500);y=await pg.evaluate("[scrollY,document.documentElement.scrollHeight-innerHeight]");ok(y[0]>=y[1]-5,'key G → bottom')
        await pg.keyboard.press('g');await pg.wait_for_timeout(2500);ok(await pg.evaluate("scrollY")<5,'key g → top')
        await pg.keyboard.press('.');await pg.wait_for_load_state('load');await pg.wait_for_timeout(800);ok(pg.url.split('?')[0].endswith('ld/06.html'),'key . → next Lord\'s Day '+pg.url)
        await pg.keyboard.press('[');await pg.wait_for_timeout(1500);ok('ld/05.html' in pg.url,'key [ → back '+pg.url)
        await pg.click('[data-nv=fwd]');await pg.wait_for_timeout(1500);ok('ld/06.html' in pg.url,'forward button '+pg.url)
        await pg.click('[data-nv=back]');await pg.wait_for_timeout(1500);ok('ld/05.html' in pg.url,'back button '+pg.url)
        nx=await pg.evaluate("document.querySelector('#nvItems .nx').getAttribute('href')");ok(nx.endswith('ld/06.html'),'next-LD button in cluster '+nx)
        await pg.keyboard.press('?');await pg.wait_for_timeout(300);ok(await pg.evaluate("document.getElementById('kbHelp').classList.contains('show')"),'? → shortcut help')
        await pg.keyboard.press('Escape')
        await pg.screenshot(path=f'{SHOT}/v8-nav-desktop.png',clip={'x':1440-200,'y':900-420,'width':200,'height':420})
        await pg.click('[data-nv=home]');await pg.wait_for_timeout(1500);ok(pg.url.split('?')[0].endswith('index.html'),'home button '+pg.url)
        await c.close()
        # nav cluster mobile
        c=await b.new_context(viewport={'width':375,'height':812},is_mobile=True,has_touch=True,device_scale_factor=2);pg=await c.new_page()
        await pg.goto(BASE+'ld/05.html?nosw',wait_until='load');await pg.wait_for_timeout(1200)
        n=await pg.evaluate("[...document.querySelectorAll('#navc button,#navc a')].filter(e=>e.offsetParent).length");ok(n==1,f'mobile: collapsed to one button ({n})')
        await pg.screenshot(path=f'{SHOT}/v8-nav-mobile-closed.png')
        await pg.tap('#nvTg');await pg.wait_for_timeout(300)
        n2=await pg.evaluate("[...document.querySelectorAll('#navc button,#navc a')].filter(e=>e.offsetParent).length");ok(n2>=8,f'mobile: tap opens cluster ({n2})')
        await pg.screenshot(path=f'{SHOT}/v8-nav-mobile-open.png')
        await pg.tap('[data-nv=bottom]');await pg.wait_for_timeout(2500)
        ov=await pg.evaluate("(()=>{const n=document.getElementById('navc').getBoundingClientRect(),f=document.querySelector('.foot').getBoundingClientRect();return {navTop:Math.round(n.top),footBottom:Math.round(f.bottom)}})()")
        n3=await pg.evaluate("[...document.querySelectorAll('#navc button,#navc a')].filter(e=>e.offsetParent).length");ok(n3==1,f'mobile: cluster auto-collapses after an action ({n3})')
        ok(ov['footBottom']<=ov['navTop'],f'mobile: at page end the cluster does not cover the footer {ov}')
        await c.close()
        # marks page on mobile
        c=await b.new_context(viewport={'width':375,'height':812},is_mobile=True,has_touch=True,device_scale_factor=2);pg=await c.new_page()
        await pg.goto(BASE+'marks.html?nosw',wait_until='load');await pg.wait_for_timeout(1000)
        await pg.screenshot(path=f'{SHOT}/v8-marks-mobile.png')
        await pg.evaluate("document.getElementById('tb').scrollIntoView()");await pg.wait_for_timeout(600)
        await pg.locator('h2#lg ~ .mklg button[data-mkf=mk-l]').first.tap();await pg.wait_for_timeout(500)
        ok(await pg.evaluate("document.documentElement.dataset.mkf==='mk-l'"),'marks: legend focus filter')
        await pg.evaluate("document.getElementById('demo').scrollIntoView()");await pg.wait_for_timeout(500)
        await pg.screenshot(path=f'{SHOT}/v8-marks-mobile-focus.png')
        await c.close()
        await b.close()
    print('FAILS',len(fails),fails)
asyncio.run(main())
