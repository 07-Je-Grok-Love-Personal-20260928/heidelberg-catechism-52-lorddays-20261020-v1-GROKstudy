import asyncio
from playwright.async_api import async_playwright
B='http://localhost:8765/'
S=[('index.html',1440,'desktop-index.png',True),('ld/01.html',1440,'desktop-ld01.png',False),('history.html',1440,'desktop-history.png',False),('ld/28.html',375,'mobile-ld28.png',False),('index.html',375,'mobile-index.png',False),('compare.html',768,'tablet-compare.png',False),('texts/creeds.html',375,'mobile-creeds.png',False)]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for u,w,fn,full in S:
            ctx=await b.new_context(viewport={'width':w,'height':900 if w>500 else 812},device_scale_factor=2 if w<500 else 1)
            pg=await ctx.new_page(); await pg.goto(B+u,wait_until='networkidle',timeout=60000)
            await pg.evaluate("document.querySelectorAll('.reveal').forEach(e=>e.classList.add('in'))"); await pg.wait_for_timeout(2500)
            await pg.screenshot(path='/workspace/hc52-20261020/shots/'+fn,full_page=False)
            await ctx.close()
        await b.close()
asyncio.run(main())
