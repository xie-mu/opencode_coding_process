---
name: 天气查询技能
description: 查询天气信息和天气预报
version: 1.0.0
author: 电子核动力驴
tags: [天气, 查询, 工具]
---

# 天气查询技能

这是一个示例天气查询技能，演示如何将技能库中的技能集成到OpenClaw系统中。

## 功能特性

- 🌤️ 当前天气查询
- 📅 天气预报
- 🌡️ 温度转换
- 💧 湿度信息
- 💨 风速和风向

## 使用方法

```bash
# 查询当前天气
weather query --city 北京

# 获取天气预报
weather forecast --city 上海 --days 3

# 温度转换
weather convert --temp 25 --from celsius --to fahrenheit
```

## API集成

该技能集成了多个天气API：
- OpenWeatherMap API
- 和风天气API
- 天气API

## 配置要求

```yaml
weather:
  api_key: "your_api_key_here"
  default_city: "北京"
  units: "metric"  # metric, imperial, kelvin
```

## 技能集成

这个技能展示了如何：
1. 创建符合规范的技能包
2. 定义技能功能和API
3. 配置技能参数
4. 集成到OpenClaw系统

**技能库集成状态：**
- ✅ 技能包结构完整
- ✅ 功能文档齐全
- ✅ API接口定义清晰
- ✅ 配置参数明确

## 开发指南

### 技能创建步骤
1. 创建技能文件夹
2. 编写SKILL.md文档
3. 添加必要的代码文件
4. 测试技能功能
5. 发布到技能库

### 技能更新
- 版本号遵循语义化版本规范
- 更新技能描述和功能说明
- 添加新功能模块
- 优化API集成

## 技能库管理

该技能演示了技能库的关键功能：
- 🔍 技能搜索和发现
- 📦 技能包分发
- 🔄 技能更新管理
- ⭐ 技能评分和评价
- 👥 技能社区协作