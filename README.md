# heidelberg-catechism-52-lorddays-20261023-v8-GROKstudy

> 《海德堡要理问答》52 主日全景深度解析：简体中文深度学习网站，共 129 问，持守欧陆改革宗立场（三项联合信条 + 三大普世信经）。

## 🌐 当前在线访问（v8）

| 平台 | 链接 |
|---|---|
| GitHub Pages | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261023-v8-grokstudy.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261023-v8-grokstudy.netlify.app |

📦 源码仓库：https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy
🏷️ Release：[v8](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v8) · [v7](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v7) · [v6](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v6) · [v5](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v5) · [v4](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v4) · [v3](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v3) · [v2](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v2) · [v1](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v1)
📝 更新记录页：`changelog.html`（站内顶栏版本徽章）

## 🆕 更新说明（v8 · 2026-10-23）

- 🗺️ 地图重做：去掉不稳定的 Leaflet / OSM CDN，改用站内自托管 MapLibre GL 4.7.1（assets/vendor，BSD-3）＋站内 Natural Earth 底图（assets/geo/base.json，公有领域）。在线瓦片按 Esri 街道图 → CARTO Voyager → OpenStreetMap 顺序并行探测、自动择优、出错自动切换；全部不可达时用站内主题底图（离线可用）；地图引擎或 WebGL 不可用时显示同一幅静态示意图，不会出现空白框。另有卫星图（Esri）与“主题底图”按钮。
- 🎨 每个地图都是“概念示意图 + 实时交互地图”成对出现：示意图（构建时由 Natural Earth 投影生成的 SVG）带渐变陆海、河流、路线描边动画、沿路线移动的光点、编号脉冲标记、指北针、比例尺、密集地区的放大镜插图，标签自动避让；实时地图与之联动（点击地点 / 路线 / ▶ 播放 / 时期筛选两边同步）。
- 🏰 新增“历史地图集”（maps.html）：1563 年普法尔茨、宗教改革的传播、两位作者的人生路线、尼德兰难民之路、多特大会代表 5 个专题，每个都有核心一句、为什么重要、站点卡、地点表、相关主日、文化背景；另有多特代表条形图、改革路线泳道图、专题卡片。
- 📖 新增“圣经地理”（geo-bible.html）：亚伯拉罕之路、出埃及、保罗的旅程 3 张地图，各配经文（已与和合本逐字比对）与要理问答对应问答；地点为传统位置。
- 🏛️ 历史页地图换成同一套成对地图（21 个地点、4 条路线、海德堡周边放大插图），“在地图上查看”与时期筛选同时作用于两张图；13 个主日新增“历史 · 地理”卡片（缩略示意图＋一句关联＋跳到地图）。
- 🧭 右下角导航簇：后退 / 前进 / 主页 / 上一主日 / 下一主日 / 到顶 / 到底 / 快捷键；桌面端竖排展开并为正文让出右侧空间（不遮挡正文），≤1024px 收成一个 🧭 按钮，点开后执行任一操作自动收起；向下滚动时淡化。快捷键 [ ] 后退前进 · H 主页 · G / Shift+G 顶部底部 · , . 上一下一主日 · N 展开收起 · ? 快捷键说明 · Esc 关闭。
- 🖍️ 笔记标记 2.0：新增第 ④ 史地层——人物（紫色粗体）、地点（青色点线）、年代（琥珀色胶囊），历史内容中自动标记（每段最多 3 处）；新增“要点底纹”块；新增 🏛️ 历史、🗺️ 地理两种提示框。新“笔记标记系统”页（marks.html）：12 种标记 × 4 层的图例表、示范段落、8 种提示框、全站各类标记数量图、三遍阅读法；图例每一行可点击“聚焦”（只突出这一种，其余淡化，Esc 取消）；桌面端悬停任一标记显示其含义。
- 🌈 配色更活泼：五套主题都加入陆地 / 海洋 / 河流 / 标记新色变量；卡片顶部渐变色条、标题图标渐变底；地图颜色随主题切换。
- ⚡ 流畅度：实时地图只在进入视野时加载（同时最多 3 个，超出自动释放）；示意图动画只在可见时播放一次；地图引擎与底图按需加载并由 Service Worker 缓存；CLS 保持 0。v7 → v8 性能与 Lighthouse 对比见 README。
- ✅ 校验：原文逐字 0 差异；经文引语与和合本 0 处不符（新增地图集与圣经地理页的引语）；全部页面 × 375 / 768 / 1024 / 1440 × 5 套主题无溢出；Playwright 测试：在线地图、瓦片全部被屏蔽、引擎被屏蔽、无 WebGL 四种情况，以及导航簇（桌面 / 手机）全部通过。

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

