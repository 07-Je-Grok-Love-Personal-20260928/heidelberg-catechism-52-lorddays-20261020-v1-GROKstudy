import asyncio,sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for url,w,sel,out in [a.split('|') for a in sys.argv[1:]]:
            pg=await b.new_page(viewport={'width':int(w),'height':900})
            await pg.goto('http://localhost:8765/'+url+'?cv0'); await pg.wait_for_timeout(800)
            await pg.evaluate("document.querySelectorAll('.reveal').forEach(e=>e.classList.add('in'))")
            el=pg.locator(sel).first; await el.scroll_into_view_if_needed(); await pg.wait_for_timeout(1800)
            await el.screenshot(path=out); await pg.close()
        await b.close()
asyncio.run(main())
