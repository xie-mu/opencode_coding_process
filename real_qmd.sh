#!/bin/bash
# 真实qmd工具 - 使用真实collection

echo "🔧 真实qmd工具"
echo "=============="

case "$1" in
    "list")
        case "$2" in
            "skills")
                echo "📋 已下载的技能列表:"
                echo "-------------------"
                node -e "
const fs = require('fs');
const collection = JSON.parse(fs.readFileSync('/root/.openclaw/workspace/real_qmd_collection.json', 'utf8'));
const skills = collection.items.filter(item => item.type === 'skill');
console.log('总技能数:', skills.length);
skills.forEach((skill, index) => {
    console.log((index + 1) + '. ' + skill.name + ' ✅');
    console.log('   分类: ' + skill.category);
    console.log('   路径: ' + skill.path);
    console.log('   大小: ' + skill.size + ' bytes');
    console.log('');
});
"
                ;;
            "documents")
                echo "📚 已下载的文档列表:"
                echo "-------------------"
                node -e "
const fs = require('fs');
const collection = JSON.parse(fs.readFileSync('/root/.openclaw/workspace/real_qmd_collection.json', 'utf8'));
const docs = collection.items.filter(item => item.type === 'document');
console.log('总文档数:', docs.length);
docs.forEach((doc, index) => {
    console.log((index + 1) + '. ' + doc.name + ' ✅');
    console.log('   分类: ' + doc.category);
    console.log('   路径: ' + doc.path);
    console.log('   大小: ' + doc.size + ' bytes');
    console.log('');
});
"
                ;;
            *)
                echo "❌ 未知类型，请使用: skills 或 documents"
                echo "示例: real_qmd.sh list skills"
                ;;
        esac
        ;;
    "search")
        if [ -z "$2" ]; then
            echo "❌ 请提供搜索关键词"
            echo "示例: real_qmd.sh search '天气查询'"
            exit 1
        fi
        echo "🔍 搜索关键词: '$2'"
        echo "-------------------"
        node -e "
const fs = require('fs');
const collection = JSON.parse(fs.readFileSync('/root/.openclaw/workspace/real_qmd_collection.json', 'utf8'));
const results = collection.items.filter(item => 
    item.name.toLowerCase().includes('$2'.toLowerCase()) ||
    item.category.toLowerCase().includes('$2'.toLowerCase())
);
console.log('找到 ' + results.length + ' 个结果:');
results.forEach((result, index) => {
    console.log((index + 1) + '. ' + result.name);
    console.log('   类型: ' + result.type + ' | 分类: ' + result.category);
    console.log('   路径: ' + result.path);
    console.log('');
});
"
        ;;
    "collection")
        echo "📊 集合信息:"
        echo "-----------"
        node -e "
const fs = require('fs');
const collection = JSON.parse(fs.readFileSync('/root/.openclaw/workspace/real_qmd_collection.json', 'utf8'));
console.log('集合名称: ' + collection.name);
console.log('版本: ' + collection.version);
console.log('创建时间: ' + collection.created);
console.log('总项目数: ' + collection.metadata.totalItems);
console.log('文档数量: ' + collection.metadata.documentCount);
console.log('技能数量: ' + collection.metadata.skillCount);
console.log('');
console.log('📋 项目详情:');
collection.items.forEach((item, index) => {
    console.log((index + 1) + '. ' + item.name + ' [' + item.type + ']');
});
"
        ;;
    *)
        echo "🔧 真实qmd工具 - 可用命令:"
        echo "=============================="
        echo "  list skills              - 列出所有技能"
        echo "  list documents           - 列出所有文档"
        echo "  search <关键词>         - 搜索项目"
        echo "  collection info          - 查看集合信息"
        echo ""
        echo "示例:"
        echo "  real_qmd.sh list skills"
        echo "  real_qmd.sh search '天气查询'"
        echo "  real_qmd.sh collection info"
        ;;
esac