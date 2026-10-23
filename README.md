# heidelberg-catechism-52-lorddays-20261023-v7-GROKstudy

> 《海德堡要理问答》52 主日全景深度解析：简体中文深度学习网站，共 129 问，持守欧陆改革宗立场（三项联合信条 + 三大普世信经）。

## 🌐 当前在线访问（v7）

| 平台 | 链接 |
|---|---|
| GitHub Pages | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261023-v7-grokstudy.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261023-v7-grokstudy.netlify.app |

📦 源码仓库：https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy
🏷️ Release：[v7](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v7) · [v6](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v6) · [v5](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v5) · [v4](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v4) · [v3](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v3) · [v2](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v2) · [v1](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v1)
📝 更新记录页：`changelog.html`（站内顶栏版本徽章）

## 🆕 更新说明（v7 · 2026-10-23）

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

<details><summary>v6 更新说明</summary>

- ⚡ 流畅度重做（针对“页面有些卡顿”）：几乎移除全部 backdrop-filter（仅桌面低 DPR 的顶栏保留，手机 / 高 DPI / 低配设备自动关闭）；移除大阴影、filter 动画与 SVG 内部过渡；背景只剩 2 个可合成图层，滚动中与标签页隐藏时暂停；滚动时不再做淡入；content-visibility 仅用在章节级。
- ⚡ 资源与 DOM：CSS / JS 压缩；人物图改为 webp（192 / 640 两档 + width/height）；Mermaid 流程图构建时预渲染为静态 SVG（不再加载 Mermaid 库）；速记中心 129 张卡片与 52 题小测分页渲染（每页 12 张 / 8 题，可按部分筛选、洗牌、跳转），DOM 从 2566 降到约 950 个元素。
- 🎨 五套配色主题：🌌 深夜星空 · 🌅 晨曦米白 · 🌲 翡翠森林 · 🍇 葡萄紫金 · 🌊 海洋蓝。顶栏 🎨 选择器（首页图例也有色板），自动保存，首屏绘制前应用（无闪烁）；所有图表、地图标记、流程图与标记颜色随主题变化；五套主题正文对比度均达 WCAG AA（实测 13.6–15.9:1）。
- ✂️ 内容提炼：主日页去掉与其他卡片重复的“八个视角罗盘”和“五问提要”；要义清单只出现一次（移到精华区，附数据卡）；易错提示合并为一处；解说中与要义重复的句子自动剔除；重复的提示语缩短。首页 52 主日一览改为紧凑格，对比页合并重复的“文体 / 历史”两条。字数：52 个主日解说 110,782 → 74,688（−32.6%）；概览页 24,716 → 21,416（−13.4%）；原文不计入，且一字未动。
- 🖍️ 笔记标记升级：三层图例（① 核心层：荧光底 + 粗体；② 重点层：金 / 绿 / 红色粗体 = 重点 / 恩典应许 / 警示；③ 语义线：实线 = 定义、波浪线 = 难点、虚线 = 对比 / 错误立场，外加经文药丸）；新增绿色“恩典 · 应许 · 安慰”标记；提示框左侧加粗色条与色块标签；五套主题下颜色统一由变量控制；M 键开关照常。
- 📊 新可视化：52 主日 × 信条交叉引用热力图（52 主日总览）、五个时期甘特图（历史页）、主日数据卡（问答数 / 经文组 / 信条对照 / 关键词），首页主题色板。
- ✅ 校验：原文逐字 0 差异（2094 段 + 53 条金句）；4 个宽度无溢出；Playwright 测试；6× CPU 降速 + 手机仿真滚动帧率与 Lighthouse 的 v5 → v6 对比见 README。

</details>

### ⚡ 流畅度对比（v6 → v7）

