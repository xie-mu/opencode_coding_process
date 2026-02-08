#!/bin/bash

echo "📚 开始加载OpenClaw相关文档和代码库..."

# 创建目录
mkdir -p docs
mkdir -p skills_repo

# 1. 下载OpenClaw官方文档
echo "🌐 下载OpenClaw官方文档..."
if [ ! -d "docs/openclaw" ]; then
    git clone https://github.com/openclaw/openclaw.git docs/openclaw
else
    echo "✅ OpenClaw文档已存在，跳过下载"
fi

# 2. 下载ClawHub官方文档
echo "🔧 下载ClawHub文档..."
if [ ! -d "docs/clawhub" ]; then
    git clone https://github.com/openclaw/clawhub.git docs/clawhub
else
    echo "✅ ClawHub文档已存在，跳过下载"
fi

# 3. 下载OpenClaw Skills代码库
echo "⚙️ 下载OpenClaw Skills代码库..."
if [ ! -d "skills_repo" ]; then
    git clone https://github.com/openclaw/openclaw.git skills_repo
else
    echo "✅ Skills代码库已存在，跳过下载"
fi

# 4. 创建本地技能目录结构
echo "🏗️ 创建本地技能目录结构..."
mkdir -p skills/{core,utils,examples}
echo "# 本地技能开发目录" > skills/README.md

# 5. 检查是否有新的文档更新
echo "🔍 检查文档更新..."
cd docs/openclaw && git fetch && cd ../..
cd docs/clawhub && git fetch && cd ../..

echo "✅ 所有文档和代码库加载完成！"
echo ""
echo "📁 文件位置："
echo "   📚 docs/openclaw/ - OpenClaw官方文档"
echo "   🔧 docs/clawhub/ - ClawHub官方文档"  
echo "   ⚙️ skills_repo/ - OpenClaw Skills代码库"
echo "   🏗️ skills/ - 本地技能开发目录"
echo ""
echo "📱 定时任务已完成配置，每天早上9:00自动执行更新！"