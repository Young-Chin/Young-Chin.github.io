---
title: '[2026/06/14] Know Each Other — 让 AI 真正认识你的 Claude 技能开源'
date: 2026-06-14
permalink: /posts/know-each-other-news
---

## 项目介绍

**Know Each Other** 是一个 Claude 技能，通过建立持久的心理画像，让 AI 跨项目记住你的思维方式、沟通偏好和决策风格——而不是每次会话重新从零开始。

> GitHub: [Young-Chin/know-each-other](https://github.com/Young-Chin/know-each-other)

## 核心特性

- **持久画像**：生成两个全局共享文件 `SOUL.md`（Agent 性格配置）和 `USER_PROFILE.md`（用户心理画像）
- **心理学框架**：基于 MBTI 四维度和荣格八维认知功能进行深度人格分析
- **自动注入**：通过 SessionStart hook，每次会话开始时自动加载画像内容
- **渐进沉淀**：会话结束后主动建议更新，静默识别持续出现的行为模式

## 安装

```bash
cp -r . ~/.claude/skills/know-each-other/
```

安装后，说出以下任意一句即可触发：
- *"你不太懂我"*
- *"记住我的工作方式"*
- *"我想初始化我的档案"*

---

*A [Kiro](https://kiro.ai) skill — built for Claude.*