测量方法：`build/perf6.py`，Playwright 无头 Chromium，CDP **6 倍 CPU 降速**；本轮只测 `desktop2x` = 1440×900、DPR 2（模拟 Windows 高 DPI，最吃力的档位；移动端自动进入轻量模式，v6 已测）。加载后用 rAF 记录连续滚动的帧时间，并用 DevTools trace 统计主线程任务与绘制。v6（`v6` 标签的 `site/`）与 v7 在**同一台机器、同一会话**中依次测量（`perf6_v6c.json` / `perf6_v7.json`）。不同长度的页面滚动距离不同，所以另给出“每滚动 1000px 的主线程 / 绘制毫秒数”。v6 的 `texts/hc.html` 是 3,724 个元素的单页；v7 中它变成目录页，原文分成 5 卷（另有全一页版）。表中 v6 列是 v6 单页 `texts/hc.html` 的数据。v7 目录页很短（滚动距离小），所以它的“每 1000px”数值被首屏固定开销放大，不宜直接比较。

| 设备 · 页面 | 滚动 FPS | p95 帧 ms | 长任务(>50ms) | 主线程任务 ms / 1000px | 绘制 ms / 1000px | DOM |
|---|---|---|---|---|---|---|
| desktop2x · index.html | 58.5 → **58.3** | 16.8 → **16.8** | 1 → 1 | 181 → **178** | 122 → **121** | 1048 → 1060 |
| desktop2x · ld/01.html | 58.0 → **57.8** | 16.8 → **16.8** | 0 → 1 | 229 → **180** | 168 → **122** | 1023 → 1108 |
| desktop2x · texts/hc-all.html（v7 全一页） | 54.5 → **56.7** | 33.3 → **33.3** | 1 → 0 | 154 → **93** | 123 → **61** | 3724 → 3750 |
| desktop2x · texts/hc-2.html（v7 分卷 2） | 54.5 → **59.8** | 33.3 → **16.8** | 1 → 0 | 154 → **81** | 123 → **36** | 3724 → 1113 |
| desktop2x · texts/hc-4.html（v7 分卷 4） | 54.5 → **59.8** | 33.3 → **16.8** | 1 → 0 | 154 → **77** | 123 → **37** | 3724 → 1106 |
| desktop2x · texts/hc.html（v7 目录页） | 54.5 → **60.0** | 33.3 → **16.8** | 1 → 0 | 154 → **287** | 123 → **151** | 3724 → 475 |
| desktop2x · history.html | 57.5 → **57.5** | 16.8 → **16.8** | 2 → 1 | 155 → **142** | 131 → **116** | 1133 → 1133 |
| desktop2x · memory.html | 58.7 → **58.5** | 16.8 → **16.8** | 0 → 1 | 137 → **134** | 108 → **102** | 969 → 973 |

### 🔦 Lighthouse（移动端预设，performance）

本地（`build/lh.py`，模拟 4× CPU + 慢速 4G，同一本地服务器，每页 3 次取中位数；`lh_v6c.json` / `lh_v7.json`）：

| 页面 | 分数 | TBT ms | CLS | LCP ms | FCP ms |
|---|---|---|---|---|---|
| index.html | 100 → **100** | 0 → **0** | 0 → **0** | 1126 → 1066 | 1074 → 1039 |
| ld/01.html | 100 → **100** | 0 → **0** | 0 → **0** | 1349 → 1159 | 1349 → 1159 |
| texts/hc-all.html（v7 全一页） | 100 → **100** | 0 → **0** | 0 → **0** | 1328 → 1367 | 1328 → 1367 |
| texts/hc-2.html（v7 分卷 2） | 100 → **100** | 0 → **5** | 0 → **0** | 1328 → 1152 | 1328 → 1097 |
| texts/hc.html（v7 目录页） | 100 → **100** | 0 → **0** | 0 → **0** | 1328 → 1042 | 1328 → 1042 |
| history.html | 100 → **100** | 0 → **6** | 0 → **0** | 1082 → 1141 | 1056 → 1085 |
| memory.html | 100 → **100** | 4 → **21** | 0 → **0** | 1346 → 1318 | 1319 → 1203 |

线上 Netlify：v7 站本轮未单独测 Lighthouse（部署后环境重置，测量工具需重装）；以上本地数据用的是同一份构建产物。

### 📝 字数（`build/wordcount.py`，只计解说文字：汉字 + 英文词；原文问答 / 信条 / 金句不计）

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

## 🏗️ v7 架构

