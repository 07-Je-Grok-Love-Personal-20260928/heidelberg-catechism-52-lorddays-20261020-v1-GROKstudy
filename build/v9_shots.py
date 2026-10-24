"""v9 screenshots → shots/: every theme (index hero + a map), marks 3.0 / typography, charts."""
import asyncio,sys,os
from playwright.async_api import async_playwright
BASE=sys.argv[1] if len(sys.argv)>1 else 'http://localhost:8780/'
OUT=sys.argv[2] if len(sys.argv)>2 else os.path.join(os.path.dirname(__file__),'..','shots')
TH=['night','dawn','forest','grape','ocean','sakura','citrus','ember','aurora','sumi']
async def shot(pg,url,theme,path,sel=None,full=False,pre=None):
    await pg.evaluate(f"localStorage.setItem('hc-theme',JSON.stringify('{theme}'))")
    await pg.goto(BASE+url+('&' if '?' in url else '?')+'nosw',wait_until='load');await pg.wait_for_timeout(1200)
    if pre: await pg.evaluate(pre);await pg.wait_for_timeout(1500)
    if sel:
        el=pg.locator(sel).first;await el.scroll_into_view_if_needed();await pg.wait_for_timeout(1400);await el.screenshot(path=path)
    else: await pg.screenshot(path=path,full_page=full)
    print('saved',path)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'])
        c=await b.new_context(viewport={'width':1440,'height':900},device_scale_factor=1);pg=await c.new_page()
        await pg.goto(BASE+'index.html?nosw')
        for t in TH: await shot(pg,'index.html',t,f'{OUT}/v9-theme-{t}.png')
        await shot(pg,'index.html','sakura',f'{OUT}/v9-theme-picker.png',pre="document.getElementById('thp').classList.add('open')")
        await shot(pg,'ld/01.html','sumi',f'{OUT}/v9-marks-typography-sumi.png',sel='section:has(#text)'
        await shot(pg,'ld/21.html','citrus',f'{OUT}/v9-marks-typography-citrus.png',sel='section:has(#essence)'
        await shot(pg,'marks.html','ember',f'{OUT}/v9-marks-legend-ember.png',sel='main section.sec')
        await shot(pg,'lorddays.html','aurora',f'{OUT}/v9-chart-terms-aurora.png',sel='section:has(#terms)')
        await shot(pg,'ld/01.html','ocean',f'{OUT}/v9-chart-kw-matrix-ocean.png',sel='section:has(#ess-kwm)')
        await shot(pg,'maps.html?maptest=local','ember',f'{OUT}/v9-map-ember.png',sel='main section.msec')
        await shot(pg,'maps.html?maptest=local','citrus',f'{OUT}/v9-map-citrus.png',sel='main section.msec')
        m=await b.new_context(viewport={'width':375,'height':812},device_scale_factor=2,is_mobile=True,has_touch=True);mp=await m.new_page()
        await mp.goto(BASE+'index.html?nosw')
        await shot(mp,'ld/01.html','sakura',f'{OUT}/v9-mobile-ld01-sakura.png')
        await shot(mp,'ld/01.html','aurora',f'{OUT}/v9-mobile-ld01-aurora.png',pre="document.getElementById('text').scrollIntoView()")
        await b.close()
asyncio.run(main())
