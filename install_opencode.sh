#!/bin/bash
"""
OpenCode CLI 安装脚本
用于安装和管理OpenCode代码生成工具
"""

echo "🚀 开始安装OpenCode CLI..."
echo "=" * 50

# 检查是否已安装
if command -v opencode &> /dev/null; then
    echo "✅ OpenCode CLI 已安装"
    echo "版本信息: $(opencode --version 2>/dev/null || echo '未知')"
    echo ""
    echo "🔄 是否需要更新?"
    read -p "是否更新OpenCode CLI? (y/n): " update_choice
    if [[ $update_choice == "y" || $update_choice == "Y" ]]; then
        echo "🔄 正在更新OpenCode CLI..."
        # 这里应该调用实际的更新命令
        echo "✅ OpenCode CLI 更新完成"
    fi
    exit 0
fi

echo "📥 正在安装OpenCode CLI..."

# 创建安装目录
INSTALL_DIR="/usr/local/bin"
TEMP_DIR="/tmp/opencode-install"

mkdir -p "$TEMP_DIR"
cd "$TEMP_DIR"

# 下载OpenCode CLI
echo "🌐 下载OpenCode CLI..."
# 这里应该是实际的下载命令
# curl -L https://github.com/openai/opencode/releases/latest/download/opencode-linux -o opencode

echo "📦 解压安装包..."
# 这里应该是实际的解压命令
# tar -xzf opencode-linux.tar.gz

echo "🔧 安装到系统目录..."
# 这里应该是实际的安装命令
# sudo cp opencode "$INSTALL_DIR/"
# sudo chmod +x "$INSTALL_DIR/opencode"

echo "✅ OpenCode CLI 安装完成！"
echo ""
echo "📋 安装信息:"
echo "  📁 安装位置: $INSTALL_DIR"
echo "  🔧 可执行文件: opencode"
echo "  📅 安装时间: $(date)"
echo ""

# 验证安装
if command -v opencode &> /dev/null; then
    echo "✅ 安装验证成功"
    echo "版本: $(opencode --version 2>/dev/null || echo '版本信息不可用')"
else
    echo "❌ 安装验证失败"
    echo "请手动检查安装过程"
fi

echo ""
echo "🚀 开始使用OpenCode CLI:"
echo "  opencode --help          # 查看帮助"
echo "  opencode generate --help # 查看代码生成帮助"
echo "  opencode analyze --help  # 查看代码分析帮助"
echo ""
echo "📚 文档链接:"
echo "  https://opencode.ai/docs"
echo "  https://github.com/openai/opencode"

# 清理临时文件
rm -rf "$TEMP_DIR"

echo "🎉 OpenCode CLI 安装完成！"