| 机制 | 实现 |
|---|---|
| 长页拆分 | `texts/hc-1…5.html`（主日 1–10 / 11–22 / 23–31 / 32–44 / 45–52），`texts/hc.html` 为目录页并把旧锚点 `#q60` `#ld23` 重定向到分卷；`texts/hc-all.html` 全一页 |
| 跨页过渡 | CSS `@view-transition{navigation:auto}`；顶栏 / 侧栏使用 `view-transition-name` 不参与淡入 |
| 预取 | `<script type="speculationrules">`：悬停 moderate 预取 + 按下 conservative 预渲染；不支持时 pointerover / touchstart 兜底 |
| 离线与秒开 | `site/sw.js`（构建哈希作为缓存名）：核心页预缓存 · 同源 stale-while-revalidate · CDN cache-first · 离线回退首页 · `?nosw` 关闭 |
| 首屏 | 每页内联压缩 CSS（约 44 KB）；目录构建时生成；主题 / 标记状态在首屏绘制前由 head 脚本应用 |
| 滚动 | 被动监听只设标志；目录高亮差异更新、scrollend 后执行；背景单层合成并在滚动中暂停 |
| 初始化 | 标签、测验、卡片、播放器、键盘、SW 注册等放进 `requestIdleCallback` |

## 🖍️ 标记图例（v7 三态）

| 层级 | 样式 | 含义 | “仅核心”模式 |
|---|---|---|---|
| ① 核心层 | 荧光底 + 粗体 | 核心词句（答案主干，背诵首选） | 保留 |
| ② 重点层 | 金色粗体 | 重点概念 / 论题关键词 | 隐藏 |
| ② 重点层 | 绿色粗体 | 恩典 · 应许 · 安慰 | 隐藏 |
| ② 重点层 | 红色粗体 | 警示 · 审判 · 严重后果 | 隐藏 |
| ③ 语义线 | 蓝色实线 | 定义 / 术语 | 隐藏 |
| ③ 语义线 | 橙色波浪线 | 难点 | 隐藏 |
| ③ 语义线 | 红色虚线 | 对比 / 错误立场 | 隐藏 |
| 附 | 经文药丸 | 圣经出处 | 保留 |
| 提示框 | 💎核心 · ⚠️难点 · 🚫易错 · ✨金句（逐字原文） · 🪝记忆钩 · 📖核心经文 | 每个主日与总览页 | 保留 |

三态：🖍️ 全部 → ⭐ 仅核心 → 🧽 关（顶栏 🖍️ 或 M 键循环；图例中的分段按钮可直接选择；保存在 localStorage `hc-marks`）。主日页原文区的“本主日笔记标记”图例显示每种标记在本页出现的次数（构建时统计）。标记只包在样式层的 `<span>` 中，原文文字不改。

## 🎨 配色主题

🌌 深夜星空 · 🌅 晨曦米白 · 🌲 翡翠森林 · 🍇 葡萄紫金 · 🌊 海洋蓝 —— 顶栏 🎨 切换，自动保存（`hc-theme`），首屏绘制前应用。v7 为每套主题加入焦点环、选中文字与滚动条颜色。`build/contrast.py` → `build/contrast_v7.json`：正文、弱化文字、强调色、标记色、色块标签全部 ≥ 4.5:1，焦点环 ≥ 3:1，**0 项不达 WCAG AA**。

## 📚 网站结构

| 页面 | 内容 |
|---|---|
| `index.html` | 首页：图例（三态标记）、全书精华、三部分比例图、52 主日问答数柱状图、圣经四幕剧、罪-恩-谢、思维导图、三大支柱、52 主日网格、学习路径 |
| `bible.html` | 圣经神学、52 主日 × 圣经大戏矩阵、圣约神学、八个视角、本质核心、🧬 圣约链统计（v7） |
| `history.html` | 三线故事线、五时期甘特图、36 事件时间线、Leaflet 地图（21 地点、4 条路线）、人物、区域文化 |
| `lorddays.html` | 52 主日按 17 个主题分组、筛选、进度、交叉引用热力图、❓ 52 个问题 · 圣约链一览（v7）、结构与信条对照总表 |
| `ld/01.html … ld/52.html` | ❓ 本主日回答的问题 + 💎 核心 → 精华（💡 为什么重要 · 🏃 本周操练 · 要义 · 数据卡 · 金句 · 易错 · 星图 · 承上启下）→ 原文（🎧 连续朗读 · 标记图例）→ 整体（🧬 圣约链 · 🔭 六级缩放 · 四视角卡）→ 局部（背景 · 难点 · 🔬 深化）→ 交叉对照 → 应用 → 记忆 → 延伸 |
| `texts/index.html` | 原文中心 |
| `texts/hc.html` | 要理问答目录页（5 卷卡片 + 52 主日跳转格；旧锚点自动跳转） |
| `texts/hc-1.html … hc-5.html` · `texts/hc-all.html` | 要理问答分卷阅读 / 背诵版 · 全一页版（打印、Ctrl+F） |
| `texts/bc.html` `cd.html` `creeds.html` | 比利时信条 · 多特信经 · 三大信经 |
| `compare.html` | 三项联合信条对比、覆盖度、维恩图、抗辩派对照、教义矩阵、三大信经对比 |
| `memory.html` | 三层标记图例、数字骨架、52 口诀、129 卡片、52 测验、进度 |
| `search.html` · `sources.html` · `changelog.html` | 搜索 · 资料与校验方法 · 版本记录 |