- ⚡ 架构级流畅度：原文阅读版拆成 5 卷（每卷约 700–1100 个元素，原单页 3,724 个），旧链接 #q60 / #ld23 自动跳到对应分卷；另保留“全一页”版供打印与 Ctrl+F。
- ⚡ 跨页 View Transitions（原生淡入淡出，顶栏与侧栏保持不动）＋ Speculation Rules 悬停 / 触摸预取与预渲染（不支持的浏览器用 fetch / link prefetch 兜底）。
- ⚡ Service Worker：核心页面预缓存，同源资源 stale-while-revalidate，CDN 缓存优先；二次访问与离线都能秒开（离线回退首页）；?nosw 可关闭。
- ⚡ 关键 CSS 内联到每页（省一次阻塞请求）；目录在构建时生成（不再在加载后插入 → 消除布局偏移）；非关键初始化放进 requestIdleCallback。
- ⚡ 滚动时主线程零工作：滚动监听只设标志；目录高亮只做差异更新并在 scrollend 后执行；数字动画等到滚动停止；整段滚动 DOM 写入 ≤ 20 次。
- ⚡ 背景“浮云”改为单一合成层（1 个元素、2 个径向渐变），滚动中与标签页隐藏时暂停。
- ⚡ 零 CLS：主日页“连续朗读 / 标记已学完”按钮改为静态占位，ld/01 的 CLS 由 0.053 → 0。
- 💎 内容深化：52 个主日都新增“❓ 本主日回答的问题”“💡 为什么重要”“🏃 本周操练”，以及三环“🧬 圣约链：旧约应许 → 在基督里成全 → 今天的教会与我”（附经文）；10 个较薄的主日（9、17、37、39、41、42、43、47、49、50）新增“🔬 深化”。
- 📖 经文核对：本站学习笔记中带出处的 119 处经文引语，逐条与和合本（信望爱 FHL 线上和合本）比对并修正措辞（如“甚么”、赛64:6、太5:22、结36:23、太26:39 的出处等）；学习笔记中引用的要理问答语句也逐字对照原文改正。
- 📊 新可视化：圣经页“圣约链统计”（52 条链引用最多的旧约 / 新约书卷条形图 + 旧约 / 新约比例条）；52 主日总览新增“52 个问题 · 圣约链一览”表；圣约链节点依次淡入（只用 opacity / transform）。
- 🎨 配色细化：五套主题各有焦点环、文字选中色与滚动条颜色；对比度检查扩展到焦点环（≥3:1）与新组件，0 项不达 WCAG AA。
- 🖍️ 标记三态：全部 / ⭐ 仅核心（只留荧光核心词与经文药丸）/ 关；M 键循环；状态在首屏绘制前应用（无闪烁）；主日页原文区新增可展开的本页标记图例，并显示每种标记在本页出现的次数（构建时统计）。
- 🐞 修复：手机上“承上启下 / 问题推进”卡片被拉高到 200px 的空白；构建脚本任何一步失败即停止。
- ✅ 校验：原文逐字 0 差异；4 个宽度无溢出；Playwright 测试；v6 → v7 性能与 Lighthouse 对比见 README。

</details>

### ⚡ 流畅度对比（v7 → v8）

测量方法：`build/perf6.py`，Playwright 无头 Chromium，CDP **6 倍 CPU 降速**；`mobile` = 375×812、DPR 3、触屏，`desktop2x` = 1440×900、DPR 2。加载后用 rAF 记录连续滚动的帧时间，并用 DevTools trace 统计主线程任务与绘制。v7（`v7` 标签的 `site/`）与 v8 在**同一台机器、同一会话**中依次测量（`perf6_v7b.json` / `perf6_v8.json`）。“每 1000px”数值按滚动距离归一化。maps.html 是 v8 新页（左列为 v7 history.html，仅供参考）。

