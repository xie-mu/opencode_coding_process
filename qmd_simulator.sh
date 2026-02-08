#!/bin/bash
# qmd工具模拟器 - 模拟qmd工具的功能

echo "🔧 qmd工具模拟器"
echo "=================="

case "$1" in
    "list")
        case "$2" in
            "skills")
                echo "📋 已下载的技能列表:"
                echo "-------------------"
                python3 /root/.openclaw/workspace/quick_search.py list skill 2>/dev/null
                ;;
            "documents")
                echo "📚 已下载的文档列表:"
                echo "-------------------"
                python3 /root/.openclaw/workspace/quick_search.py list document 2>/dev/null
                ;;
            *)
                echo "❌ 未知类型，请使用: skills 或 documents"
                echo "示例: qmd_simulator.sh list skills"
                ;;
        esac
        ;;
    "search")
        if [ -z "$2" ]; then
            echo "❌ 请提供搜索关键词"
            echo "示例: qmd_simulator.sh search '天气查询'"
            exit 1
        fi
        case "$3" in
            "--type")
                case "$4" in
                    "skill")
                        echo "🔍 搜索技能: '$2'"
                        echo "-------------------"
                        python3 /root/.openclaw/workspace/quick_search.py search "$2" skill 2>/dev/null
                        ;;
                    "document")
                        echo "🔍 搜索文档: '$2'"
                        echo "-------------------"
                        python3 /root/.openclaw/workspace/quick_search.py search "$2" document 2>/dev/null
                        ;;
                    *)
                        echo "❌ 未知类型，请使用: skill 或 document"
                        ;;
                esac
                ;;
            *)
                echo "🔍 搜索所有: '$2'"
                echo "-------------------"
                python3 /root/.openclaw/workspace/quick_search.py search "$2" 2>/dev/null
                ;;
        esac
        ;;
    "collection")
        case "$2" in
            "info")
                echo "📊 集合信息:"
                echo "-----------"
                echo "集合名称: OpenClaw文档与技能集合"
                echo "版本: 2.0.0"
                echo "创建时间: 2026-02-08"
                echo "总项目数: $(python3 -c "
import json
with open('/root/.openclaw/workspace/collections/optimized_openclaw_collection.json') as f:
    data = json.load(f)
    print(data['metadata']['total_items'])
")"
                echo "优化状态: 已优化"
                echo "检索索引: 已启用"
                ;;
            *)
                echo "❌ 未知命令，请使用: info"
                ;;
        esac
        ;;
    *)
        echo "🔧 qmd工具模拟器 - 可用命令:"
        echo "=============================="
        echo "  list skills          - 列出所有技能"
        echo "  list documents       - 列出所有文档"
        echo "  search <关键词>     - 搜索关键词"
        echo "  search <关键词> --type skill - 搜索技能"
        echo "  search <关键词> --type document - 搜索文档"
        echo "  collection info      - 查看集合信息"
        echo ""
        echo "示例:"
        echo "  qmd_simulator.sh list skills"
        echo "  qmd_simulator.sh search '天气查询'"
        echo "  qmd_simulator.sh search '文件管理' --type skill"
        ;;
esac