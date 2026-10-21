# Real-world-ish runtime benchmark: 6x CPU, mobile DPR3 touch + desktop DPR2, wheel scrolling through the compositor,
# rAF frame gaps + CDP main-thread metrics + trace (Paint / Raster / Layerize / Composite) cost during scroll.
import asyncio,sys,json
from playwright.async_api import async_playwright
BASE=sys.argv[1]; OUT=sys.argv[2]
PAGES=sys.argv[3].split(',') if len(sys.argv)>3 else ['index.html','ld/01.html','texts/hc.html','history.html','memory.html']
PROF0=[('mobile',dict(viewport={'width':375,'height':812},device_scale_factor=3,is_mobile=True,has_touch=True),6),
      ('desktop2x',dict(viewport={'width':1440,'height':900},device_scale_factor=2),6)]
PROF=[x for x in PROF0 if x[0] in __import__('os').environ.get('PROFS','mobile,desktop2x').split(',')]
FR='''window.__fr=[];(function f(t){window.__fr.push(t);if(window.__fr.length<100000)requestAnimationFrame(f)})(performance.now());'''
PAINT={'Paint','RasterTask','PaintImage','Layerize','UpdateLayerTree','CompositeLayers','Decode Image','PrePaint','Layout','UpdateLayoutTree'}
async def main():
    res={}
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--enable-gpu-rasterization','--ignore-gpu-blocklist'])
        for name,opt,rate in PROF:
            for u in PAGES:
                ctx=await b.new_context(**opt); pg=await ctx.new_page()
                if __import__('os').environ.get('INIT'): await pg.add_init_script(__import__('os').environ['INIT'])
                cdp=await ctx.new_cdp_session(pg); await cdp.send('Emulation.setCPUThrottlingRate',{'rate':rate}); await cdp.send('Performance.enable')
                await pg.goto(BASE+u+__import__('os').environ.get('Q',''),wait_until='load',timeout=120000); await pg.wait_for_timeout(2500)
                m0={x['name']:x['value'] for x in (await cdp.send('Performance.getMetrics'))['metrics']}
                await b.start_tracing(page=pg,categories=['devtools.timeline','disabled-by-default-devtools.timeline'])
                await pg.evaluate(FR)
                await pg.mouse.move(int(__import__('os').environ.get('MX',opt['viewport']['width']//2)),opt['viewport']['height']//2)
                for i in range(90):
                    await pg.mouse.wheel(0,160); await pg.wait_for_timeout(33)
                await pg.wait_for_timeout(500)
                fr=await pg.evaluate('window.__fr.slice(1)')
                tr=json.loads(await b.stop_tracing())
                m1={x['name']:x['value'] for x in (await cdp.send('Performance.getMetrics'))['metrics']}
                gaps=[fr[i+1]-fr[i] for i in range(len(fr)-1)]
                gs=sorted(gaps); p95=gs[int(len(gs)*.95)] if gs else 0
                paint={}
                for e in tr.get('traceEvents',[]):
                    if e.get('ph')=='X' and e.get('name') in PAINT: paint[e['name']]=paint.get(e['name'],0)+e.get('dur',0)/1000
                dur=(fr[-1]-fr[0])/1000 if len(fr)>1 else 1
                r=dict(fps=round(len(gaps)/dur,1) if gaps else 0,p95=round(p95,1),long50=sum(1 for g in gaps if g>50),
                       task_ms=round((m1['TaskDuration']-m0['TaskDuration'])*1000),style_ms=round((m1['RecalcStyleDuration']-m0['RecalcStyleDuration'])*1000),
                       layout_ms=round((m1['LayoutDuration']-m0['LayoutDuration'])*1000),script_ms=round((m1['ScriptDuration']-m0['ScriptDuration'])*1000),
                       paint_ms=round(sum(paint.values())),layers=None,dom=await pg.evaluate('document.getElementsByTagName("*").length'),
                       scrolled=await pg.evaluate('scrollY'))
                res[f'{name}/{u}']=r; print(name,u,r,flush=True)
                await ctx.close()
        await b.close()
    json.dump(res,open(OUT,'w'),indent=1)
asyncio.run(main())
