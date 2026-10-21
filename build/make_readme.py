import json
from common import VERSION,DATE,REPO
V=json.load(open('versions.json'))
import os
J=lambda f:json.load(open(f)) if os.path.exists(f) else {}
a=J('perf6_v5.json');b=J('perf6_v6.json')
rows=[]
for k in a:
    if k not in b: continue
    x,y=a[k],b[k]
    rows.append(f"| {k} | {x['fps']} → **{y['fps']}** | {x['p95']} → **{y['p95']}** | {x['long50']} → {y['long50']} | {x['paint_ms']} → **{y['paint_ms']}** | {x['style_ms']+x['layout_ms']} → {y['style_ms']+y['layout_ms']} | {x['dom']} → {y['dom']} |")
perf='| 设备/页面 | 滚动 FPS | p95 帧 ms | 长任务数 | 绘制 ms | 样式+布局 ms | DOM |\n|---|---|---|---|---|---|---|\n'+'\n'.join(rows)
def lht(f5,f6):
    A,B=J(f5),J(f6)
    return '| 页面 | 分数 | TBT ms | CLS | LCP ms | FCP ms |\n|---|---|---|---|---|---|\n'+'\n'.join(f"| {k} | {A[k]['score']} → **{B[k]['score']}** | {A[k]['tbt']} → **{B[k]['tbt']}** | {A[k]['cls']} → **{B[k]['cls']}** | {A[k]['lcp']} → {B[k]['lcp']} | {A[k]['fcp']} → {B[k]['fcp']} |" for k in A if k in B)
W5,W6=J('wc_v5.json').get('summary',{}),J('wc_v6.json').get('summary',{})
wct='| 范围 | v5 | v6 | 变化 |\n|---|---|---|---|\n'+f"| 52 主日解说合计 | {W5['ld_total']:,} | {W6['ld_total']:,} | {100*(W6['ld_total']-W5['ld_total'])/W5['ld_total']:+.1f}% |\n| 平均每主日 | {W5['ld_avg']:,} | {W6['ld_avg']:,} | |\n"+''.join(f"| {k} | {W5['overview'][k]:,} | {W6['overview'][k]:,} | {100*(W6['overview'][k]-W5['overview'][k])/W5['overview'][k]:+.1f}% |\n" for k in W5['overview'])+f"| 概览页合计 | {W5['overview_total']:,} | {W6['overview_total']:,} | {100*(W6['overview_total']-W5['overview_total'])/W5['overview_total']:+.1f}% |"
toc=json.load(open('toc_test_result.json'))
tt='\n'.join(f"- {'✅' if r[1] else '❌'} {r[0]} {('（'+r[2]+'）') if r[2] and len(r[2])<60 else ''}" for r in toc)
REL='https://github.com/07-Je-Grok-Love-Personal-20260928/heidelberg-catechism-52-lorddays-GROKstudy/releases/tag/'
L=lambda key:'\n'.join(f'| {t} | {u} |' for t,u in V[key])
md=f'''# heidelberg-catechism-52-lorddays-20261021-v6-GROKstudy

> 《海德堡要理问答》52 主日全景深度解析：简体中文深度学习网站，共 129 问，持守欧陆改革宗立场（三项联合信条 + 三大普世信经）。

## 🌐 当前在线访问（v6）

| 平台 | 链接 |
|---|---|
| GitHub Pages | https://07-je-grok-love-personal-20260928.github.io/heidelberg-catechism-52-lorddays-GROKstudy/ |
| Surge | https://heidelberg-catechism-52-lorddays-20261021-v6-grokstudy.surge.sh |
| Netlify | https://heidelberg-catechism-52-lorddays-20261021-v6-grokstudy.netlify.app |

📦 源码仓库：https://github.com/07-Je-Grok-Love-Personal-20260928/{REPO}
🏷️ Release：[v6]({REL}v6) · [v5]({REL}v5) · [v4]({REL}v4) · [v3]({REL}v3) · [v2]({REL}v2) · [v1]({REL}v1)

## 🆕 更新说明（v6 · {DATE}）

''' + '\n'.join(f'- {x}' for x in V['changes_v6']) + f'''

<details><summary>v5 更新说明</summary>

''' + '\n'.join(f'- {x}' for x in V['changes_v5']) + f'''

</details>

### ⚡ 流畅度对比（v5 → v6）

测量方法：`build/perf6.py`，Playwright 无头 Chromium，CDP **6 倍 CPU 降速**；`mobile` = 390×844、DPR 3、触屏仿真；`desktop2x` = 1440×900、DPR 2（模拟 Windows 高 DPI）。加载后用 rAF 记录约 4 秒连续滚动的帧时间，并从 Chrome trace 统计绘制、样式与布局耗时。两版在同一台机器、同一脚本下测得（原始数据：`build/perf6_v5.json` / `build/perf6_v6.json`）。无头测量不等于真机，但可用于同条件对比。

{perf}

### 🔦 Lighthouse（移动端预设，performance）

本地（`build/lh.py`，模拟 4× CPU + 慢速 4G，同一本地服务器）：

{lht('lh_v5.json','lh_v6.json')}

线上 Netlify（v5 站 vs v6 站）：

{lht('lh_v5_netlify.json','lh_v6_netlify.json')}

### ✂️ 提炼字数（`build/wordcount.py`，只计解说文字：汉字 + 英文词；原文问答 / 信条 / 金句不计）

{wct}

### 🧪 目录与互动测试（`build/toc_test.py`，Playwright）

{tt}

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
netlify deploy --prod --dir site --site {open('netlify_v6_id.txt').read().strip() if __import__('os').path.exists('netlify_v6_id.txt') else '<v6-site-id>'}
```

## 🗂️ 版本历史

### v6 · {DATE} · [Release]({REL}v6)
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
