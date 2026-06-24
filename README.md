# Academic Paper Review Skill 📄🔍

面向科研论文的结构化预审 Skill，用于在投稿、送导师、组会讨论或合作修改前，检查论文中的研究问题、方法、变量、证据、图表、附录和引用一致性。
本项目受到Prism的审阅论文功能启发并结合日常使用痛点，目标是提供一个开源、可检查、可修改的 Skill，用于对科研论文进行结构化预审。

它不只是做语法润色，而是帮助作者发现那些**可定位、可修改、可复核**的问题，例如：

* 研究问题和研究方法是否真正匹配；
* 变量、概念、符号、单位是否前后一致；
* 图表结果是否支撑正文解释；
* 结论是否超过数据、实验或文献能够支持的范围；
* 引用是否真正支撑当前段落的判断；
* 附录、补充材料和正文主张是否一致；
* 题目、摘要、引言、方法、结果、讨论与结论之间是否形成清晰主线。

本项目定位为一个轻量级论文质量预审工具，不替代导师、审稿人或正式 peer review，而是帮助作者在正式反馈前先完成一轮高密度自查。

---

## 🚀 快速上手

### 通用论文预审

适用于 Markdown、DOCX、PDF、LaTeX 源码和纯文本论文材料。

```text
Use $paper-review to review this manuscript and write a concise Markdown review report.
```

### Word / DOCX 论文预审

```text
Use $paper-review to review the attached DOCX manuscript.
```

### 中文审阅报告

```text
Use $paper-review to review this manuscript. Write the review in Simplified Chinese.
```

### LaTeX 专项审阅

适用于 LaTeX 源码、公式、交叉引用、引用键、编号和编译表达检查。

```text
Use $latex-paper-review to review this LaTeX manuscript and write a concise LaTeX review file.
```

### 需要外部资料核对时

默认情况下，Skill 不主动联网检索。若你希望它在必要时核对权威资料，可以明确授权：

```text
Use $paper-review to review this manuscript. If a finding depends on external literature or method norms, ask before searching authoritative sources.
```

### 复核修改稿

如果你已经有上一轮审阅报告，可以把旧 review 和修改后的论文一起提供，让 Skill 检查问题是否真的解决：

```text
Use $paper-review to recheck this revised manuscript against the previous review. Focus on resolved issues, remaining blockers, and newly introduced problems.
```

---

## 🛠️ 安装步骤

本仓库包含两个 Skill：

* `paper-review`：通用论文审阅 Skill；
* `latex-paper-review`：LaTeX 专项论文审阅 Skill。

你可以只安装其中一个，也可以同时安装两个。

### 选项 A：安装通用版

推荐大多数用户使用。支持 Markdown、DOCX、PDF、LaTeX 源码和纯文本论文材料。

```bash
git clone https://github.com/Conradgui/Academic-Paper-Review-Skill.git
cd Academic-Paper-Review-Skill

mkdir -p ~/.codex/skills
cp -R paper-review ~/.codex/skills/
```

安装后可通过以下方式调用：

```text
Use $paper-review to review this manuscript.
```

### 选项 B：安装 LaTeX 专项版

适合主要处理 LaTeX 源码、公式、引用键、交叉引用和 LaTeX review 文件的用户。

```bash
git clone https://github.com/Conradgui/Academic-Paper-Review-Skill.git
cd Academic-Paper-Review-Skill

mkdir -p ~/.codex/skills
cp -R latex-paper-review ~/.codex/skills/
```

安装后可通过以下方式调用：

```text
Use $latex-paper-review to review this LaTeX manuscript.
```

### 选项 C：同时安装两个 Skill

```bash
git clone https://github.com/Conradgui/Academic-Paper-Review-Skill.git
cd Academic-Paper-Review-Skill

mkdir -p ~/.codex/skills
cp -R paper-review ~/.codex/skills/
cp -R latex-paper-review ~/.codex/skills/
```

---

## 💡 核心检查项

### 核心审计流程

Skill 会先建立一份简短的论文理解模型，再输出审阅意见。也就是说，它会先梳理论文属于什么领域、研究问题是什么、核心概念/变量/符号是什么、方法或材料如何支撑结论，再检查证据链是否闭合。

这个流程的目的不是增加形式感，而是减少泛泛建议：审阅意见应当尽量基于论文中的具体位置、具体主张和具体证据，而不是直接输出“增强创新性”“补充文献”“优化结构”这类难以执行的结论。

