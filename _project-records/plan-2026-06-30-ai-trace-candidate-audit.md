# AI 痕迹候选审阅迭代记录

日期：2026-06-30

## 目标

在不改变“科学性审阅 + 文本质量审阅”双线定位的前提下，将 AI 痕迹候选审阅作为文本质量子模块。所有论文默认轻量扫描，用户明确要求或出现材料级风险时输出详细候选矩阵。

## 来源评估

- `Wikipedia:Signs of AI writing`：吸收“模式是候选而非问题本身”、高信号工具污染、模糊归因、空泛重要性、通用结论和误报警告。
- `Wikipedia:WikiProject AI Cleanup/Guide`：吸收从表面痕迹继续核验来源存在性、来源质量和 source-to-claim alignment 的处理原则。
- `hardikpandya/stop-slop`：吸收具体化、减少低信息铺垫和机械结构的思路。

本项目不吸收禁用所有副词、被动语态、破折号、三项并列，强制句长变化或使用“Authenticity”评分等规则。这些规则会误伤科研论文中的方法语态、审慎限定和学科惯例。

所有规则均独立重写，不复制第三方大段内容。Wikipedia 内容仅作为设计参考并提供链接；`stop-slop` 使用 MIT License，本项目继续保持 MIT License。

## 已锁定契约

- 不判断作者身份，不声称文本由 AI 生成。
- 不输出 AI 概率、检测器分数或规避检测器建议。
- 默认轻量扫描；明确请求或材料级候选触发详细矩阵。
- 固定核验链：表面候选、上下文功能、具体性、证据或引用、章节适配、最终判断。
- 详细结论使用 `Confirmed Text Issue`、`Source Integrity Risk`、`Contextually Acceptable`、`Needs Verification`。
- 表达问题提升为 `T-*`，证据或引用风险提升为 `S-*`，语境合理候选不进入行动表。
- 脚本只扫描高置信工具污染，不建立普通学术词汇黑名单。
- 外部来源核查继续严格 opt-in，本轮不实现 DOI/ISBN 联网验证器。
- `$latex-paper-review` 专项版保持不变。

## 测试驱动证据

- 基线：现有 19 项测试全部通过。
- RED：新增目标测试后，扩展工具标记、reference、README 和 FWD-05/FWD-06 均按预期失败或缺失。
- GREEN：25 项本地测试全部通过；两个 Skill validator、Python 编译和 `git diff --check` 通过。
- FWD-05 首次运行正确发现合成“干净稿”中的 `robust` 无证据和方法信息缺口，证明失败来自夹具而不是误伤规则。补全重复测量设计、CV 计算和温度敏感性证据后重跑，通过 9/9 断言。
- FWD-06 通过 19/19 断言，详细报告同时输出 `Source Integrity Risk`、`Confirmed Text Issue` 和 `Contextually Acceptable`，并把来源风险提升为 `S-*`。
- FWD-05 与 FWD-06 使用相同 Skill SHA-256：`1457b1af1d77fed5a2a35085835f981b39095f8eb39871663ab45bec6aa09b49`。
- Agent 默认 prompt 增加 128 字符上限契约，并从 184 字符收紧到 124 字符。
