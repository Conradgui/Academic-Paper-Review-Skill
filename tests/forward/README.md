# 独立 Codex 前向评测

本目录验证 `$paper-review` 在真实、全新 Codex 会话中的行为，而不只检查 Markdown 是否包含某些关键词。

## 覆盖路径

| 用例 | 目标 |
|---|---|
| `FWD-01` | 干净理论稿只输出轻量文本质量结论，不强行生成 `T-*` finding |
| `FWD-02` | 严重实证与文本问题触发双线详细审阅、主张校准和修改行动表 |
| `FWD-03` | Delta Review 保留原 finding ID，使用强制状态矩阵和精确状态 token |
| `FWD-04` | 无作者样本时执行 Markdown 全文受保护润色，不覆盖原稿或伪称匹配作者文风 |
| `FWD-05` | 正常 Methods 中的被动语态、副词、破折号和三项并列不会触发详细 AI 痕迹 finding |
| `FWD-06` | 显式 AI 痕迹审阅输出候选矩阵、反误伤结论和深层来源风险，不判断作者身份或概率 |

所有输入都位于 `fixtures/`，是专门构造的合成论文，不包含私人稿件。

## 隔离方式

runner 会为每个用例：

1. 创建独立临时工作区；
2. 创建临时 `CODEX_HOME`；
3. 复制当前仓库中的 `paper-review/` 精确版本；
4. 仅用临时符号链接复用本机 Codex 认证，不复制认证文件；
5. 记录 Skill SHA-256；
6. 单次调用 Codex，不自动重试；
7. 用例结束后销毁临时工作区和临时 `CODEX_HOME`。

这种隔离用于防止会话误读 `~/.codex/skills` 中的旧版或其他同名 Skill。

## 运行

```bash
python3 tests/forward/run_forward_evals.py
```

只运行指定用例：

```bash
python3 tests/forward/run_forward_evals.py --case FWD-03
```

前提：本机已经安装并登录 `codex` CLI。每个用例会发起一次真实模型调用并消耗账户额度；默认超时为 420 秒。

## 结果与隐私

结构化结果、事件日志和合成输出默认写入：

```text
_project-records/forward-evals/<run-id>/
```

该目录已被 Git 忽略。认证内容不会进入仓库、结果目录或合成夹具。

截至 2026-06-29，基础四个用例使用同一 Skill SHA-256，结果为 4/4 用例、47/47 项断言通过。汇总见 [`_project-records/forward-eval-summary-2026-06-29.md`](../../_project-records/forward-eval-summary-2026-06-29.md)。

2026-06-30 的 AI 痕迹候选审阅增量评测使用更新后的同一 Skill SHA-256，FWD-05 与 FWD-06 为 2/2 用例、28/28 项断言通过。汇总见 [`_project-records/forward-eval-summary-2026-06-30-ai-trace.md`](../../_project-records/forward-eval-summary-2026-06-30-ai-trace.md)。

这些评测用于验证核心路径是否可工作，不是跨模型、跨学科或多次重复运行的统计 Benchmark。