### 研究问题与方法是否匹配

检查论文提出的问题，是否真的能够被当前方法、数据、实验、模型或理论分析回答。

例如：

* 研究问题过大，但方法只能回答局部问题；
* 结论使用因果表达，但研究设计只能支持相关性判断；
* 方法章节没有解释为什么适合当前研究目标；
* 研究目标、数据来源和结果解释之间没有形成闭环。

### 全文结构与叙事是否连贯

检查题目、摘要、引言、相关工作、方法、结果、讨论和结论之间是否形成清晰一致的论证路径，避免局部段落写得完整，但整篇论文主线松散或前后目标漂移。

例如：

* 摘要强调一个贡献，但正文主要讨论另一个问题；
* 引言提出的问题没有在方法或结果中被正面回答；
* 讨论部分引入新的重大判断，但前文没有提供足够铺垫；
* 结论没有回到研究问题和核心发现。

### 变量、概念与符号是否一致

检查核心概念、变量、构念、公式符号、下标、单位和术语是否在全文保持一致。

例如：

* 同一变量在正文、表格、附录中含义不同；
* 公式符号出现后没有定义；
* 图表中的变量名和正文表述不一致；
* 控制变量、参数或实验条件前后口径变化。

### 图表、正文与附录是否对齐

检查图表结果、图注、表格说明、附录推导、补充实验和正文解释之间是否互相支撑。

例如：

* 正文说结果显著，但表格中并不显著；
* 附录稳健性检验与正文结论不一致；
* 图注、表头或编号和正文引用不匹配；
* 算法说明、证明过程或数据处理细节与正文主张不一致。

### 证据链审核（Evidence Chain Review）

检查论文中的核心结论是否得到数据、图表、研究方法和参考文献的充分支撑，并识别证据不足、图文不一致、引用不匹配或结论过度延伸等问题。

### 主张强度校准

Skill 会特别检查论文中的强判断是否被证据支撑，例如“证明”“导致”“决定性影响”“完全支持”“高度稳健”“全面提升”等表达。

当问题主要来自主张过强时，报告应尽量给出可直接替换的改写建议，而不只是说“语气过强”。典型输出会围绕：

```markdown
| Claim | Evidence | Recommended Wording |
|---|---|---|
```

这适合用于摘要、假设、结果解释、讨论、政策建议和结论部分，帮助作者把“证据能支持什么”与“论文实际写了什么”对齐。

### 按论文类型调整审阅重点

Skill 会根据论文类型调整检查重点，而不是用同一套模板机械审阅所有论文。

例如：

* 实证论文更关注变量定义、测量有效性、模型设定、稳健性、异质性、机制检验、内生性、选择偏差、因果措辞和结论边界；
* 理论或数学论文更关注定义、假设、符号一致性、证明逻辑和边界条件；
* 工程或系统论文更关注实验设置、基线选择、公平比较、指标解释和复现性；
* 综述或概念论文更关注文献覆盖、分类框架、概念边界和引用支撑；
* 混合型论文会同时检查多个维度之间是否一致。

实证论文检查是增强模块，不会把 `$paper-review` 变成实证论文专用工具。只有当论文呈现变量、模型、回归、实验、稳健性检验、异质性分析、机制检验或表格结果等特征时，Skill 才会追加这些更细的审计视角。

### 结构化问题分级

审阅报告会区分问题的严重程度与确定性，帮助作者快速判断哪些问题最影响论文可信度，哪些只是表达、格式或 proofing 层面的建议。

### 复核 / 二次审阅

当用户提供旧 review、修改后的论文，或明确要求“复核”“再检查”“看是否解决上一轮问题”时，Skill 会进入二次审阅模式。

它不会简单重复上一轮 findings，而是把旧问题映射到当前稿件位置，并标记状态：

* `Resolved`：问题已解决；
* `Still Open`：问题仍然存在；
* `Downgraded`：问题有所缓解，但还没有完全解决；
* `Upgraded`：问题变得更严重，或影响了更重要的主张；
* `New`：新引入或新发现的问题；
* `Needs External Verification`：需要数据、代码、文献或额外背景才能判断。

### 防泛化审阅

