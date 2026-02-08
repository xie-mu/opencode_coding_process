#!/bin/bash

echo "📚 开始加载OpenClaw相关文档和代码库..."

# 创建文档目录
mkdir -p docs
cd docs

# 加载OpenClaw官方文档
echo "🌐 下载OpenClaw官方文档..."
git clone https://github.com/openclaw/openclaw.git || echo "文档已存在或克隆失败"

# 加载ClawHub官方文档  
echo "🔧 下载ClawHub文档..."
git clone https://github.com/openclaw/clawhub.git || echo "ClawHub文档已存在或克隆失败"

# 加载OpenClaw Skills代码库
echo "⚙️ 下载OpenClaw Skills代码库..."
cd ..
git clone https://github.com/openclaw/openclaw.git skills_repo || echo "Skills代码库已存在或克隆失败"

echo "✅ 文档和代码库加载完成！"
echo "📁 文件位置："
echo "   - docs/openclaw/"
echo "   - docs/clawhub/"  
echo "   - skills_repo/"