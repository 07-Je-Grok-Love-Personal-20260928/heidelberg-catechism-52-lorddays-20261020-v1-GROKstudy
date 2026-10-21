# heidelberg-catechism-52-lorddays-20261021-v6-GROKstudy

> 《海德堡要理问答》52 主日全景深度解析：简体中文深度学习网站，共 129 问，持守欧陆改革宗立场（三项联合信条 + 三大普世信经）。

## 🌐 当前在线访问（v6）

| 平台 | 链接 |
|---|---|
| GitHub Pages | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261021-v6-grokstudy.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261021-v6-grokstudy.netlify.app |

📦 源码仓库：https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy
🏷️ Release：[v6](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v6) · [v5](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v5) · [v4](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v4) · [v3](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v3) · [v2](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v2) · [v1](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v1)

## 🆕 更新说明（v6 · 2026-10-21）

- ⚡ 流畅度重做（针对“页面有些卡顿”）：几乎移除全部 backdrop-filter（仅桌面低 DPR 的顶栏保留，手机 / 高 DPI / 低配设备自动关闭）；移除大阴影、filter 动画与 SVG 内部过渡；背景只剩 2 个可合成图层，滚动中与标签页隐藏时暂停；滚动时不再做淡入；content-visibility 仅用在章节级。
- ⚡ 资源与 DOM：CSS / JS 压缩；人物图改为 webp（192 / 640 两档 + width/height）；Mermaid 流程图构建时预渲染为静态 SVG（不再加载 Mermaid 库）；速记中心 129 张卡片与 52 题小测分页渲染（每页 12 张 / 8 题，可按部分筛选、洗牌、跳转），DOM 从 2566 降到约 950 个元素。
- 🎨 五套配色主题：🌌 深夜星空 · 🌅 晨曦米白 · 🌲 翡翠森林 · 🍇 葡萄紫金 · 🌊 海洋蓝。顶栏 🎨 选择器（首页图例也有色板），自动保存，首屏绘制前应用（无闪烁）；所有图表、地图标记、流程图与标记颜色随主题变化；五套主题正文对比度均达 WCAG AA（实测 13.6–15.9:1）。
- ✂️ 内容提炼：主日页去掉与其他卡片重复的“八个视角罗盘”和“五问提要”；要义清单只出现一次（移到精华区，附数据卡）；易错提示合并为一处；解说中与要义重复的句子自动剔除；重复的提示语缩短。首页 52 主日一览改为紧凑格，对比页合并重复的“文体 / 历史”两条。字数：52 个主日解说 110,782 → 74,688（−32.6%）；概览页 24,716 → 21,416（−13.4%）；原文不计入，且一字未动。
- 🖍️ 笔记标记升级：三层图例（① 核心层：荧光底 + 粗体；② 重点层：金 / 绿 / 红色粗体 = 重点 / 恩典应许 / 警示；③ 语义线：实线 = 定义、波浪线 = 难点、虚线 = 对比 / 错误立场，外加经文药丸）；新增绿色“恩典 · 应许 · 安慰”标记；提示框左侧加粗色条与色块标签；五套主题下颜色统一由变量控制；M 键开关照常。
- 📊 新可视化：52 主日 × 信条交叉引用热力图（52 主日总览）、五个时期甘特图（历史页）、主日数据卡（问答数 / 经文组 / 信条对照 / 关键词），首页主题色板。
- ✅ 校验：原文逐字 0 差异（2094 段 + 53 条金句）；4 个宽度无溢出；Playwright 测试；6× CPU 降速 + 手机仿真滚动帧率与 Lighthouse 的 v5 → v6 对比见 README。

<details><summary>v5 更新说明</summary>

