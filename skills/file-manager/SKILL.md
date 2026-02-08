---
name: 文件管理器
description: 文件操作和管理工具
version: 1.0.0
author: 电子核动力驴
tags: [文件, 管理, 工具, 系统]
---

# 文件管理器技能

这是一个强大的文件操作和管理工具，提供丰富的文件管理功能。

## 功能特性

- 📁 **文件浏览** - 递归查看目录结构
- 📋 **文件操作** - 复制、移动、删除、重命名
- 🔍 **文件搜索** - 基于名称、内容、大小搜索
- 📊 **文件统计** - 目录大小、文件数量统计
- 🔒 **权限管理** - 文件权限设置和修改
- 📈 **磁盘分析** - 磁盘使用情况分析

## 使用方法

```bash
# 浏览目录
file-manager browse --path /home/user

# 搜索文件
file-manager search --name "*.txt" --path /home

# 统计目录大小
file-manager stats --path /home/user/documents
```

## 技能集成

该技能展示了如何：
1. 创建系统级工具技能
2. 实现复杂的文件操作
3. 提供命令行接口
4. 集成到OpenClaw系统
