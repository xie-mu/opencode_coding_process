#!/bin/bash
# 启动OpenClaw检索系统

echo "🚀 OpenClaw检索系统启动"
echo "================================"

# 检查Python环境
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3未安装"
    exit 1
fi

# 检查检索集合
COLLECTION="/root/.openclaw/workspace/collections/optimized_openclaw_collection.json"
if [ ! -f "$COLLECTION" ]; then
    echo "❌ 检索集合不存在，正在构建..."
    python3 /root/.openclaw/workspace/build_retrieval_collection.py
fi

# 显示系统信息
echo "📊 系统信息:"
echo "   检索集合: $COLLECTION"
echo "   总项目数: $(python3 -c "
import json
with open('$COLLECTION') as f:
    data = json.load(f)
    print(data['metadata']['total_items'])
")"
echo ""

echo "🔍 可用命令:"
echo "   搜索关键词: python3 /root/.openclaw/workspace/quick_search.py search <关键词>"
echo "   列出所有技能: python3 /root/.openclaw/workspace/quick_search.py list skill"
echo "   列出所有文档: python3 /root/.openclaw/workspace/quick_search.py list document"
echo "   构建新集合: python3 /root/.openclaw/workspace/build_retrieval_collection.py"
echo ""

echo "💡 示例搜索:"
echo "   python3 /root/.openclaw/workspace/quick_search.py search '天气查询'"
echo "   python3 /root/.openclaw/workspace/quick_search.py search '文件管理' skill"
echo "   python3 /root/.openclaw/workspace/quick_search.py search 'API文档' document"
echo ""

echo "✅ 检索系统准备就绪！"
echo "================================"