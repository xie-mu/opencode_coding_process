#!/usr/bin/env python3
"""
PMD (Personal Media Database) 工具
用于将下载的文件和代码整理成有序的collection
"""

import os
import json
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

class PMDTool:
    """PMD工具类"""
    
    def __init__(self, workspace_dir: str = "/root/.openclaw/workspace"):
        self.workspace_dir = Path(workspace_dir)
        self.collections_dir = self.workspace_dir / "collections"
        self.temp_dir = self.workspace_dir / "temp"
        self.metadata_file = self.collections_dir / "pmd_metadata.json"
        
        # 确保目录存在
        self.collections_dir.mkdir(exist_ok=True)
        self.temp_dir.mkdir(exist_ok=True)
        
        # 加载元数据
        self.metadata = self._load_metadata()
    
    def _load_metadata(self) -> Dict[str, Any]:
        """加载PMD元数据"""
        if self.metadata_file.exists():
            try:
                with open(self.metadata_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"⚠️  加载元数据失败: {e}")
        
        return {
            "version": "1.0.0",
            "created": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat(),
            "collections": {},
            "file_index": {}
        }
    
    def _save_metadata(self):
        """保存元数据"""
        self.metadata["last_updated"] = datetime.now().isoformat()
        with open(self.metadata_file, 'w', encoding='utf-8') as f:
            json.dump(self.metadata, f, indent=2, ensure_ascii=False)
    
    def scan_files(self) -> Dict[str, List[str]]:
        """扫描工作区文件"""
        print("🔍 扫描工作区文件...")
        
        file_categories = {
            "python_scripts": [],
            "markdown_docs": [],
            "shell_scripts": [],
            "json_configs": [],
            "skill_packages": [],
            "documentation": [],
            "tools": [],
            "other": []
        }
        
        for file_path in self.workspace_dir.rglob("*"):
            if file_path.is_file() and not any(part.startswith('.') for part in file_path.parts):
                relative_path = file_path.relative_to(self.workspace_dir)
                
                if file_path.suffix == ".py":
                    file_categories["python_scripts"].append(str(relative_path))
                elif file_path.suffix == ".md":
                    if "skill" in str(relative_path).lower():
                        file_categories["skill_packages"].append(str(relative_path))
                    elif "doc" in str(relative_path).lower() or "readme" in str(relative_path).lower():
                        file_categories["documentation"].append(str(relative_path))
                    else:
                        file_categories["markdown_docs"].append(str(relative_path))
                elif file_path.suffix == ".sh":
                    file_categories["shell_scripts"].append(str(relative_path))
                elif file_path.suffix == ".json":
                    file_categories["json_configs"].append(str(relative_path))
                elif "skill" in str(relative_path).lower():
                    file_categories["skill_packages"].append(str(relative_path))
                elif "tool" in str(relative_path).lower():
                    file_categories["tools"].append(str(relative_path))
                else:
                    file_categories["other"].append(str(relative_path))
        
        return file_categories
    
    def create_collection(self, collection_name: str, description: str = "", files: List[str] = None):
        """创建新的collection"""
        print(f"📁 创建collection: {collection_name}")
        
        # 创建collection目录
        collection_dir = self.collections_dir / collection_name
        collection_dir.mkdir(exist_ok=True)
        
        # 创建collection元数据
        collection_metadata = {
            "name": collection_name,
            "description": description,
            "created": datetime.now().isoformat(),
            "files": files or [],
            "size": 0,
            "file_count": 0
        }
        
        # 复制文件到collection
        if files:
            for file_path in files:
                src = self.workspace_dir / file_path
                if src.exists():
                    dest = collection_dir / src.name
                    shutil.copy2(src, dest)
                    collection_metadata["files"].append(src.name)
                    collection_metadata["size"] += src.stat().st_size
                    collection_metadata["file_count"] += 1
        
        # 保存collection元数据
        collection_metadata_file = collection_dir / "collection.json"
        with open(collection_metadata_file, 'w', encoding='utf-8') as f:
            json.dump(collection_metadata, f, indent=2, ensure_ascii=False)
        
        # 更新主元数据
        self.metadata["collections"][collection_name] = collection_metadata
        self._save_metadata()
        
        print(f"✅ Collection '{collection_name}' 创建完成")
        print(f"   📄 文件数量: {collection_metadata['file_count']}")
        print(f"   💾 总大小: {collection_metadata['size'] / 1024:.1f} KB")
    
    def create_openclaw_collection(self):
        """创建OpenClaw专用collection"""
        print("🚀 创建OpenClaw专用collection...")
        
        # 定义OpenClaw相关文件
        openclaw_files = [
            "AGENTS.md",
            "SOUL.md",
            "TOOLS.md",
            "IDENTITY.md",
            "USER.md",
            "HEARTBEAT.md",
            "BOOTSTRAP.md",
            "docs/clawhub/README.md",
            "docs/clawhub/CHANGELOG.md",
            "docs/clawhub/docs/README.md",
            "docs/clawhub/docs/architecture.md",
            "docs/clawhub/docs/api.md",
            "docs/clawhub/docs/auth.md",
            "skills/example-weather/SKILL.md",
            "skills/file-manager/SKILL.md",
            "skills/calculator/SKILL.md",
            "CURRENT_SKILLS.md",
            "FINAL_SKILLS_REPORT.md"
        ]
        
        self.create_collection(
            "openclaw-core",
            "OpenClaw核心文档和技能库",
            openclaw_files
        )
    
    def create_skills_collection(self):
        """创建技能库collection"""
        print("🧩 创建技能库collection...")
        
        # 扫描技能文件
        skills_files = []
        for skill_dir in self.workspace_dir.glob("skills/*"):
            if skill_dir.is_dir():
                skill_md = skill_dir / "SKILL.md"
                if skill_md.exists():
                    skills_files.append(str(skill_md.relative_to(self.workspace_dir)))
                
                # 添加Python文件
                for py_file in skill_dir.glob("*.py"):
                    skills_files.append(str(py_file.relative_to(self.workspace_dir)))
                
                # 添加requirements文件
                req_file = skill_dir / "requirements.txt"
                if req_file.exists():
                    skills_files.append(str(req_file.relative_to(self.workspace_dir)))
        
        self.create_collection(
            "skills-repository",
            "OpenClaw技能库集合",
            skills_files
        )
    
    def create_tools_collection(self):
        """创建工具collection"""
        print("🔧 创建工具collection...")
        
        tool_files = [
            "load_docs_and_skills.sh",
            "update_skills.sh",
            "add_multiple_skills.sh",
            "skill_loader.py",
            "skills_manager.py",
            "github_skills_loader.py",
            "fixed_github_skills_loader.py",
            "pmd_tool.py"
        ]
        
        self.create_collection(
            "development-tools",
            "开发工具集合",
            tool_files
        )
    
    def create_documentation_collection(self):
        """创建文档collection"""
        print("📚 创建文档collection...")
        
        doc_files = [
            "AGENTS.md",
            "SOUL.md",
            "TOOLS.md",
            "IDENTITY.md",
            "USER.md",
            "HEARTBEAT.md",
            "BOOTSTRAP.md",
            "docs/clawhub/README.md",
            "docs/clawhub/CHANGELOG.md",
            "docs/clawhub/docs/README.md",
            "docs/clawhub/docs/architecture.md",
            "docs/clawhub/docs/api.md",
            "docs/clawhub/docs/auth.md",
            "CURRENT_SKILLS.md",
            "FINAL_SKILLS_REPORT.md"
        ]
        
        self.create_collection(
            "documentation",
            "OpenClaw文档集合",
            doc_files
        )
    
    def create_complete_collection(self):
        """创建完整的collection集合"""
        print("🎯 开始创建完整的collection集合...")
        print("=" * 60)
        
        # 创建各个collection
        self.create_openclaw_collection()
        self.create_skills_collection()
        self.create_tools_collection()
        self.create_documentation_collection()
        
        # 显示结果
        print("\n📊 Collection创建完成:")
        for name, collection in self.metadata["collections"].items():
            print(f"  📁 {name}: {collection['file_count']} 个文件")
        
        print(f"\n✅ 总共创建了 {len(self.metadata['collections'])} 个collection")
        print(f"💾 存储位置: {self.collections_dir}")
    
    def show_collection_info(self, collection_name: str = None):
        """显示collection信息"""
        if collection_name:
            if collection_name in self.metadata["collections"]:
                collection = self.metadata["collections"][collection_name]
                print(f"📁 Collection: {collection['name']}")
                print(f"📝 描述: {collection['description']}")
                print(f"📅 创建时间: {collection['created']}")
                print(f"📄 文件数量: {collection['file_count']}")
                print(f"💾 总大小: {collection['size'] / 1024:.1f} KB")
                print(f"📋 文件列表:")
                for file_name in collection['files']:
                    print(f"   • {file_name}")
            else:
                print(f"❌ Collection '{collection_name}' 不存在")
        else:
            print("📊 所有collection:")
            for name, collection in self.metadata["collections"].items():
                print(f"  📁 {name}: {collection['file_count']} 个文件")

def main():
    """主函数"""
    print("🚀 PMD (Personal Media Database) 工具启动")
    print("=" * 60)
    
    # 创建PMD工具实例
    pmd = PMDTool()
    
    # 扫描文件
    file_categories = pmd.scan_files()
    print(f"\n📊 文件扫描完成:")
    for category, files in file_categories.items():
        if files:
            print(f"  {category}: {len(files)} 个文件")
    
    # 创建完整collection集合
    pmd.create_complete_collection()
    
    # 显示collection信息
    print("\n" + "=" * 60)
    print("📋 Collection信息:")
    pmd.show_collection_info()

if __name__ == "__main__":
    main()