| 设备 · 页面 | 滚动 FPS | p95 帧 ms | 长任务(>50ms) | 主线程任务 ms / 1000px | 绘制 ms / 1000px | DOM |
|---|---|---|---|---|---|---|
| mobile · index.html | 56.8 → **58.1** | 16.8 → **16.8** | 3 → 1 | 152 → **120** | 87 → **85** | 1060 → 1097 |
| mobile · ld/01.html | 56.9 → **58.5** | 16.8 → **16.8** | 1 → 1 | 155 → **116** | 92 → **83** | 1108 → 1278 |
| mobile · ld/34.html | 57.2 → **58.1** | 16.8 → **16.8** | 2 → 2 | 141 → **111** | 85 → **81** | 1116 → 1262 |
| mobile · texts/hc-2.html | 60.0 → **60.0** | 16.8 → **16.8** | 0 → 0 | 80 → **41** | 26 → **19** | 1113 → 1134 |
| mobile · history.html（v8 双地图） | 56.2 → **57.8** | 16.8 → **16.8** | 2 → 2 | 151 → **129** | 102 → **102** | 1127 → 1380 |
| mobile · memory.html | 51.3 → **58.7** | 33.4 → **16.8** | 5 → 1 | 199 → **101** | 104 → **76** | 973 → 1028 |
| mobile · maps.html（v8 新页；左列为 v7 history） | 56.2 → **57.2** | 16.8 → **16.8** | 2 → 4 | 151 → **162** | 102 → **107** | 1127 → 2798 |
| desktop2x · index.html | 57.4 → **58.5** | 16.8 → **16.8** | 2 → 1 | 232 → **188** | 136 → **131** | 1060 → 1097 |
| desktop2x · ld/01.html | 57.1 → **56.7** | 16.8 → **16.8** | 2 → 2 | 201 → **217** | 131 → **164** | 1108 → 1278 |
| desktop2x · ld/34.html | 57.4 → **56.6** | 16.8 → **16.8** | 1 → 1 | 195 → **180** | 113 → **129** | 1116 → 1262 |
| desktop2x · texts/hc-2.html | 59.0 → **59.4** | 16.8 → **16.8** | 0 → 0 | 141 → **109** | 40 → **54** | 1113 → 1134 |
| desktop2x · history.html（v8 双地图） | 54.7 → **56.6** | 33.3 → **16.8** | 3 → 2 | 204 → **239** | 139 → **195** | 1133 → 1380 |
| desktop2x · memory.html | 58.3 → **57.8** | 16.8 → **16.8** | 0 → 2 | 198 → **180** | 98 → **133** | 973 → 1028 |
| desktop2x · maps.html（v8 新页；左列为 v7 history） | 54.7 → **46.4** | 33.3 → **33.4** | 3 → 5 | 204 → **383** | 139 → **311** | 1133 → 2777 |

### 🔦 Lighthouse（移动端预设，performance）

本地（`build/lh.py`，模拟 4× CPU + 慢速 4G，同一本地服务器，每页 3 次取中位数；`lh_v7b.json` / `lh_v8.json`）：

| 页面 | 分数 | TBT ms | CLS | LCP ms | FCP ms |
|---|---|---|---|---|---|
| index.html | 99 → **99** | 0 → **0** | 0 → **0** | 1575 → 1680 | 1550 → 1659 |
| ld/01.html | 99 → **99** | 0 → **0** | 0 → **0** | 1638 → 1748 | 1638 → 1748 |
| ld/34.html | 99 → **99** | 0 → **0** | 0 → **0** | 1624 → 1731 | 1624 → 1731 |
| history.html（v8 双地图） | 100 → **98** | 0 → **0** | 0 → **0** | 1537 → 1951 | 1537 → 1685 |
| memory.html | 98 → **98** | 0 → **0** | 0 → **0** | 1978 → 1987 | 1944 → 1936 |

v8 新页（本地，同上方法；`lh_v8.json`）：

| 页面 | 分数 | TBT ms | CLS | LCP ms | FCP ms |
|---|---|---|---|---|---|
| maps.html | 94 | 0 | 0 | 2551 | 2338 |
| geo-bible.html | 98 | 0 | 0 | 1952 | 1730 |
| marks.html | 100 | 0 | 0 | 1395 | 1395 |

线上 Netlify（v7 站 vs v8 站，同一会话连续测量；`lh_v7_netlify8.json` / `lh_v8_netlify.json`）：

| 页面 | 分数 | TBT ms | CLS | LCP ms | FCP ms |
|---|---|---|---|---|---|


