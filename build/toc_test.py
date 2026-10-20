# Playwright test: TOC resize (mouse + touch), persistence, collapse/expand-all, scrollspy auto-expand, ellipsis+tooltip, marks toggle
import asyncio,sys,json
from playwright.async_api import async_playwright
BASE=sys.argv[1] if len(sys.argv)>1 else 'http://localhost:8765/'
R=[]
def ok(name,cond,info=''): R.append((name,bool(cond),info)); print(('PASS' if cond else 'FAIL'),name,info)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        ctx=await b.new_context(viewport={'width':1440,'height':900})
        pg=await ctx.new_page()
        await pg.goto(BASE+'ld/01.html',wait_until='networkidle')
        w0=await pg.evaluate("document.getElementById('side').getBoundingClientRect().width")
        box=await pg.locator('#resizer').bounding_box()
        x=box['x']+box['width']/2; y=box['y']+box['height']/2
        await pg.mouse.move(x,y); await pg.mouse.down(); await pg.mouse.move(x+120,y,steps=8); await pg.mouse.up()
        await pg.wait_for_timeout(200)
        w1=await pg.evaluate("document.getElementById('side').getBoundingClientRect().width")
        ok('drag widens sidebar',abs(w1-(w0+120))<=3,f'{w0:.0f}->{w1:.0f}')
        st=await pg.evaluate("localStorage.getItem('hc-side-w')")
        ok('width persisted to localStorage',st and abs(int(st)-w1)<=1,str(st))
        await pg.mouse.move(x+120,y); await pg.mouse.down(); await pg.mouse.move(x+2000,y,steps=6); await pg.mouse.up()
        wmax=await pg.evaluate("document.getElementById('side').getBoundingClientRect().width")
        ok('max clamp = min(640,70vw)',abs(wmax-640)<=1,f'{wmax:.0f}')
        b2=await pg.locator('#resizer').bounding_box()
        await pg.mouse.move(b2['x']+6,y); await pg.mouse.down(); await pg.mouse.move(-500,y,steps=6); await pg.mouse.up()
        wmin=await pg.evaluate("document.getElementById('side').getBoundingClientRect().width")
        ok('min clamp = 220',abs(wmin-220)<=1,f'{wmin:.0f}')
        await pg.goto(BASE+'texts/hc.html',wait_until='networkidle')
        wp=await pg.evaluate("document.getElementById('side').getBoundingClientRect().width")
        ok('width persists across pages',abs(wp-220)<=1,f'{wp:.0f}')
        # keyboard resize
        await pg.focus('#resizer'); await pg.keyboard.press('ArrowRight'); await pg.keyboard.press('ArrowRight')
        wk=await pg.evaluate("document.getElementById('side').getBoundingClientRect().width")
        ok('keyboard arrows resize',abs(wk-268)<=1,f'{wk:.0f}')
        await pg.dblclick('#resizer'); wd=await pg.evaluate("document.getElementById('side').getBoundingClientRect().width")
        ok('double-click resets to 300',abs(wd-300)<=1,f'{wd:.0f}')
        # hierarchy
        info=await pg.evaluate("""()=>{const t=document.getElementById('toc');return {l1:t.querySelectorAll('li.l1').length,l2:t.querySelectorAll('li.l2').length,l3:t.querySelectorAll('li.l3').length,
          firstNo:t.querySelector('li.l1 .no')?.textContent,l2No:t.querySelector('li.l2 .no')?.textContent,l3No:t.querySelector('li.l3 .no')?.textContent,closed:t.querySelectorAll('li.closed').length}}""")
        ok('3-level numbered TOC (texts/hc)',info['l1']>=4 and info['l2']>=52 and info['l3']>=129 and info['firstNo']=='一、',json.dumps(info,ensure_ascii=False))
        await pg.click('#tocExpand'); c1=await pg.evaluate("document.querySelectorAll('#toc li.closed').length")
        await pg.click('#tocCollapse'); c2=await pg.evaluate("[document.querySelectorAll('#toc li.closed').length,document.querySelectorAll('#toc li:has(>ul)').length]")
        ok('expand all',c1==0,str(c1)); ok('collapse all (current path stays open)',c2[0]>=c2[1]-3 and c2[0]>0,str(c2))
        tw=pg.locator('#toc li.l1:has(>ul) > .row .tw').first
        await tw.click(); o=await pg.evaluate("!document.querySelector('#toc li.l1:has(>ul)').classList.contains('closed')")
        ok('single twisty toggles',o)
        # scrollspy auto-expand
        await pg.click('#tocCollapse')
        await pg.click('#tocExpand'); await pg.locator('#toc a[href="#q60"]').scroll_into_view_if_needed(); await pg.click('#toc a[href="#q60"]'); await pg.click('#tocCollapse'); await pg.wait_for_timeout(1500)
        land=await pg.evaluate("document.getElementById('q60').getBoundingClientRect().top")
        ok('TOC jump lands on target despite content-visibility',abs(land-72)<=6,f'top={land:.0f}')
        await pg.mouse.wheel(0,40); await pg.wait_for_timeout(700)
        sp=await pg.evaluate("""()=>{const a=document.querySelector('#toc a.on');if(!a)return null;let li=a.closest('li'),open=true;for(let p=li.parentElement.closest('li');p;p=p.parentElement.closest('li'))if(p.classList.contains('closed'))open=false;return {href:a.getAttribute('href'),open}}""")
        ok('scrollspy highlights current Q and auto-expands parents',sp and sp['href']=='#q60' and sp['open'],json.dumps(sp))
        # ellipsis + tooltip
        await pg.click('#tocExpand')
        el=await pg.evaluate("""()=>{const a=[...document.querySelectorAll('#toc a')].find(a=>a.scrollWidth>a.clientWidth);if(!a)return null;const cs=getComputedStyle(a);return {ws:cs.whiteSpace,to:cs.textOverflow,title:!!a.title}}""")
        ok('long titles: nowrap + ellipsis + title',el and el['ws']=='nowrap' and el['to']=='ellipsis' and el['title'],json.dumps(el))
        # marks toggle
        await pg.click('#marksBtn'); nm=await pg.evaluate("[document.body.classList.contains('nomarks'),getComputedStyle(document.querySelector('.qa .a .mk-k')).backgroundImage]")
        ok('marks toggle hides marks',nm[0] and nm[1]=='none',str(nm))
        await pg.reload(); nm2=await pg.evaluate("document.body.classList.contains('nomarks')"); ok('marks preference persisted',nm2)
        await pg.click('#marksBtn')
        # collapse sidebar desktop
        await pg.click('#tocBtn'); await pg.wait_for_timeout(450)
        hid=await pg.evaluate("document.getElementById('side').getBoundingClientRect().right<=1"); ok('☰ hides sidebar on desktop',hid)
        await pg.click('#tocBtn'); await ctx.close()
        # touch: mobile drawer + touch drag
        ctx=await b.new_context(viewport={'width':390,'height':844},has_touch=True,is_mobile=True,device_scale_factor=2)
        pg=await ctx.new_page(); await pg.goto(BASE+'ld/16.html',wait_until='networkidle')
        await pg.tap('#tocBtn'); await pg.wait_for_timeout(450)
        op=await pg.evaluate("document.getElementById('side').getBoundingClientRect().left>=-1"); ok('mobile drawer opens',op)
        bb=await pg.locator('#resizer').bounding_box(); w0=await pg.evaluate("document.getElementById('side').getBoundingClientRect().width")
        cdp=await ctx.new_cdp_session(pg); x=bb['x']+bb['width']/2; y=bb['y']+200
        await cdp.send('Input.dispatchTouchEvent',{'type':'touchStart','touchPoints':[{'x':x,'y':y}]})
        for i in range(1,9): await cdp.send('Input.dispatchTouchEvent',{'type':'touchMove','touchPoints':[{'x':x+i*6,'y':y}]})
        await cdp.send('Input.dispatchTouchEvent',{'type':'touchEnd','touchPoints':[]}); await pg.wait_for_timeout(200)
        w1=await pg.evaluate("document.getElementById('side').getBoundingClientRect().width")
        ok('touch drag resizes (pointer events)',w1>w0+30 and w1<=390*.92+1,f'{w0:.0f}->{w1:.0f}')
        await pg.tap('.backdrop',position={'x':380,'y':400}); await pg.wait_for_timeout(450)
        cl=await pg.evaluate("!document.body.classList.contains('toc-open')"); ok('backdrop tap closes drawer',cl)
        await ctx.close(); await b.close()
    print('RESULT',sum(1 for r in R if r[1]),'/',len(R),'passed')
    json.dump(R,open('/workspace/hc52-20261020/build/toc_test_result.json','w'),ensure_ascii=False,indent=1)
asyncio.run(main())