Skill 会避免输出“增强创新性”“补充文献”“加强讨论”等无具体定位、无事实依据、不可执行的泛泛建议。

每条实质性问题都应尽量包含：

* 位置；
* 问题；
* 为什么重要；
* 修改建议；
* 严重程度；
* 判断确定性。

如果没有发现明确问题，应说明检查过哪些关键内容，而不是用空泛建议填充报告。

---

## 📂 两个 Skill 版本

| Skill      | 调用名                   | 适合场景                                       | 默认输出          |
| ---------- | --------------------- | ------------------------------------------ | ------------- |
| 通用论文审阅     | `$paper-review`       | Markdown、DOCX、PDF、LaTeX、纯文本论文预审            | Markdown 审阅报告 |
| LaTeX 专项审阅 | `$latex-paper-review` | LaTeX 源码、公式、交叉引用、引用键、编译表达和 LaTeX review 文件 | LaTeX 审阅文件    |

如果你不确定该用哪个，优先使用 `$paper-review`。

如果你的主要问题是 LaTeX 源码、公式表达、交叉引用、引用键或编译后的 LaTeX review 文件，再使用 `$latex-paper-review`。

LaTeX 专项版默认生成可独立编译的 LaTeX 审阅文件，适合需要保留公式、引用键、交叉引用和源码级问题定位的论文项目。

