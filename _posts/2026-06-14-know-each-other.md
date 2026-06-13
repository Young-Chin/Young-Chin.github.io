---
title: 'Know Each Other：让 AI 真正认识你，而不只是记住你的偏好清单'
date: 2026-06-14
permalink: /posts/know-each-other
tags:
  - Claude
  - AI Tools
  - Productivity
---

我用 Claude 很久了，但有一个问题始终没解决：**每次新开会话，它都不认识我。**

我得重新说明我喜欢简洁的回复、不要废话、代码不加注释……每次，都要重新建立这个默契。

所以我做了 [Know Each Other](https://github.com/Young-Chin/know-each-other)。

---

## 它解决什么问题

大多数 AI "记住偏好"的方式，本质上是维护一个清单：
- 回复要简洁
- 不要用 emoji
- 技术问题直接给代码

这些偏好清单有效，但很浅。它记住了**你想要什么**，却不理解**你是怎样的人**。

Know Each Other 的思路不同：通过一次自然对话，用 MBTI 四维度和荣格认知功能框架，生成真正的**心理画像**。

---

## 两个文件，跨项目全局生效

初始化完成后，会在 `~/.claude/` 生成两个文件：

| 文件 | 内容 |
|------|------|
| `SOUL.md` | Agent 的性格：沟通方式、反馈风格、主动程度 |
| `USER_PROFILE.md` | 你的心理画像：认知功能、决策方式、工作模式 |

比如，如果对话中你表现出"先想清楚全局再动手"的倾向，画像里会写：

> *Ni 主导倾向 — 习惯从整体框架向下推导，不喜欢在思路未成形时被追问细节*

这比"不要催我"更有信息量，也更能指导 AI 的行为方式。

---

## 会话开始，自动加载

技能配置好后，会在 `~/.claude/settings.json` 里添加一个 SessionStart hook：

```bash
[ -f ~/.claude/SOUL.md ] && cat ~/.claude/SOUL.md
[ -f ~/.claude/USER_PROFILE.md ] && cat ~/.claude/USER_PROFILE.md
```

每次新开会话，两份档案的完整内容直接注入上下文。Claude 从第一条消息起，就已经"认识"你了。

---

## 它会随着使用慢慢变准

每次有意义的对话结束后，技能会回顾：*这次交互里，你展示了哪些认知模式？*

如果有值得沉淀的内容，它会这样提示：

```
📝 本次对话有些内容值得沉淀到档案：

USER_PROFILE.md → 已观察到的模式：
  + 「反复确认细节再推进 → Si（内向感知）信号」

SOUL.md → 特别约定：
  + 「代码默认不加注释」

确认后写入，或告诉我调整措辞。
```

清晰、主动，但不强制。你来决定写不写。

---

## 安装与触发

```bash
cp -r . ~/.claude/skills/know-each-other/
```

安装后，说以下任意一句即可触发初始化：

- *"你不太懂我"*
- *"记住我的工作方式"*
- *"我想让你有一致的性格"*
- *"你对我有什么了解？"*

---

如果你也觉得每次跟 AI 重新自我介绍这件事很烦，可以试试。

> GitHub: [Young-Chin/know-each-other](https://github.com/Young-Chin/know-each-other)
