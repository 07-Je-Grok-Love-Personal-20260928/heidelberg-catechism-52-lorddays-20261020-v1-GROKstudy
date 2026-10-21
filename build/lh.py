import subprocess,json,sys,os,glob
BASE=sys.argv[1].rstrip('/')+'/'; OUT=sys.argv[2]; RUNS=int(sys.argv[3]) if len(sys.argv)>3 else 1
CH=glob.glob(os.path.expanduser('~/.cache/ms-playwright/chromium-1248/chrome-linux*/chrome'))[0]
P=sys.argv[4].split(',') if len(sys.argv)>4 else ['index.html','ld/01.html','texts/hc.html','history.html','memory.html']
res={}
for p in P:
    rs=[]
    for i in range(RUNS):
        f=f'/tmp/lh_{os.getpid()}.json'
        subprocess.run(['/tmp/lh/node_modules/.bin/lighthouse',BASE+p,'--only-categories=performance','--output=json',f'--output-path={f}','--quiet',*(['--throttling-method=devtools'] if os.environ.get('LHDEV') else []),f'--chrome-path={CH}','--chrome-flags=--headless=new --no-sandbox'],env={**os.environ,'CHROME_PATH':CH},timeout=300)
        j=json.load(open(f));a=j['audits']
        rs.append(dict(score=round(j['categories']['performance']['score']*100),fcp=round(a['first-contentful-paint']['numericValue']),lcp=round(a['largest-contentful-paint']['numericValue']),tbt=round(a['total-blocking-time']['numericValue']),cls=round(a['cumulative-layout-shift']['numericValue'],3),si=round(a['speed-index']['numericValue'])))
    rs.sort(key=lambda r:r['score']); res[p]=rs[len(rs)//2]; print(p,res[p],flush=True)
json.dump(res,open(OUT,'w'),indent=1)