当前 LaTeX-only 版本也保留在 [`latex-paper-review`](https://github.com/Conradgui/Academic-Paper-Review-Skill/tree/latex-paper-review) 分支中，方便需要历史快照的用户查看。

---

## 📥 输入形式说明

通用版 `$paper-review` 支持：

* Markdown (`.md`)
* Word (`.docx`)
* PDF (`.pdf`)
* LaTeX 源码 (`.tex`)
* 纯文本 (`.txt`)
* 多文件项目或论文材料包

输入越完整，审阅越可靠。对于多文件论文，建议提供正文、附录、图表说明、参考文献、补充材料和相关说明。

若只提供 PDF，Skill 仍可审阅可见内容，但对源码结构、隐藏批注、交叉引用、宏定义和编译问题的判断会受到限制。

对于 DOCX，Skill 与内置 Proofing 脚本支持正文、页眉、页脚、脚注与尾注的文本提取。但 DOCX 文本提取主要用于轻量级文本审阅和 Proofing 扫描，无法完整保留批注、修订痕迹、文本框、复杂表格结构以及高级 Word 样式。

---

## 🔬 本地 Proofing 扫描工具

两个 Skill 都包含一个轻量脚本：

```text
scripts/proofing_scan.py
```

它用于扫描一些高置信、低成本但容易遗漏的问题，原生支持：

* PDF (`.pdf`)
* Word (`.docx`)
* Markdown (`.md`)
* LaTeX (`.tex`)
* TXT (`.txt`)

可以扫描的问题包括：

* 重复标点：`, ,`、`,,`、`..`
* 引号附近的异常标点
* `javascript`、`ios`、`iphone` 等大小写问题
* `arctan(x/y)` 这类可能存在象限或分支歧义的表达
* 推导文字中常见的异常表达模式
* 中文论文中可能过强的候选措辞，例如“证明”“导致”“完全支持”“高度稳健”“全面提升”“显著正相关”与“边界证据”混用等

### 扫描 PDF 文件

```bash
python3 paper-review/scripts/proofing_scan.py path/to/manuscript.pdf --max-hits 80
```

### 扫描 Word 文件

```bash
python3 paper-review/scripts/proofing_scan.py path/to/manuscript.docx
```

DOCX 扫描会尝试解析正文、页眉、页脚、脚注和尾注中的文本。

### 扫描 Markdown 文件

```bash
python3 paper-review/scripts/proofing_scan.py path/to/manuscript.md
```

脚本输出只是候选风险线索，不能自动判定论文错误。作者或 AI 仍需要结合上下文 spot-check，确认该表达是否真的过强、不一致或容易误导，再写入审阅意见。

---

## 🛡️ 隐私保护与外部检索策略

默认情况下，Skill 不会主动联网检索。

原因很直接：

* 未发表论文、课程论文、组内初稿和合作稿可能包含敏感信息；
* 外部资料质量参差不齐，错误资料会污染审阅判断；
* 很多问题可以先通过论文内部一致性检查发现。

当审阅需要判断领域背景、经典理论、方法规范、事实性声明或引用支撑时，Skill 可以建议用户授权检索。

授权后应优先使用：

* 论文原文引用；
* 官方机构或标准文件；
* 教材、手册、方法论文；
* 顶级期刊、会议或领域权威综述；
* 可核查的 DOI、出版社页面或学术数据库页面。

博客、营销文章、论坛回答和无来源摘要只能作为线索，不能作为学术证据或错误判定依据。

外部资料只能用于增强判断或标注“需要核查”，不能把未验证内容说成确定错误。

---

## 🧾 输出行为

默认情况下，Skill 只生成审阅报告，不直接修改原稿。只有在用户明确要求 revision、inline edits 或改写时，才会进入修改模式。

通用版会生成 Markdown 审阅报告：

```text
paper-reviews/review-YYYY-MM-DD-HHMMSS.md
```

审阅内容会优先覆盖：

* 研究问题、方法、变量、证据和结论之间的一致性；
* 题目、摘要、引言、方法、结果、讨论和结论之间的叙事连贯性；
* 数学、公式、符号、单位、定义、算法和实现表达；
* 图表、附录、引用和正文主张之间的支撑关系；
* 有明确价值的写作和 proofing 问题。

如果论文没有发现明确技术或证据问题，Skill 应说明它检查过哪些关键内容，而不是用泛泛建议填充报告。

### Action Plan / 修改行动表

当报告中存在具体可执行问题时，末尾会附上一张修改行动表，帮助作者把审阅意见转成下一步修改任务：

```markdown
| 优先级 | 问题 | 修改类型 | 建议修改位置 | 是否阻塞提交 |
|---|---|---|---|---|
```

字段含义如下：

* `优先级`：`P0 / P1 / P2`
  * `P0`：必须优先处理，可能影响论文可信度或提交质量；
  * `P1`：建议处理，会明显提升论文质量；
  * `P2`：有空再处理，主要是局部优化。
* `问题`：一句话说明要解决什么。
* `修改类型`：说明这属于哪类修改，例如 `主张强度校准`、`变量定义补充`、`表文一致性`、`方法说明补充`、`文献支撑补充`、`结构调整`、`表达澄清`、`格式/引用修正`、`需外部核查`。
* `建议修改位置`：告诉作者去哪里改，例如 `摘要`、`引言第 3 段`、`变量定义小节`、`表 4 后正文解释`、`稳健性检验部分`、`结论第一段`、`附录 A`、`参考文献列表`。
* `是否阻塞提交`：`是 / 否 / 取决于要求`
  * `是`：不改会明显影响提交质量；
  * `否`：不影响基本提交，但建议优化；
  * `取决于要求`：要看导师、期刊、课程或答辩标准。

如果没有真实可执行的问题，Skill 不应为了填表硬凑条目。

---

## 📁 项目结构

```text
paper-review/
  SKILL.md                    # 通用科研论文审阅 Skill
  agents/openai.yaml          # Codex UI 元数据
  references/review-rubric.md # 可选审阅检查表
  scripts/proofing_scan.py    # 高置信 proofing 扫描脚本

latex-paper-review/
  SKILL.md                    # LaTeX 专项论文审阅 Skill
  agents/openai.yaml
  references/review-rubric.md
  scripts/proofing_scan.py

_project-records/
  plan-2026-06-23.md
  plan-2026-06-24-generalization.md
```

---

## 👥 适合谁

* 正在写科研论文的学生和研究者；
* 使用 Markdown、DOCX、PDF 或 LaTeX 管理论文草稿的作者；
* 投稿前想做系统自查的作者；
* 希望减少基础反馈成本的导师或课题组；
* 多人合作论文中需要统一变量、图表、附录、引用和结论口径的团队；
* 正在学习和探索 Skill 结构和工作流设计的人。

---

## 🚧 边界与限制

`paper-review` 不能替代正式 peer review，也不能替代导师、审稿人或领域专家的最终判断。

它不保证发现所有数学、计量、理论或领域问题，尤其是高度专业、依赖外部文献或深层背景知识的错误。

它也不是单纯 grammar checker，不是只把句子改得更“学术”，更不是一键投稿工具。

更合理的使用方式是：把它作为论文写作流程中的前置质量控制环节。作者仍然需要判断、取舍和修改。

---

## License

MIT License. See [LICENSE](LICENSE).
