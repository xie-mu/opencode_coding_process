#!/bin/bash

echo "🔄 开始更新技能库..."
echo "📅 更新时间: $(date)"
echo ""

# 创建memory目录（如果不存在）
mkdir -p memory

# 检查技能注册表是否存在
if [ ! -f "memory/skills_registry.json" ]; then
    echo "📝 创建新的技能注册表..."
    python3 -c "
import json
from datetime import datetime

skills_data = {
    'version': '1.0.0',
    'last_updated': datetime.now().isoformat(),
    'total_skills': 0,
    'skills': []
}

with open('memory/skills_registry.json', 'w', encoding='utf-8') as f:
    json.dump(skills_data, f, indent=2, ensure_ascii=False)

print('✅ 技能注册表创建成功')
"
fi

# 扫描技能目录
echo "🔍 扫描技能目录..."
skill_count=$(find skills/ -name "SKILL.md" -exec dirname {} \; | wc -l)

if [ "$skill_count" -eq 0 ]; then
    echo "⚠️  未找到技能文件"
    exit 1
fi

echo "✅ 发现 $skill_count 个技能"

# 更新技能注册表
echo "📊 更新技能注册表..."
python3 -c "
import json
import os
from datetime import datetime

# 加载现有注册表
try:
    with open('memory/skills_registry.json', 'r', encoding='utf-8') as f:
        registry = json.load(f)
except:
    registry = {'version': '1.0.0', 'last_updated': datetime.now().isoformat(), 'total_skills': 0, 'skills': []}

# 扫描技能目录
skills = []
for skill_dir in os.listdir('skills'):
    skill_path = os.path.join('skills', skill_dir)
    if os.path.isdir(skill_path) and os.path.exists(os.path.join(skill_path, 'SKILL.md')):
        skills.append({
            'name': skill_dir,
            'path': skill_path,
            'description': f'从技能库加载的技能: {skill_dir}',
            'version': '1.0.0',
            'author': '电子核动力驴',
            'category': '工具',
            'tags': ['技能库', '自动加载'],
            'created': datetime.now().isoformat(),
            'last_used': None,
            'usage_count': 0,
            'rating': 5.0,
            'status': 'active',
            'files': {
                'total': len([f for f in os.listdir(skill_path) if os.path.isfile(os.path.join(skill_path, f))]),
                'py': len([f for f in os.listdir(skill_path) if f.endswith('.py')]),
                'md': len([f for f in os.listdir(skill_path) if f.endswith('.md')]),
                'txt': len([f for f in os.listdir(skill_path) if f.endswith('.txt')])
            },
            'functions': [
                {'name': 'query', 'description': '执行技能查询', 'parameters': ['query']}
            ],
            'integration_status': 'complete',
            'api_endpoints': ['https://api.example.com']
        })

# 更新注册表
registry['skills'] = skills
registry['total_skills'] = len(skills)
registry['last_updated'] = datetime.now().isoformat()

# 保存更新
with open('memory/skills_registry.json', 'w', encoding='utf-8') as f:
    json.dump(registry, f, indent=2, ensure_ascii=False)

print(f'✅ 技能库更新完成: {len(skills)} 个技能')
print(f'💾 数据已保存到: memory/skills_registry.json')
"

echo ""
echo "📋 技能库更新摘要:"
echo "  🔢 总技能数: $(cat memory/skills_registry.json | grep 'total_skills' | head -1 | cut -d':' -f2 | tr -d ' ,')"
echo "  📅 更新时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo "  📁 技能位置: memory/skills_registry.json"
echo ""
echo "🎉 技能库更新完成！"
echo "💡 现在AI助手可以使用这些技能来增强功能！"