- ⏳ 历史时间线扩充到 36 个事件，分为五个时期（背景 / 普法尔茨 / 尼德兰 / 多特 / 传承），新增苏黎世辩论、重洗派、加尔文《教会法令》、特伦托会议、《苏黎世协议》、圣像破坏、八十年战争、《誓绝法案》、十二年停战、奥尔登巴内费尔特、威斯特伐利亚、1834 分离运动、北美改革宗教会等；每个事件尽量附上相关主日链接。
- 🎚️ 时间线概览条（36 个圆点依次弹出，点击跳到事件；大圆点＝与主日相关）＋“时期”筛选按钮，筛选会同步淡化地图上的地点。
- 🗺️ 地图升级：21 个地点（新增马尔堡、特伦托、安特卫普、伦敦），按时期着色，弹窗列出相关主日；21 张地点卡片可“在地图上查看”（飞到该地并打开弹窗）；4 条路线可开关（乌尔西努求学、要理问答北传、比利时信条之路、新增“圣餐之争”路线）。
- 🏞️ 区域文化：六个舞台卡片（选帝侯普法尔茨、瑞士城市共和国、萨克森、南尼德兰、荷兰共和国、流亡社区），每张列出政体 / 语言或宗教 / 经济 / 与信条的关系。
- 🔭 每个主日新增“从整体到局部：六级缩放”——圣经大戏（创造 / 堕落 / 救赎 / 完成 / 回应）→ 圣约阶段 → 教义主题 → 要理问答的部与主题 → 本主日 → 各问，逐级展开动画；以及“八个视角罗盘”（整本圣经、圣约、圣经画面、指向基督、历史背景、核心要点、难点、应用），点击翻开一句话并跳到详解。
- 🧩 圣经页新增“52 主日 × 圣经大戏”教义主题矩阵（13 个教义主题 × 5 幕，点击进入主日）；与主日页的缩放使用同一张映射表。
- ⚖️ 对比页新增：“三个处境 → 三份文件”问题—文件—回答流程（说明为什么是三份而不是一份）；可点击的三圆维恩图（独有重点 / 两两共同 / 共同核心）；“抗辩派五条 vs 多特 vs 海德堡 vs 比利时”对照表。
- 🎧 连续朗读播放器：主日页与原文阅读版一键“连续朗读”，底部播放条支持 上一段 / 播放暂停 / 下一段 / 语速 / 进度，当前朗读的问答高亮并自动滚动到视野内（使用浏览器自带语音，效果取决于系统中文语音）。
- ✅ 校验：原文逐字 0 差异；全部页面 375 / 768 / 1024 / 1440 无溢出；Playwright 测试（新增地图飞行、时期筛选、朗读播放器、缩放与罗盘测试）；v4 → v5 性能对比见 README。

</details>

### ⚡ 流畅度对比（v5 → v6）

测量方法：`build/perf6.py`，Playwright 无头 Chromium，CDP **6 倍 CPU 降速**；`mobile` = 390×844、DPR 3、触屏仿真；`desktop2x` = 1440×900、DPR 2（模拟 Windows 高 DPI）。加载后用 rAF 记录约 4 秒连续滚动的帧时间，并从 Chrome trace 统计绘制、样式与布局耗时。两版在同一台机器、同一脚本下测得（原始数据：`build/perf6_v5.json` / `build/perf6_v6.json`）。无头测量不等于真机，但可用于同条件对比。

