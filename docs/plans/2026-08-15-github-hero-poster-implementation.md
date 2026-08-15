# GitHub Hero Poster Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 生成一张准确、酷炫且适配 GitHub README 的万维钢.skill v1.1.0 Hero 海报，并发布到仓库 `main`。

**Architecture:** 使用内置 `image_gen` 生成单张 16:9 位图，在生成后用 `view_image` 检查文字、层级和主视觉；若失败，只做一次针对性编辑。最终图片保存到仓库 `assets/`，README 通过相对路径引用，Git 只提交计划、最终图片、README 和项目进展。

**Tech Stack:** `@imagegen`、Codex `view_image`、Markdown、Git、GitHub CLI（遵循 `@web-access`）、`@verification-before-completion`

---

### Task 1: 建立发布基线

**Files:**
- Read: `README.md`
- Read: `docs/plans/2026-08-15-github-hero-poster-design.md`
- Create directory if missing: `assets/`

**Step 1: 核对 Git 状态**

Run: `git status --short`

Expected: 只有用户既有的 `.claude/`、海报和脚本为未跟踪文件；没有意外的已跟踪修改。

**Step 2: 核对远端基线**

Run: `git fetch origin main && git rev-list --left-right --count main...origin/main`

Expected: 设计文档提交导致本地领先远端1个提交，远端不领先本地。

**Step 3: 准备资产目录**

Run: `New-Item -ItemType Directory -Force -Path assets`

Expected: `assets/` 存在，不删除或覆盖任何已有文件。

### Task 2: 生成 Hero 海报

**Files:**
- Create: `assets/wanweigang-skill-hero-v1.1.0.png`

**Step 1: 使用内置图像生成**

调用 `@imagegen` 的内置模式，使用 `ads-marketing` 分类和设计文档中的精确视觉规范。提示词必须包含：

```text
Use case: ads-marketing
Asset type: GitHub README hero poster, 16:9 landscape
Primary request: a premium abstract “thinking reactor” for WanWeigang.skill, expressing scientific thinking as an executable operating system
Scene/backdrop: deep space navy-black background, subtle engineering grid, large clean dark areas
Subject: a luminous transparent cognitive core on the right, seven precise orbital layers and ten distinct nodes, red-gold energy stream crossing cool electric-blue structures
Style/medium: premium cinematic 3D editorial design, scientific instrument precision, restrained futuristic Chinese design
Composition/framing: wide GitHub hero; title hierarchy on the left; main reactor on the right; readable when displayed at repository width
Lighting/mood: controlled volumetric glow, intelligent, rigorous, surprising, calm power
Color palette: deep navy-black, electric blue, Chinese red, small gold highlights, white title
Text (verbatim): "万维钢.skill"; "MODERN THINKING OPERATING SYSTEM"; "7 MENTAL MODELS · 10 HEURISTICS"; "v1.1.0"
Constraints: render every text string exactly once and verbatim; large crisp title; no other text; no portrait; no person; no logos; no watermark
Avoid: AI brain icon, robot head, code rain, cheap cyberpunk, excessive neon, course-ad language, tiny decorative copy, duplicated letters, garbled Chinese
```

Expected: 内置工具返回生成结果和 `$CODEX_HOME/generated_images/` 下的保存位置。

**Step 2: 将候选图复制到项目**

把选中的生成结果复制为 `assets/wanweigang-skill-hero-v1.1.0.png`，不得覆盖其他海报。

Expected: 文件存在且为非空 PNG。

### Task 3: 视觉与文字验收

**Files:**
- Inspect: `assets/wanweigang-skill-hero-v1.1.0.png`

**Step 1: 检查基础属性**

Run: 用系统图像读取能力输出宽度、高度、格式和文件大小。

Expected: 横向 16:9 左右；PNG；尺寸足以覆盖 GitHub README 宽度；文件非空。

**Step 2: 使用 `view_image` 视觉检查**

逐项检查：

- `万维钢.skill` 是否准确、清晰且只出现一次
- 三组英文/数字是否准确
- 是否存在额外文字、水印或乱码
- 是否为左文右图的清晰层级
- 是否能读出核心、轨道、节点和能量流
- 是否避开人物、AI大脑、机器人头和代码雨

Expected: 设计文档6项验收标准全部满足。

**Step 3: 只在必要时做一次针对性修正**

若只有一个局部问题，使用 `@imagegen` 编辑当前候选图，只修正该问题并保持其余构图不变；重新执行 Step 1—2。若文字持续不可靠，停止发布并向用户展示候选图与具体失败点，不用错误海报上线。

### Task 4: 集成 README

**Files:**
- Modify: `README.md`

**Step 1: 添加 Hero 图片**

在 `# 万维钢.skill` 与徽章之间插入：

```markdown
![万维钢.skill：现代思维操作系统](assets/wanweigang-skill-hero-v1.1.0.png)
```

Expected: README 只引用一次图片，路径大小写与真实文件完全一致。

**Step 2: 检查 Markdown 上下文**

Run: `rg -n "wanweigang-skill-hero|^# 万维钢\.skill|Claude Code Skill" README.md`

Expected: 标题、Hero、徽章依次出现；Hero 引用只有1处。

### Task 5: 发布前验证

**Files:**
- Verify: `README.md`
- Verify: `assets/wanweigang-skill-hero-v1.1.0.png`
- Verify: `docs/plans/2026-08-15-github-hero-poster-implementation.md`
- Verify: `PROJECT_PROGRESS.md`

**Step 1: 检查差异**

Run: `git diff --check`

Expected: 无错误；Windows 行尾提示不算错误。

**Step 2: 暂存白名单文件**

Run: `git add -- README.md assets/wanweigang-skill-hero-v1.1.0.png docs/plans/2026-08-15-github-hero-poster-implementation.md PROJECT_PROGRESS.md`

Expected: 暂存区不包含 `references/sources/`、现有海报、生成脚本或 `.claude/`。

**Step 3: 检查暂存区**

Run: `git diff --cached --check && git diff --cached --name-status`

Expected: 仅4个实施文件；无空白错误。

### Task 6: 提交并发布

**Files:**
- Commit: `README.md`
- Commit: `assets/wanweigang-skill-hero-v1.1.0.png`
- Commit: `docs/plans/2026-08-15-github-hero-poster-implementation.md`
- Commit: `PROJECT_PROGRESS.md`

**Step 1: 在 `main` 工作区直接提交**

Run: `git commit -m "feat: 添加 GitHub 首页 Hero 海报"`

Expected: 当前受限环境已在 `main` 工作区完成集成；使用用户确认的提交信息直接提交成功，用户既有未跟踪文件仍被保留。

**Step 2: 推送 `main`**

Run（工作目录：`D:\6Sundries\书柜\得到资源\万维刚skill项目`）：`git push origin main`

Expected: `main` 推送成功。

**Step 3: 最终核验**

Run: 拉取远端引用，核对 `HEAD == origin/main`；核对远端 README 的图片路径与本地一致，并确认最终图片 blob 已进入提交。

Expected: 本地与远端提交一致，Hero 图片可由 GitHub 仓库相对路径加载。

## 执行决策

- 用户于 2026-08-15 明确接受海报中 9 个可见大节点；画面文字仍准确显示 `10 HEURISTICS`，因此原设计对 10 个节点的视觉计数要求由本次确认覆盖。
- 因当前权限仅允许写入主仓库，已将验收通过的海报资产与本实施计划从外部 worktree 复制回主仓库，并在主仓库完成 README 集成。
