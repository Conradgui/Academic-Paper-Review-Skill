# Paper Review 双线审阅与作者化润色执行记录

日期：2026-06-28 至 2026-06-29

## 目标

在不削弱现有科学性审阅的前提下，为通用版 `$paper-review` 增加默认轻量的文本质量审阅，并在用户明确要求时支持受保护的局部、章节和全文作者化润色。

## 已锁定决策

- 默认同时运行 Scientific Review 和轻量 Text Quality Review。
- 文本质量没有明显问题时只输出一句结论；出现材料级问题或用户明确要求时才展开详细小节。
- 默认 finding 使用修改指导，不再提供完整可复制段落。
- 润色必须由用户明确触发；全文润色按章节处理并生成新文件，绝不覆盖原稿。
- Markdown、LaTeX、TXT 可直接生成润色副本；DOCX 仅在具备编辑与渲染核验工具时生成副本；PDF 只审阅或输出修改指导。
- 内置流程必须独立工作；本地 Nature/Humanizer Skill 只作为询问后启用的可选增强。
- 不输出 AI 概率，不优化 perplexity 或固定句长方差，不根据文本推断作者身份。
- 本轮只修改通用版 `paper-review`，不修改 `latex-paper-review` 或历史分支。

## 第三方来源审查

| 项目 | 许可证 | 可参考部分 | 不吸收部分 |
|---|---|---|---|
| `Yuan1z0825/nature-skills` | Apache-2.0 | 论证先于句子、术语约束、章节化润色、局部修订 | 直接复制规则、示例或 Nature 专属格式假设 |
| `blader/humanizer` | MIT | 模板化表达候选、作者样本校准、诊断后改写 | 困惑度目标、强制句长变化、个性注入 |
| `Aboudjem/humanizer-skill` | MIT | detect/rewrite/verify 分阶段思路 | AI 分数、硬词表、全文自动接管 |
| `op7418/Humanizer-zh` | MIT | 中文适配风险样本 | 机械翻译规则、擅自补充事实、博客式个性写法 |

本项目只参考公开思路并独立重写，不复制第三方大段内容。README 保留来源链接与用途说明。

## 实现模块

- `paper-review/SKILL.md`：双线路由、文本质量输出契约、显式润色模式。
- `paper-review/references/`：通用审计、中英文规则、作者化润色、外部 Skill 路由。
- `paper-review/scripts/proofing_scan.py`：聊天残留、占位符、异常引用标记候选规则。
- `README.md`：双线定位、调用示例、格式边界、参考与启发。
- `paper-review/agents/openai.yaml`：默认同时强调科学性与文本质量。

## 验证目标

- 两个 Skill 目录均通过 `quick_validate.py`。
- `proofing_scan.py` 通过语法检查和新旧规则单元测试。
- README 和 SKILL 输出契约一致，不出现检测器分数承诺。
- 通用版包含双线审阅、详细触发、修改指导、全文副本和可选外部增强规则。
- LaTeX 专项版保持无差异。
- 使用既有毕业论文 review 和 Nature 候选稿进行只读回归，不把私人论文内容提交到仓库。

## 执行证据

- 隔离工作区：`/tmp/paper-review-text-quality-worktree`，分支 `codex/text-quality-review`。
- `quick_validate.py paper-review`：通过，输出 `Skill is valid!`。
- `quick_validate.py latex-paper-review`：通过，输出 `Skill is valid!`。
- `python3 -m unittest discover -s tests -v`：7 项测试通过，覆盖新旧 proofing 规则、正常中英文不误报、双线契约、README 定位和 metadata。
- `PYTHONPYCACHEPREFIX=/tmp/paper-review-pycache python3 -m py_compile paper-review/scripts/proofing_scan.py`：通过。
- 既有 Nature 润色候选稿只读扫描：`[OK] No high-confidence pattern-scan hits found.`。
- 两份旧 review 分别包含 9 条和 11 条 `Suggested revision`，其中存在完整可复制句段，验证了本轮问题来源。
- `git diff --exit-code main -- latex-paper-review`：通过，LaTeX 专项版没有改动。
- 当时独立 Codex 前向测试未执行：Codex CLI 调用被账户用量上限拒绝。未尝试绕过；额度恢复后已补测，最终结果见本文件后续“独立模型前向评测计划”。
- 私人论文和 review 仅用于本地只读验证，没有复制到仓库或测试夹具。

## 2026-06-29 复核修正

