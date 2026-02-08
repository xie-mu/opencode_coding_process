#!/usr/bin/env python3
"""
GPT-5.3查询工具
专门查询GPT-5.3的提升方面
"""

import json
from skills.web-search.web_search import WebSearchSkill

def query_gpt5_improvements():
    """查询GPT-5.3的提升方面"""
    print("🚀 查询GPT-5.3提升方面...")
    print("=" * 60)
    
    skill = WebSearchSkill()
    
    # 搜索GPT-5.3的提升方面
    improvements_query = "GPT-5.3 提升方面 改进功能 2026"
    result = skill.search_google(improvements_query, 10)
    
    print("📊 GPT-5.3提升方面搜索结果:")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
    # 搜索技术文档
    tech_query = "GPT-5.3 技术文档 架构 2026"
    tech_result = skill.search_tech_docs("GPT-5.3")
    
    print("\n🔧 技术文档搜索结果:")
    print(json.dumps(tech_result, indent=2, ensure_ascii=False))
    
    # 搜索新闻
    news_query = "GPT-5.3 发布新闻 2026"
    news_result = skill.search_news("GPT-5.3")
    
    print("\n📰 新闻资讯搜索结果:")
    print(json.dumps(news_result, indent=2, ensure_ascii=False))
    
    # 多引擎搜索
    multi_result = skill.multi_engine_search("GPT-5.3 最新功能")
    
    print("\n🌐 多引擎搜索结果:")
    print(json.dumps(multi_result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    query_gpt5_improvements()