import asyncio
from playwright.async_api import async_playwright
async def m():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1200,'height':900})
        for u in ['index.html','bible.html','history.html','compare.html']:
            await pg.goto('http://localhost:8765/'+u,wait_until='networkidle'); await pg.wait_for_timeout(3000)
            r=await pg.evaluate("[...document.querySelectorAll('.mermaid')].map(e=>(e.querySelector('svg')?'svg':'nosvg')+(e.textContent.includes('Syntax error')?':ERR':':ok'))")
            print(u,r)
        await b.close()
asyncio.run(m())
