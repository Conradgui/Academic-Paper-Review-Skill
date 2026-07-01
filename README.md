# Academic Paper Review Skill

面向科研论文的结构化预审与受保护润色 Skill。它不是只改语法，而是在投稿、送导师、组会讨论或合作修改前，帮助作者系统检查论文的科学可信度、证据链和文本质量。

通用版 `$paper-review` 默认执行两条并列审阅线：

- **Scientific Review / 科学性审阅**：检查研究问题、方法、变量或概念、证据、图表、附录、引用和结论边界。
- **Text Quality Review / 文本质量审阅**：检查清晰度、术语、冗余、段落衔接、语体和稿件文风一致性，并包含 AI 痕迹候选审阅子模块。

两条审阅线写入同一份报告，但默认只审阅、不修改原稿。只有用户明确要求润色或改写时，Skill 才会创建新副本。

支持 Markdown、DOCX、PDF、LaTeX 源码和纯文本。主要面向中文用户，默认报告语言为简体中文；论文原稿可以是中文、英文或中英混合文本。

## 为什么使用它

普通语言润色容易把重点放在句子是否流畅，却忽略更影响论文可信度的问题，例如：

- 研究问题与方法并不匹配；
- 变量、概念、符号、单位或样本口径前后不一致；
- 图表和附录并不支持正文中的解释；
- 相关性证据被写成因果结论；
- 引用没有真正支撑当前主张；
- 摘要、正文和结论对研究贡献的表述互相偏离；
- 文本出现模板化衔接、重复解释、术语漂移或聊天残留。

`$paper-review` 会先建立论文理解模型，再输出有位置、有证据、有严重度、有确定性和可执行动作的 findings，避免用“增强创新性”“补充文献”“优化结构”等泛泛建议填充报告。

## 快速开始

### 通用论文预审

```text
Use $paper-review to review this manuscript and write a concise Markdown review report in Simplified Chinese.
```

### Word / DOCX 论文预审

```text
Use $paper-review to review the attached DOCX manuscript. Do not modify the source file.
```

### 详细 AI 痕迹候选审阅

所有论文都会接受默认轻量扫描；用户明确要求时，Skill 才输出包含成立问题和反误伤结论的详细候选矩阵：

```text
Use $paper-review to perform a detailed AI-trace candidate audit. List both confirmed and contextually acceptable candidates, inspect underlying evidence and citation risks, and do not infer authorship or output an AI probability.
```

### LaTeX 专项审阅

当主要目标是检查 LaTeX 源码、公式表达、引用键、交叉引用、编号和编译表达时，使用专项版：

```text
Use $latex-paper-review to review this LaTeX manuscript and write a concise LaTeX review file.
```

### 复核修改稿

同时提供上一轮 review 和修改后的论文：

```text
Use $paper-review to recheck this revised manuscript against the previous review. Preserve prior finding IDs, report the mandatory status matrix, and focus on unresolved, changed, and new issues.
```

### 按 finding 局部润色

```text
Use $paper-review to polish finding S-01 only. Preserve all facts, terminology, data, citations, equations, and claim strength. Use my confirmed writing sample if provided; otherwise preserve the manuscript's established register and state that limitation.
```

### 章节润色

```text
Use $paper-review to polish the Discussion section only. Preserve the evidence, citations, terminology, and conclusion boundaries, and write the result to a new file.
```

### 全文受保护润色

```text
Use $paper-review to polish this manuscript section by section. Do not overwrite the source. Create a new copy and a Markdown change report, preserving all facts, numbers, variables, equations, citations, labels, and claim boundaries.
```

### 授权外部资料核查

默认不联网。只有用户明确授权后，Skill 才能检索外部资料：

```text
Use $paper-review to review this manuscript. I authorize external research when a finding depends on literature, method norms, or factual verification. Use anonymized queries and cite authoritative sources.
```

## 工作方式

### 1. 建立论文理解模型

Skill 会先梳理：

- 论文所属领域、类型和主要受众；
- 研究问题、核心主张和预期贡献；
- 变量、概念、构念、符号、参数或系统模块；
- 变量关系、逻辑依赖、理论机制或数学关系；
- 数据、材料、实验、模型、证明或综述框架；
- 主要结论及其证据来源。

这份模型用于后续审计，不会为了展示流程而机械写入最终报告。

### 2. 执行通用核心审计

所有论文都必须经过以下检查：

