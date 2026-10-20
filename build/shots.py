import asyncio,sys
from playwright.async_api import async_playwright
B=sys.argv[1] if len(sys.argv)>1 else 'http://localhost:8765/'
S=[('index.html',1440,'v2-desktop-index.png',None),('ld/01.html',1440,'v2-desktop-ld01.png',None),('ld/01.html',1440,'v2-desktop-ld01-deep.png','#deep'),('history.html',1440,'v2-desktop-history-map.png','#map'),('bible.html',1440,'v2-desktop-bible-covenant.png','#covenant'),('compare.html',768,'v2-tablet-compare.png',None),('search.html?q=安慰',1440,'v2-desktop-search.png',None),
('index.html',375,'v2-mobile-index.png',None),('ld/28.html',375,'v2-mobile-ld28.png',None),('ld/28.html',375,'v2-mobile-ld28-deep.png','#deep'),('bible.html',375,'v2-mobile-bible-covenant.png','#covenant'),('texts/creeds.html',375,'v2-mobile-creeds.png',None),('changelog.html',375,'v2-mobile-changelog.png',None)]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for u,w,fn,anc in S:
            ctx=await b.new_context(viewport={'width':w,'height':900 if w>500 else 812},device_scale_factor=2 if w<500 else 1)
            pg=await ctx.new_page(); await pg.goto(B+u,wait_until='networkidle',timeout=60000)
            await pg.evaluate("document.querySelectorAll('.reveal').forEach(e=>e.classList.add('in'))")
            if anc:
                await pg.evaluate(f"document.querySelector('{anc}').scrollIntoView()"); await pg.wait_for_timeout(3500)
                await pg.evaluate(f"document.querySelector('{anc}').scrollIntoView()")
            await pg.wait_for_timeout(1500)
            await pg.screenshot(path='/workspace/hc52-20261020/shots/'+fn)
            if 'search' in u: print('search results:',await pg.inner_text('#cnt'))
            if 'bible' in u: print(w,'mermaid svgs',await pg.evaluate("document.querySelectorAll('.mermaid svg').length"),'err',await pg.evaluate("document.body.innerText.includes('Syntax error')"))
            if 'history' in u: print('leaflet tiles',await pg.evaluate("document.querySelectorAll('.leaflet-tile').length"))
            await ctx.close()
        await b.close()
asyncio.run(main())
