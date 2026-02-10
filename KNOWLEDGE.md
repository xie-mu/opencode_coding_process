# OpenClaw AI Agent 系统知识库

## 📖 文档索引

### 快速入门
- **[README.md](README.md)** - 快速入门指南
- **[SUMMARY.md](SUMMARY.md)** - 核心概念总结

### 详细指南
- **[AI-Agent-System-Guide.md](AI-Agent-System-Guide.md)** - AI Agent 系统完整指南
- **[Reminder-Guide.md](Reminder-Guide.md)** - 定时提醒系统指南

## 🎯 核心概念

### 代理系统 (Agent System)
- **定义**：基于 pi-mono 的嵌入式代理运行时
- **工作空间**：代理的唯一工作目录
- **会话管理**：稳定的会话ID和状态存储
- **人格定制**：通过 SOUL.md 和 IDENTITY.md 定义个性

### 多代理路由 (Multi-Agent Routing)
- **隔离性**：每个代理独立的工作空间、认证和会话
- **路由规则**：确定性路由，最具体匹配优先
- **应用场景**：
  - 家庭代理：绑定到家庭群组，严格工具限制
  - 工作代理：使用高级模型处理深度工作
  - 日常聊天：使用快速模型处理日常对话

### 消息平台集成
- **支持平台**：WhatsApp、Telegram、Discord、iMessage
- **账户管理**：多账户支持，每个账户可路由到不同代理
- **绑定机制**：基于通道、账户ID、peer ID 的确定性路由

## ⚙️ 配置系统

### 核心配置文件
- **主配置**：`~/.openclaw/openclaw.json`
- **工作空间**：`~/.openclaw/workspace/`
- **代理配置**：`~/.openclaw/agents/<agentId>/agent/`

### 关键配置项
```json5
{
  "agents": {
    "defaults": {
      "workspace": "~/.openclaw/workspace",
      "model": "anthropic/claude-opus-4-6",
      "thinkingDefault": "high",
      "timeoutSeconds": 1800,
      "heartbeat": { "every": "30m" }
    },
    "list": [
      {
        "id": "personal",
        "workspace": "~/.openclaw/workspace-personal",
        "sandbox": { "mode": "off" }
      }
    ]
  },
  "channels": {
    "whatsapp": {
      "allowFrom": ["+15555550123"],
      "accounts": { "personal": {} }
    }
  },
  "bindings": [
    { "agentId": "personal", "match": { "channel": "whatsapp" } }
  ]
}
```

## 🛠️ 工具系统

### 核心工具
- **文件操作**：read、write、edit、apply_patch
- **执行命令**：exec（受工具策略限制）
- **会话管理**：sessions_list、sessions_history、sessions_send
- **子代理**：sessions_spawn
- **状态检查**：session_status

### 高级工具
- **浏览器控制**：browser（headless 模式）
- **画布系统**：canvas（A2UI 渲染）
- **节点管理**：nodes（摄像头、屏幕控制）
- **定时任务**：cron（精确调度）
- **心跳系统**：heartbeat（周期性检查）

### 工具策略
```json5
{
  "tools": {
    "exec": { "allowed": true, "timeout": 300 },
    "browser": { "enabled": true, "headless": true },
    "nodes": { "enabled": true, "camera": ["living-room"] },
    "cron": { "enabled": true },
    "heartbeat": { "enabled": true }
  }
}
```

## 🔄 自动化系统

### 心跳机制 (Heartbeat)
- **默认间隔**：30分钟
- **触发条件**：HEARTBEAT.md 文件存在且非空
- **智能抑制**：回复 `HEARTBEAT_OK` 时不发送消息
- **配置选项**：
  ```json5
  {
    "heartbeat": {
      "every": "30m",
      "target": "last",
      "activeHours": { "start": "08:00", "end": "22:00" }
    }
  }
  ```

### 定时任务 (Cron)
- **调度格式**：5字段 cron 表达式
- **时区支持**：完整的 timezone 配置
- **会话类型**：
  - `isolated`：隔离会话，不影响主会话
  - `main`：主会话，通过系统事件触发
- **交付模式**：
  - `announce`：发送摘要（默认）
  - `none`：仅内部处理

### 决策流程图
```
需要精确时间？ → YES → 使用 cron
                ↓ NO
需要会话隔离？ → YES → 使用 cron (isolated)
                ↓ NO
可以批量处理？ → YES → 使用 heartbeat
                ↓ NO
一次性提醒？ → YES → 使用 cron with --at
                ↓ NO
需要不同模型？ → YES → 使用 cron (isolated) with --model
                ↓ NO → 使用 heartbeat
```

