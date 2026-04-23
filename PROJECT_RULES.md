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
│   └── research/                ← 调研文件（01-08）
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

## 提交约定
- 提交信息：英文前缀（feat/fix/rename/docs）+ 中文说明
- 版本标签：遵循 semver
