#!/usr/bin/env python3
"""
智能计算器技能实现
"""

import math
import statistics
import argparse
from typing import Dict, Any, List
import re

class Calculator:
    """智能计算器类"""
    
    def __init__(self, precision: int = 10):
        self.precision = precision
        self.supported_functions = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'asin': math.asin,
            'acos': math.acos,
            'atan': math.atan,
            'log': math.log,
            'log10': math.log10,
            'exp': math.exp,
            'sqrt': math.sqrt,
            'abs': abs,
            'pow': math.pow
        }
    
    def basic_calculation(self, expression: str) -> Dict[str, Any]:
        """基础计算"""
        try:
            # 安全地计算表达式
            allowed_chars = set('0123456789+-*/(). ')
            if not all(c in allowed_chars for c in expression):
                return {"error": "表达式包含不允许的字符"}
            
            result = eval(expression, {"__builtins__": {}}, self.supported_functions)
            return {
                "expression": expression,
                "result": round(float(result), self.precision),
                "type": "basic"
            }
            
        except Exception as e:
            return {"error": f"计算错误: {str(e)}"}
    
    def scientific_calculation(self, func: str, value: float, unit: str = "radians") -> Dict[str, Any]:
        """科学计算"""
        try:
            if func not in self.supported_functions:
                return {"error": f"不支持的函数: {func}"}
            
            # 角度转弧度
            if unit == "degrees":
                value = math.radians(value)
            
            result = self.supported_functions[func](value)
            return {
                "function": func,
                "value": value,
                "unit": unit,
                "result": round(float(result), self.precision),
                "type": "scientific"
            }
            
        except Exception as e:
            return {"error": f"科学计算错误: {str(e)}"}
    
    def statistical_analysis(self, data_str: str) -> Dict[str, Any]:
        """统计分析"""
        try:
            # 解析数据字符串
            numbers = [float(x.strip()) for x in data_str.split(',') if x.strip()]
            
            if len(numbers) < 2:
                return {"error": "需要至少2个数据点"}
            
            result = {
                "data": numbers,
                "count": len(numbers),
                "mean": round(statistics.mean(numbers), self.precision),
                "median": round(statistics.median(numbers), self.precision),
                "stdev": round(statistics.stdev(numbers), self.precision),
                "min": min(numbers),
                "max": max(numbers),
                "type": "statistics"
            }
            
            return result
            
        except Exception as e:
            return {"error": f"统计分析错误: {str(e)}"}
    
    def base_conversion(self, number: int, from_base: str, to_base: str) -> Dict[str, Any]:
        """进制转换"""
        try:
            # 转换为目标进制
            if from_base == "decimal":
                decimal_num = number
            elif from_base == "binary":
                decimal_num = int(str(number), 2)
            elif from_base == "octal":
                decimal_num = int(str(number), 8)
            elif from_base == "hex":
                decimal_num = int(str(number), 16)
            else:
                return {"error": f"不支持的源进制: {from_base}"}
            
            # 转换为目标进制
            if to_base == "decimal":
                result = decimal_num
            elif to_base == "binary":
                result = bin(decimal_num)[2:]
            elif to_base == "octal":
                result = oct(decimal_num)[2:]
            elif to_base == "hex":
                result = hex(decimal_num)[2:].upper()
            else:
                return {"error": f"不支持的目标进制: {to_base}"}
            
            return {
                "original": number,
                "original_base": from_base,
                "result": str(result),
                "target_base": to_base,
                "type": "conversion"
            }
            
        except Exception as e:
            return {"error": f"进制转换错误: {str(e)}"}
    
    def geometry_calculation(self, shape: str, **kwargs) -> Dict[str, Any]:
        """几何计算"""
        try:
            if shape == "circle":
                radius = kwargs.get('radius', 1)
                area = math.pi * radius ** 2
                circumference = 2 * math.pi * radius
                return {
                    "shape": "circle",
                    "radius": radius,
                    "area": round(area, self.precision),
                    "circumference": round(circumference, self.precision),
                    "type": "geometry"
                }
            elif shape == "rectangle":
                length = kwargs.get('length', 1)
                width = kwargs.get('width', 1)
                area = length * width
                perimeter = 2 * (length + width)
                return {
                    "shape": "rectangle",
                    "length": length,
                    "width": width,
                    "area": round(area, self.precision),
                    "perimeter": round(perimeter, self.precision),
                    "type": "geometry"
                }
            elif shape == "sphere":
                radius = kwargs.get('radius', 1)
                volume = (4/3) * math.pi * radius ** 3
                surface_area = 4 * math.pi * radius ** 2
                return {
                    "shape": "sphere",
                    "radius": radius,
                    "volume": round(volume, self.precision),
                    "surface_area": round(surface_area, self.precision),
                    "type": "geometry"
                }
            else:
                return {"error": f"不支持的几何形状: {shape}"}
                
        except Exception as e:
            return {"error": f"几何计算错误: {str(e)}"}

def main():
    """主函数"""
    calc = Calculator()
    
    # 示例使用
    result = calc.basic_calculation("2+3*4")
    print("基础计算:", result)

if __name__ == "__main__":
    main()