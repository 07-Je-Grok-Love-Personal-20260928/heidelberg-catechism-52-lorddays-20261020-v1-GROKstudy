import json
from common import VERSION,DATE,REPO
V=json.load(open('versions.json'))
a=json.load(open('perf_v2.json'));b=json.load(open('perf_v3.json'))
rows=[]
for k in a:
    x,y=a[k],b[k]
    rows.append(f"| {k} | {x['fps']} → **{y['fps']}** | {x['maxframe']} → **{y['maxframe']}** | {x['lt_load']} → **{y['lt_load']}** | {x['lt_scroll']} → **{y['lt_scroll']}** | {x['dom']} → {y['dom']} |")
perf='| 宽度/页面 | 滚动 FPS | 最长帧 ms | 加载长任务 ms | 滚动长任务 ms | DOM 节点 |\n|---|---|---|---|---|---|\n'+'\n'.join(rows)
toc=json.load(open('toc_test_result.json'))
tt='\n'.join(f"- {'✅' if r[1] else '❌'} {r[0]} {('（'+r[2]+'）') if r[2] and len(r[2])<60 else ''}" for r in toc)
REL='https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/'
L=lambda key:'\n'.join(f'| {t} | {u} |' for t,u in V[key])
md=f'''# heidelberg-catechism-52-lorddays-20261020-v3-GROKstudy

> 《海德堡要理问答》52 主日全景深度解析：简体中文深度学习网站，共 129 问，持守欧陆改革宗立场（三项联合信条 + 三大普世信经）。

## 🌐 当前在线访问（v3）

| 平台 | 链接 |
|---|---|
| GitHub Pages | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261020-v3-grokser.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261020-v3-grokser.netlify.app |

📦 源码仓库：https://github.com/07-Je-Grok-Love-Personal-20260928/{REPO}
🏷️ Release：[v3]({REL}v3) · [v2]({REL}v2) · [v1]({REL}v1)

## 🆕 更新说明（v3 · {DATE}）

''' + '\n'.join(f'- {x}' for x in V['changes_v3']) + f'''

### ⚡ 性能对比（v2 → v3）

测量方法：`build/perf.py`，Playwright 无头 Chromium，CDP 模拟 **4 倍 CPU 降速**，页面加载后以 rAF 记录 4 秒自动滚动的帧时间，并用 PerformanceObserver 统计长任务（>50 ms）。两版在同一台机器、同一脚本下测得（原始数据：`build/perf_v2.json`、`build/perf_v3.json`）。无头环境数字只用于前后对比，不等同于真机体验。

{perf}

### 🧪 目录测试（`build/toc_test.py`，Playwright）

{tt}

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

### v3 · {DATE} · [Release]({REL}v3)
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
