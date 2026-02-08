#!/usr/bin/env python3
"""
天气查询技能实现
"""

import requests
import json
from typing import Dict, Any

class WeatherSkill:
    """天气查询技能类"""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or "demo_key"
        self.base_url = "https://api.openweathermap.org/data/2.5"
    
    def query_current_weather(self, city: str) -> Dict[str, Any]:
        """查询当前天气"""
        try:
            url = f"{self.base_url}/weather"
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric',
                'lang': 'zh_cn'
            }
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": f"查询失败: {str(e)}"}
    
    def get_forecast(self, city: str, days: int = 5) -> Dict[str, Any]:
        """获取天气预报"""
        try:
            url = f"{self.base_url}/forecast"
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric',
                'lang': 'zh_cn',
                'cnt': days * 8  # 每3小时一个预报
            }
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": f"预报查询失败: {str(e)}"}
    
    def convert_temperature(self, temp: float, from_unit: str, to_unit: str) -> float:
        """温度转换"""
        if from_unit == to_unit:
            return temp
        
        # 摄氏度转华氏度
        if from_unit == "celsius" and to_unit == "fahrenheit":
            return (temp * 9/5) + 32
        # 华氏度转摄氏度
        elif from_unit == "fahrenheit" and to_unit == "celsius":
            return (temp - 32) * 5/9
        # 摄氏度转开尔文
        elif from_unit == "celsius" and to_unit == "kelvin":
            return temp + 273.15
        # 开尔文转摄氏度
        elif from_unit == "kelvin" and to_unit == "celsius":
            return temp - 273.15
        else:
            raise ValueError(f"不支持的转换: {from_unit} -> {to_unit}")

def main():
    """主函数"""
    skill = WeatherSkill()
    
    # 示例使用
    result = skill.query_current_weather("北京")
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()