1. 研究问题是否明确，正文是否持续回答它；
2. 核心概念、变量、符号或构念是否定义清楚并保持一致；
3. 主张是否得到方法、数据、图表、推导、引用或附录支持；
4. 研究方法是否能够回答研究问题；
5. 题目、摘要、引言、方法、结果、讨论和结论是否形成连贯主线；
6. 图表、公式、附录、引用和补充材料是否与正文一致；
7. 因果措辞、结论、政策建议和外部有效性是否超过证据边界；
8. 重要问题是否被转化为可执行的修改行动表。

这里的“变量”是广义概念：实证论文对应变量与指标，理论论文对应概念与命题，数学论文对应符号与定理条件，系统论文对应模块、输入输出与指标，综述论文对应分类维度与概念边界。

### 3. 按论文类型追加增强审计

- **实证论文**：变量测量、模型设定、样本与缺失值、效应量与不确定性、稳健性、异质性、机制检验、内生性、选择偏差、因果语言和政策建议边界。
- **理论或数学论文**：定义、假设、符号、边界条件、命题、证明步骤、量纲、符号、分支和推导一致性。
- **工程或系统论文**：任务定义、基线公平性、实验设置、指标解释、消融、复现性和结论与结果的匹配。
- **综述或概念论文**：检索与纳入边界、文献代表性、分类框架、概念边界、引用支撑和综合分析质量。
- **混合型论文**：同时检查各方法模块之间是否共享一致的研究问题、样本口径和结论边界。

实证论文协议是条件增强模块，不会把项目改造成实证论文专用工具。

### 4. 检查常见论文写作问题

除论文类型特有问题外，Skill 还会检查：摘要与正文不一致、引言缺少明确研究缺口、文献综述逐篇罗列、方法缺少数据或材料来源、结果只报告显著性、讨论把解释写成事实、局限性空泛，以及结论引入新证据。伦理审批、知情同意、利益冲突、资金来源和数据或代码可用性声明只在研究类型或提交要求适用时检查。

## 文本质量审阅

文本质量审阅不会替代科学性审阅，也不会为了“更像人工写作”而强制使用生僻词、制造句长波动、加入个人观点或写不完整句。

默认先执行轻量检查：

- 清晰度、歧义和句子过载；
- 术语、缩写、变量名和符号稳定性；
- 人称、时态、语体和主张语气；
- 段落功能、重复解释和逻辑推进；
- 无理由的持续文风漂移；
- 聊天残留、占位符和异常引用标记。

若只有孤立且不影响理解的小问题，报告用一句话提示，**轻量观察不分配 `T-*`**，不生成详细表格，也不进入修改行动表。

只有问题跨多个段落反复出现、影响摘要或结论等核心位置、造成术语或语义歧义、出现明显语体断裂，或用户明确要求语言审阅时，才触发详细文本质量报告，并使用 `T-01`、`T-02` 等编号。

Methods 与 Discussion 本来就承担不同写作任务；章节之间的合理语体差异不会被机械判为文风不一致。

### AI 痕迹候选审阅

这项能力属于文本质量审阅子模块，不是第三条审阅线，也不是 AI 检测器。

- **默认轻量扫描**：检查工具污染、空泛重要性、模糊归因、低信息分析、机械结构和持续文风漂移；没有材料级问题时只输出一句结论。
- **用户明确要求**：输出详细候选矩阵，同时列出成立的问题和 `Contextually Acceptable` 的反误伤结论。
- **高风险自动展开**：聊天残留、占位符、异常工具标记，或影响核心主张、证据、引用和术语的候选，会触发详细核验。

固定核验顺序为：表面候选、上下文功能、具体性、证据或引用、章节适配、最终判断。单个词、一次被动语态、破折号、副词或三项并列都不能单独构成问题。

详细矩阵使用：

```markdown
| Candidate ID | 位置 | 可观察模式 | 原文证据 | 深层核验 | 结论 | 修改方向 |
|---|---|---|---|---|---|---|
```

结论固定为 `Confirmed Text Issue`、`Source Integrity Risk`、`Contextually Acceptable` 或 `Needs Verification`。成立的表达问题提升为 `T-*` finding；证据或引用风险提升为 `S-*` finding；语境合理的候选不进入修改行动表。

Skill **不判断作者身份**、**不输出 AI 概率**或检测器分数，也不以规避检测器为修改目标。

## 报告与判断规则

### Findings

科学性 findings 使用 `S-01`、`S-02` 等编号；材料级文本质量 findings 使用 `T-01`、`T-02` 等编号。每条实质性 finding 应尽量包含：

