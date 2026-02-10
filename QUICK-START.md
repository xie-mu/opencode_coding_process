# OpenClaw AI Agent 系统 - 快速开始

## 🎯 我们为您整理了什么？

基于您提供的微信文章"借助 AI Coding 快速打造 AI Agent 系统"和 OpenClaw 官方文档，我们为您创建了一个完整的 AI Agent 系统文档体系。

## 📚 核心文档

### 🚀 立即开始
**[README.md](README.md)** - 5分钟快速入门指南

### 📖 学习路径
1. **[SUMMARY.md](SUMMARY.md)** - OpenClaw 核心概念总结
2. **[AI-Agent-System-Guide.md](AI-Agent-System-Guide.md)** - 详细使用指南
3. **[Reminder-Guide.md](Reminder-Guide.md)** - 定时提醒系统
4. **[KNOWLEDGE.md](KNOWLEDGE.md)** - 完整知识库
5. **[LEARNING-SUMMARY.md](LEARNING-SUMMARY.md)** - 学习总结

## 🔧 快速上手

### 1. 安装 OpenClaw
```bash
openclaw setup
```

### 2. 启动网关
```bash
openclaw gateway --port 18789
```

### 3. 创建定时提醒
```bash
# 5分钟后提醒喝水
openclaw cron add \
  --name "提醒喝水" \
  --at "5m" \
  --session isolated \
  --message "💧 该喝水啦！" \
  --deliver \
  --channel qqbot \
  --to "85EAAA7E3B6F73D23B4708739A38083F" \
  --delete-after-run
```

## 📁 重要文件

- `SOUL.md` - 定义代理人格
- `IDENTITY.md` - 设置代理身份
- `AGENTS.md` - 操作指南
- `HEARTBEAT.md` - 心跳任务清单
- `~/.openclaw/openclaw.json` - 主配置文件

## 🛡️ 安全建议

1. 使用专用电话号码
2. 设置 `allowFrom` 限制访问
3. 初始禁用心跳机制
4. 定期备份工作空间

## 📞 支持

- **文档**：https://docs.openclaw.ai
- **社区**：https://discord.com/invite/clawd
- **问题**：GitHub Issues

---

**祝您使用 OpenClaw 愉快！如有问题，请随时提问。**