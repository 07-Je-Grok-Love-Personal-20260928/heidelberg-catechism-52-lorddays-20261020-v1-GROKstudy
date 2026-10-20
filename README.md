# heidelberg-catechism-52-lorddays-20261020-v3-GROKstudy

> 《海德堡要理问答》52 主日全景深度解析：简体中文深度学习网站，共 129 问，持守欧陆改革宗立场（三项联合信条 + 三大普世信经）。

## 🌐 当前在线访问（v3）

| 平台 | 链接 |
|---|---|
| GitHub Pages | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261020-v3-grokser.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261020-v3-grokser.netlify.app |

📦 源码仓库：https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy
🏷️ Release：[v3](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v3) · [v2](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v2) · [v1](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v1)

## 🆕 更新说明（v3 · 2026-10-20）

- ⚡ 流畅度重构：毛玻璃 backdrop-filter 只保留在顶栏、悬浮按钮与提示条；卡片改为“伪玻璃”渐变；背景改为预模糊的径向渐变云层，只用 transform 漂移（不再对大面积元素做 filter:blur 动画）；各 section 使用 content-visibility:auto；目录高亮改用 IntersectionObserver，进度条使用 CSS scroll-timeline（不支持时用 rAF）；所有监听器 passive；支持 prefers-reduced-motion。
- ↔️ 左侧目录可拖动右边缘调整宽度（220px – min(640px, 70vw)），支持鼠标、触屏与键盘方向键，宽度保存在本机；双击把手恢复默认；长标题单行省略并带悬停提示。
- 📑 目录改为三级编号树：一级“一、二、三”，二级“1. 2.”，三级“1.1”；每级可折叠，提供“全部展开 / 全部折叠”，滚动时自动展开并高亮当前所在小节。
- 🖍️ 新增笔记标记系统：高亮、粗体金、蓝实线（定义）、橙波浪线（难点）、红虚线（对比/错误立场）、红字（警示）、经文标签；五类提示框：核心 · 难点 · 易错 · 金句 · 记忆钩。顶栏 🖍️ 或 M 键一键显示/隐藏。原文只包标签，文字一字不改（校验 0 差异）。
- 💎 每个主日新增“精华速览”：五问提要（论题 · 为什么 · 写了什么 · 怎么活 · 圣经与圣约）、逐字金句、易错提醒，以及“关联星图”（各问与关键词、比利时信条、多特信经、威斯敏斯特的连线动画）和 52 主日位置条。
- 📊 新增图表：首页 129 问三部分比例条、52 主日问答数柱状图（可点击）；对比页“覆盖度图”；原文中心卡片进度条；动画只用 transform / stroke-dashoffset。
- 🧭 结构收紧：顶栏导航精简为 8 项（修复约 1024px 宽度时最后一项被截断），新增“原文中心”汇总四部原文；52 主日总览按 17 个主题分组；主日页重排为 精华 → 原文 → 整体 → 局部 → 对照 → 应用（分页签）→ 记忆 → 延伸。
- ✅ 校验：原文逐字比对 0 差异（含金句）；375 / 768 / 1440 全部页面无横向溢出；Playwright 测试目录拖动与折叠；截图全部重拍（v3-*）。

### ⚡ 性能对比（v2 → v3）

测量方法：`build/perf.py`，Playwright 无头 Chromium，CDP 模拟 **4 倍 CPU 降速**，页面加载后以 rAF 记录 4 秒自动滚动的帧时间，并用 PerformanceObserver 统计长任务（>50 ms）。两版在同一台机器、同一脚本下测得（原始数据：`build/perf_v2.json`、`build/perf_v3.json`）。无头环境数字只用于前后对比，不等同于真机体验。

| 宽度/页面 | 滚动 FPS | 最长帧 ms | 加载长任务 ms | 滚动长任务 ms | DOM 节点 |
|---|---|---|---|---|---|
| 1440/index.html | 49.2 → **59.8** | 50.1 → **33.3** | 595 → **347** | 0 → **0** | 635 → 1025 |
| 1440/ld/01.html | 45.3 → **60.0** | 50.0 → **16.8** | 291 → **0** | 0 → **0** | 434 → 869 |
| 1440/texts/hc.html | 36.4 → **60.0** | 50.0 → **16.8** | 392 → **142** | 0 → **0** | 2657 → 3620 |
| 1440/memory.html | 36.7 → **59.8** | 50.0 → **33.3** | 358 → **170** | 0 → **0** | 2314 → 2447 |
| 1440/history.html | 55.2 → **60.0** | 50.0 → **16.8** | 1725 → **150** | 0 → **0** | 483 → 489 |
| 375/index.html | 60.0 → **60.0** | 16.8 → **16.8** | 382 → **236** | 0 → **0** | 635 → 1025 |
| 375/ld/01.html | 60.0 → **60.0** | 16.8 → **16.8** | 226 → **185** | 0 → **0** | 434 → 869 |
| 375/texts/hc.html | 59.7 → **60.0** | 49.9 → **16.8** | 474 → **164** | 63 → **0** | 2657 → 3620 |
| 375/memory.html | 60.0 → **59.8** | 16.8 → **33.3** | 369 → **63** | 0 → **0** | 2314 → 2447 |
| 375/history.html | 60.0 → **60.0** | 16.8 → **16.8** | 1664 → **181** | 0 → **0** | 483 → 489 |