- 位置；
- 问题与稿内证据；
- 为什么重要；
- `Revision guidance / 修改指导`；
- 严重程度；
- 判断确定性。

默认提供修改目标、必须保留的信息、建议动作和必要的短语级选项，不直接生成可复制的完整段落。用户点名 finding、段落或章节后，才进入改写流程。

### 严重程度

| 等级 | 含义 |
|---|---|
| Critical | 威胁论文主要结论或整体有效性的事实、逻辑或方法问题 |
| Major | 明显削弱结果可信度、证据链或可复核性的问题 |
| Minor | 局部影响清晰度、一致性或专业性的错误 |
| Writing Suggestion | 不影响科学结论的表达优化建议 |

### 判断确定性

| 标签 | 含义 |
|---|---|
| 确定错误 | 可由稿件内部内容、数学或明确逻辑直接证伪 |
| 证据不足 | 主张强于稿件现有数据、结果或引用能够支持的范围 |
| 疑似问题 | 高概率存在问题，但仅凭当前材料不能完全确认 |
| 需核对/确认 | 依赖外部文献、数据、代码或领域背景才能判断 |

### 主张强度校准

Skill 会检查“证明”“导致”“决定性影响”“完全支持”“高度稳健”“全面提升”等强表述。若证据只能支持相关性、边界证据或线索性发现，报告会按 `Claim -> Evidence -> Calibrated Level -> Minimal Phrase Options` 给出校准方向，而不是默认代写整句。

### 修改行动表

有真实可执行问题时，报告末尾使用：

```markdown
| 优先级 | 问题 | 修改类型 | 建议修改位置 | 是否阻塞提交 |
|---|---|---|---|---|
```

- `优先级`：`P0` 可能影响可信度或提交质量；`P1` 会明显提升论文质量；`P2` 为局部优化。
- `问题`：一句话说明需要解决什么。
- `修改类型`：例如 `主张强度校准`、`变量定义补充`、`表文一致性`、`方法说明补充`、`文献支撑补充`、`结构调整`、`表达澄清`、`文本清晰度`、`文风一致性`、`冗余压缩`、`作者化润色`、`格式/引用修正`、`需外部核查`。
- `建议修改位置`：例如 `摘要`、`引言第 3 段`、`变量定义小节`、`表 4 后正文解释`、`结论第一段` 或 `附录 A`。
- `是否阻塞提交`：`是 / 否 / 取决于要求`。

Skill 不会为了填表硬凑条目。`P0/P1/P2` 是修改优先级，不是 finding ID 或严重程度。

## 复核 / Delta Review

当用户提供旧 review 与修改稿，或明确要求“复核”“再检查”“看上一轮问题是否解决”时，Skill 会逐条映射旧 finding，而不是重新生成一份与上一轮脱节的报告。

复核状态使用以下精确 token：

- `Resolved`
- `Still Open`
- `Downgraded`
- `Upgraded`
- `New`
- `Needs External Verification`

`The status matrix is mandatory`：状态矩阵为必选输出，至少包含原 Finding ID、当前位置、状态、证据变化和下一步动作。映射到旧问题时保留原 ID；只有真正的新问题才新建后续 `S-*` 或 `T-*`。所有未关闭项必须进入修改行动表。

## 受保护润色

润色必须由用户明确触发，且始终以语义保真为第一优先级。

文风基线优先级为：

1. 用户明确提供并确认的本人写作样本，称为“作者文风基线”；
2. 论文中风格稳定且未被标记的问题段落，称为“论文一致性基线”；
3. 无可靠样本时使用中性学术语体，并明确说明限制。

Skill 不会把论文内部风格自动声称为作者个人文风。

全文润色按章节处理：先建立术语、变量、数字、公式、引用、图表编号和主张边界账本；逐章修改并核对；最后执行跨章节一致性复核。输出写入：

```text
paper-revisions/<原文件名>-polished-<timestamp>.<ext>
paper-revisions/<原文件名>-polish-report-<timestamp>.md
```

原稿不得被覆盖。

### 格式边界

| 输入格式 | 审阅 | 受保护润色 |
|---|---|---|
| Markdown / TXT | 支持 | 生成新副本和修改报告 |
| LaTeX | 支持；源码级问题可使用专项版 | 生成新副本并保留命令、标签、引用键和数学环境 |
| DOCX | 支持可提取内容 | **只有在具备可用的 DOCX 编辑与渲染核验工具时**才生成 DOCX 副本；否则输出结构化修改文本或请求其他可编辑源 |
| PDF | 审阅可见内容 | 不直接进行保真全文润色；需提供可编辑源 |

