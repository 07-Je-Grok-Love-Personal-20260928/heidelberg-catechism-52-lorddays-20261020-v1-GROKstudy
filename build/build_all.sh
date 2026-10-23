set -e
cd "$(dirname "$0")"
python3 build_ld.py
python3 build_texts.py
python3 build_pages.py
python3 build_history.py
python3 build_pages2.py
python3 build_v2.py
python3 prerender_mermaid.py
# v6: minify CSS/JS from build/src → site/assets (sources stay readable in build/src)
/workspace/tools/node_modules/.bin/esbuild src/style.css --minify --target=chrome100,safari15,firefox100 --outfile=../site/assets/css/style.css --log-level=warning
/workspace/tools/node_modules/.bin/esbuild src/app.js --minify --target=es2020 --outfile=../site/assets/js/app.js --log-level=warning
ls -l ../site/assets/css/style.css ../site/assets/js/app.js | awk '{print $5, $9}'
python3 finalize.py
