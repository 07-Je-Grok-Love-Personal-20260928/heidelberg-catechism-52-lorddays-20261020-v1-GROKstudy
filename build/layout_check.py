import asyncio,sys,json
from playwright.async_api import async_playwright
BASE=sys.argv[1] if len(sys.argv)>1 else 'http://localhost:8765/'
pages=['index.html','bible.html','history.html','lorddays.html','compare.html','memory.html','sources.html','texts/hc.html','texts/bc.html','texts/cd.html','texts/creeds.html']+[f'ld/{n:02d}.html' for n in (1,16,28,34,52)]
widths=[375,768,1440]
JS='''()=>{const W=document.documentElement.clientWidth;const res={sw:document.documentElement.scrollWidth,W,off:[]};
for(const el of document.querySelectorAll('main *')){if(el.closest('.tbl,.mm,.mermaid,.leaflet-container,.nav,.fc,svg'))continue;const r=el.getBoundingClientRect();if(r.width===0)continue;
if(r.right>W+1||r.left<-1){const cs=getComputedStyle(el);if(cs.position==='fixed')continue;res.off.push((el.className||el.tagName)+' '+Math.round(r.left)+'-'+Math.round(r.right));if(res.off.length>8)break}}
const ov=[];for(const el of document.querySelectorAll('.card,.qa,.art,.chip,.btn,.node,.ld')){if(el.scrollWidth>el.clientWidth+2&&getComputedStyle(el).overflowX!=='auto'){ov.push((el.className)+':'+el.scrollWidth+'>'+el.clientWidth);if(ov.length>6)break}}
res.ov=ov;return res}'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        issues=0
        for w in widths:
            ctx=await b.new_context(viewport={'width':w,'height':900},device_scale_factor=1)
            pg=await ctx.new_page()
            for u in pages:
                await pg.goto(BASE+u,wait_until='networkidle',timeout=60000)
                await pg.evaluate("document.querySelectorAll('.reveal').forEach(e=>e.classList.add('in'))")
                await pg.wait_for_timeout(300)
                r=await pg.evaluate(JS)
                if r['sw']>r['W'] or r['off'] or r['ov']:
                    issues+=1; print(w,u,json.dumps(r,ensure_ascii=False)[:600])
            await ctx.close()
        print('issues',issues)
        await b.close()
asyncio.run(main())
