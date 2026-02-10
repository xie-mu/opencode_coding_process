# OpenClaw AI Agent 系统文档总结

## 核心概念

### 什么是 OpenClaw？
OpenClaw 是一个 WhatsApp + Telegram + Discord + iMessage 网关，用于 **Pi** 代理。它是一个端到端的个人助理解决方案，可以将多个消息平台连接到 AI 代理系统。

### 核心组件

1. **Agent Runtime (🤖)**
   - 基于 pi-mono 构建的嵌入式代理运行时
   - 单个工作空间作为代理的唯一工作目录
   - 支持会话管理和工具集成

2. **工作空间 (Workspace)**
   - 代理的"记忆"和操作指南
   - 包含关键文件：
     - `AGENTS.md` - 操作指南和记忆
     - `SOUL.md` - 人格、边界和语调
     - `TOOLS.md` - 工具使用说明
     - `IDENTITY.md` - 代理名称、特征和表情符号
     - `USER.md` - 用户配置文件
     - `HEARTBEAT.md` - 周期性检查任务

3. **多代理路由 (Multi-Agent)**
   - 支持多个隔离的代理（独立工作空间、认证和会话）
   - 通过绑定（bindings）将入站消息路由到特定代理
   - 每个代理可以有不同的个性、模型和工具配置

## 安全设置

### ⚠️ 安全第一
- 代理可以：
  - 在您的机器上运行命令
  - 读写工作空间文件
  - 通过 WhatsApp/Telegram/Discord 发送消息

### 推荐配置
```json5
{
  channels: {
    whatsapp: {
      allowFrom: ["+15555550123"] // 仅允许特定号码
    }
  },
  agent: {
    heartbeat: { every: "0m" } // 初始禁用心跳
  }
}
```

## 代理配置

### 人格设置
在 `SOUL.md` 中定义：
- 人格特质
- 边界限制
- 语调风格

### 工具配置
在 `TOOLS.md` 中记录：
- 摄像头位置
- SSH 连接信息
- TTS 语音偏好
- 设备昵称

### 身份设置
在 `IDENTITY.md` 中设置：
- 代理名称
- 代理类型（AI/机器人/精灵等）
- 语调风格
- 表情符号

## 多代理系统

### 代理隔离
每个代理拥有：
- 独立的工作空间
- 独立的认证配置
- 独立的会话存储

### 路由规则
消息路由遵循确定性原则：
1. 精确 peer 匹配（DM/群组 ID）
2. guildId 匹配（Discord）
3. teamId 匹配（Slack）
4. accountId 匹配
5. 通道级别匹配
6. 默认代理

### 使用场景
1. **家庭代理**：绑定到家庭群组，严格工具限制
2. **工作代理**：使用高级模型处理深度工作
3. **日常聊天**：使用快速模型处理日常对话

## 心跳机制

### 周期性检查
默认每 30 分钟运行一次心跳：
```
Read HEARTBEAT.md if it exists. Follow it strictly. If nothing needs attention, reply HEARTBEAT_OK.
```

### 心跳任务
可以设置定期检查：
- 邮件检查
- 日历事件
- 天气信息
- 项目状态

## 媒体处理

### 入站媒体
支持通过模板传递附件：
- `{{MediaPath}}` - 本地临时文件路径
- `{{MediaUrl}}` - 伪 URL
- `{{Transcript}}` - 音频转录文本

### 出站媒体
代理可以通过以下方式发送媒体：
```
这里是我的截图。
MEDIA:https://example.com/screenshot.png
```

## 操作命令

### 基础命令
```bash
openclaw status          # 本地状态检查
openclaw status --all    # 完整诊断
openclaw status --deep   # 深度检查（包含网关健康）
openclaw health --json   # 网关健康快照
```

### 代理管理
```bash
openclaw agents add <name>     # 添加新代理
openclaw agents list --bindings # 查看绑定
openclaw setup                # 初始化工作空间
```

## 配置文件结构

### 最小配置
```json5
{
  agents: {
    defaults: {
      workspace: "~/.openclaw/workspace"
    }
  },
  channels: {
    whatsapp: {
      allowFrom: ["+15555550123"]
    }
  }
}
```

### 完整配置示例
```json5
{
  logging: { level: "info" },
  agent: {
    model: "anthropic/claude-opus-4-6",
    workspace: "~/.openclaw/workspace",
    thinkingDefault: "high",
    timeoutSeconds: 1800,
    heartbeat: { every: "30m" }
  },
  channels: {
    whatsapp: {
      allowFrom: ["+15555550123"],
      groups: {
        "*": { requireMention: true }
      }
    }
  },
  routing: {
    groupChat: {
      mentionPatterns: ["@openclaw", "openclaw"]
    }
  }
}
```

## 会话管理

### 会话文件
- 存储位置：`~/.openclaw/agents/<agentId>/sessions/<SessionId>.jsonl`
- 会话元数据：`~/.openclaw/agents/<agentId>/sessions/sessions.json`

### 会话控制
- `/new` 或 `/reset` 开始新会话
- `/compact [instructions]` 压缩会话上下文

## 下一步

1. **WebChat**: [WebChat 文档](/web/webchat)
2. **网关操作**: [网关运行手册](/gateway)
3. **定时任务**: [Cron 任务](/automation/cron-jobs)
4. **平台支持**: macOS/iOS/Android/Linux 应用
5. **安全**: [安全配置](/gateway/security)