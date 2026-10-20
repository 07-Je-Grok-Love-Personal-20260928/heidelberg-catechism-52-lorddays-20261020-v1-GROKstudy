import asyncio,sys,json
from playwright.async_api import async_playwright
BASE=sys.argv[1]; OUT=sys.argv[2]
PAGES=['index.html','ld/01.html','texts/hc.html','memory.html','history.html']
INIT='''window.__lt=[];try{new PerformanceObserver(l=>{for(const e of l.getEntries())window.__lt.push(e.duration)}).observe({type:'longtask',buffered:true})}catch(e){}'''
SCROLL='''async()=>{const H=document.documentElement.scrollHeight-innerHeight;const T=6000;const fr=[];let t0=null;
return await new Promise(res=>{function step(ts){if(t0===null)t0=ts;fr.push(ts);const p=Math.min(1,(ts-t0)/T);scrollTo(0,H*p);if(p<1)requestAnimationFrame(step);else res(fr)}requestAnimationFrame(step)})}'''
async def main():
    res={}
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--enable-gpu-rasterization'])
        for w in (1440,375):
            for u in PAGES:
                ctx=await b.new_context(viewport={'width':w,'height':900 if w>500 else 812},device_scale_factor=1)
                pg=await ctx.new_page(); await pg.add_init_script(INIT)
                cdp=await ctx.new_cdp_session(pg); await cdp.send('Emulation.setCPUThrottlingRate',{'rate':4})
                await pg.goto(BASE+u,wait_until='load',timeout=90000); await pg.wait_for_timeout(1500)
                ltload=await pg.evaluate('window.__lt.reduce((a,b)=>a+b,0)')
                n0=len(await pg.evaluate('window.__lt'))
                fr=await pg.evaluate(SCROLL)
                lt=await pg.evaluate('window.__lt'); scr=lt[n0:]
                gaps=[fr[i+1]-fr[i] for i in range(len(fr)-1)]
                fps=1000*len(gaps)/sum(gaps) if gaps else 0
                jank=sum(1 for g in gaps if g>50)
                dom=await pg.evaluate('document.getElementsByTagName("*").length')
                res[f'{w}/{u}']=dict(fps=round(fps,1),jank50=jank,maxframe=round(max(gaps),1),lt_load=round(ltload),lt_scroll=round(sum(scr)),dom=dom)
                print(w,u,res[f'{w}/{u}'],flush=True)
                await ctx.close()
        await b.close()
    json.dump(res,open(OUT,'w'),indent=1)
asyncio.run(main())
