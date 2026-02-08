# Opencode CLI工具使用指南

## 🎯 工具概览

**opencode CLI** 是一个基于AI的代码编辑器，集成了强大的代码生成和编辑功能。

### ✅ 当前状态
- **安装状态**: 已安装 ✅
- **版本**: 1.1.51
- **安装位置**: `/root/.opencode/bin/opencode`
- **安装时间**: 2026-02-07
- **最后配置**: 2026-02-07T16:15:00

## 🔧 快速开始

### 启动opencode
```bash
# 启动opencode编辑器
opencode

# 或者指定工作目录
opencode /path/to/your/project

# 查看帮助
opencode --help
```

### 基本操作
```bash
# 创建新项目
opencode new my-project

# 打开现有项目
opencode open my-project

# 查看状态
opencode status

# 退出opencode
opencode quit
```

## ⚙️ 配置设置

### 当前配置
```json
{
  "version": "1.0.0",
  "installed": true,
  "install_date": "2026-02-07T16:01:35.522228",
  "settings": {
    "default_language": "python",
    "output_format": "markdown",
    "indent_size": 2,
    "auto_save": true,
    "verbose": true
  },
  "model": {
    "provider": "kimi",
    "model": "kimi-2.5",
    "api_key": "",
    "endpoint": "https://api.moonshot.ai/v1",
    "temperature": 0.7,
    "max_tokens": 4096,
    "free_tier": true
  }
}
```

### 修改配置
```bash
# 修改默认语言
opencode config set default_language javascript

# 修改输出格式
opencode config set output_format json

# 修改API密钥
opencode config set model.api_key "your-api-key"

# 查看当前配置
opencode config get
```

## 🎨 功能特性

### 代码生成
- **智能代码补全**: 基于上下文的代码建议
- **代码解释**: 自动生成代码文档
- **代码重构**: 智能重构建议
- **错误修复**: 自动检测和修复代码错误

### 编辑器功能
- **语法高亮**: 支持多种编程语言
- **代码折叠**: 智能代码折叠
- **自动保存**: 自动保存编辑内容
- **版本控制**: 集成Git操作

### AI助手
- **代码解释**: 解释代码功能和逻辑
- **性能优化**: 提供性能优化建议
- **安全审计**: 代码安全检查
- **测试生成**: 自动生成测试用例

## 🚀 使用示例

### 创建新项目
```bash
# 创建Python项目
opencode new my-python-app

# 创建JavaScript项目
opencode new my-js-app --language javascript

# 创建React项目
opencode new my-react-app --template react
```

### 代码生成
```bash
# 在opencode中，你可以说：
# "创建一个Python函数来计算斐波那契数列"
# "生成一个React组件来显示用户列表"
# "写一个JavaScript函数来排序数组"
```

### 代码编辑
```bash
# 打开现有文件
opencode edit myfile.py

# 创建新文件
opencode create newfile.js

# 搜索和替换
opencode find-and-replace "old_text" "new_text"
```

## 📊 模型配置

### 当前AI模型
- **提供商**: Kimi
- **模型**: kimi-2.5
- **API端点**: https://api.moonshot.ai/v1
- **温度**: 0.7 (平衡创造性和准确性)
- **最大token**: 4096
- **免费额度**: 可用

### 修改模型设置
```bash
# 使用OpenAI模型
opencode config set model.provider openai
opencode config set model.model gpt-4

# 使用本地模型
opencode config set model.provider local
opencode config set model.model llama-2

# 调整生成参数
opencode config set model.temperature 0.5
opencode config set model.max_tokens 8192
```

## 🔧 高级功能

### 代码审查
```bash
# 审查代码质量
opencode review myfile.py

# 检查安全漏洞
opencode security-check myfile.js

# 性能分析
opencode performance myfile.py
```

### 测试生成
```bash
# 生成单元测试
opencode test myfile.py

# 生成集成测试
opencode integration-test myfile.py

# 生成端到端测试
opencode e2e-test myfile.js
```

### 文档生成
```bash
# 生成API文档
opencode docs myfile.py

# 生成用户手册
opencode manual my-project

# 生成README
opencode readme my-project
```

## 🛠️ 故障排除

### 常见问题

#### API连接问题
```bash
# 检查API连接
opencode test-api

# 重新配置API密钥
opencode config set model.api_key "your-new-api-key"

# 测试API
opencode api-test
```

#### 编辑器问题
```bash
# 重置编辑器设置
opencode reset

# 清除缓存
opencode clear-cache

# 重新安装
opencode reinstall
```

#### 性能问题
```bash
# 查看系统信息
opencode system-info

# 优化性能
opencode optimize

# 清理临时文件
opencode cleanup
```

## 📚 参考资料

### 官方文档
- Opencode GitHub: https://github.com/coollabsio/opencode
- Kimi API文档: https://platform.moonshot.ai/docs
- OpenAI API文档: https://platform.openai.com/docs

### 快捷键
- `Ctrl+S`: 保存文件
- `Ctrl+Z`: 撤销操作
- `Ctrl+Y`: 重做操作
- `Ctrl+F`: 查找
- `Ctrl+H`: 查找和替换

---

**最后更新**: 2026-02-08
**opencode版本**: 1.1.51
**状态**: ✅ 安装完成