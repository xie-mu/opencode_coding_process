#!/usr/bin/env python3
"""
OpenClaw技能加载器
用于将技能库中的技能加载到AI助手的技能列表中
"""

import os
import json
import glob
from pathlib import Path

class SkillLoader:
    """技能加载器类"""
    
    def __init__(self, skills_dir: str = "skills"):
        self.skills_dir = Path(skills_dir)
        self.loaded_skills = []
        self.skill_stats = {
            "total_skills": 0,
            "total_files": 0,
            "skill_types": {},
            "last_updated": None
        }
    
    def scan_skills(self) -> list:
        """扫描技能目录"""
        skills = []
        
        if not self.skills_dir.exists():
            print(f"⚠️ 技能目录不存在: {self.skills_dir}")
            return skills
        
        # 查找所有包含SKILL.md的技能文件夹
        skill_dirs = self.skills_dir.glob("*/SKILL.md")
        
        for skill_file in skill_dirs:
            skill_dir = skill_file.parent
            skill_name = skill_dir.name
            
            skill_info = {
                "name": skill_name,
                "path": str(skill_dir),
                "skill_file": str(skill_file),
                "files": self._count_files(skill_dir),
                "size": self._get_directory_size(skill_dir),
                "created": skill_file.stat().st_ctime,
                "modified": skill_file.stat().st_mtime
            }
            
            skills.append(skill_info)
        
        return skills
    
    def _count_files(self, directory: Path) -> dict:
        """统计目录文件"""
        files = {"total": 0, "py": 0, "md": 0, "txt": 0, "json": 0, "yaml": 0}
        
        for file_path in directory.rglob("*"):
            if file_path.is_file():
                files["total"] += 1
                suffix = file_path.suffix.lower()
                if suffix == ".py":
                    files["py"] += 1
                elif suffix == ".md":
                    files["md"] += 1
                elif suffix == ".txt":
                    files["txt"] += 1
                elif suffix == ".json":
                    files["json"] += 1
                elif suffix in [".yaml", ".yml"]:
                    files["yaml"] += 1
        
        return files
    
    def _get_directory_size(self, directory: Path) -> int:
        """获取目录大小"""
        total_size = 0
        for file_path in directory.rglob("*"):
            if file_path.is_file():
                total_size += file_path.stat().st_size
        return total_size
    
    def load_skill_metadata(self, skill_info: dict) -> dict:
        """加载技能元数据"""
        try:
            with open(skill_info["skill_file"], 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 简单的元数据提取（可以扩展为完整的YAML解析）
            metadata = {
                "name": skill_info["name"],
                "description": "从SKILL.md加载的技能",
                "version": "1.0.0",
                "author": "电子核动力驴",
                "files": skill_info["files"],
                "size": skill_info["size"],
                "loaded_at": self.skill_stats["last_updated"] or "刚刚"
            }
            
            return metadata
            
        except Exception as e:
            print(f"❌ 加载技能元数据失败: {skill_info['name']} - {e}")
            return None
    
    def update_skill_list(self):
        """更新技能列表"""
        print("🔍 开始扫描技能库...")
        
        # 扫描技能
        skills = self.scan_skills()
        
        if not skills:
            print("📭 未找到任何技能")
            return
        
        # 更新统计信息
        self.skill_stats["total_skills"] = len(skills)
        self.skill_stats["total_files"] = sum(s["files"]["total"] for s in skills)
        self.skill_stats["last_updated"] = "刚刚"
        self.skill_stats["size"] = sum(s["size"] for s in skills)
        
        # 加载技能元数据
        loaded_skills = []
        for skill in skills:
            metadata = self.load_skill_metadata(skill)
            if metadata:
                loaded_skills.append(metadata)
        
        self.loaded_skills = loaded_skills
        
        # 输出结果
        print(f"✅ 成功加载 {len(loaded_skills)} 个技能")
        print(f"📊 总文件数: {self.skill_stats['total_files']}")
        print(f"💾 总大小: {self.skill_stats['size'] / 1024:.1f} KB")
        
        # 显示技能详情
        print("\n🎯 已加载的技能:")
        for i, skill in enumerate(loaded_skills, 1):
            print(f"  {i}. {skill['name']} - {skill['files']['total']} 个文件")
        
        return loaded_skills
    
    def get_skill_summary(self) -> str:
        """获取技能摘要"""
        if not self.loaded_skills:
            return "暂无加载的技能"
        
        summary = f"📚 技能库摘要:\n"
        summary += f"  🔢 总技能数: {self.skill_stats['total_skills']}\n"
        summary += f"  📁 总文件数: {self.skill_stats['total_files']}\n"
        summary += f"  💾 总大小: {self.skill_stats['size'] / 1024:.1f} KB\n"
        summary += f"  🕒 最后更新: {self.skill_stats['last_updated']}\n"
        
        return summary

def main():
    """主函数"""
    loader = SkillLoader()
    
    print("🚀 OpenClaw技能加载器启动")
    print("=" * 50)
    
    # 加载技能
    skills = loader.update_skill_list()
    
    # 显示摘要
    print("\n" + loader.get_skill_summary())
    
    print("\n🎉 技能库加载完成！")

if __name__ == "__main__":
    main()