即使成功生成 DOCX，批注、修订痕迹、文本框、域代码、复杂表格和高级样式仍需要人工核验。PDF 对隐藏批注、宏定义、源码交叉引用和复杂阅读顺序的判断存在限制。

## 输出目录

默认审阅报告写入：

```text
paper-reviews/review-YYYY-MM-DD-HHMMSS.md
```

`paper-reviews/` 和 `paper-revisions/` **只允许存放面向用户的最终交付物**。计划、草稿、运行日志、评测事件和临时文件不得写入这两个目录。

如果没有发现明确问题，报告应说明已检查的关键维度并直接给出结论，不用泛泛建议填充篇幅。

## 隐私与外部检索

默认不主动联网，原因包括未发表论文的隐私风险和外部资料质量不稳定。

在未获得明确授权时：

- 不上传论文全文、标题、作者姓名或敏感数据；
- 无法仅凭稿件判断的问题标记为 `Needs External Verification`；
- 可以说明需要核查什么，但不得自行联网。

获得授权后，优先使用论文原文引用、官方机构或标准、同行评议论文、权威教材或手册、顶级期刊或会议、领域权威综述和可核查的 DOI 或出版社页面。预印本和高质量技术材料可作为补充；博客、营销文章、论坛回答和无来源摘要只能作为检索线索，不能作为强证据。

对于未发表论文，应使用匿名化关键词检索，不提交全文或可识别的敏感片段。

## 两个 Skill 版本

| Skill | 调用名 | 适合场景 | 默认输出 |
|---|---|---|---|
| 通用论文审阅 | `$paper-review` | Markdown、DOCX、PDF、LaTeX、纯文本；科学性与文本质量双线审阅 | Markdown 审阅报告 |
| LaTeX 专项审阅 | `$latex-paper-review` | LaTeX 源码、公式、引用键、交叉引用、编号、编译表达 | LaTeX 审阅文件 |

不确定时优先使用 `$paper-review`。两个 Skill 的目录名和 frontmatter `name` 不同，可以同时安装。

