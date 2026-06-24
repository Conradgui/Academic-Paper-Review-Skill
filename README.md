# Academic Paper Review Skill

面向科研论文的结构化 AI 预审 Skill。它不局限于 LaTeX，也适用于 Markdown、DOCX、PDF、LaTeX 源码和纯文本论文材料。

它不只是做语法润色，而是帮助研究者系统检查研究问题、论证链条、变量定义、变量关系、研究方法、数据证据、图表解释、附录一致性、引用支撑和写作清晰度。

这个项目适合在论文送导师、组内讨论、投稿前或合作修改前使用。目标不是替代正式 peer review，而是先暴露那些可定位、可修改、可复核的问题，让作者、导师和合作者把更多时间用在研究贡献、识别策略、理论机制和结果解释上。

## 两个 Skill 版本

本仓库包含两个可安装 Skill：

| Skill | 调用名 | 适合场景 | 默认输出 |
|---|---|---|---|
| 通用论文审阅 | `$paper-review` | Markdown、DOCX、PDF、LaTeX、纯文本论文预审 | Markdown 审阅报告 |
| LaTeX 专项审阅 | `$latex-paper-review` | LaTeX 源码、公式、交叉引用、引用键、编译表达和 LaTeX review 文件 | LaTeX 审阅文件 |

如果你不确定该用哪个，优先用 `$paper-review`。如果你的主要问题是 LaTeX 源码、公式表达、交叉引用或编译后的 LaTeX review 文件，再使用 `$latex-paper-review`。