| 设备/页面 | 滚动 FPS | p95 帧 ms | 长任务数 | 绘制 ms | 样式+布局 ms | DOM |
|---|---|---|---|---|---|---|
| mobile/index.html | 54.1 → **57.9** | 33.3 → **16.8** | 1 → 1 | 1531 → **741** | 493 → 262 | 1239 → 1048 |
| mobile/ld/01.html | 56.5 → **58.4** | 16.8 → **16.8** | 1 → 1 | 1854 → **1050** | 485 → 309 | 1122 → 1023 |
| mobile/texts/hc.html | 55.8 → **58.1** | 33.3 → **16.8** | 0 → 0 | 2028 → **1074** | 549 → 339 | 3713 → 3724 |
| mobile/history.html | 56.9 → **57.3** | 16.8 → **16.7** | 1 → 2 | 2234 → **1449** | 586 → 277 | 1069 → 1127 |
| mobile/memory.html | 55.0 → **58.5** | 33.3 → **16.8** | 1 → 0 | 1554 → **1083** | 420 → 356 | 2566 → 969 |
| desktop2x/index.html | 53.8 → **57.9** | 33.3 → **16.8** | 1 → 1 | 1793 → **686** | 513 → 271 | 1239 → 1048 |
| desktop2x/ld/01.html | 55.0 → **58.2** | 33.3 → **16.8** | 2 → 1 | 1922 → **929** | 392 → 318 | 1122 → 1023 |
| desktop2x/texts/hc.html | 49.1 → **55.1** | 33.4 → **33.3** | 2 → 0 | 3633 → **1759** | 802 → 539 | 3713 → 3724 |
| desktop2x/history.html | 50.0 → **57.8** | 33.4 → **16.8** | 5 → 1 | 3323 → **1376** | 652 → 302 | 1075 → 1133 |
| desktop2x/memory.html | 44.8 → **58.2** | 50.0 → **16.8** | 10 → 2 | 2879 → **816** | 748 → 294 | 2566 → 969 |

### 🔦 Lighthouse（移动端预设，performance）

本地（`build/lh.py`，模拟 4× CPU + 慢速 4G，同一本地服务器）：

| 页面 | 分数 | TBT ms | CLS | LCP ms | FCP ms |
|---|---|---|---|---|---|
| index.html | 100 → **100** | 0 → **0** | 0 → **0** | 1140 → 1385 | 1117 → 1201 |
| ld/01.html | 100 → **99** | 0 → **0** | 0.008 → **0.053** | 1212 → 1384 | 1177 → 1265 |
| texts/hc.html | 100 → **97** | 0 → **0** | 0.027 → **0** | 1112 → 2060 | 1071 → 2060 |
| history.html | 100 → **100** | 0 → **0** | 0 → **0** | 1099 → 1373 | 1075 → 1201 |
| memory.html | 100 → **97** | 4 → **0** | 0 → **0** | 1188 → 2072 | 1119 → 2056 |

线上 Netlify（v5 站 vs v6 站）：

| 页面 | 分数 | TBT ms | CLS | LCP ms | FCP ms |
|---|---|---|---|---|---|
| index.html | 99 → **100** | 0 → **0** | 0 → **0.003** | 1532 → 1369 | 1485 → 1317 |
| ld/01.html | 98 → **99** | 141 → **85** | 0.001 → **0.001** | 1548 → 1392 | 1285 → 1186 |
| texts/hc.html | 98 → **100** | 127 → **0** | 0.001 → **0.029** | 1447 → 1346 | 1244 → 1311 |
| history.html | 99 → **100** | 1 → **0** | 0.001 → **0.003** | 1328 → 1255 | 1274 → 1228 |
| memory.html | 99 → **100** | 60 → **0** | 0.001 → **0.003** | 1415 → 1249 | 1254 → 1229 |

### ✂️ 提炼字数（`build/wordcount.py`，只计解说文字：汉字 + 英文词；原文问答 / 信条 / 金句不计）

| 范围 | v5 | v6 | 变化 |
|---|---|---|---|
| 52 主日解说合计 | 110,782 | 74,688 | -32.6% |
| 平均每主日 | 2,130 | 1,436 | |
| index.html | 3,706 | 1,433 | -61.3% |
| bible.html | 1,628 | 1,628 | +0.0% |
| history.html | 3,366 | 3,378 | +0.4% |
| lorddays.html | 4,715 | 3,666 | -22.2% |
| compare.html | 2,945 | 2,808 | -4.7% |
| memory.html | 8,356 | 8,503 | +1.8% |
| 概览页合计 | 24,716 | 21,416 | -13.4% |

