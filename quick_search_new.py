#!/usr/bin/env python3
"""
快速检索工具 - 使用构建的collection进行快速搜索
"""

import json
import sys
from pathlib import Path

class QuickSearchTool:
    def __init__(self):
        self.collection_path = Path("workspace/collections/optimized_openclaw_collection.json")
        self.collection = self.load_collection()

    def load_collection(self):
        """加载检索集合"""
        try:
            with open(self.collection_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"❌ 加载集合失败: {e}")
            return None

    def search(self, query: str, search_type: str = None):
        """搜索集合"""
        if not self.collection:
            return []

        results = []
        query_lower = query.lower()

        for key, item in self.collection['retrieval_index'].items():
            # 如果指定了类型，只搜索该类型
            if search_type and item['type'] != search_type:
                continue

            # 检查查询是否匹配标题或关键词
            title_match = query_lower in item['title'].lower()
            keyword_match = any(query_lower in kw for kw in item['keywords'])

            if title_match or keyword_match:
                results.append({
                    'title': item['title'],
                    'type': item['type'],
                    'category': item['category'],
                    'path': item['path'],
                    'keywords': item['keywords'][:5]  # 显示前5个关键词
                })

        return results

    def list_items(self, item_type: str = None):
        """列出所有项目"""
        if not self.collection:
            return []

        items = []
        for key, item in self.collection['retrieval_index'].items():
            if not item_type or item['type'] == item_type:
                items.append({
                    'title': item['title'],
                    'type': item['type'],
                    'category': item['category'],
                    'path': item['path']
                })

        return items

def main():
    """主函数"""
    tool = QuickSearchTool()

    if len(sys.argv) < 2:
        print("🔍 快速检索工具")
        print("=" * 40)
        print("用法:")
        print("  python3 quick_search.py search <关键词> [类型]")
        print("  python3 quick_search.py list [类型]")
        print("\n示例:")
        print("  python3 quick_search.py search '天气查询'")
        print("  python3 quick_search.py search '文件管理' skill")
        print("  python3 quick_search.py list document")
        print("  python3 quick_search.py list skill")
        return

    command = sys.argv[1]

    if command == "search":
        if len(sys.argv) < 3:
            print("❌ 请提供搜索关键词")
            return

        query = sys.argv[2]
        search_type = sys.argv[3] if len(sys.argv) > 3 else None

        results = tool.search(query, search_type)

        if results:
            print(f"🔍 搜索结果: '{query}'")
            print("-" * 50)
            for i, result in enumerate(results, 1):
                print(f"{i}. {result['title']}")
                print(f"   类型: {result['type']} | 分类: {result['category']}")
                print(f"   路径: {result['path']}")
                print(f"   关键词: {', '.join(result['keywords'])}")
                print()
        else:
            print(f"❌ 未找到匹配 '{query}' 的结果")

    elif command == "list":
        item_type = sys.argv[2] if len(sys.argv) > 2 else None
        items = tool.list_items(item_type)

        if items:
            print(f"📋 项目列表 ({len(items)} 个)")
            print("-" * 50)
            for i, item in enumerate(items, 1):
                print(f"{i}. {item['title']}")
                print(f"   类型: {item['type']} | 分类: {item['category']}")
                print(f"   路径: {item['path']}")
                print()
        else:
            print("❌ 未找到项目")

if __name__ == "__main__":
    main()