### 📝 字数（v6 → v7，`build/wordcount.py`，只计解说文字：汉字 + 英文词；原文问答 / 信条 / 金句不计）

| 范围 | v6 | v7 | 变化 |
|---|---|---|---|
| 52 主日解说合计 | 74,584 | 86,788 | +16.4% |
| 平均每主日 | 1,434 | 1,669 | |
| index.html | 1,349 | 1,349 | +0.0% |
| bible.html | 1,628 | 1,793 | +10.1% |
| history.html | 3,378 | 3,378 | +0.0% |
| lorddays.html | 3,666 | 5,058 | +38.0% |
| compare.html | 2,786 | 2,786 | +0.0% |
| memory.html | 8,503 | 8,514 | +0.1% |
| 概览页合计 | 21,310 | 22,878 | +7.4% |

### 🧪 v8 地图与导航测试（`build/v8_test.py`，Playwright）

- ✅ live map loads with online tiles + 12 markers
- ✅ tiles blocked → site-hosted vector base (no blank)
- ✅ engine blocked → static illustration visible
- ✅ no WebGL → static illustration visible
- ✅ history: “在地图上查看” flies live map + highlights concept map (20. 多德雷赫特 Dordrecht1)
- ✅ history: era filter dims both maps [22, 19]
- ✅ desktop: cluster expanded ['back', 'fwd', 'home', 'nb ld pv', 'nb ld nx', 'top', 'bottom', 'help']
- ✅ desktop: cluster never overlaps content {'left': 1369, 'mainRight': 1361, 'hit': 0}
- ✅ bottom button [8250, 8250]
- ✅ top button 0
- ✅ key G → bottom
- ✅ key g → top
- ✅ key . → next Lord's Day http://localhost:8780/ld/06.html
- ✅ key [ → back http://localhost:8780/ld/05.html?nosw
- ✅ forward button http://localhost:8780/ld/06.html
- ✅ back button http://localhost:8780/ld/05.html?nosw
- ✅ next-LD button in cluster http://localhost:8780/ld/06.html
- ✅ ? → shortcut help
- ✅ home button http://localhost:8780/index.html
- ✅ mobile: collapsed to one button (1)
- ✅ mobile: tap opens cluster (9)
- ✅ mobile: cluster auto-collapses after an action (1)
- ✅ mobile: at page end the cluster does not cover the footer {'navTop': 752, 'footBottom': 702}
- ✅ marks: legend focus filter
FAILS 0 []

### 🧪 互动与架构测试（`build/toc_test.py`，Playwright）

- ✅ drag widens sidebar （300->420）
- ✅ width persisted to localStorage （420）
- ✅ max clamp = min(640,70vw) （640）
- ✅ min clamp = 220 （220）
- ✅ width persists across pages （220）
- ✅ keyboard arrows resize （268）
- ✅ double-click resets to 300 （300）
- ✅ multi-level numbered TOC (texts/hc: 部→主题→主日→问) 
- ✅ expand all （0）
- ✅ collapse all (current path stays open) （[64, 64]）
- ✅ single twisty toggles 
- ✅ TOC jump lands on target despite content-visibility （top=72）
- ✅ scrollspy highlights current Q and auto-expands parents （{"href": "#q60", "open": true}）
- ✅ long titles: nowrap + ellipsis + title （{"ws": "nowrap", "to": "ellipsis", "title": true}）
- ✅ marks toggle hides marks (all → core → off) （[True, 'none']）
- ✅ marks preference persisted 
- ✅ ☰ hides sidebar on desktop 
- ✅ mobile drawer opens 
- ✅ touch drag resizes (pointer events) （300->348）
- ✅ backdrop tap closes drawer 
- ✅ texts/hc-all: 52 unique LD entries "n.🔣 主日n · 标题" （1.✝️ 主日1 · 唯一的安慰 … 52.⚔️ 主日52 · 第六个祈求、结语与“阿们”）
- ✅ part headings have icons 
- ✅ nav 52-LD list numbered + icons, synced with TOC （1. ✝️ 主日1 · 唯一的安慰）
- ✅ texts/bc.html: specific numbered article titles （37 e.g. 2.📖 论神启示自己的方法）
- ✅ texts/cd.html: specific numbered article titles （63 e.g. 2.🌟 神差爱子）
- ✅ drag-to-order solved by pointer drag （🎉 完全正确！问题的推进你已经掌握）
- ✅ cloze generated from marks and checks （5 blanks · ✅ 5 / 5 全部正确！）
- ✅ constellation nodes clickable （13）
- ✅ LD game scores （得分 0 / 1 · 连对 0 · 最佳连对 0）
- ✅ v5 timeline: scrubber dots = events, era filter （35 dots / 35 events）
- ✅ v5 place card flies map + opens popup with LD links （海德堡 Heidelberg普法尔茨选帝侯首府；1563 要理问答在此写成。📅 ）
- ✅ v5 route toggle （btn）
- ✅ v5 zoom ladder 6 levels + current act （{"n": 6, "on": "✝️ 救赎", "op": "1"}）
- ✅ v6 LD distilled: no compass, core list once in essence + KPI card （{"pv": 0, "core": 3, "kpi": 4, "dupcore": 1}）
- ✅ v5 read-aloud player opens, highlights, next （{"show": true, "hl": ["q29"]} Q30 · 2/2）
- ✅ v5 compare: problems flow + Venn + Remonstrance table （{"v": 10, "p": 3, "r": 5}）
- ✅ v5 bible matrix has all 52 LDs （52）
- ✅ v6 backdrop-filter only on topbar (if any) （["topbar"]）
- ✅ v6 picker lists 5 themes （5）
- ✅ v6 theme switch applies + persists + syncs strip （["forest", "\"forest\"", "#08160f", "true"]）
- ✅ v6 theme strip changes colors （rgb(8, 22, 15) -> rgb(20, 12, 34)）
- ✅ v6 theme applied before paint on next page （grape）
- ✅ v6 LD svgs themed via CSS vars (no hard-coded hex attrs except logo) （0）
- ✅ v6 marks toggle (M) still works （[true, "none"]）
- ✅ v7 marks 仅核心: L1 highlight kept, L2 colour removed, radio checked, saved 
- ✅ v7 marks state applied before paint on next page (html class from head script) 
- ✅ v7 legacy marks=false maps to 关 
- ✅ v7 legend counts are static and match the DOM 
- ✅ v6 memory deck paginated (12/page, next, part filter, jump) 
- ✅ v6 three-level marks legend (8 rows) （8）
- ✅ v6 mermaid prerendered, library not loaded （{"st": 1, "lib": false, "err": false}）
- ✅ v6 cross-reference heatmap 52x4 （208）
- ✅ v6 era gantt 5 bars （5）
- ✅ v7 CSS inlined (no render-blocking stylesheet request) 
- ✅ v7 cross-document @view-transition rule present 
- ✅ v7 speculation rules (prefetch/prerender) present + supported 
- ✅ v7 floating sky = one composited layer （1）
- ✅ v7 service worker registered + controlling 
- ✅ v7 offline repeat visit served by SW cache （✝️ 主日 1　唯一的安慰）
- ✅ v7 ld/01 CLS = 0 （0.0000）
- ✅ v7 legacy deep link hc.html#q60 → volume 3, target in view （["hc-3.html", "#q60", 72]）
- ✅ v7 HC volume page is small (<1300 nodes) with 5 volumes + all-in-one nav （[972, 6, 27]）
- ✅ v7 no DOM writes during scroll (≤ 20 mutations for a long scroll, all after scrollend) （9）

## 🏗️ 架构（v7 起）

| 机制 | 实现 |
|---|---|
| 长页拆分 | `texts/hc-1…5.html`（主日 1–10 / 11–22 / 23–31 / 32–44 / 45–52），`texts/hc.html` 为目录页并把旧锚点 `#q60` `#ld23` 重定向到分卷；`texts/hc-all.html` 全一页 |
| 跨页过渡 | CSS `@view-transition{navigation:auto}`；顶栏 / 侧栏使用 `view-transition-name` 不参与淡入 |
| 预取 | `<script type="speculationrules">`：悬停 moderate 预取 + 按下 conservative 预渲染；不支持时 pointerover / touchstart 兜底 |
| 离线与秒开 | `site/sw.js`（构建哈希作为缓存名）：核心页预缓存 · 同源 stale-while-revalidate · CDN cache-first · 离线回退首页 · `?nosw` 关闭 |
| 首屏 | 每页内联压缩 CSS（约 44 KB）；目录构建时生成；主题 / 标记状态在首屏绘制前由 head 脚本应用 |
| 滚动 | 被动监听只设标志；目录高亮差异更新、scrollend 后执行；背景单层合成并在滚动中暂停 |
| 初始化 | 标签、测验、卡片、播放器、键盘、SW 注册等放进 `requestIdleCallback` |

## 🖍️ 标记图例（v8：四层 + 聚焦）

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
| 附 | 经文药丸 | 圣经出处 | 保留 |
| 提示框 | 💎核心 · ⚠️难点 · 🚫易错 · ✨金句（逐字原文） · 🪝记忆钩 · 📖核心经文 · 🏛️历史 · 🗺️地理（v8） | 每个主日与总览页 | 保留 |

三态：🖍️ 全部 → ⭐ 仅核心 → 🧽 关（顶栏 🖍️ 或 M 键循环；图例中的分段按钮可直接选择；保存在 localStorage `hc-marks`）。v8：`marks.html` 是完整说明页；图例每一行可点击“聚焦”只突出这一种标记（Esc 取消）；桌面端悬停标记显示含义。主日页原文区的“本主日笔记标记”图例显示每种标记在本页出现的次数（构建时统计）。标记只包在样式层的 `<span>` 中，原文文字不改。

## 🎨 配色主题

🌌 深夜星空 · 🌅 晨曦米白 · 🌲 翡翠森林 · 🍇 葡萄紫金 · 🌊 海洋蓝 —— 顶栏 🎨 切换，自动保存（`hc-theme`），首屏绘制前应用。v7 为每套主题加入焦点环、选中文字与滚动条颜色。`build/contrast.py` → `build/contrast_v7.json`：正文、弱化文字、强调色、标记色、色块标签全部 ≥ 4.5:1，焦点环 ≥ 3:1，**0 项不达 WCAG AA**。

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
- `build/layout_check.py`（v8）：全部 73 个页面（含 52 主日、5 个分卷与 v8 新增的 maps / geo-bible / marks）× 375 / 768 / 1024 / 1440 四种宽度 × 🌌🌅🌲🍇🌊 五套主题，横向溢出与顶栏截断 **0 个问题**。
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
surge site heidelberg-catechism-52-lorddays-20261023-v8-grokstudy.surge.sh
netlify deploy --prod --dir site --site <v8-site-id>
```

## 🗂️ 版本历史

### v8 · 2026-10-23 · [Release](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v8)
| 平台 | 链接 |
|---|---|
| GitHub Pages | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261023-v8-grokstudy.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261023-v8-grokstudy.netlify.app |

### v7 · 2026-10-23 · [Release](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v7)
| 平台 | 链接 |
|---|---|
| GitHub Pages（与 v8 同一地址，现显示最新版） | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261023-v7-grokstudy.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261023-v7-grokstudy.netlify.app |

### v6 · 2026-10-21 · [Release](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v6)
| 平台 | 链接 |
|---|---|
| GitHub Pages（与 v8 同一地址，现显示最新版） | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261021-v6-grokstudy.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261021-v6-grokstudy.netlify.app |

### v5 · 2026-10-21 · [Release](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v5)
| 平台 | 链接 |
|---|---|
| GitHub Pages（与 v8 同一地址，现显示最新版） | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261021-v5-grokstudy.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261021-v5-grokstudy.netlify.app |

### v4 · 2026-10-21 · [Release](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v4)
| 平台 | 链接 |
|---|---|
| GitHub Pages（与 v8 同一地址，现显示最新版） | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261021-v4-grokser.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261021-v4-grokser.netlify.app |

### v3 · 2026-10-20 · [Release](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v3)
| 平台 | 链接 |
|---|---|
| GitHub Pages（与 v8 同一地址，现显示最新版） | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261020-v3-grokser.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261020-v3-grokser.netlify.app |

### v2 · 2026-10-20 · [Release](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v2)
| 平台 | 链接 |
|---|---|
| GitHub Pages（与 v8 同一地址，现显示最新版） | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261020-v2-grokser.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261020-v2-grokser.netlify.app |

### v1 · 2026-10-20 · [Release](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v1)
| 平台 | 链接 |
|---|---|
| GitHub Pages（旧仓库名，仓库更名后已失效） | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-20261020-v1-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261020-v1-grokstudy.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261020-v1-grokstudy.netlify.app |
