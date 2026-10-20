# heidelberg-catechism-52-lorddays-20261020-v2-GROKstudy

> 《海德堡要理问答》52 主日全景深度解析：简体中文深度学习网站，共 129 问，持守欧陆改革宗立场（三项联合信条 + 三大普世信经）。

## 🌐 当前在线访问（v2）

| 平台 | 链接 |
|---|---|
| GitHub Pages | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261020-v2-grokser.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261020-v2-grokser.netlify.app |

📦 源码仓库：https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy

## 🆕 更新说明（v2 · 2026-10-20）

- 📱 手机端圣约神学流程图改为竖排“盟约阶梯”，平板与桌面仍显示 Mermaid 流程图；其余流程图在手机上按原始比例横向滑动，文字清晰。
- 🪔 52 个主日全部新增“深化”板块：一个圣经画面、如何指向基督、一句祷告、两道小组/家庭讨论题（共 208 条新内容）。
- 🔎 新增全文搜索页：129 问、37 条比利时信条、多特信经全部条文、三大信经与 52 篇解读，可按类别筛选并高亮关键词。
- 🆕 新增版本徽章（顶栏）与本更新记录页。
- ⚡ 性能：脚本 defer；Mermaid 只在图表接近可视区时才加载；地图库 Leaflet 改为按需加载；手机端减少毛玻璃模糊层以提升滚动流畅度；长列表卡片使用 content-visibility；图片标注尺寸并懒加载。
- 🎨 主题在页面渲染前即应用（无闪烁）；表格首列不折行；打印样式优化。
- 🏷️ 仓库更名为 heidelberg-catechism-52-lorddays-GROKstudy（保留全部历史），GitHub Pages 地址随之更新；全站只用相对路径。
- ✅ 原文逐字校验仍为 0 处差异；375 / 768 / 1440 三种宽度的溢出检测重新跑过；截图全部重拍。

## 📚 网站结构

| 页面 | 内容 |
|---|---|
| `index.html` | 首页：圣经四幕剧、罪-恩-谢三重结构、可点击思维导图、52 主日颜色网格、学习路径 |
| `bible.html` | 整本圣经（圣经神学）、圣约神学流程图、八个视角、本质核心 |
| `history.html` | 故事线流程图、1386–2015 时间线、Leaflet 交互地图（17 个地点 + 3 条路线）、人物图像、文化区域特征 |
| `lorddays.html` | 52 主日总览：筛选、搜索、学习进度、总表 |
| `ld/01.html … ld/52.html` | 每主日：原文问答（一字不改）、逻辑链、圣经整体视角、圣约视角、真实背景、核心要点、难点、驳斥的错误、比利时信条/多特信经原文交叉对照、威斯敏斯特对照、应用、翻转卡片、小测验、ccifellowship 证道链接 |
| `texts/hc.html` `texts/bc.html` `texts/cd.html` `texts/creeds.html` | 干净阅读版/背诵版：海德堡要理问答、比利时信条、多特信经（含错谬反驳）、三大普世信经 |
| `compare.html` | 三项联合信条深度对比、为什么三份而不是一份、教义矩阵、三大信经对比 |
| `memory.html` | 速记中心：数字骨架、52 口诀、129 张卡片、52 题测验 |
| `sources.html` | 资料来源、原文校验方法、图片致谢 |
| `search.html` | 全文搜索：信条、信经原文与本站解读（v2 新增） |
| `changelog.html` | 版本更新记录（v2 新增） |

功能：毛玻璃 UI、深/浅色、可隐藏目录（T 键）、背诵模式（R 键）、脚注开关、中文语音朗读、学习进度（本地保存）、←/→ 切换主日、全响应式（手机/平板/桌面）。

## ✅ 原文来源与校验

- 三项联合信条与三大普世信经的全部中文原文均由程序抓取自 https://ccifellowship.org/books/book-of-praise （《中国改革宗敬拜手册》2015），提取到 `data.json` 后生成页面，未做任何文字改动。
- `build/verify_verbatim.py` 将站内全部 2094 个原文块与抓取到的原网页逐字比对：0 处不一致（v2 重新校验）。
- `build/layout_check.py` 和 `build/layout_all_ld.py` 在 375、768、1440 三种宽度下检测溢出：0 个问题（v2 重新检测）。
- ccifellowship.org 未收录多特信经的“结论”部分，本站也没有收录。原文版权归《中国改革宗敬拜手册》出版委员会所有，本站仅作学习引用，并逐条注明出处。

## 🛠️ 构建与部署

```bash
python3 src/crawl.py && python3 src/extract.py   # 抓取并提取原文（在 src/ 目录下运行）
bash build/build_all.sh                          # 生成 site/
python3 build/verify_verbatim.py                 # 逐字校验
python3 build/layout_check.py                    # 布局溢出检测（需本地 http://localhost:8765）
git subtree push --prefix site origin gh-pages   # GitHub Pages
surge site heidelberg-catechism-52-lorddays-20261020-v2-grokser.surge.sh
netlify deploy --prod --dir site --site 63dd7379-0a1f-4f0a-aadb-7d6460e10fe0
```

## 🗂️ 版本历史

### v2 · 2026-10-20
| 平台 | 链接 |
|---|---|
| GitHub Pages | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261020-v2-grokser.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261020-v2-grokser.netlify.app |

变更：见上方“更新说明”。仓库由 `heidelberg-catechism-52-lorddays-20261020-v1-GROKstudy` 更名为 `heidelberg-catechism-52-lorddays-GROKstudy`（保留全部历史）。

### v1 · 2026-10-20
| 平台 | 链接 |
|---|---|
| GitHub Pages（旧仓库名，仓库更名后已失效） | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-20261020-v1-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261020-v1-grokstudy.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261020-v1-grokstudy.netlify.app |

首版：52 主日深度解析、全文阅读/背诵版、圣经与圣约、历史地理、信条对比、速记中心。v1 的 Surge 和 Netlify 部署保留未动；v1 的 GitHub Pages 地址因仓库更名而失效。
