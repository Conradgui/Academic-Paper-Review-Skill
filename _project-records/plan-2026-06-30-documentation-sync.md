# Paper Review 项目文档同步记录

日期：2026-06-30

## 目标

让公开 README、Codex Agent 入口、前向评测说明与当前 `$paper-review` 实现保持一致，重点公开会影响用户选择、使用和判断的行为契约，同时减少 README 中重复、失真或过度承诺的内容。

## 文档审计结论

本轮修改前，主 README 已覆盖大部分功能，但存在以下问题：

1. 核心检查项、输出行为和使用示例重复较多，用户难以快速建立产品心智模型。
2. 通用版扫描器已经增强，但 README 仍暗示两个 Skill 的 Proofing 能力相同。
3. Delta Review 没有完整公开强制状态矩阵、原 finding ID 保留和未关闭项进入行动表的规则。
4. 轻量文本观察不分配 `T-*` 的行为没有写入公开文档。
5. `paper-reviews/` 与 `paper-revisions/` 只允许存放交付物的目录卫生规则没有公开。
6. README 提到前向评测入口，但没有公开 4/4 用例、47/47 断言的结果与证据边界。
7. 局部润色示例容易在没有作者样本时错误宣称使用“作者文风”。
8. 项目第一屏仍使用“轻量级”定位，不能准确表达当前结构化审计和受保护润色的完整能力。

## 已实施

- 重构 `README.md`，按定位、快速使用、工作方式、判断规则、复核、润色、隐私、版本、安装、扫描器和验证证据组织内容。
- 明确 Scientific Review 与 Text Quality Review 的并列关系，科学性仍优先。
- 公开轻量观察、详细文本 finding、严重程度、确定性、主张校准和修改行动表契约。
- 公开 Delta Review 精确状态 token、强制矩阵、旧 ID 保留和未关闭项处理规则。
- 修正润色调用示例，区分作者文风基线、论文一致性基线和中性学术基线。
- 明确 Markdown/TXT/LaTeX、DOCX、PDF 的润色边界和输出目录卫生规则。
- 分开说明通用版与 LaTeX 专项版 Proofing 扫描器的实际能力。
- 加入 2026-06-29 隔离前向评测结果及“不构成统计 Benchmark”的限制。
- 将 `tests/forward/README.md` 改为中文维护者文档，补充用例、隔离方式、成本、隐私和结果解释。
- 同步 `paper-review/agents/openai.yaml` 的简短描述与默认 prompt。
- 增加 README 契约测试，防止后续删除关键公开边界。

## 不改变的内容

- 项目仍是通用科研论文预审 Skill，不转为实证论文专用或论文润色专用。
- 默认仍只审阅、不修改原稿。
- 外部检索仍严格 opt-in。
- `$latex-paper-review` 目录及历史分支保持隔离，本轮不修改。
- 不使用任何文本检测器分数作为产品定位或验收标准。

## 验证表

1. README 关键契约测试 -> 验证：`tests/test_skill_contract.py`。
2. 两个 Skill metadata -> 验证：分别运行 `quick_validate.py`。
3. Python 脚本 -> 验证：`py_compile` 与完整单元测试。
4. 文档格式 -> 验证：`git diff --check`。
5. LaTeX 专项隔离 -> 验证：`git diff --exit-code HEAD -- latex-paper-review`。
6. 公开说法与评测证据 -> 验证：对比 README 与 `_project-records/forward-eval-summary-2026-06-29.md`。

## 最终验证结果

- `quick_validate.py paper-review`：通过。
- `quick_validate.py latex-paper-review`：通过。
- `py_compile`：通用扫描器与前向评测 runner 均通过。
- `python3 -m unittest discover -s tests -v`：19 项通过。
- `git diff --check`：通过。
- `git diff --exit-code HEAD -- latex-paper-review`：通过，专项目录无改动。
- README 相对链接、Markdown 围栏和关键公开契约：通过文本检查。
