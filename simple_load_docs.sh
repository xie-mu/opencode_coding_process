#!/bin/bash

echo "📚 开始加载OpenClaw相关文档..."

# 创建docs目录
mkdir -p docs

# 检查并下载文档
if [ ! -d "docs/openclaw" ]; then
    echo "🌐 下载OpenClaw官方文档..."
    git clone https://github.com/openclaw/openclaw.git docs/openclaw
fi

if [ ! -d "docs/clawhub" ]; then
    echo "🔧 下载ClawHub文档..."
    git clone https://github.com/openclaw/clawhub.git docs/clawhub
fi

echo "✅ 文档加载完成！"
echo "📁 已加载到：docs/openclaw/ 和 docs/clawhub/"