---
title: '[2026/05/18] DeepTalk Agent — 本地语音 AI 助手开源'
date: 2026-05-18
permalink: /posts/deeptalk-agent
---

## 项目介绍

**DeepTalk Agent** 是一个完全基于 [MLX](https://github.com/ml-explore/mlx) 框架运行在 macOS Apple Silicon 上的本地语音对话助手。所有 AI 推理均在本地完成，无需联网，保护隐私的同时实现低延迟的实时语音交互。

> GitHub: [Young-Chin/DeepTalk-Agent](https://github.com/Young-Chin/DeepTalk-Agent)

## 核心特性

- **完全本地离线**：ASR / LLM / TTS 全部运行在本地，首次运行自动下载模型，之后无需网络
- **实时流式响应**：LLM 输出按句子流式切分，即时合成语音播放，降低等待感知
- **支持打断**：播放过程中可随时打断，进入下一轮对话
- **双模式交互**：支持 CLI 推按说话 和 Web UI（带 Three.js 3D 动态球体可视化）

## 技术架构

```
🎤 Mic ──→ 📝 ASR ──→ 🧠 LLM ──→ 🔊 TTS ──→ 🔈 Speaker
            │                    │
            └── 本地离线 ─────────┴── 支持打断
```

| 组件 | 模型 | 大小 |
|:----:|:----:|:----:|
| 🎤 ASR | Qwen3-ASR-0.6B | ~500MB |
| 🧠 LLM | Gemma-4-E2B-4bit | ~2GB |
| 🔊 TTS | Qwen3-TTS-0.6B | ~800MB |

## 快速开始

```bash
git clone https://github.com/Young-Chin/DeepTalk-Agent.git
cd DeepTalk-Agent
uv sync

# CLI 模式
python -m app.main

# Web UI 模式
python run.py
```

## 当前状态与展望

目前版本是一个完整的本地语音对话基础管道，具备端到端的交互流程和现代化 Web UI。未来会在此基础上进一步细化 Agent 能力和使用场景，重点平衡 Agent 智能与时延体验。

---

*License: [Apache 2.0](https://github.com/Young-Chin/DeepTalk-Agent/blob/main/LICENSE)*
