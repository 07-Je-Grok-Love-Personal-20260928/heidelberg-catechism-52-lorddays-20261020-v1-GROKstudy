# contention-independent estimate: main-thread CPU time (tdur, excludes time the OS gave to other processes) ×6 → dropped vsyncs
import asyncio,sys,json
from playwright.async_api import async_playwright
BASES=sys.argv[1].split('|');PROFN=sys.argv[2];PAGES=sys.argv[3].split(',');REPS=int(sys.argv[4]) if len(sys.argv)>4 else 1
OPT={'mobile':dict(viewport={'width':375,'height':812},device_scale_factor=3,is_mobile=True,has_touch=True),'desktop2x':dict(viewport={'width':1440,'height':900},device_scale_factor=2)}[PROFN]
CSS={'base':'','noprog':'.progress{display:none!important;animation:none!important}','nosky':'.sky{display:none!important}','nofixed':'.sky,.progress,.topbar,.fab,#navc,.toast{display:none!important}','notrans':'*,*::before,*::after{transition:none!important;animation:none!important}','nocv':'main section.sec{content-visibility:visible!important}','nopre':'main section.sec.ncv{content-visibility:auto!important}','noanim':'*,*::before,*::after{animation:none!important}','notr':'*,*::before,*::after{transition:none!important}','nopretty':'*{text-wrap:wrap!important;text-autospace:normal!important;text-spacing-trim:normal!important}','split':'.msec>.mpair>figure,.msec>.card,.msec>.mpair{content-visibility:auto;contain-intrinsic-size:auto 480px}','noglass':'*{backdrop-filter:none!important;-webkit-backdrop-filter:none!important}','nosh':'#scrshield{display:none!important}','nosticky':'*{position:static!important}' }
async def run(b,url):
    v,url=url.split('@') if '@' in url else ('base',url)
    ctx=await b.new_context(**OPT);pg=await ctx.new_page()
    css='+'.join(CSS[x] for x in v.split('+'))
    if css: await pg.add_init_script("document.addEventListener('DOMContentLoaded',()=>{const s=document.createElement('style');s.textContent=%s;document.head.appendChild(s)})"%json.dumps(css))
    await pg.goto(url,wait_until='load',timeout=120000);await pg.wait_for_timeout(2500)
    await b.start_tracing(page=pg,categories=['devtools.timeline','disabled-by-default-devtools.timeline'])
    await pg.mouse.move(OPT['viewport']['width']//2,OPT['viewport']['height']//2)
    for i in range(90): await pg.mouse.wheel(0,160);await pg.wait_for_timeout(33)
    await pg.wait_for_timeout(500)
    tr=json.loads(await b.stop_tracing());await ctx.close()
    ev=tr['traceEvents'];tn={(e['pid'],e['tid']):e['args']['name'] for e in ev if e.get('name')=='thread_name'}
    # renderer main for this page = the CrRendererMain with most events
    from collections import Counter
    c=Counter((e.get('pid'),e.get('tid')) for e in ev if tn.get((e.get('pid'),e.get('tid')))=='CrRendererMain')
    key=c.most_common(1)[0][0]
    tops=[e for e in ev if (e.get('pid'),e.get('tid'))==key and e.get('ph')=='X' and e.get('name') in ('RunTask','ThreadControllerImpl::RunTask') and 'tdur' in e]
    # drop nested RunTask
    tops.sort(key=lambda e:e['ts']);flat=[];end=0
    for e in tops:
        if e['ts']>=end: flat.append(e);end=e['ts']+e['dur']
    if not flat: return None
    pc=[e for e in ev if (e.get('pid'),e.get('tid'))==key and e.get('name')=='Paint' and e.get('ph')=='X'];print('   paints',len(pc),'est',round(sum(e.get('tdur',0) for e in pc)/1000*6))
    if __import__('os').environ.get('DBG'):
        allx=[e for e in ev if (e.get('pid'),e.get('tid'))==key and e.get('ph')=='X']
        for t in sorted(flat,key=lambda e:-e['tdur'])[:8]:
            s_,en=t['ts'],t['ts']+t['dur'];loc={}
            for k in allx:
                if k is not t and s_<=k['ts']<en and k['name'] not in('RunTask','ThreadControllerImpl::RunTask'): loc[k['name']]=loc.get(k['name'],0)+k.get('tdur',k.get('dur',0))/1000
            ly=[k for k in allx if k['name']=='Layout' and s_<=k['ts']<en]
            for k in ly[:2]: print('     LAYOUT t=%.2fs'%((k['ts']-flat[0]['ts'])/1e6),json.dumps(k.get('args',{}))[:300])
            print('  task est',round(t['tdur']/1000*6),'ms',[(a,round(b*6)) for a,b in sorted(loc.items(),key=lambda x:-x[1])[:7]])
    span=(flat[-1]['ts']+flat[-1]['dur']-flat[0]['ts'])/1e6
    cpu=sum(e['tdur'] for e in flat)/1000
    # sequential simulation at 6x: tasks run back-to-back; each vsync the main thread is free produces a frame
    drop=0
    for e in flat:
        est=e['tdur']/1000*6
        if est>16.7: drop+=int(est//16.7)
    frames=span*60
    return dict(fps_est=round(60*max(0,frames-drop)/frames,1),cpu6_ms=round(cpu*6),long_est=sum(1 for e in flat if e['tdur']/1000*6>50),span=round(span,1))
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--enable-gpu-rasterization','--ignore-gpu-blocklist'])
        R={}
        for r in range(REPS):
            for u in PAGES:
                for B in BASES:
                    x=await run(b,B+u);R.setdefault((u,B),[]).append(x);print(r,u,B.split('@')[0],B[-6:],x,flush=True)
        await b.close()
    for (u,B),l in R.items(): print('SUM',u,B[-6:],'fps_est',[x['fps_est'] for x in l],'cpu6',[x['cpu6_ms'] for x in l])
asyncio.run(main())