当前 LaTeX-only 版本也保留在 [`latex-paper-review`](https://github.com/Conradgui/Academic-Paper-Review-Skill/tree/latex-paper-review) 分支中，方便需要历史快照的用户查看。

## 为什么做这个 Skill

普通 AI 审稿常常“看起来很认真”，但建议容易停留在泛泛层面：增强创新性、补充文献、优化表达、加强讨论。真正写论文时，更耗时间、也更影响可信度的，往往是这些细节：

- 研究问题和方法并没有完全对齐
- 变量在正文、公式、表格和附录里口径不一致
- 结论写得比数据、实验或引用更强
- 图表结果和正文解释存在细微矛盾
- 公式符号、下标、假设条件或分支条件没有定义清楚
- 附录推导、补充实验、算法说明或稳健性检验和正文主张没有对齐
- 引用、编号、表格结构或文档格式影响读者理解

`paper-review` 更关注论文内部的一致性和可验证性。它像一轮低成本、高密度的预审，帮助作者在正式反馈环节前先处理基础但关键的问题。

## 它适合检查什么

- **全文结构预审**：检查题目、摘要、引言、相关工作、方法、结果、讨论、结论之间是否连贯。
- **研究问题与方法对齐**：检查研究设计、模型、实验、证明或综述框架是否能回答研究问题。
- **变量与概念一致性**：检查变量定义、构念、符号、术语、下标、单位和假设条件是否前后一致。
- **证据链条检查**：检查主张是否由数据、图表、实验、推导、引用或附录支持。
- **图表与正文对齐**：检查表格、图注、实验结果和正文解释是否互相支撑。
- **附录与正文对齐**：检查附录推导、证明、算法、稳健性检验或数据处理过程是否支撑正文。
- **Unsupported claims 扫描**：找出缺少数据、文献、图表或实验结果支持的判断。
- **审阅报告生成**：输出可追踪、可修改的 Markdown 审阅报告，方便作者逐条处理。

## 它和普通 AI 润色有什么区别

普通 AI 润色更像是“把句子改得更顺”。  
`paper-review` 更像是“帮你检查论文能不能经得起读者追问”。

它关心的问题包括：

- 这个结论有没有证据支持？
- 这个变量前面有没有定义？
- 这个符号或概念在全文是不是同一个意思？
- 这个方法是否真的回答了研究问题？
- 这个表格是否真的支持正文说法？
- 这个附录是在补充正文，还是制造了新的矛盾？
- 这个引用是否真的支撑当前句子的判断？

## 安装方式

复制你需要的 Skill 目录到 Codex skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -R paper-review ~/.codex/skills/
cp -R latex-paper-review ~/.codex/skills/
```

只需要通用版时，只复制 `paper-review/` 即可。

## 使用示例

通用论文预审：

```text
Use $paper-review to review this manuscript and write a concise Markdown review report.
```

中文审阅报告：

```text
Use $paper-review to review this manuscript. Write the review in Simplified Chinese.
```

结合权威资料审阅时，建议显式授权检索：

```text
Use $paper-review to review this manuscript. If a finding depends on external literature or method norms, ask before searching authoritative sources.
```

LaTeX 专项审阅：

```text
Use $latex-paper-review to review this LaTeX manuscript and write a concise LaTeX review file.
```

## 输入形式说明

通用版 `$paper-review` 支持：

- Markdown
- DOCX
- PDF
- LaTeX 源码
- 纯文本
- 多文件项目或论文材料包

输入越完整，审阅越可靠。对于多文件论文，建议提供正文、附录、图表说明、参考文献、补充材料和相关说明。若只提供 PDF，Skill 仍可审阅可见内容，但对源码结构、隐藏批注、交叉引用、宏定义和编译问题的判断会受到限制。

对于 DOCX，Skill 会以内容审阅为主；如需保留批注、修订痕迹或 Word 样式，需要另行使用文档编辑工具或明确提出该需求。

## 外部资料检索策略

默认情况下，Skill 不会主动联网检索。原因很直接：未发表论文、课程论文、组内初稿和合作稿可能包含敏感信息；同时，外部资料质量参差不齐，错误资料会污染审阅判断。

当审阅需要判断领域背景、经典理论、方法规范、事实性声明或引用支撑时，Skill 可以建议用户授权检索。授权后应优先使用：

- 论文原文引用
- 官方机构或标准文件
- 教材、手册、方法论文
- 顶级期刊、会议或领域权威综述
- 可核查的 DOI、出版社页面或学术数据库页面

博客、营销文章、论坛回答和无来源摘要不应作为强证据。外部资料只能用于增强判断或标注“需要核查”，不能把未验证内容说成确定错误。

## 输出行为

默认情况下，通用版会生成 Markdown 审阅报告：

```text
paper-reviews/review-YYYY-MM-DD-HHMMSS.md
```

审阅内容会优先覆盖：

1. 研究问题、方法、变量、证据和结论之间的一致性
2. 数学、公式、符号、单位、定义、算法和实现表达
3. 图表、附录、引用和正文主张之间的支撑关系
4. 有明确价值的写作和 proofing 问题

如果论文没有发现明确技术或证据问题，Skill 应该说明它检查过哪些关键内容，而不是用泛泛建议填充报告。

## 内置 proofing scan

两个 Skill 都包含一个轻量脚本：

```text
scripts/proofing_scan.py
```

它用于扫描一些高置信、低成本但容易遗漏的问题，例如：

- 重复标点：`, ,`、`,,`、`..`
- 引号附近的异常标点
- `javascript`、`ios`、`iphone` 等大小写问题
- `arctan(x/y)` 这类可能存在象限或分支歧义的表达
- 推导文字中常见的异常表达模式

示例：

```bash
python3 paper-review/scripts/proofing_scan.py path/to/manuscript.pdf --max-hits 80
```

脚本输出只是候选线索，仍需要人工或 AI spot-check 后再写入审阅意见。

## 项目结构

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
  plan-2026-06-23.md          # 初始 LaTeX 版整理记录
  plan-2026-06-24-generalization.md # 通用版升级记录
```

## 适合谁

- 正在写科研论文的学生和研究者
- 使用 Markdown、DOCX、PDF 或 LaTeX 管理论文草稿的作者
- 投稿前想做系统自查的作者
- 希望减少基础反馈成本的导师或课题组
- 多人合作论文中需要统一变量、图表、附录、引用和结论口径的团队
- 想学习 Codex Skill 结构和工作流设计的人

## 边界和限制

`paper-review` 不能替代正式 peer review，也不能替代导师、审稿人或领域专家的最终判断。

它不保证发现所有数学、计量、理论或领域问题，尤其是高度专业、依赖外部文献或深层背景知识的错误。它也不是单纯 grammar checker，不是只把句子改得更“学术”，更不是一键投稿工具。

更合理的使用方式是：把它作为论文写作流程中的前置质量控制环节。作者仍然需要判断、取舍和修改。

## License

MIT License. See [LICENSE](LICENSE).
