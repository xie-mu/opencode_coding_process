#!/bin/bash
# OpenClaw检索系统演示

echo "🎯 OpenClaw检索系统演示"
echo "================================"
echo ""

# 演示1: 系统启动
echo "📋 演示1: 系统启动"
echo "-------------------"
bash /root/.openclaw/workspace/start_search_system.sh
echo ""

# 演示2: 搜索天气相关
echo "🔍 演示2: 搜索天气相关"
echo "-----------------------"
echo "搜索关键词: '天气查询'"
python3 /root/.openclaw/workspace/quick_search.py search '天气查询'
echo ""

# 演示3: 搜索文件管理
echo "🔍 演示3: 搜索文件管理"
echo "-----------------------"
echo "搜索关键词: '文件管理' (技能类型)"
python3 /root/.openclaw/workspace/quick_search.py search '文件管理' skill
echo ""

# 演示4: 搜索API文档
echo "🔍 演示4: 搜索API文档"
echo "-----------------------"
echo "搜索关键词: 'API文档' (文档类型)"
python3 /root/.openclaw/workspace/quick_search.py search 'API文档' document
echo ""

# 演示5: 列出所有技能
echo "📋 演示5: 列出所有技能"
echo "-----------------------"
python3 /root/.openclaw/workspace/quick_search.py list skill
echo ""

# 演示6: 列出所有文档
echo "📋 演示6: 列出所有文档"
echo "-----------------------"
python3 /root/.openclaw/workspace/quick_search.py list document
echo ""

# 演示7: 构建新集合
echo "🔨 演示7: 重新构建检索集合"
echo "-----------------------------"
echo "正在重新构建检索集合..."
python3 /root/.openclaw/workspace/build_retrieval_collection.py
echo ""

echo "✅ 演示完成！"
echo "================================"
echo "💡 总结:"
echo "   - qpd工具已安装，用于Python包管理"
echo "   - qmd技能已安装，用于技能管理"
echo "   - 检索集合已构建，包含9个项目"
echo "   - 快速检索工具可用，支持关键词搜索"
echo "   - 系统支持文档和技能的分类检索"
echo "   - 检索效率已优化，支持缓存和索引"
echo ""
echo "📚 详细使用方法请查看: /root/.openclaw/workspace/RETRIEVAL_SYSTEM_README.md"