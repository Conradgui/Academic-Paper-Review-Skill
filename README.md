# LaTeX Paper Review Skill
本项目受到 AI 辅助论文审阅的启发并结合日常使用痛点，目标是提供一个开源、可检查、可修改的 Skill，用于对 LaTeX 科研论文进行结构化预审。
面向使用 LaTeX 写作和排版的科研论文的结构化 AI 预审 Skill。它不只是做语法润色，而是帮助研究者系统检查论文中的研究问题、论证链条、公式符号、变量定义、图表解释、附录推导、引用支撑和 LaTeX 表达是否一致。

这个项目适合在论文送导师、组内讨论或投稿前使用。它的目标不是替代正式 peer review，而是先把那些可定位、可修改、可复核的问题暴露出来，让导师、合作者和作者本人把更多时间用在研究贡献、识别策略、理论机制和结果解释上。

## 为什么做这个 Skill

普通 AI 审稿常常“看起来很认真”，但建议容易停留在泛泛层面：增强创新性、补充文献、优化表达、加强讨论。真正写论文时，更耗时间、也更影响可信度的，往往是这些细节：

- 变量在正文、公式、表格和附录里口径不一致
- 结论写得比数据或实验结果更强
- 图表结果和正文解释存在细微矛盾
- 公式符号、下标、假设条件或分支条件没有定义清楚
- 附录推导、补充实验或算法说明和正文模型没有对齐
- 引用、编号、表格结构或 LaTeX 表达影响读者理解

`paper-review` 更关注论文内部的一致性和可验证性。它像一轮低成本、高密度的预审，帮助作者在正式反馈环节前先处理基础但关键的问题。

## 它适合检查什么

- **LaTeX 格式全文预审**：检查论文结构、章节衔接、研究问题、贡献表述和结论边界。
- **公式与符号一致性**：检查变量定义、下标、函数、单位、假设条件、编号和文字解释是否一致。
- **图表与正文对齐**：检查表格、图注、实验结果和正文解释是否互相支持。
- **附录与正文对齐**：检查附录推导、证明、算法、稳健性检验或数据处理过程是否支撑正文。
- **Unsupported claims 扫描**：找出缺少数据、文献、表格或实验结果支持的判断。
- **LaTeX 审阅文件生成**：输出一份可追踪、可修改的审阅文件，方便作者逐条处理。

## 它和普通 AI 润色有什么区别

普通 AI 润色更像是“把句子改得更顺”。  
`paper-review` 更像是“帮你检查论文能不能经得起读者追问”。

它关心的问题包括：

- 这个结论有没有证据支持？
- 这个变量前面有没有定义？
- 这个符号在全文是不是同一个意思？
- 这个公式和文字解释是否一致？
- 这个表格是否真的支持正文说法？
- 这个附录是在补充正文，还是制造了新的矛盾？
- 这个 LaTeX 表达是否影响审稿人理解？

## 使用方式

这个仓库的真正 Skill 包在 `paper-review/` 目录中。安装时复制这个目录即可。

```bash
mkdir -p ~/.codex/skills
cp -R paper-review ~/.codex/skills/
```

安装后，可以在 Codex 中这样调用：

```text
Use $paper-review to review this LaTeX manuscript and write a concise review file.
```

如果希望输出中文审阅意见，可以明确写：

```text
Use $paper-review to review this LaTeX manuscript. Write the review in Simplified Chinese.
```

如果希望输出英文审阅意见，也可以明确写：

```text
Use $paper-review to review this manuscript and write the review in English.
```

Skill 本身不会强制中文或英文；它会根据用户请求选择输出语言。这对中文研究者尤其有用，因为很多论文写作和审稿材料本身是英文的。

## 输入形式说明

这个 Skill 主要面向使用 LaTeX 写作和排版的科研论文。它可以基于 LaTeX 源码、编译后的 PDF，或用户提供的论文文本进行审阅。

如果论文是多文件 LaTeX 项目，建议提供完整项目目录，包括 `main.tex`、章节文件、参考文献文件、图片/表格说明和自定义宏定义。输入越完整，Skill 越容易检查公式、引用、交叉引用、附录和正文之间的一致性。

如果只提供单个 PDF，Skill 仍然可以审阅论文内容，但对 LaTeX 源码结构、宏定义、交叉引用和编译问题的判断会受到限制。

## 输出行为

默认情况下，Skill 会生成一个独立的 LaTeX 审阅文件：

```text
paper-reviews/review-YYYY-MM-DD-HHMMSS.tex
```

审阅内容会优先覆盖：

1. 数学、公式、符号、单位、定义、算法和实现表达
2. 论文主张、证据、图表、附录和结论之间的一致性
3. 有明确价值的写作和 proofing 问题

如果论文没有发现明确技术问题，Skill 应该明确说明它检查过关键技术内容，而不是用泛泛建议填充审阅文件。

## 内置 proofing scan

Skill 包含一个轻量脚本：

```text
paper-review/scripts/proofing_scan.py
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
  SKILL.md                    # Skill 的核心工作流
  agents/openai.yaml          # Codex UI 元数据
  references/review-rubric.md # 可选审阅检查表
  scripts/proofing_scan.py    # 高置信 proofing 扫描脚本

_project-records/
  plan-2026-06-23.md          # 本仓库整理过程记录
```

## 适合谁

- 正在用 LaTeX 写作科研论文的学生和研究者
- 投稿前想做系统自查的作者
- 希望减少基础反馈成本的导师或课题组
- 多人合作论文中需要统一变量、表格、附录和结论口径的团队
- 想学习 Codex Skill 结构和工作流设计的人

## 边界和限制

`paper-review` 不能替代正式 peer review，也不能替代导师、审稿人或领域专家的最终判断。

它不保证发现所有数学、计量、理论或领域问题，尤其是高度专业、依赖外部文献或深层背景知识的错误。它也不是单纯 grammar checker，不是只把句子改得更“学术”，更不是一键投稿工具。

更合理的使用方式是：把它作为论文写作流程中的前置质量控制环节。作者仍然需要判断、取舍和修改。

## License

MIT License. See [LICENSE](LICENSE).
