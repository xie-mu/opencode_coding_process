# OpenClaw AI Agent 系统

这是一个基于 OpenClaw 构建的 AI Agent 系统文档集合。

## 📚 核心文档

- **[SUMMARY.md](SUMMARY.md)** - OpenClaw 核心概念和配置总结
- **[AI-Agent-System-Guide.md](AI-Agent-System-Guide.md)** - 详细的使用指南和最佳实践
- **[Reminder-Guide.md](Reminder-Guide.md)** - 定时提醒系统使用指南
- **[README.md](README.md)** - 快速入门指南

## 🚀 快速开始

### 1. 安装 OpenClaw
```bash
openclaw setup
```

### 2. 初始化工作空间
```bash
openclaw setup --workspace ~/.openclaw/workspace
```

### 3. 配置代理
编辑 `~/.openclaw/openclaw.json`：
```json5
{
  "agents": {
    "defaults": {
      "workspace": "~/.openclaw/workspace",
      "model": "anthropic/claude-opus-4-6"
    }
  },
  "channels": {
    "whatsapp": {
      "allowFrom": ["+15555550123"]
    }
  }
}
```

### 4. 启动网关
```bash
openclaw gateway --port 18789
```

### 5. 设置定时提醒（可选）
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

## 🎯 核心特性

- **多代理支持**：创建多个隔离的 AI 代理
- **多平台集成**：支持 WhatsApp、Telegram、Discord、iMessage
- **安全隔离**：每个代理独立的工作空间和工具权限
- **人格定制**：通过 SOUL.md 和 IDENTITY.md 定义代理个性
- **心跳机制**：周期性任务检查和自动化提醒
- **媒体处理**：支持图片、音频、文档的收发和处理

## 📖 重要文件

- `SOUL.md` - 代理人格定义
- `IDENTITY.md` - 代理身份设置
- `AGENTS.md` - 操作指南
- `TOOLS.md` - 工具使用说明
- `HEARTBEAT.md` - 周期性任务

## 🔧 常用命令

### 代理管理
```bash
# 查看状态
openclaw status

# 添加代理
openclaw agents add <name>

# 查看绑定
openclaw agents list --bindings

# 健康检查
openclaw health --json
```

### 定时任务管理
```bash
# 列出所有定时任务
openclaw cron list

# 查看任务运行历史
openclaw cron runs <jobId>

# 立即运行任务
openclaw cron run <jobId>

# 删除任务
openclaw cron remove <jobId>
```

### 心跳管理
```bash
# 查看心跳状态
openclaw status --heartbeat

# 修改心跳配置
# 编辑 ~/.openclaw/openclaw.json 中的 heartbeat 配置
```

## 🛡️ 安全建议

1. **访问控制**：始终设置 `allowFrom` 限制访问
2. **专用号码**：使用专用电话号码，避免使用个人号码
3. **初始设置**：初始禁用 heartbeat 机制，待信任后再启用
4. **定期备份**：定期备份工作空间文件
5. **日志监控**：定期检查代理活动日志
6. **工具限制**：为不同代理设置适当的工具权限
7. **一次性任务**：使用 `--delete-after-run` 避免重复提醒

## 📞 支持

- 文档：https://docs.openclaw.ai
- 社区：https://discord.com/invite/clawd
- 问题反馈：GitHub Issues

---

**祝您使用愉快！如有问题，请随时提问。**