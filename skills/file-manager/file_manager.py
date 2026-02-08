#!/usr/bin/env python3
"""
文件管理器技能实现
"""

import os
import shutil
import glob
from pathlib import Path
from typing import Dict, List, Any
import argparse

class FileManager:
    """文件管理器类"""
    
    def __init__(self, default_path: str = "/home/user"):
        self.default_path = Path(default_path)
    
    def browse(self, path: str = None) -> Dict[str, Any]:
        """浏览目录"""
        target_path = Path(path) if path else self.default_path
        
        if not target_path.exists():
            return {"error": f"路径不存在: {target_path}"}
        
        if not target_path.is_dir():
            return {"error": f"路径不是目录: {target_path}"}
        
        result = {
            "path": str(target_path),
            "items": [],
            "total_files": 0,
            "total_dirs": 0,
            "total_size": 0
        }
        
        try:
            for item in target_path.iterdir():
                item_info = {
                    "name": item.name,
                    "type": "directory" if item.is_dir() else "file",
                    "size": item.stat().st_size if item.is_file() else 0,
                    "modified": item.stat().st_mtime,
                    "path": str(item)
                }
                result["items"].append(item_info)
                
                if item.is_dir():
                    result["total_dirs"] += 1
                else:
                    result["total_files"] += 1
                    result["total_size"] += item_info["size"]
            
            result["items"].sort(key=lambda x: (x["type"] == "directory", x["name"]))
            
        except Exception as e:
            return {"error": f"浏览目录失败: {str(e)}"}
        
        return result
    
    def search(self, pattern: str, path: str = None, recursive: bool = True) -> Dict[str, Any]:
        """搜索文件"""
        target_path = Path(path) if path else self.default_path
        
        if not target_path.exists():
            return {"error": f"路径不存在: {target_path}"}
        
        try:
            if recursive:
                files = list(target_path.rglob(pattern))
            else:
                files = list(target_path.glob(pattern))
            
            result = {
                "pattern": pattern,
                "path": str(target_path),
                "found_files": len(files),
                "files": []
            }
            
            for file_path in files:
                if file_path.is_file():
                    file_info = {
                        "name": file_path.name,
                        "path": str(file_path),
                        "size": file_path.stat().st_size,
                        "modified": file_path.stat().st_mtime,
                        "relative_path": str(file_path.relative_to(target_path))
                    }
                    result["files"].append(file_info)
            
            return result
            
        except Exception as e:
            return {"error": f"搜索文件失败: {str(e)}"}
    
    def stats(self, path: str = None) -> Dict[str, Any]:
        """统计目录信息"""
        target_path = Path(path) if path else self.default_path
        
        if not target_path.exists():
            return {"error": f"路径不存在: {target_path}"}
        
        if not target_path.is_dir():
            return {"error": f"路径不是目录: {target_path}"}
        
        try:
            total_size = 0
            file_count = 0
            dir_count = 0
            
            for root, dirs, files in os.walk(target_path):
                dir_count += len(dirs)
                file_count += len(files)
                
                for file in files:
                    file_path = Path(root) / file
                    try:
                        total_size += file_path.stat().st_size
                    except:
                        pass
            
            result = {
                "path": str(target_path),
                "total_size": total_size,
                "total_size_mb": round(total_size / (1024 * 1024), 2),
                "file_count": file_count,
                "directory_count": dir_count,
                "depth": len(target_path.parts)
            }
            
            return result
            
        except Exception as e:
            return {"error": f"统计信息失败: {str(e)}"}
    
    def copy(self, source: str, dest: str) -> Dict[str, Any]:
        """复制文件"""
        try:
            source_path = Path(source)
            dest_path = Path(dest)
            
            if not source_path.exists():
                return {"error": f"源文件不存在: {source_path}"}
            
            if source_path.is_dir():
                if dest_path.exists():
                    shutil.rmtree(dest_path)
                shutil.copytree(source_path, dest_path)
            else:
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source_path, dest_path)
            
            return {
                "success": True,
                "source": source,
                "dest": dest,
                "size": source_path.stat().st_size
            }
            
        except Exception as e:
            return {"error": f"复制文件失败: {str(e)}"}
    
    def delete(self, path: str) -> Dict[str, Any]:
        """删除文件或目录"""
        try:
            target_path = Path(path)
            
            if not target_path.exists():
                return {"error": f"路径不存在: {target_path}"}
            
            if target_path.is_dir():
                shutil.rmtree(target_path)
            else:
                target_path.unlink()
            
            return {
                "success": True,
                "deleted": path,
                "type": "directory" if target_path.is_dir() else "file"
            }
            
        except Exception as e:
            return {"error": f"删除失败: {str(e)}"}

def main():
    """主函数"""
    manager = FileManager()
    
    # 示例使用
    result = manager.browse("/tmp")
    print("目录浏览:", result)

if __name__ == "__main__":
    main()