import json
from common import VERSION,DATE,REPO
V=json.load(open('versions.json'))
import os
J=lambda f:json.load(open(f)) if os.path.exists(f) else {}
a=J('perf6_v8_base.json');b=J('perf6_v9.json');CF=J('cpuf_v9.json')
PG=['index.html','ld/01.html','ld/34.html','texts/hc-2.html','history.html','memory.html','maps.html','geo-bible.html','marks.html','compare.html','bible.html','lorddays.html']
MAP=[(u,u,'') for u in PG]
rows=[]
pk=lambda r,k:round(1000*r[k]/max(r['scrolled'],1))
for prof in ['mobile','desktop2x']:
    for u6,u7,note in MAP:
        x,y=a.get(f'{prof}/{u6}'),b.get(f'{prof}/{u7}')
        if not x or not y: continue
        rows.append(f"| {prof} · {u7}{note} | {x['fps']} → **{y['fps']}** | {x['p95']} → **{y['p95']}** | {x['long50']} → {y['long50']} | {pk(x,'task_ms')} → **{pk(y,'task_ms')}** | {pk(x,'paint_ms')} → **{pk(y,'paint_ms')}** | {x['dom']} → {y['dom']} |")
crow=[]
for prof in ['mobile','desktop2x']:
    for u in PG:
        k=f'{prof}/{u}'
        if k in CF: x=CF[k]; crow.append(f"| {prof} · {u} | {x['v8']} → **{x['v9']}** | {x['v8cpu']} → **{x['v9cpu']}** | {x['v8long']} → {x['v9long']} |")
cpuft='| 设备 · 页面 | 估算 FPS（6×） | 主线程 CPU ms（×6） | 长任务 >50ms |\n|---|---|---|---|\n'+'\n'.join(crow)
perf='| 设备 · 页面 | 滚动 FPS | p95 帧 ms | 长任务(>50ms) | 主线程任务 ms / 1000px | 绘制 ms / 1000px | DOM |\n|---|---|---|---|---|---|---|\n'+'\n'.join(rows)
def lht(f6,f7):
    A,B=J(f6),J(f7); out=[]
    for u6,u7,note in MAP:
        if u6 in A and u7 in B and u7!='maps.html':
            x,y=A[u6],B[u7]; out.append(f"| {u7}{note} | {x['score']} → **{y['score']}** | {x['tbt']} → **{y['tbt']}** | {x['cls']} → **{y['cls']}** | {x['lcp']} → {y['lcp']} | {x['fcp']} → {y['fcp']} |")
    return '| 页面 | 分数 | TBT ms | CLS | LCP ms | FCP ms |\n|---|---|---|---|---|---|\n'+'\n'.join(out)
def newp():
    B=J('lh_v8.json');return '| 页面 | 分数 | TBT ms | CLS | LCP ms | FCP ms |\n|---|---|---|---|---|---|\n'+'\n'.join(f"| {u} | {B[u]['score']} | {B[u]['tbt']} | {B[u]['cls']} | {B[u]['lcp']} | {B[u]['fcp']} |" for u in ['maps.html','geo-bible.html','marks.html'] if u in B)