LaTeX 专项历史快照保留在 [`latex-paper-review` 分支](https://github.com/Conradgui/Academic-Paper-Review-Skill/tree/latex-paper-review)。本轮通用版升级不会修改该专项目录或历史分支。

## 安装

### 通用版

```bash
git clone https://github.com/Conradgui/Academic-Paper-Review-Skill.git
cd Academic-Paper-Review-Skill
mkdir -p ~/.codex/skills
cp -R paper-review ~/.codex/skills/
```

### LaTeX 专项版

```bash
git clone https://github.com/Conradgui/Academic-Paper-Review-Skill.git
cd Academic-Paper-Review-Skill
mkdir -p ~/.codex/skills
cp -R latex-paper-review ~/.codex/skills/
```

也可以从同一次 clone 中复制两个目录。安装后重启 Codex，使 Skill 重新载入。

更新已有安装时，应以完整目录替换已有同名 Skill，不要把新目录嵌套进旧目录；若本地改过 Skill，先备份自定义内容。

## 本地 Proofing 扫描器

两个 Skill 都带有 `scripts/proofing_scan.py`，但功能版本并不相同：

- **通用版扫描器**包含基础 proofing、中文过强主张候选、聊天残留、未填写占位符、异常 AI 引用标记、泄漏的工具元数据和明确的 AI 工具追踪参数，以及更严格的 PDF/DOCX 错误处理和邻近候选降噪。
- **LaTeX 专项版保留原有基础扫描器**，用于历史专项流程；若需要新增候选规则和更严格的文件错误处理，应运行通用版脚本。

通用版支持 PDF、DOCX、Markdown、LaTeX 和 TXT：

```bash
python3 paper-review/scripts/proofing_scan.py path/to/manuscript.pdf --max-hits 80
python3 paper-review/scripts/proofing_scan.py path/to/manuscript.docx
python3 paper-review/scripts/proofing_scan.py path/to/manuscript.md
```

扫描候选包括重复标点、异常引号标点、常见大小写问题、可能存在分支歧义的 `arctan(x/y)`、中文过强表述、聊天残留、占位符、异常引用标记、`attributableIndex`、`:::writing` 和明确的 AI 工具追踪参数。

PDF 扫描需要本地 Python 环境提供 `pypdf`，脚本不会自动安装依赖。扫描版或无法提取文本的 PDF 需要先 OCR，或改用可编辑源。

扫描结果只是候选风险线索，不能自动判定论文错误。AI 或作者必须结合上下文 spot-check 后，才能把命中项写入审阅报告。

## 验证状态

仓库包含静态契约测试、Proofing 回归测试和可选的独立 Codex 前向评测。

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" paper-review
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" latex-paper-review
PYTHONPYCACHEPREFIX=/tmp/paper-review-pycache python3 -m py_compile paper-review/scripts/proofing_scan.py
PYTHONPYCACHEPREFIX=/tmp/paper-review-tests python3 -m unittest discover -s tests -v
```

截至 2026-06-30，两个 Skill validator、Python 编译和 25 项本地测试通过。基础隔离前向评测中，**4/4 个用例、47/47 项断言通过**，覆盖：

- 干净理论稿的轻量文本结论；
- 严重实证与文本问题的双线详细审阅；
- 保留旧 finding ID 的 Delta Review；
- 无作者样本时的 Markdown 全文受保护润色。

本轮 AI 痕迹候选审阅使用更新后的同一 Skill 哈希追加了 **2/2 个用例、28/28 项断言**：

- 默认轻量扫描保留正常 Methods 被动语态、副词、破折号和三项并列，不生成候选矩阵或 `T-*` finding；
- 显式详细审阅输出成立与 `Contextually Acceptable` 候选，把来源风险提升为 `S-*`，且不输出作者身份或概率判断。

前向评测使用临时 `CODEX_HOME`、当前仓库 Skill 的精确副本和合成论文，不读取私人稿件。完整证据见 [`_project-records/forward-eval-summary-2026-06-29.md`](_project-records/forward-eval-summary-2026-06-29.md)、[`_project-records/forward-eval-summary-2026-06-30-ai-trace.md`](_project-records/forward-eval-summary-2026-06-30-ai-trace.md) 和 [`tests/forward/README.md`](tests/forward/README.md)。

需要注意：这些都是**合成任务的单次独立运行**，用于验证核心路径能否工作，不是统计稳定性 Benchmark，也**不能外推到所有学科**、模型版本、超长论文或复杂文档。

## 项目结构

```text
paper-review/                 # 通用 Skill
  SKILL.md
  agents/openai.yaml
  references/
  scripts/proofing_scan.py

latex-paper-review/           # LaTeX 专项 Skill
  SKILL.md
  agents/openai.yaml
  references/
  scripts/proofing_scan.py

tests/
  test_proofing_scan.py       # 扫描器回归测试
  test_skill_contract.py      # Skill 与公开文档契约测试
  forward/                    # 隔离 Codex 前向评测及合成夹具

_project-records/             # 计划、审计、执行记录和评测汇总
```

## 边界与限制

- 不能替代导师、审稿人、领域专家或正式 peer review。
- 不保证发现所有数学、计量、理论、引用或领域错误。
- 不保证从 PDF、复杂 DOCX 或多文件项目中完整恢复所有结构和格式。
- 不对文本作者身份或生成来源作判断，也不输出概率分数。
- 润色不能替代作者判断；修改稿仍需重新核对事实、数据、公式、引用和结论边界。
- 外部资料只能增强判断，不能把未经验证的内容包装成确定错误。

## 参考与启发

科学性审查基于Open AI旗下Prism平台“审阅论文”功能以及各开源项目的公开思路进行优化迭代。
文本质量和受保护润色流程参考了以下开源项目的公开思路，并针对科研论文场景独立重写：
- [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)：论证优先、术语约束、章节化润色和局部修订。
- [blader/humanizer](https://github.com/blader/humanizer)：模板化表达诊断和写作样本校准。
- [Aboudjem/humanizer-skill](https://github.com/Aboudjem/humanizer-skill)：检测、改写和复核的分阶段流程。
- [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh)：中文表达风险样本。
- [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)：候选模式、误报警告和“表面线索不等于深层问题”的审阅边界。
- [Wikipedia:WikiProject AI Cleanup/Guide](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup/Guide)：从表面痕迹继续核验来源、事实和引用完整性的处理原则。
- [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)：具体化、减少低信息铺垫和机械结构的参考；本项目不采用其词汇、语法和句式硬禁令。

本项目不直接复制第三方大段规则或示例，不以任何文本检测器分数作为成功标准。科学含义、证据边界、术语和作者明确表达的研究意图始终优先。

## License

MIT License. See [LICENSE](LICENSE).
