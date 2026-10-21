import asyncio,sys
from playwright.async_api import async_playwright
B=sys.argv[1] if len(sys.argv)>1 else 'http://localhost:8765/'
S=[('texts/hc.html',1440,'v4-desktop-texts-hc-toc.png','sub34','expand'),('texts/bc.html',1440,'v4-desktop-texts-bc-toc.png','g18',''),('texts/cd.html',1440,'v4-desktop-texts-cd-toc.png','section3-4',''),
('ld/16.html',1440,'v4-desktop-ld16-nav-drawer-list.png',None,''),('ld/16.html',1440,'v4-desktop-ld16-essence.png','essence',''),('ld/16.html',1440,'v4-desktop-ld16-sort-cloze.png','m-sort','cloze'),
('memory.html',1440,'v4-desktop-memory-game.png','progress',''),('compare.html',1440,'v4-desktop-compare-donut.png','bcgroups',''),('lorddays.html',1440,'v4-desktop-lorddays-hover.png','grid','hover'),
('index.html',1440,'v4-desktop-index.png',None,''),('texts/hc.html',375,'v4-mobile-texts-hc-toc-drawer.png','ld11','drawer'),('ld/28.html',375,'v4-mobile-ld28-nav-drawer.png',None,'drawernav'),
('ld/28.html',375,'v4-mobile-ld28-essence.png','essence',''),('changelog.html',375,'v4-mobile-changelog.png',None,'')]
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
            if mode in('drawer','drawernav'): await pg.click('#tocBtn'); await pg.wait_for_timeout(400)
            if mode=='drawernav': await pg.evaluate("(()=>{const sc=document.querySelector('.side .scroll');const a=document.querySelector('.ldnav a.on');sc.scrollTop+=a.getBoundingClientRect().top-sc.getBoundingClientRect().top-200})()")
            if mode=='drawer': await pg.evaluate("(()=>{const sc=document.querySelector('.side .scroll');const a=document.querySelector('#toc a.on');if(a)sc.scrollTop+=a.getBoundingClientRect().top-sc.getBoundingClientRect().top-160})()")
            if mode=='expand': await pg.click('#tocExpand'); await pg.evaluate("(()=>{const sc=document.querySelector('.side .scroll');document.querySelectorAll('#toc li.l3,#toc li.l2').forEach(li=>{if(li.querySelector(':scope>ul')&&li.textContent.includes('主日'))li.classList.add('closed')});const a=document.querySelector('#toc a[href=\"#p5\"]')||document.querySelector('#toc a.on');if(a)sc.scrollTop+=a.getBoundingClientRect().top-sc.getBoundingClientRect().top-60})()")
            if mode=='hover': await pg.hover('.ld[data-ld-card="12"]')
            if mode=='cloze': await pg.click('[data-clozestart]')
            await pg.wait_for_timeout(1500)
            await pg.screenshot(path='/workspace/hc52-20261020/shots/'+fn)
            if 'search' in u: print('search results:',await pg.inner_text('#cnt'))
            if 'bible' in u: print(w,'mermaid svgs',await pg.evaluate("document.querySelectorAll('.mermaid svg').length"),'err',await pg.evaluate("document.body.innerText.includes('Syntax error')"))
            if 'history' in u: print('leaflet tiles',await pg.evaluate("document.querySelectorAll('.leaflet-tile').length"))
            await ctx.close()
        await b.close()
asyncio.run(main())