W5,W6=J('wc_v6.json').get('summary',{}),J('wc_v7.json').get('summary',{})  # unchanged in v8 (word count is v6→v7)
wct='| 范围 | v6 | v7 | 变化 |\n|---|---|---|---|\n'+f"| 52 主日解说合计 | {W5['ld_total']:,} | {W6['ld_total']:,} | {100*(W6['ld_total']-W5['ld_total'])/W5['ld_total']:+.1f}% |\n| 平均每主日 | {W5['ld_avg']:,} | {W6['ld_avg']:,} | |\n"+''.join(f"| {k} | {W5['overview'][k]:,} | {W6['overview'][k]:,} | {100*(W6['overview'][k]-W5['overview'][k])/W5['overview'][k]:+.1f}% |\n" for k in W5['overview'])+f"| 概览页合计 | {W5['overview_total']:,} | {W6['overview_total']:,} | {100*(W6['overview_total']-W5['overview_total'])/W5['overview_total']:+.1f}% |"
toc=json.load(open('toc_test_result.json'))
tt='\n'.join(f"- {'✅' if r[1] else '❌'} {r[0]} {('（'+r[2]+'）') if r[2] and len(r[2])<60 else ''}" for r in toc)
V9T=open('v9_test_result.txt').read().strip() if os.path.exists('v9_test_result.txt') else ''
V8T=open('v8_test_result.txt').read().strip() if os.path.exists('v8_test_result.txt') else ''
REL='https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/'
L=lambda key:'\n'.join(f'| {t} | {u} |' for t,u in V[key])
md=f'''# heidelberg-catechism-52-lorddays-20261024-v9-GROKstudy

> 《海德堡要理问答》52 主日全景深度解析：简体中文深度学习网站，共 129 问，持守欧陆改革宗立场（三项联合信条 + 三大普世信经）。

## 🌐 当前在线访问（v9）

| 平台 | 链接 |
|---|---|
| GitHub Pages | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261024-v9-grokstudy.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261024-v9-grokstudy.netlify.app |

📦 源码仓库：https://github.com/07-Je-Grok-Love-Personal-20260928/{REPO}
🏷️ Release：[v9]({REL}v9) · [v8]({REL}v8) · [v7]({REL}v7) · [v6]({REL}v6) · [v5]({REL}v5) · [v4]({REL}v4) · [v3]({REL}v3) · [v2]({REL}v2) · [v1]({REL}v1)
📝 更新记录页：`changelog.html`（站内顶栏版本徽章）

## 🆕 更新说明（v9 · {DATE}）

''' + '\n'.join(f'- {x}' for x in V['changes_v9']) + f'''

<details><summary>v8 更新说明</summary>

''' + '\n'.join(f'- {x}' for x in V['changes_v8']) + f'''

</details>

### 🗺️ 地图来源与回退链（v8）

| 层 | 来源 | 何时使用 |
|---|---|---|
| ① 在线街道图 | Esri World_Street_Map → CARTO Voyager → OpenStreetMap | 并行探测（6 秒超时），用优先级最高的可达源；运行中 8 次瓦片错误且成功不足 2 次 → 自动换下一源；结果缓存在 sessionStorage |
| ② 站内主题底图 | `assets/geo/base.json`（Natural Earth 陆地 / 国界 / 河流 / 湖泊，约 250 KB） | 永远在最底层；所有在线源都不可达时单独使用（离线可用，颜色随主题） |
| ③ 静态示意图 | 构建时生成的 SVG（与左侧概念图同一幅） | 地图引擎加载失败或浏览器无 WebGL 时显示，并有状态提示 |
| 卫星图 | Esri World_Imagery | 点“🛰️ 卫星”按钮 |

地图引擎：MapLibre GL JS 4.7.1，自托管于 `site/assets/vendor/`（不依赖任何 CDN）。测试开关：`?maptest=nolib`（模拟引擎失败）、`?maptest=nogl`（模拟无 WebGL）、`?maptest=local`（只用站内底图）；控制台 `hcMaps.status()` 查看每张地图的状态。
注意：Esri / CARTO / OSM 在中国大陆的可达性无法保证；不可达时会自动显示站内底图，地图仍可拖动缩放，只是没有街道细节。区域范围为示意；圣经地点为传统位置。

<details><summary>v7 更新说明</summary>

''' + '\n'.join(f'- {x}' for x in V['changes_v7']) + f'''

</details>

### ⚡ 流畅度对比（v8 → v9）

测量方法：`build/perf6.py`，Playwright 无头 Chromium，CDP **6 倍 CPU 降速**；`mobile` = 375×812、DPR 3、触屏，`desktop2x` = 1440×900、DPR 2；加载 2.5 秒后，用 90 次滚轮（每次 160px，间隔 33ms）连续滚动，rAF 记录帧间隔。v8（`v8` 标签的 `site/`）与 v9 在同一台机器上测量（`perf6_v8_base.json` / `perf6_v9.json`）。“每 1000px”按滚动距离归一化。

{perf}

⚠️ 这台构建机与其他任务共用 8 核 CPU（负载常在 8–16），rAF 帧率受“别人占用 CPU”的影响很大，同一页面重复测量可相差 ±5 fps。因此另附一个**不受抢占影响的估算**（`build/cpuf.py` → `cpuf_v9.json`）：同样的滚动脚本，不降速运行，用 trace 中主线程的**线程 CPU 时间**（tdur，不含被其他进程占用的时间）× 6 模拟 6× 降速，每个超过 16.7ms 的任务按丢掉的 vsync 计。v8 与 v9 交替测量。

{cpuft}

### 🔦 Lighthouse（移动端预设，performance；以下为 v8 发布时的测量，v9 未改动加载路径）

本地（`build/lh.py`，模拟 4× CPU + 慢速 4G，同一本地服务器，每页 3 次取中位数；`lh_v7b.json` / `lh_v8.json`）：

{lht('lh_v7b.json','lh_v8.json')}

v8 新页（本地，同上方法；`lh_v8.json`）：

{newp()}

线上 Netlify（v7 站 vs v8 站，同一会话连续测量；`lh_v7_netlify8.json` / `lh_v8_netlify.json`）：

{lht('lh_v7_netlify8.json','lh_v8_netlify.json')}

### 📝 字数（v6 → v7，`build/wordcount.py`，只计解说文字：汉字 + 英文词；原文问答 / 信条 / 金句不计）

{wct}

### 🧪 v9 主题 / 标记 / 滚动测试（`build/v9_test.py`，Playwright）

{V9T}

### 🧪 v8 地图与导航测试（`build/v8_test.py`，Playwright）

{V8T}

### 🧪 互动与架构测试（`build/toc_test.py`，Playwright）

{tt}

## 🏗️ 架构（v7 起）

| 机制 | 实现 |
|---|---|
| 长页拆分 | `texts/hc-1…5.html`（主日 1–10 / 11–22 / 23–31 / 32–44 / 45–52），`texts/hc.html` 为目录页并把旧锚点 `#q60` `#ld23` 重定向到分卷；`texts/hc-all.html` 全一页 |
| 跨页过渡 | CSS `@view-transition{{navigation:auto}}`；顶栏 / 侧栏使用 `view-transition-name` 不参与淡入 |
| 预取 | `<script type="speculationrules">`：悬停 moderate 预取 + 按下 conservative 预渲染；不支持时 pointerover / touchstart 兜底 |
| 离线与秒开 | `site/sw.js`（构建哈希作为缓存名）：核心页预缓存 · 同源 stale-while-revalidate · CDN cache-first · 离线回退首页 · `?nosw` 关闭 |
| 首屏 | 每页内联压缩 CSS（约 44 KB）；目录构建时生成；主题 / 标记状态在首屏绘制前由 head 脚本应用 |
| 滚动（v9） | 滚轮 / 触摸 / scroll 被动监听只记时间；380 ms 真正静止才算“滚动结束”；滚动中透明护罩挡住悬停重算、暂停 SMIL 与背景漂移、路线动画直接定格；图表展开与描线一律等到静止后；空闲时逐段预排版 content-visibility 区块 |
| 初始化 | 标签、测验、卡片、播放器、键盘、SW 注册等放进 `requestIdleCallback` |

## 🖍️ 标记图例（v9：标记 3.0）

| 层级 | 样式 | 含义 | “仅核心”模式 |
|---|---|---|---|
| ① 核心层 | 荧光底 + 粗体 | 核心词句（答案主干，背诵首选） | 保留 |
| ② 重点层 | 金色粗体 | 重点概念 / 论题关键词 | 隐藏 |
| ② 重点层 | 绿色粗体 | 恩典 · 应许 · 安慰 | 隐藏 |
| ② 重点层 | 红色粗体 | 警示 · 审判 · 严重后果 | 隐藏 |
| ③ 语义线 | 蓝色实线 | 定义 / 术语 | 隐藏 |
| ③ 语义线 | 橙色波浪线 | 难点 | 隐藏 |
| ③ 语义线 | 红色虚线 | 对比 / 错误立场 | 隐藏 |
| ③ 块 | 要点底纹 | 一句话要点 | 隐藏 |
| ④ 史地层（v8） | 紫色粗体 | 人物 | 隐藏 |
| ④ 史地层（v8） | 青色点线 | 地点 | 隐藏 |
| ④ 史地层（v8） | 琥珀色胶囊 | 年代 | 隐藏 |
| ① 核心层（v9） | 着重号（字下圆点） | 要义里最该背的关键词 | 保留 |
| 附 | 经文药丸 | 圣经出处 | 保留 |
| 提示框 | 💎核心 · ⚠️难点 · 🚫易错 · ✨金句（逐字原文） · 🪝记忆钩 · 📖核心经文 · 🏛️历史 · 🗺️地理（v8） | 每个主日与总览页 | 保留 |

三态：🖍️ 全部 → ⭐ 仅核心 → 🧽 关（顶栏 🖍️ 或 M 键循环；图例中的分段按钮可直接选择；保存在 localStorage `hc-marks`）。v8：`marks.html` 是完整说明页；图例每一行可点击“聚焦”只突出这一种标记（Esc 取消）；桌面端悬停标记显示含义。主日页原文区的“本主日笔记标记”图例显示每种标记在本页出现的次数（构建时统计）。标记只包在样式层的 `<span>` 中，原文文字不改。

## 🎨 配色主题（v9：十套）

🌌 深夜星空 · 🌅 晨曦米白 · 🌲 翡翠森林 · 🍇 葡萄紫金 · 🌊 海洋蓝 · 🌸 樱花粉霞（v9）· 🍋 柠檬薄荷（v9）· 🔥 暮光琥珀（v9，深色）· 🌠 极光青紫（v9，深色）· 🖋️ 水墨朱砂（v9）—— 顶栏 🎨 打开色板预览，一键切换，自动保存（`hc-theme`），首屏绘制前应用（无闪烁）。`build/contrast.py` → `build/contrast_v9.json`（十套主题）：正文、弱化文字、强调色、标记色、色块标签全部 ≥ 4.5:1，焦点环 ≥ 3:1，**0 项不达 WCAG AA**。

## 📚 网站结构

| 页面 | 内容 |
|---|---|
| `index.html` | 首页：图例（三态标记）、全书精华、三部分比例图、52 主日问答数柱状图、圣经四幕剧、罪-恩-谢、思维导图、三大支柱、52 主日网格、学习路径 |
| `bible.html` | 圣经神学、52 主日 × 圣经大戏矩阵、圣约神学、八个视角、本质核心、🧬 圣约链统计（v7） |
| `history.html` | 三线故事线、五时期甘特图、36 事件时间线、概念示意图 + 实时地图（21 地点、4 条路线、放大插图）、人物、区域文化 |
| `maps.html`（v8） | 历史地图集：1563 普法尔茨 · 宗教改革的传播 · 两位作者 · 难民之路 · 多特代表，每个专题成对地图 + 站点 + 地点表 + 文化 + 相关主日 |
| `geo-bible.html`（v8） | 圣经地理：亚伯拉罕之路 · 出埃及 · 保罗的旅程 |
| `marks.html`（v8） | 笔记标记系统：图例与聚焦、示范、提示框、全站标记统计、三遍阅读法 |
| `lorddays.html` | 52 主日按 17 个主题分组、筛选、进度、交叉引用热力图、❓ 52 个问题 · 圣约链一览（v7）、结构与信条对照总表 |
| `ld/01.html … ld/52.html` | ❓ 本主日回答的问题 + 💎 核心 → 精华（💡 为什么重要 · 🏃 本周操练 · 要义 · 数据卡 · 金句 · 易错 · 星图 · 承上启下）→ 原文（🎧 连续朗读 · 标记图例）→ 整体（🧬 圣约链 · 🔭 六级缩放 · 四视角卡）→ 局部（背景 · 难点 · 🔬 深化）→ 交叉对照 → 应用 → 记忆 → 延伸 |
| `texts/index.html` | 原文中心 |
| `texts/hc.html` | 要理问答目录页（5 卷卡片 + 52 主日跳转格；旧锚点自动跳转） |
| `texts/hc-1.html … hc-5.html` · `texts/hc-all.html` | 要理问答分卷阅读 / 背诵版 · 全一页版（打印、Ctrl+F） |
| `texts/bc.html` `cd.html` `creeds.html` | 比利时信条 · 多特信经 · 三大信经 |
| `compare.html` | 三项联合信条对比、覆盖度、维恩图、抗辩派对照、教义矩阵、三大信经对比 |
| `memory.html` | 三层标记图例、数字骨架、52 口诀、129 卡片、52 测验、进度 |
| `search.html` · `sources.html` · `changelog.html` | 搜索 · 资料与校验方法 · 版本记录 |

快捷键：T 目录 · R 背诵模式 · M 标记三态 · ←/→ 或 , . 切换主日 · [ ] 后退前进 · H 主页 · G / Shift+G 顶部底部 · N 导航簇 · ? 快捷键说明。

## ✅ 原文来源与校验

- 全部信条与信经中文原文由程序抓取自 https://ccifellowship.org/books/book-of-praise （《中国改革宗敬拜手册》2015），未做任何文字改动。
- `build/verify_verbatim.py`：站内 2,712 个原文块逐字比对 **0 处差异**；53 条“金句”均为原文的逐字子串（0 处差异）。
- `build/check_cuv.py`（v7，v8 扩展到地图集与圣经地理）：学习笔记中带出处的经文引语 138 处，与信望爱 FHL 线上和合本（https://bible.fhl.net/ ，version=unv）逐条比对，**0 处不符**（修正 30 余处措辞 / 出处）。学习笔记中加引号的要理问答语句已与原文逐字对照。
- `build/layout_check.py`（v8）：全部 73 个页面（含 52 主日、5 个分卷与 v8 新增的 maps / geo-bible / marks）× 375 / 768 / 1024 / 1440 四种宽度 × 十套主题（v9），横向溢出与顶栏截断 **0 个问题**。
- ccifellowship.org 未收录多特信经的“结论”部分，本站也未收录。威斯敏斯特小要理问答英文引文取自 opc.org。原文版权归原出版委员会，本站仅作学习引用。解读为学习笔记，未经神学家审阅；图标、分组与“圣约链”均为学习标签。

## 🛠️ 构建与部署

```bash
bash build/build_all.sh                 # 生成 site/（最后一步 finalize.py：内联 CSS、生成 sw.js、标记计数）
python3 build/verify_verbatim.py        # 原文逐字校验
python3 build/check_cuv.py              # 经文引语 × 和合本
python3 build/contrast.py               # WCAG 对比度
python3 build/layout_check.py URL 375   # 布局检测（需本地服务器）
python3 build/toc_test.py               # Playwright 互动 / 架构测试
python3 build/perf6.py URL out.json     # 流畅度测量（6× CPU）
python3 build/lh.py URL out.json 3      # Lighthouse
git subtree push --prefix site origin gh-pages
python3 build/v8_test.py URL OUTDIR     # v8 地图回退 + 导航簇测试
python3 build/v9_test.py URL OUTDIR     # v9 主题 / 标记 / 滚动测试
python3 build/cpuf.py "URL_A|URL_B" desktop2x pages 1   # 不受抢占影响的帧率估算
surge site heidelberg-catechism-52-lorddays-20261024-v9-grokstudy.surge.sh
netlify deploy --prod --dir site --site {open('netlify_v9_id.txt').read().strip() if __import__('os').path.exists('netlify_v9_id.txt') else '<v9-site-id>'}
```

## 🗂️ 版本历史

### v9 · {DATE} · [Release]({REL}v9)
| 平台 | 链接 |
|---|---|
{L('V9')}

### v8 · 2026-10-23 · [Release]({REL}v8)
| 平台 | 链接 |
|---|---|
{L('V8')}

### v7 · 2026-10-23 · [Release]({REL}v7)
| 平台 | 链接 |
|---|---|
{L('V7')}

### v6 · 2026-10-21 · [Release]({REL}v6)
| 平台 | 链接 |
|---|---|
{L('V6')}

### v5 · 2026-10-21 · [Release]({REL}v5)
| 平台 | 链接 |
|---|---|
{L('V5')}

### v4 · 2026-10-21 · [Release]({REL}v4)
| 平台 | 链接 |
|---|---|
{L('V4')}

### v3 · 2026-10-20 · [Release]({REL}v3)
| 平台 | 链接 |
|---|---|
{L('V3')}

### v2 · 2026-10-20 · [Release]({REL}v2)
| 平台 | 链接 |
|---|---|
{L('V2')}

### v1 · 2026-10-20 · [Release]({REL}v1)
| 平台 | 链接 |
|---|---|
{L('V1')}
'''
open('../README.md','w').write(md); print('README ok')
