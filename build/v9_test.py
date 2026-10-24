"""v9 tests: 10-theme picker (swatches, click, persistence, no flash), marks 3.0 (着重号), kw matrix + term chart,
scroll state (shield during gesture, settles after quiet, click right after scrolling still works), deferred route animation."""
import asyncio,sys,json
from playwright.async_api import async_playwright
BASE=sys.argv[1] if len(sys.argv)>1 else 'http://localhost:8780/'
SHOT=sys.argv[2] if len(sys.argv)>2 else '/tmp/v9shots'
TH=['night','dawn','forest','grape','ocean','sakura','citrus','ember','aurora','sumi']
fails=[];LINES=[]
def ok(c,msg):
    print(('PASS ' if c else 'FAIL ')+msg,flush=True);LINES.append(('- ✅ ' if c else '- ❌ ')+msg)
    if not c: fails.append(msg)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        c=await b.new_context(viewport={'width':1440,'height':900});pg=await c.new_page();errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto(BASE+'index.html?nosw',wait_until='load')
        n=await pg.evaluate("document.querySelectorAll('#thpop [data-theme-set]').length");ok(n==10,f'picker has 10 themes ({n})')
        sw=await pg.evaluate("document.querySelectorAll('#thpop [data-theme-set] .sw').length");ok(sw==10,f'every theme has a swatch preview ({sw})')
        bgs=set()
        for t in TH:
            await pg.evaluate("document.getElementById('thp').classList.add('open')")
            await pg.click(f'#thpop [data-theme-set={t}]');await pg.wait_for_timeout(350)
            cur=await pg.evaluate("[document.documentElement.dataset.theme,getComputedStyle(document.documentElement).getPropertyValue('--bg').trim(),JSON.parse(localStorage.getItem('hc-theme'))]")
            bgs.add(cur[1]);ok(cur[0]==t and cur[2]==t,f'click sets + saves theme {t} (bg {cur[1]})')
        ok(len(bgs)==10,f'10 distinct backgrounds ({len(bgs)})')
        # persistence + no flash: theme attribute already set when first <body> parse happens
        await pg.evaluate("localStorage.setItem('hc-theme',JSON.stringify('aurora'))")
        await c.add_init_script("document.addEventListener('readystatechange',()=>{if(document.readyState==='interactive')window.__t0=document.documentElement.dataset.theme},{once:true});new MutationObserver((m,o)=>{if(document.body){window.__tb=document.documentElement.dataset.theme;o.disconnect()}}).observe(document,{childList:true,subtree:true})")
        await pg.goto(BASE+'ld/01.html?nosw',wait_until='load')
        tb=await pg.evaluate('window.__tb');ok(tb=='aurora',f'saved theme applied before <body> is parsed (no flash): {tb}')
        ne=await pg.evaluate("document.querySelectorAll('.mk-e').length");ok(ne>0,f'着重号 marks on ld/01 ({ne})')
        te=await pg.evaluate("getComputedStyle(document.querySelector('.mk-e')).textEmphasisStyle||getComputedStyle(document.querySelector('.mk-e')).webkitTextEmphasisStyle");ok(bool(te) and te!='none',f'mk-e has text-emphasis ({te})')
        kw=await pg.evaluate("document.querySelectorAll('#ess-kwm ~ * .kwm i, .kwm i').length");ok(kw>0,f'keyword × Q&A matrix cells ({kw})')
        await pg.evaluate("document.getElementById('ess-kwm').scrollIntoView({block:'start'})");await pg.wait_for_timeout(900)
        await pg.locator('#ess-kwm').locator('xpath=..').screenshot(path=f'{SHOT}/v9-kw-matrix-aurora.png')
        await pg.goto(BASE+'lorddays.html?nosw',wait_until='load')
        tb2=await pg.evaluate("document.getElementById('terms').parentElement.querySelectorAll('.tbar').length");ok(tb2>=20,f'term-distribution chart bars ({tb2})')
        # scroll state + click right after scroll
        await pg.goto(BASE+'maps.html?nosw',wait_until='load');await pg.wait_for_timeout(1500)
        await pg.mouse.move(700,450)
        for i in range(6): await pg.mouse.wheel(0,200);await pg.wait_for_timeout(40)
        mid=await pg.evaluate("[document.documentElement.classList.contains('scr'),getComputedStyle(document.getElementById('scrshield')).display,document.querySelectorAll('svg.cmap.go:not(.done)').length]")
        ok(mid[0] and mid[1]=='block',f'during scroll: html.scr + shield shown ({mid[:2]})')
        await pg.wait_for_timeout(900)
        aft=await pg.evaluate("[document.documentElement.classList.contains('scr'),getComputedStyle(document.getElementById('scrshield')).display]")
        ok((not aft[0]) and aft[1]=='none',f'after 900 ms quiet: scroll state cleared ({aft})')
        go=await pg.evaluate("document.querySelectorAll('svg.cmap.go').length");ok(go>0,f'route diagrams in view play after settle ({go})')
        # click immediately after a wheel → forwarded to the real target
        for i in range(3): await pg.mouse.wheel(0,120);await pg.wait_for_timeout(40)
        box=await pg.evaluate("(()=>{const e=document.getElementById('themeBtn');const r=e.getBoundingClientRect();return [r.x+r.width/2,r.y+r.height/2]})()")
        await pg.mouse.move(box[0]+3,box[1]);await pg.mouse.move(box[0],box[1])
        for i in range(2): await pg.mouse.wheel(0,80);await pg.wait_for_timeout(30)
        await pg.mouse.click(box[0],box[1]);await pg.wait_for_timeout(300)
        op=await pg.evaluate("document.getElementById('thp').classList.contains('open')");ok(op,'click right after scrolling still reaches the button (theme picker opens)')
        await pg.screenshot(path=f'{SHOT}/v9-picker-aurora.png')
        ok(not errs,f'no page errors {errs[:2]}')
        await b.close()
    print('RESULT',len(fails),'failures')
    open('v9_test_result.txt','w').write('\n'.join(LINES)+f'\n\n结果：{len(LINES)-len(fails)}/{len(LINES)} 通过')
asyncio.run(main())