### 🧪 目录测试（`build/toc_test.py`，Playwright）

- ✅ drag widens sidebar （300->420）
- ✅ width persisted to localStorage （420）
- ✅ max clamp = min(640,70vw) （640）
- ✅ min clamp = 220 （220）
- ✅ width persists across pages （220）
- ✅ keyboard arrows resize （268）
- ✅ double-click resets to 300 （300）
- ✅ 3-level numbered TOC (texts/hc) 
- ✅ expand all （0）
- ✅ collapse all (current path stays open) （[56, 56]）
- ✅ single twisty toggles 
- ✅ TOC jump lands on target despite content-visibility （top=70）
- ✅ scrollspy highlights current Q and auto-expands parents （{"href": "#q60", "open": true}）
- ✅ long titles: nowrap + ellipsis + title （{"ws": "nowrap", "to": "ellipsis", "title": true}）
- ✅ marks toggle hides marks （[True, 'none']）
- ✅ marks preference persisted 
- ✅ ☰ hides sidebar on desktop 
- ✅ mobile drawer opens 
- ✅ touch drag resizes (pointer events) （300->348）
- ✅ backdrop tap closes drawer 

## 🖍️ 标记图例

| 样式 | 含义 |
|---|---|
| 黄色高亮 | 核心词句 |
| 粗体金色 | 重点 |
| 蓝色实下划线 | 定义 / 术语 |
| 橙色波浪线 | 难点 |
| 红色虚线 | 对比 / 错误立场 |
| 红字 | 警示 |
| 青色小字 | 经文出处 |
| 提示框 💎核心 · ⚠️难点 · 🚫易错 · ✨金句（逐字原文） · 🪝记忆钩 | 每个主日与总览页 |

标记只包在样式层的 `<span>` 中，原文文字不改；可用顶栏 🖍️ 或 M 键一键隐藏。

## 📚 网站结构

| 页面 | 内容 |
|---|---|
| `index.html` | 首页：图例、全书精华（论题/金句/易错/记忆钩）、三部分比例图、52 主日问答数柱状图、圣经四幕剧、罪-恩-谢、思维导图、三大支柱、52 主日网格、学习路径 |
| `bible.html` | 圣经神学、圣约神学（桌面流程图 / 手机盟约阶梯）、八个视角、本质核心 |
| `history.html` | 三线故事线、时间线、Leaflet 地图、人物图像、区域文化 |
| `lorddays.html` | 52 主日按 17 个主题分组、筛选、进度、总表 |
| `ld/01.html … ld/52.html` | 精华速览（五问提要 · 金句 · 易错 · 关联星图）→ 原文 → 整体 → 局部 → 交叉对照 → 应用（页签）→ 记忆 → 延伸 |
| `texts/index.html` | 原文中心（v3 新增） |
| `texts/hc.html` `bc.html` `cd.html` `creeds.html` | 干净阅读版/背诵版（三级目录：部 → 主日 → 问） |
| `compare.html` | 覆盖度图（v3 新增）、总对比、为什么三份、教义矩阵、三大信经对比 |
| `memory.html` | 标记图例、数字骨架、52 口诀、129 卡片、52 测验 |
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
python3 build/perf.py URL out.json      # 性能测量
git subtree push --prefix site origin gh-pages
surge site heidelberg-catechism-52-lorddays-20261020-v3-grokser.surge.sh
netlify deploy --prod --dir site --site 22d5c459-5918-4538-83ec-156d777963e0
```

## 🗂️ 版本历史

### v3 · 2026-10-20 · [Release](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v3)
| 平台 | 链接 |
|---|---|
| GitHub Pages | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261020-v3-grokser.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261020-v3-grokser.netlify.app |

### v2 · 2026-10-20 · [Release](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v2)
| 平台 | 链接 |
|---|---|
| GitHub Pages（与 v3 同一地址，现显示 v3） | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261020-v2-grokser.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261020-v2-grokser.netlify.app |

### v1 · 2026-10-20 · [Release](https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/v1)
| 平台 | 链接 |
|---|---|
| GitHub Pages（旧仓库名，仓库更名后已失效） | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-20261020-v1-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261020-v1-grokstudy.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261020-v1-grokstudy.netlify.app |
