# Paper Review 双线审阅与作者化润色执行记录

日期：2026-06-28 至 2026-06-29

## 目标

在不削弱现有科学性审阅的前提下，为通用版 `$paper-review` 增加默认轻量的文本质量审阅，并在用户明确要求时支持受保护的局部、章节和全文作者化润色。

## 已锁定决策

- 默认同时运行 Scientific Review 和轻量 Text Quality Review。
- 文本质量没有明显问题时只输出一句结论；出现材料级问题或用户明确要求时才展开详细小节。
- 默认 finding 使用修改指导，不再提供完整可复制段落。
- 润色必须由用户明确触发；全文润色按章节处理并生成新文件，绝不覆盖原稿。
- Markdown、LaTeX、TXT、DOCX 可生成润色副本；PDF 只审阅或输出修改指导。
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
- 独立 Codex 前向测试未执行：Codex CLI 调用被账户用量上限拒绝。未尝试绕过；改用契约测试、合成样本和既有论文只读回归。
- 私人论文和 review 仅用于本地只读验证，没有复制到仓库或测试夹具。