快捷键：T 目录 · R 背诵模式 · M 标记三态 · ←/→ 切换主日。

## ✅ 原文来源与校验

- 全部信条与信经中文原文由程序抓取自 https://ccifellowship.org/books/book-of-praise （《中国改革宗敬拜手册》2015），未做任何文字改动。
- `build/verify_verbatim.py`：站内 2,712 个原文块逐字比对 **0 处差异**；53 条“金句”均为原文的逐字子串（0 处差异）。
- `build/check_cuv.py`（v7）：学习笔记中带出处的经文引语 119 处，与信望爱 FHL 线上和合本（https://bible.fhl.net/ ，version=unv）逐条比对，**0 处不符**（修正 30 余处措辞 / 出处）。学习笔记中加引号的要理问答语句已与原文逐字对照。
- `build/layout_check.py`：全部页面（含 52 主日与 5 个分卷）：v7 最终构建在 375 / 768 宽度下横向溢出与顶栏截断 **0 个问题**。1024 / 1440 宽度与主题抽查的完整复测被环境重置中断；7 张 v7 截图（1440 / 1024 / 390 宽，五套主题）的 scrollWidth 检查均无溢出。
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
surge site heidelberg-catechism-52-lorddays-20261023-v7-grokstudy.surge.sh
netlify deploy --prod --dir site --site 2a8c313e-9174-4a68-8b90-3d0a56c29809
```

## 🗂️ 版本历史

### v7 · 2026-10-23 · [Release](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v7)
| 平台 | 链接 |
|---|---|
| GitHub Pages | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261023-v7-grokstudy.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261023-v7-grokstudy.netlify.app |

### v6 · 2026-10-21 · [Release](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v6)
| 平台 | 链接 |
|---|---|
| GitHub Pages（与 v7 同一地址，现显示最新版） | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261021-v6-grokstudy.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261021-v6-grokstudy.netlify.app |

### v5 · 2026-10-21 · [Release](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v5)
| 平台 | 链接 |
|---|---|
| GitHub Pages（与 v7 同一地址，现显示最新版） | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261021-v5-grokstudy.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261021-v5-grokstudy.netlify.app |

### v4 · 2026-10-21 · [Release](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v4)
| 平台 | 链接 |
|---|---|
| GitHub Pages（与 v7 同一地址，现显示最新版） | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261021-v4-grokser.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261021-v4-grokser.netlify.app |

### v3 · 2026-10-20 · [Release](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v3)
| 平台 | 链接 |
|---|---|
| GitHub Pages（与 v7 同一地址，现显示最新版） | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261020-v3-grokser.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261020-v3-grokser.netlify.app |

### v2 · 2026-10-20 · [Release](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v2)
| 平台 | 链接 |
|---|---|
| GitHub Pages（与 v7 同一地址，现显示最新版） | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261020-v2-grokser.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261020-v2-grokser.netlify.app |

### v1 · 2026-10-20 · [Release](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v1)
| 平台 | 链接 |
|---|---|
| GitHub Pages（旧仓库名，仓库更名后已失效） | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-20261020-v1-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261020-v1-grokstudy.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261020-v1-grokstudy.netlify.app |
