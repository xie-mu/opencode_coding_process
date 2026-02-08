# OpenClaw检索系统使用指南

## 🎯 系统概述

这是一个基于OpenClaw文档和技能的智能检索系统，通过qpd工具和qmd技能构建，用于加速文档和技能的检索效率。

## 📦 系统组件

### 1. qpd工具
- 用于Python包管理
- 已安装版本: qpd@0.0.0

### 2. qmd技能
- 用于技能管理和检索
- 已安装版本: qmd@0.0.0

### 3. 检索集合
- **位置**: `/root/.openclaw/workspace/collections/optimized_openclaw_collection.json`
- **包含项目**: 9个文档和技能
- **索引方式**: 关键词索引 + 类型分类

## 🚀 快速开始

### 启动检索系统
```bash
bash /root/.openclaw/workspace/start_search_system.sh
```

### 搜索文档和技能
```bash
# 搜索关键词
python3 /root/.openclaw/workspace/quick_search.py search '天气查询'
python3 /root/.openclaw/workspace/quick_search.py search '文件管理'
python3 /root/.openclaw/workspace/quick_search.py search 'API文档'

# 搜索特定类型
python3 /root/.openclaw/workspace/quick_search.py search '天气查询' skill
python3 /root/.openclaw/workspace/quick_search.py search 'CLI文档' document

# 列出所有项目
python3 /root/.openclaw/workspace/quick_search.py list skill
python3 /root/.openclaw/workspace/quick_search.py list document
```

### 重新构建检索集合
```bash
python3 /root/.openclaw/workspace/build_retrieval_collection.py
```

## 📊 检索集合内容

### 文档 (5个)
1. **OpenClaw官方文档** - 核心文档
2. **ClawHub官方文档** - 核心文档
3. **ClawHub API文档** - API文档
4. **ClawHub架构文档** - 架构文档
5. **ClawHub CLI文档** - CLI文档

### 技能 (7个)
1. **天气查询技能** - 实用工具
2. **文件管理器技能** - 实用工具
3. **智能计算器技能** - 实用工具
4. **网络搜索技能** - 实用工具
5. **数据分析技能** - 实用工具
6. **PR合并技能** - 开发工具

## 🔍 搜索功能

### 关键词搜索
- 支持中文关键词搜索
- 支持英文关键词搜索
- 自动过滤停用词

### 类型过滤
- `document`: 仅搜索文档
- `skill`: 仅搜索技能
- 无参数: 搜索所有类型

### 分类检索
- 实用工具
- 开发工具
- 核心文档
- API文档
- 架构文档
- CLI文档

## ⚙️ 系统维护

### 更新检索集合
当文档或技能更新时，运行：
```bash
python3 /root/.openclaw/workspace/build_retrieval_collection.py
```

### 查看集合信息
```bash
cat /root/.openclaw/workspace/collections/optimized_openclaw_collection.json | python3 -m json.tool
```

## 📈 性能优化

- **索引优化**: 使用MD5哈希值快速比较内容
- **关键词提取**: 自动提取中英文关键词
- **缓存机制**: 搜索结果缓存提高重复查询效率
- **类型分类**: 按文档类型和技能类型分类存储

## 🔧 自定义扩展

### 添加新文档
1. 将文档添加到 `docs/` 目录
2. 更新 `collections/openclaw-docs-skills.json`
3. 重新构建检索集合

### 添加新技能
1. 将技能添加到 `skills/` 目录
2. 更新 `collections/openclaw-docs-skills.json`
3. 重新构建检索集合

## 📝 使用示例

### 搜索天气相关功能
```bash
python3 quick_search.py search '天气查询' skill
```
**结果**: 找到"天气查询技能"，包含关键词: 查询, 创建, 系统, 技能集成

### 搜索文件管理功能
```bash
python3 quick_search.py search '文件管理' skill
```
**结果**: 找到"文件管理器技能"，包含关键词: 文件, 管理, 操作, 删除, 移动

### 搜索API文档
```bash
python3 quick_search.py search 'API文档' document
```
**结果**: 找到"ClawHub API文档"，包含关键词: API, 接口, 认证, 技能, 部署

## 🎯 最佳实践

1. **定期更新**: 每周运行一次集合重建
2. **关键词优化**: 使用具体、描述性的关键词
3. **类型过滤**: 使用类型参数提高搜索精度
4. **组合搜索**: 结合关键词和类型进行精确搜索

## 📞 技术支持

如有问题，请检查:
1. Python环境是否正确配置
2. 检索集合文件是否存在
3. 文件路径是否正确
4. 权限设置是否正确

---

**最后更新**: 2026-02-08
**系统版本**: 1.0.0