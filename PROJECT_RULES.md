# 项目规则

## 项目结构
```
WanWeigang.skill/
├── SKILL.md                     ← 核心思维操作系统
├── README.md                    ← 项目介绍
├── LICENSE                      ← MIT 许可
├── PROJECT_OVERVIEW.md          ← 项目概览
├── PROJECT_PROGRESS.md          ← 进展日志
├── PROJECT_RULES.md             ← 本文件
├── .gitignore
├── references/
│   ├── research/                ← 持续维护的调研、提炼与验证文件
│   └── sources/                 ← 本地一手素材（必须由 .gitignore 排除）
└── scripts/
    └── ocr_scanned_pdfs.py      ← OCR处理脚本
```

## 命名规范
- 仓库名：WanWeigang.skill
- 目录名：万维钢-perspective（限于用户本地安装路径）
- 中文名：万维钢.skill

## 固定工作流
- 更新时只增量更新，不重写整个 Skill
- 每次更新需重新运行 Phase 4 质量验证
- 重大更新需创建新的 GitHub Release
- 付费课程原文不得提交或发布；只允许公开非替代性的提炼、短摘要和证据定位
- 所有推导须区分材料事实、作者原话、研究概括和框架推断

## 提交约定
- 提交信息：英文前缀（feat/fix/rename/docs）+ 中文说明
- 版本标签：遵循 semver
