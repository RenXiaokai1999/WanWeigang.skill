# 项目进展

## 2026-04-24 — 首次发布

### 完成事项
- 完成 Phase 0-5 全部蒸馏流程
- 创建 SKILL.md（347行，6个心智模型，8条决策启发式，完整表达DNA）
- 通过 Phase 4 质量验证（5/5 PASS）
- 完成 Phase 5 双Agent精炼（7项改进）
- OCR处理：8卷扫描PDF → 9MB可分析文本
- 创建 README.md、LICENSE、PROJECT_OVERVIEW.md
- 发布到 GitHub：https://github.com/RenXiaokai1999/WanWeigang.skill
- 创建 Release v1.0.0「万维钢.skill」

### 修改文件清单
- `SKILL.md` — 核心思维操作系统
- `README.md` — 项目介绍与使用指南
- `LICENSE` — MIT 许可协议
- `PROJECT_OVERVIEW.md` — 项目概览
- `PROJECT_PROGRESS.md` — 本文件
- `PROJECT_RULES.md` — 项目规则
- `.gitignore` — Git 忽略规则
- `references/research/01-writings.md` ~ `08-quality-validation.md` — 8份调研文件
- `scripts/ocr_scanned_pdfs.py` — OCR处理脚本

### 下一步计划
- 关注万维钢新动态，定期更新 Skill
- 收集用户反馈，迭代心智模型精度

### 风险/阻塞
- 信息截止到2026年4月，需关注万维钢后续思想演化
- OCR文本存在噪声，部分精确引用需对照原文

## 2026-08-15 — v1.1.0 完课材料增量更新

### 已完成事项
- 完成《现代思维工具100讲》完课材料去重审计：180个一级标题片段归并为123个唯一单元
- 确认课程于2026年8月9日完结，核心内容为100讲正文与19章正式问答
- 完成对话、决策、时间线三条证据链的增量调研
- 将核心框架升级为7个心智模型、10条决策启发式
- 完成 v1.1.0 候选版 `SKILL.md` 构建，并同步更新项目说明
- 将课程全文保留在本地忽略目录，避免发布可替代原课程的付费内容
- Phase 4 的已知、边缘、文风与结构四项独立验证全部通过，并经用户确认
- 完成 Phase 5 双Agent精炼：收紧触发、透明人物视角、研究失败降级和选模预算
- 精炼回归通过，并经用户确认变更
- 同步到本地安装目录 `C:\Users\11789\.claude\skills\wanweigang-perspective`
- 使用确认的提交信息推送 GitHub，并发布 Release v1.1.0

### 本轮修改文件
- `SKILL.md` — 更新角色协议、心智模型、决策启发式、表达DNA、时间线与诚实边界
- `README.md` — 更新结构、框架、素材范围与验证状态
- `PROJECT_OVERVIEW.md` — 更新范围、里程碑和验收标准
- `PROJECT_RULES.md` — 增加原始素材发布边界与证据分层规则
- `references/research/02-conversations.md` — 增量补充完课问答与对话证据
- `references/research/05-decisions.md` — 增量补充真实决策、行为案例和领域规则
- `references/research/06-timeline.md` — 增量补充课程后半程与完课时间线
- `references/research/09-course-completion-delta.md` — 完课材料范围、去重和证据审计
- `references/research/10-synthesis-2026-08.md` — v1.1.0 综合提炼记录
- `references/research/11a-known-validation.md` — 已知立场验证
- `references/research/11b-edge-validation.md` — 边缘问题验证
- `references/research/11c-voice-validation.md` — 文风盲测
- `references/research/11d-structural-validation.md` — 结构质量审计
- `references/research/12a-refinement-optimizer.md` — 优化器8维评审与干跑
- `references/research/12b-refinement-creator.md` — 触发、角色和路由评审
- `references/research/13-refinement-regression.md` — 精炼后的静态与行为回归

### 下一步
- 关注万维钢后续课程、著作与AI实践，只在出现真实思想增量时更新
- 收集实际调用中的误触发、过度框架化和事实研究失败案例

### 风险/阻塞
- 完课材料存在重复抓取片段，引用前必须以唯一单元和最新版本为准
- AI、健康等时效性较高的观点需保留时间戳，不应外推为永久立场
- 原始课程全文是本地研究素材，后续维护仍须确保 `references/sources/` 不进入 Git 暂存区

## 2026-08-15 — GitHub 首页 Hero 海报

### 已完成事项
- 确定无真人的“思维反应堆”方向，以深空结构、认知核心、轨道和能量流表现现代思维操作系统
- 使用内置 `image_gen` 生成并验收 Hero 海报，最终尺寸为 1672×941，文件约 2.06 MB
- 用户明确接受画面中的 9 个可见大节点；文字仍准确显示 `10 HEURISTICS`，覆盖原设计对 10 个节点的视觉计数要求
- 将 Hero 海报集成到 README 首屏，位于项目标题与徽章之间
- 完成双重质量评审，并通过源文件与仓库资产 SHA256 一致性验证

### 本轮修改文件
- `README.md` — 在首屏集成 Hero 海报
- `assets/wanweigang-skill-hero-v1.1.0.png` — GitHub 首页海报资产
- `docs/plans/2026-08-15-github-hero-poster-design.md` — 海报设计文档
- `docs/plans/2026-08-15-github-hero-poster-implementation.md` — 海报实施与发布计划
- `PROJECT_PROGRESS.md` — 记录本轮设计、验收与集成进展

### 下一步
- 使用已确认的提交信息发布到 GitHub，并观察仓库首页的实际显示效果

### 风险/阻塞
- 图片约 2 MB，网络较慢时 README 首屏加载可能稍有延迟
- 未来发布新版本时，需要同步更新海报文件名、画面版本号与 README 引用