### 🧪 目录与互动测试（`build/toc_test.py`，Playwright）

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
- ✅ marks toggle hides marks （[True, 'none']）
- ✅ marks preference persisted 
- ✅ ☰ hides sidebar on desktop 
- ✅ mobile drawer opens 
- ✅ touch drag resizes (pointer events) （300->348）
- ✅ backdrop tap closes drawer 
- ✅ texts/hc: 52 unique LD entries "n.🔣 主日n · 标题" （1.✝️ 主日1 · 唯一的安慰 … 52.⚔️ 主日52 · 第六个祈求、结语与“阿们”）
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
- ✅ v6 memory deck paginated (12/page, next, part filter, jump) 
- ✅ v6 three-level marks legend (8 rows) （8）
- ✅ v6 mermaid prerendered, library not loaded （{"st": 1, "lib": false, "err": false}）
- ✅ v6 cross-reference heatmap 52x4 （208）
- ✅ v6 era gantt 5 bars （5）

## 🖍️ 标记图例（v6 三层）

| 层级 | 样式 | 含义 |
|---|---|---|
| ① 核心层 | 荧光底 + 粗体 | 核心词句（答案主干，背诵首选） |
| ② 重点层 | 金色粗体 | 重点概念 / 论题关键词 |
| ② 重点层 | 绿色粗体 | 恩典 · 应许 · 安慰（v6 新增） |
| ② 重点层 | 红色粗体 | 警示 · 审判 · 严重后果 |
| ③ 语义线 | 蓝色实线 | 定义 / 术语 |
| ③ 语义线 | 橙色波浪线 | 难点 |
| ③ 语义线 | 红色虚线 | 对比 / 错误立场 |
| 附 | 经文药丸 | 圣经出处 |
| 提示框 | 💎核心 · ⚠️难点 · 🚫易错 · ✨金句（逐字原文） · 🪝记忆钩 · 📖核心经文 | 每个主日与总览页 |

一种样式只表达一种含义；颜色由主题变量控制，五套配色下都可读。标记只包在样式层的 `<span>` 中，原文文字不改；可用顶栏 🖍️ 或 M 键一键隐藏。

## 🎨 配色主题

🌌 深夜星空 · 🌅 晨曦米白 · 🌲 翡翠森林 · 🍇 葡萄紫金 · 🌊 海洋蓝 —— 顶栏 🎨 切换，自动保存（localStorage `hc-theme`），首屏绘制前应用。正文对比度（`build/contrast.py` → `build/contrast_v6.json`）：13.6–15.9:1，全部 WCAG AA。

## 📚 网站结构

| 页面 | 内容 |
|---|---|
| `index.html` | 首页：图例、全书精华（论题/金句/易错/记忆钩）、三部分比例图、52 主日问答数柱状图、圣经四幕剧、罪-恩-谢、思维导图、三大支柱、52 主日网格、学习路径 |
| `bible.html` | 圣经神学、52 主日 × 圣经大戏矩阵（v5）、圣约神学（桌面流程图 / 手机盟约阶梯）、八个视角、本质核心 |
| `history.html` | 三线故事线、五时期甘特图（v6）+ 36 事件时间线（概览条 + 时期筛选）、Leaflet 地图（21 地点、4 条可开关路线、地点卡片飞行定位，v5）、人物、六个区域文化舞台（v5） |
| `lorddays.html` | 52 主日按 17 个主题分组、筛选、进度、交叉引用热力图（v6）、结构与信条对照总表 |
| `ld/01.html … ld/52.html` | 精华（要义 + 数据卡 · 金句 · 易错 · 核心经文 · 关联星图 · 承上启下）→ 原文（🎧 连续朗读）→ 整体（🔭 六级缩放 + 四视角卡）→ 局部（背景 · 难点） → 交叉对照 → 应用（页签）→ 记忆 → 延伸 |
| `texts/index.html` | 原文中心（v3 新增） |
| `texts/hc.html` `bc.html` `cd.html` `creeds.html` | 干净阅读版/背诵版（要理问答四级目录：部 → 主题 → 主日 → 问；比利时信条 12 主题 → 37 条；多特信经 4 项 → 条目） |
| `compare.html` | 总对比、覆盖度图、BC 12 主题环形图、为什么三份、三个处境 → 三份文件（v5）、维恩图（v5）、抗辩派五条对照（v5）、教义矩阵、三大信经对比 |
| `memory.html` | 三层标记图例、数字骨架、52 口诀、129 卡片（分页 · 筛选 · 洗牌 · 跳转）、52 测验（分页） |
| `search.html` · `sources.html` · `changelog.html` | 搜索 · 资料与校验方法 · 版本记录 |