## 💾 会话管理

### 会话存储
- **文件路径**：`~/.openclaw/agents/<agentId>/sessions/<SessionId>.jsonl`
- **元数据**：`~/.openclaw/agents/<agentId>/sessions/sessions.json`

### 会话控制
- **重置触发器**：`/new`、`/reset`
- **自动重置**：每日凌晨4点或空闲1周后
- **会话范围**：`per-sender`（每个发送者独立会话）

## 🛡️ 安全系统

### 访问控制
- **通道限制**：`channels.whatsapp.allowFrom`
- **代理限制**：`agents.list[].groupChat.mentionPatterns`
- **工具限制**：`agents.list[].tools.allow/deny`

### 沙箱配置
```json5
{
  "sandbox": {
    "mode": "all", // off | all | none
    "scope": "agent", // shared | agent
    "docker": {
      "setupCommand": "apt-get update && apt-get install -y git curl"
    }
  }
}
```

### 安全最佳实践
1. 始终设置 `allowFrom` 限制访问
2. 使用专用电话号码
3. 初始禁用 heartbeat 机制
4. 为不同代理设置适当的工具权限
5. 定期备份工作空间
6. 监控代理活动日志

## 📱 媒体处理

### 入站媒体
- **模板变量**：
  - `{{MediaPath}}`：本地临时文件路径
  - `{{MediaUrl}}`：伪 URL
  - `{{Transcript}}`：音频转录文本

### 出站媒体
- **格式**：`MEDIA:<path-or-url>`
- **示例**：
  ```
  这里是我的截图。
  MEDIA:https://example.com/screenshot.png
  ```

## 🔧 操作命令

### 基础命令
```bash
openclaw status                    # 本地状态检查
openclaw status --all              # 完整诊断
openclaw status --deep             # 深度检查（包含网关健康）
openclaw health --json             # 网关健康快照
```

### 代理管理
```bash
openclaw agents add <name>         # 添加新代理
openclaw agents list --bindings    # 查看绑定配置
openclaw setup                     # 初始化工作空间
```

### 定时任务
```bash
openclaw cron list                 # 列出所有定时任务
openclaw cron runs <jobId>         # 查看任务运行历史
openclaw cron run <jobId>          # 立即运行任务
openclaw cron remove <jobId>       # 删除任务
```

### 心跳管理
```bash
openclaw status --heartbeat        # 查看心跳状态
# 编辑 ~/.openclaw/openclaw.json 中的 heartbeat 配置
```

## 📚 相关文档

### OpenClaw 文档
- [WebChat 文档](/web/webchat)
- [网关运行手册](/gateway)
- [定时任务文档](/automation/cron-jobs)
- [安全配置文档](/gateway/security)

### 技能文档
- [多代理沙箱工具](/tools/multi-agent-sandbox-tools)
- [子代理系统](/tools/subagents)
- [浏览器工具](/tools/browser)
- [节点管理](/tools/nodes)

## 🚀 快速参考

### 创建第一个代理
```bash
openclaw setup
# 编辑 ~/.openclaw/openclaw.json
openclaw gateway --port 18789
```

### 设置定时提醒
```bash
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

### 配置多代理
```json5
{
  "agents": {
    "list": [
      {
        "id": "personal",
        "workspace": "~/.openclaw/workspace-personal",
        "sandbox": { "mode": "off" }
      },
      {
        "id": "family",
        "workspace": "~/.openclaw/workspace-family",
        "sandbox": { "mode": "all", "scope": "agent" },
        "tools": {
          "allow": ["read"],
          "deny": ["exec", "write", "edit"]
        }
      }
    ]
  }
}
```

## ❓ 常见问题

### Q: 如何设置代理的人格？
A: 编辑工作空间中的 `SOUL.md` 和 `IDENTITY.md` 文件。

### Q: 如何创建定时提醒？
A: 使用 `openclaw cron add` 命令，选择合适的时间格式和会话类型。

### Q: 如何限制代理的工具权限？
A: 在代理配置中使用 `tools.allow` 和 `tools.deny` 列表。

### Q: 如何查看代理的运行状态？
A: 使用 `openclaw status` 和 `openclaw health --json` 命令。

### Q: 如何备份代理配置？
A: 将整个工作空间目录作为 git 仓库管理，或使用 `openclaw setup` 初始化时自动创建。

---

**更多详细信息，请查看各个文档文件！**