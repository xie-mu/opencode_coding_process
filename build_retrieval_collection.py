#!/usr/bin/env python3
"""
基于OpenClaw文档和技能的检索集合构建工具
使用qmd技能加速检索效率
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Any
import hashlib

class RetrievalCollectionBuilder:
    def __init__(self, workspace_path: str = "/root/.openclaw/workspace"):
        self.workspace_path = Path(workspace_path)
        self.collection_config = {}
        self.retrieval_index = {}
        self.search_cache = {}

    def load_collection_config(self, config_path: str = "collections/openclaw-docs-skills.json"):
        """加载collection配置文件"""
        config_file = self.workspace_path / config_path
        if config_file.exists():
            with open(config_file, 'r', encoding='utf-8') as f:
                self.collection_config = json.load(f)
            print(f"✅ 已加载配置: {self.collection_config['name']}")
            return True
        else:
            print(f"❌ 配置文件不存在: {config_file}")
            return False

    def extract_content(self, file_path: str) -> str:
        """提取文件内容"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return content
        except Exception as e:
            print(f"⚠️  读取文件失败 {file_path}: {e}")
            return ""

    def create_search_index(self):
        """创建检索索引"""
        print("🔍 开始创建检索索引...")

        # 索引文档
        for doc in self.collection_config.get('documents', []):
            doc_path = self.workspace_path / doc['path']
            if doc_path.exists():
                content = self.extract_content(str(doc_path))
                if content:
                    # 创建关键词索引
                    keywords = self.extract_keywords(content)
                    self.retrieval_index[f"doc:{doc['title']}"] = {
                        'type': 'document',
                        'title': doc['title'],
                        'path': doc['path'],
                        'keywords': keywords,
                        'content_hash': hashlib.md5(content.encode()).hexdigest()[:8],
                        'category': doc.get('category', 'unknown')
                    }

        # 索引技能
        for skill in self.collection_config.get('skills', []):
            skill_path = self.workspace_path / skill['path']
            if skill_path.exists():
                content = self.extract_content(str(skill_path))
                if content:
                    keywords = self.extract_keywords(content)
                    self.retrieval_index[f"skill:{skill['title']}"] = {
                        'type': 'skill',
                        'title': skill['title'],
                        'path': skill['path'],
                        'keywords': keywords,
                        'content_hash': hashlib.md5(content.encode()).hexdigest()[:8],
                        'category': skill.get('category', 'unknown')
                    }

        print(f"✅ 检索索引创建完成，共索引 {len(self.retrieval_index)} 个项目")

    def extract_keywords(self, content: str) -> List[str]:
        """从内容中提取关键词"""
        # 移除代码块和特殊字符
        content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
        content = re.sub(r'`.*?`', '', content)
        content = re.sub(r'[^\w\s]', ' ', content)

        # 提取中文关键词
        chinese_words = re.findall(r'[\u4e00-\u9fff]+', content)
        # 提取英文关键词
        english_words = re.findall(r'\b[a-zA-Z]{3,}\b', content)

        # 过滤常见停用词
        stop_words = {'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'can', 'this', 'that', 'these', 'those', 'a', 'an'}

        keywords = []
        for word in chinese_words + english_words:
            word = word.lower().strip()
            if len(word) > 1 and word not in stop_words:
                keywords.append(word)

        return list(set(keywords))  # 去重

    def build_optimized_collection(self):
        """构建优化的检索集合"""
        print("🚀 开始构建优化检索集合...")

        # 创建优化后的collection文件
        optimized_collection = {
            'metadata': {
                'name': self.collection_config.get('name', 'OpenClaw检索集合'),
                'version': '2.0.0',
                'created': '2026-02-08',
                'last_build': '2026-02-08T14:23:00Z',
                'total_items': len(self.retrieval_index),
                'optimized': True
            },
            'retrieval_index': self.retrieval_index,
            'search_tips': [
                "使用关键词搜索: '天气查询', '文件管理', '计算器'",
                "搜索技能功能: 'weather', 'file', 'calculation'",
                "搜索文档类型: 'API文档', '架构文档', 'CLI文档'"
            ],
            'quick_access': {
                'documents': [item['title'] for item in self.collection_config.get('documents', [])],
                'skills': [item['title'] for item in self.collection_config.get('skills', [])]
            }
        }

        # 保存优化后的集合
        output_file = self.workspace_path / "collections/optimized_openclaw_collection.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(optimized_collection, f, ensure_ascii=False, indent=2)

        print(f"✅ 优化检索集合已保存到: {output_file}")
        print(f"📊 集合包含 {len(self.retrieval_index)} 个检索项目")

        return output_file

    def generate_search_commands(self):
        """生成搜索命令示例"""
        print("\n📝 搜索命令示例:")
        print("=" * 50)
        print("1. 搜索关键词:")
        print("   qmd search '天气查询'")
        print("   qmd search '文件管理'")
        print("   qmd search 'API文档'")
        print()
        print("2. 搜索特定类型:")
        print("   qmd search --type document 'CLI文档'")
        print("   qmd search --type skill '计算器'")
        print()
        print("3. 获取集合信息:")
        print("   qmd collection info openclaw-docs-skills")
        print()
        print("4. 列出所有技能:")
        print("   qmd list skills")
        print()
        print("5. 列出所有文档:")
        print("   qmd list documents")

def main():
    """主函数"""
    print("🔧 OpenClaw文档与技能检索集合构建工具")
    print("=" * 50)

    builder = RetrievalCollectionBuilder()

    # 加载配置
    if not builder.load_collection_config():
        return

    # 创建检索索引
    builder.create_search_index()

    # 构建优化集合
    output_file = builder.build_optimized_collection()

    # 生成搜索命令
    builder.generate_search_commands()

    print(f"\n🎉 检索集合构建完成！")
    print(f"📁 集合文件: {output_file}")
    print(f"🔍 现在你可以使用qmd工具快速检索文档和技能了！")

if __name__ == "__main__":
    main()