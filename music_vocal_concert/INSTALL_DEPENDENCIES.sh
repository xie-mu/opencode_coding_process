#!/bin/bash
# Music Vocal Concert 依赖安装脚本

echo "📦 Music Vocal Concert 依赖安装"
echo "==============================="
echo ""
echo "🔍 检查环境..."
echo "Python版本: $(python3 --version 2>/dev/null || echo '未安装')"
echo "Node.js版本: $(node --version 2>/dev/null || echo '未安装')"
echo ""

# 安装Python依赖
echo "📦 安装Python依赖..."
echo "requirements.txt内容:"
head -15 requirements.txt
echo "...（省略）"
echo ""

if command -v pip3 &> /dev/null; then
    echo "✅ pip3已安装，开始安装依赖..."
    pip3 install -r requirements.txt
    if [ $? -eq 0 ]; then
        echo "✅ Python依赖安装成功"
    else
        echo "❌ Python依赖安装失败"
        exit 1
    fi
else
    echo "⚠️ pip3未安装，跳过Python依赖安装"
fi

# 安装Node.js依赖
echo ""
echo "📦 安装Node.js依赖..."
echo "package.json内容:"
head -15 package.json
echo "...（省略）"
echo ""

if command -v npm &> /dev/null; then
    echo "✅ npm已安装，开始安装依赖..."
    npm install
    if [ $? -eq 0 ]; then
        echo "✅ Node.js依赖安装成功"
    else
        echo "❌ Node.js依赖安装失败"
        exit 1
    fi
else
    echo "⚠️ npm未安装，跳过Node.js依赖安装"
fi

echo ""
echo "✅ 依赖安装完成！"
echo ""
echo "📋 安装摘要:"
echo "   • Python依赖: $(pip3 list | grep -E '(fastapi|sqlalchemy)' | wc -l) 个包"
echo "   • Node.js依赖: $(npm list --depth=0 2>/dev/null | wc -l) 个包"
echo ""
echo "🎯 下一步:"
echo "   • 配置数据库"
echo "   • 启动开发服务器"
echo "   • 运行测试"

exit 0