- 将中英文专项 reference 改为详细审阅触发后再加载；所有论文仍执行语言无关的轻量文本质量检查，避免默认上下文膨胀。
- 统一详细文本质量表与全局 finding 契约，补充“严重程度”和“判断确定性”。
- 区分“已确认作者文风基线”“论文一致性基线”和“中性学术基线”，不再把稿件内部一致性误称为已验证作者个人文风。
- 收紧 DOCX 承诺：只有具备编辑和渲染核验工具时才生成 DOCX，否则降级为结构化修改文本或请求其他可编辑源。
- 补充中英文常见论文写作问题：缩写首次定义、标点与数字/单位、指代与平行结构、英语主谓一致/冠词/可数性/拼写体系，以及文献综述逐篇罗列。
- Proofing 仅对过强主张和聊天残留等语义候选合并邻近命中；确定性标点问题仍逐条保留，兼顾降噪与召回率。
- 修复外部检索 opt-in 边界：无法仅靠稿件判断时先标记 `Needs External Verification` 并请求授权，未授权不得联网。
- 增加跨论文类型的章节级高频问题检查，并补充实证论文中的效应量、置信区间、多重检验、缺失值、样本量与数据泄漏风险。
- Proofing 不再静默吞掉 DOCX 主文档解析失败或不可提取文本的 PDF；辅助 DOCX 部件失败会告警，非正数 `--max-hits` 会被拒绝。
- README 明确 PDF Proofing 的 `pypdf` 依赖和 OCR/可编辑源降级路径，并将默认文本审阅表述统一为“稿件文风一致性”。

## 独立模型前向评测计划

额度恢复后追加四条隔离合成用例，不使用私人论文：

- `FWD-01`：文本质量良好的理论稿，验证轻量文本结论和非过度审阅。
- `FWD-02`：含因果越界、显著性误读、样本/变量不一致和聊天残留的实证稿，验证双线详细审阅。
- `FWD-03`：旧 review 与修改稿，验证 `Resolved`、剩余问题和新问题的 Delta Review。
- `FWD-04`：未提供作者样本的 Markdown 全文润色，验证新副本、事实保真、伴随报告和论文一致性基线。

每个用例使用独立 ephemeral Codex 会话、临时工作区、单次调用和 420 秒上限。原始事件日志默认忽略，不进入公开仓库；结构化结果和合成输出可用于本地复核。

首次 `FWD-01` 调用链成功，但夹具被模型正确识别出“局部到全局未形式化、有限性未使用、充分条件误写成必要条件”等实质问题，因此未满足轻量文本审阅预期。该失败归因于测试夹具，不降低 Skill 标准；夹具已改为一般偏序集上的自包含技术札记并明确非新颖性定位，等待重新评测。

第二次 `FWD-01` 已达到轻量结论，但模型把单处“状态/元素”术语漂移扩写为完整 `T-01`。根因是“孤立问题保持简短”与“每个 finding 使用完整字段”之间存在歧义。协议现明确：孤立非材料级文本观察只用一句话，不分配 `T-*`、不生成详细表格、不进入行动表；`T-*` 仅保留给触发详细审阅的文本问题。夹具同时补全偏序定义并统一“元素”称谓。

第三次 `FWD-01` 通过，轻量文本结论、无 `T-*` 和源文件不变均符合预期。完整套件中的 `FWD-02` 也通过，正确识别因果越界、p=0.08 显著性误读、样本/变量不一致和材料级文本问题。

首次 `FWD-03` 的内容判断正确，但没有使用精确状态 token 和强制状态矩阵，并将映射后的 S-02 另编为 D-01。协议现要求：状态矩阵必选、状态使用精确英文枚举、映射问题保留原 ID、新问题才延续 S/T 编号、所有未关闭项进入修改行动表。

`FWD-01` 还暴露出内部 `plan.md` 被放入 `paper-reviews/`。输出目录现明确只用于用户交付物；evaluator 也只读取 `review-*` 报告并单独检查目录卫生，避免计划文本污染断言。

随后确认前向评测存在隔离缺陷：部分 Codex 会话自动读取了全局安装的旧版 `~/.codex/skills/paper-review`，而不是仓库最新版，因此这些结果不能证明当前实现。runner 现为每个用例建立临时 `CODEX_HOME`，仅复制当前仓库 Skill，并通过临时符号链接复用本机认证；会话结束后整体销毁，并记录 Skill SHA-256 作为隔离证据。后续前向结果必须来自该隔离 runner。

最终隔离结果：`FWD-01`、`FWD-02`、`FWD-03`、`FWD-04` 全部通过，共 47/47 断言。四条结果使用同一 Skill SHA-256 `e64077dc15030e1cc75a307bc56aec7f3b4baf6c69ccb94d8c4f948bc41e4044`，总耗时 456.12 秒。完整汇总见 `_project-records/forward-eval-summary-2026-06-29.md`。
- 复核后完整测试增至 18 项并全部通过；两个 Skill validator、Python 编译、`git diff --check` 和 LaTeX 专项目录零改动检查均通过。