快捷键：T 目录 · R 背诵模式 · M 标记开关 · ←/→ 切换主日。目录右边缘可拖动调整宽度（双击恢复）。

## ✅ 原文来源与校验

- 全部信条与信经中文原文由程序抓取自 https://ccifellowship.org/books/book-of-praise （《中国改革宗敬拜手册》2015），未做任何文字改动。
- `build/verify_verbatim.py`：站内 2094 个原文块逐字比对 **0 处差异**；53 条“金句”均为原文的逐字子串（0 处差异）。
- `build/layout_check.py`：66 个页面（含全部 52 主日）× 375 / 768 / 1024 / 1440 四种宽度，横向溢出与顶栏截断 **0 个问题**。
- ccifellowship.org 未收录多特信经的“结论”部分，本站也未收录。威斯敏斯特小要理问答英文引文取自 opc.org。原文版权归原出版委员会，本站仅作学习引用。解读为学习笔记，未经神学家审阅。

## 🛠️ 构建与部署

```bash
bash build/build_all.sh                 # 生成 site/
python3 build/verify_verbatim.py        # 逐字校验
python3 build/layout_check.py URL 375   # 布局检测（需本地服务器）
python3 build/toc_test.py URL           # 目录拖动/折叠测试
python3 build/perf6.py URL out.json     # 流畅度测量（6× CPU）
python3 build/lh.py URL out.json        # Lighthouse
git subtree push --prefix site origin gh-pages
surge site heidelberg-catechism-52-lorddays-20261021-v6-grokstudy.surge.sh
netlify deploy --prod --dir site --site 2a9598b6-33b0-421c-808f-27bd72a25ea6
```

## 🗂️ 版本历史

### v6 · 2026-10-21 · [Release](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v6)
| 平台 | 链接 |
|---|---|
| GitHub Pages | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261021-v6-grokstudy.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261021-v6-grokstudy.netlify.app |

### v5 · 2026-10-21 · [Release](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v5)
| 平台 | 链接 |
|---|---|
| GitHub Pages（与 v6 同一地址，现显示最新版） | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261021-v5-grokstudy.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261021-v5-grokstudy.netlify.app |

### v4 · 2026-10-21 · [Release](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v4)
| 平台 | 链接 |
|---|---|
| GitHub Pages（与 v6 同一地址，现显示最新版） | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261021-v4-grokser.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261021-v4-grokser.netlify.app |

### v3 · 2026-10-20 · [Release](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v3)
| 平台 | 链接 |
|---|---|
| GitHub Pages（与 v6 同一地址，现显示最新版） | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261020-v3-grokser.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261020-v3-grokser.netlify.app |

### v2 · 2026-10-20 · [Release](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v2)
| 平台 | 链接 |
|---|---|
| GitHub Pages（与 v6 同一地址，现显示最新版） | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261020-v2-grokser.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261020-v2-grokser.netlify.app |

### v1 · 2026-10-20 · [Release](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v1)
| 平台 | 链接 |
|---|---|
| GitHub Pages（旧仓库名，仓库更名后已失效） | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-20261020-v1-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261020-v1-grokstudy.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261020-v1-grokstudy.netlify.app |
