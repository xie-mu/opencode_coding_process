#!/usr/bin/env python3
"""
构建完整的 OpenClaw 检索集合
包含所有本地技能和文档
"""

import json
import os
from pathlib import Path

def extract_skill_info(skill_path):
    """从技能文件中提取信息"""
    try:
        with open(skill_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 提取技能名称（通常是第一行或 # 标题）
        lines = content.split('\n')
        title = "未知技能"
        for line in lines[:5]:  # 检查前几行
            line = line.strip()
            if line.startswith('# '):
                title = line[2:].strip()
                break
            elif line and not line.startswith('#'):
                title = line.strip()
                break

        # 提取描述（第一段非空文本）
        description = "暂无描述"
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#') and len(line) > 20:
                description = line[:100] + "..." if len(line) > 100 else line
                break

        # 生成关键词
        keywords = []
        title_lower = title.lower()
        desc_lower = description.lower()

        # 从标题中提取关键词
        for word in title_lower.split():
            if len(word) > 2 and word not in ['技能', '工具', '助手']:
                keywords.append(word)

        # 从描述中提取关键词
        common_keywords = ['查询', '管理', '搜索', '工具', '助手', '集成', 'API', '文档', '系统', '功能']
        for kw in common_keywords:
            if kw in desc_lower and kw not in keywords:
                keywords.append(kw)

        # 确保有基本关键词
        if not keywords:
            keywords = ['openclaw', '技能', '工具']

        return {
            'title': title,
            'description': description,
            'keywords': list(set(keywords))[:10],  # 去重并限制数量
            'category': '实用工具' if '工具' in title or '管理' in title else '开发工具',
            'path': str(skill_path)
        }
    except Exception as e:
        print(f"处理技能 {skill_path} 时出错: {e}")
        return None

def extract_document_info(doc_path):
    """从文档文件中提取信息"""
    try:
        with open(doc_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 提取标题
        lines = content.split('\n')
        title = os.path.basename(doc_path).replace('.md', '').replace('_', ' ')

        for line in lines[:10]:
            line = line.strip()
            if line.startswith('# '):
                title = line[2:].strip()
                break

        # 提取描述
        description = "文档内容"
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#') and len(line) > 20:
                description = line[:100] + "..." if len(line) > 100 else line
                break

        # 生成关键词
        keywords = []
        title_lower = title.lower()

        # 从标题中提取关键词
        for word in title_lower.split():
            if len(word) > 2:
                keywords.append(word)

        # 添加文档相关关键词
        doc_keywords = ['文档', '说明', '指南', 'API', '接口', '功能']
        for kw in doc_keywords:
            if kw in title_lower and kw not in keywords:
                keywords.append(kw)

        if not keywords:
            keywords = ['文档', 'openclaw', '说明']

        return {
            'title': title,
            'description': description,
            'keywords': list(set(keywords))[:10],
            'category': '核心文档',
            'path': str(doc_path)
        }
    except Exception as e:
        print(f"处理文档 {doc_path} 时出错: {e}")
        return None

def build_collection():
    """构建完整的检索集合"""
    collection = {
        'metadata': {
            'name': 'OpenClaw完整文档与技能集合',
            'version': '3.0.0',
            'created': '2026-02-10',
            'total_items': 0
        },
        'retrieval_index': {}
    }

    index = collection['retrieval_index']
    item_count = 0

    # 1. 添加本地技能（5个）
    local_skills_dir = Path('/root/.openclaw/workspace/workspace/skills')
    for skill_dir in local_skills_dir.iterdir():
        if skill_dir.is_dir() and (skill_dir / 'SKILL.md').exists():
            skill_info = extract_skill_info(skill_dir / 'SKILL.md')
            if skill_info:
                key = f"local_skill_{item_count:04d}"
                index[key] = {
                    'type': 'skill',
                    **skill_info
                }
                item_count += 1

    # 2. 添加 openclaw-skills 中的技能（52个）
    openclaw_skills_dir = Path('/root/.openclaw/workspace/workspace/skills/openclaw-skills/skills')
    for skill_dir in openclaw_skills_dir.iterdir():
        if skill_dir.is_dir() and (skill_dir / 'SKILL.md').exists():
            skill_info = extract_skill_info(skill_dir / 'SKILL.md')
            if skill_info:
                key = f"openclaw_skill_{item_count:04d}"
                index[key] = {
                    'type': 'skill',
                    **skill_info
                }
                item_count += 1

    # 3. 添加文档（4个）
    docs_dir = Path('/root/.openclaw/workspace/workspace/docs')
    if docs_dir.exists():
        for doc_file in docs_dir.rglob('*.md'):
            if doc_file.name != 'README.md':  # 跳过 README
                doc_info = extract_document_info(doc_file)
                if doc_info:
                    key = f"doc_{item_count:04d}"
                    index[key] = {
                        'type': 'document',
                        **doc_info
                    }
                    item_count += 1

    # 更新元数据
    collection['metadata']['total_items'] = item_count

    # 保存集合
    output_path = Path('workspace/collections/optimized_openclaw_collection.json')
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(collection, f, ensure_ascii=False, indent=2)

    print(f"✅ 集合构建完成！")
    print(f"   总项目数: {item_count}")
    print(f"   技能数: {len([k for k in index.keys() if index[k]['type'] == 'skill'])}")
    print(f"   文档数: {len([k for k in index.keys() if index[k]['type'] == 'document'])}")
    print(f"   集合文件: {output_path}")

    return collection

if __name__ == "__main__":
    build_collection()