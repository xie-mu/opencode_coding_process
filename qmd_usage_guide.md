# qmd工具使用指南

## 🎯 检索结果总结

### ✅ 使用qmd工具检索到的所有已下载技能名

**📋 技能列表:**
1. 天气查询技能 ✅
2. 文件管理器技能 ✅
3. 智能计算器技能 ✅
4. 网络搜索技能 ✅
5. PR合并技能 ✅

**📊 统计信息:**
- 总技能数量: 5个
- 技能分类: 实用工具、开发工具
- 检索工具: qmd + 优化检索集合

---

## 🔧 qmd工具功能演示

### 1. 列出所有技能
```bash
qmd list skills
```
**输出:**
```
📋 已下载的技能列表:
-------------------
📋 项目列表 (5 个)
--------------------------------------------------
1. 天气查询技能
   类型: skill | 分类: 实用工具
   路径: /root/.openclaw/workspace/skills/weather-query/SKILL.md

2. 文件管理器技能
   类型: skill | 分类: 实用工具
   路径: /root/.openclaw/workspace/skills/file-manager/SKILL.md

3. 智能计算器技能
   类型: skill | 分类: 实用工具
   路径: /root/.openclaw/workspace/skills/calculator/SKILL.md

4. 网络搜索技能
   类型: skill | 分类: 实用工具
   路径: /root/.openclaw/workspace/skills/web-search/SKILL.md

5. PR合并技能
   类型: skill | 分类: 开发工具
   路径: /root/.openclaw/workspace/skills/openclaw-skills/.agents/skills/merge-pr/SKILL.md
```

### 2. 搜索特定技能
```bash
qmd search '天气查询'
```
**输出:**
```
🔍 搜索所有: '天气查询'
--------------------------------------------------
1. 天气查询技能
   类型: skill | 分类: 实用工具
   路径: /root/.openclaw/workspace/skills/weather-query/SKILL.md
   关键词: 查询, 创建, 系统, 技能集成, author
```

### 3. 按类型搜索
```bash
qmd search '文件管理' --type skill
```
**输出:**
```
🔍 搜索技能: '文件管理'
--------------------------------------------------
1. 文件管理器技能
   类型: skill | 分类: 实用工具
   路径: /root/.openclaw/workspace/skills/file-manager/SKILL.md
   关键词: 实现复杂的文件操作, 复制, 移动, 基于名称, 大小搜索
```

### 4. 查看集合信息
```bash
qmd collection info
```
**输出:**
```
📊 集合信息:
-----------
集合名称: OpenClaw文档与技能集合
版本: 2.0.0
创建时间: 2026-02-08
总项目数: 9
优化状态: 已优化
检索索引: 已启用
文档数量: 4
技能数量: 5
```

---

## 📚 技能详情

### 1. 天气查询技能
- **类型**: 实用工具
- **功能**: 查询天气信息
- **关键词**: 查询, 创建, 系统, 技能集成, author
- **路径**: `/root/.openclaw/workspace/skills/weather-query/SKILL.md`

### 2. 文件管理器技能
- **类型**: 实用工具
- **功能**: 文件操作管理
- **关键词**: 实现复杂的文件操作, 复制, 移动, 基于名称, 大小搜索
- **路径**: `/root/.openclaw/workspace/skills/file-manager/SKILL.md`

### 3. 智能计算器技能
- **类型**: 实用工具
- **功能**: 数学计算和科学计算
- **关键词**: 数学, 计算, 科学, 高级, 功能
- **路径**: `/root/.openclaw/workspace/skills/calculator/SKILL.md`

### 4. 网络搜索技能
- **类型**: 实用工具
- **功能**: 网络信息搜索
- **关键词**: 搜索, 网络, 信息, 查询, 结果
- **路径**: `/root/.openclaw/workspace/skills/web-search/SKILL.md`

### 5. PR合并技能
- **类型**: 开发工具
- **功能**: Git PR合并操作
- **关键词**: PR, 合并, 代码, 分支, 提交
- **路径**: `/root/.openclaw/workspace/skills/openclaw-skills/.agents/skills/merge-pr/SKILL.md`

---

## 🚀 快速使用

### 安装qmd工具
```bash
# 已安装完成
npm install -g qmd
```

### 配置环境
```bash
# 添加到PATH
export PATH="/root/.openclaw/workspace:$PATH"
```

### 常用命令
```bash
# 列出所有技能
qmd list skills

# 搜索技能
qmd search '天气查询'
qmd search '文件管理' --type skill

# 查看集合信息
qmd collection info
```

---

## 📈 性能特点

- **检索速度**: 毫秒级响应
- **索引优化**: 关键词索引 + MD5哈希
- **缓存机制**: 提高重复查询效率
- **类型过滤**: 精确匹配文档和技能

---

## 🔄 更新维护

### 重新构建检索集合
```bash
python3 /root/.openclaw/workspace/build_retrieval_collection.py
```

### 更新技能列表
```bash
# 添加新技能后重新运行构建脚本
qmd list skills
```

---

**最后更新**: 2026-02-08
**qmd版本**: 1.0.0
**检索集合**: OpenClaw文档与技能集合