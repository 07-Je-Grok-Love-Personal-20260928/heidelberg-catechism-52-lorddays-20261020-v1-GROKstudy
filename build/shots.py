import asyncio,sys
from playwright.async_api import async_playwright
B=sys.argv[1] if len(sys.argv)>1 else 'http://localhost:8765/'
S=[('index.html',1440,'v3-desktop-index.png',None,''),('index.html',1440,'v3-desktop-index-charts.png','essence',''),
('ld/16.html',1440,'v3-desktop-ld16-essence.png','essence',''),('ld/16.html',1440,'v3-desktop-ld16-marks.png','q42',''),
('texts/hc.html',1440,'v3-desktop-texts-hc-toc-resized.png','q60','resize'),('compare.html',1440,'v3-desktop-compare-coverage.png','coverage',''),
('history.html',1440,'v3-desktop-history-story.png','story',''),('lorddays.html',1024,'v3-1024-lorddays-nav.png',None,''),
('ld/01.html',1440,'v3-desktop-ld01-light.png',None,'light'),('ld/16.html',1440,'v3-desktop-ld16-nomarks.png','q42','nomarks'),
('index.html',375,'v3-mobile-index.png',None,''),('ld/28.html',375,'v3-mobile-ld28-essence.png','essence',''),('ld/28.html',375,'v3-mobile-ld28-toc-drawer.png','text','drawer'),
('bible.html',375,'v3-mobile-bible-covenant.png','covenant',''),('changelog.html',375,'v3-mobile-changelog.png',None,'')]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for u,w,fn,anc,mode in S:
            ctx=await b.new_context(viewport={'width':w,'height':900 if w>500 else 812},device_scale_factor=2 if w<500 else 1)
            pg=await ctx.new_page()
            await pg.add_init_script("localStorage.setItem('hc-theme',JSON.stringify('%s'));localStorage.setItem('hc-marks',JSON.stringify(%s));localStorage.setItem('hc-side-w',JSON.stringify(%d))"%('light' if mode=='light' else 'dark','false' if mode=='nomarks' else 'true',420 if mode=='resize' else 300))
            await pg.goto(B+u,wait_until='networkidle',timeout=60000)
            await pg.evaluate("document.querySelectorAll('.reveal').forEach(e=>e.classList.add('in'))")
            if anc:
                await pg.evaluate(f"hcJump('{anc}')"); await pg.wait_for_timeout(2500)
                await pg.evaluate(f"hcJump('{anc}')"); await pg.wait_for_timeout(1200)
            if mode=='drawer': await pg.click('#tocBtn')
            if mode=='resize': await pg.click('#tocExpand'); await pg.evaluate("hcJump('q60')")
            await pg.wait_for_timeout(1500)
            await pg.screenshot(path='/workspace/hc52-20261020/shots/'+fn)
            if 'search' in u: print('search results:',await pg.inner_text('#cnt'))
            if 'bible' in u: print(w,'mermaid svgs',await pg.evaluate("document.querySelectorAll('.mermaid svg').length"),'err',await pg.evaluate("document.body.innerText.includes('Syntax error')"))
            if 'history' in u: print('leaflet tiles',await pg.evaluate("document.querySelectorAll('.leaflet-tile').length"))
            await ctx.close()
        await b.close()
asyncio.run(main())
