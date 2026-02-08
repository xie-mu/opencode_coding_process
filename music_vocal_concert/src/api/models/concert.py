#!/usr/bin/env python3
"""
Music Vocal Concert - 演唱会数据模型
"""

from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional, List
from enum import Enum

class Region(str, Enum):
    """地区枚举"""
    MAINLAND = "mainland"  # 中国大陆
    HONGKONG = "hongkong"  # 香港
    MACAO = "macao"  # 澳门
    TAIWAN = "taiwan"  # 台湾

class ConcertPlatform(str, Enum):
    """官方合作平台枚举"""
    DAMAI = "damai"  # 大麦网
    MAOYAN = "maoyan"  # 猫眼演出
    SHOWSTART = "showstart"  # 秀动
    TOUMINGLUN = "touminglun"  # 摩天轮
    YONGLE = "yongle"  # 永乐票务
    OTHER = "other"  # 其他

class Concert(BaseModel):
    """演唱会信息模型"""
    id: int = Field(..., description="演唱会ID")
    name: str = Field(..., description="演唱会名称", max_length=200)
    artist: str = Field(..., description="演唱者/乐队名称", max_length=100)
    city: str = Field(..., description="举办城市", max_length=50)
    region: Region = Field(..., description="地区")
    date: datetime = Field(..., description="演唱会日期")
    address: str = Field(..., description="详细地址", max_length=300)
    venue: str = Field(..., description="场馆名称", max_length=100)
    platform: ConcertPlatform = Field(..., description="官方合作平台")
    price_range: Optional[str] = Field(None, description="票价范围", max_length=50)
    duration: Optional[int] = Field(None, description="演出时长（分钟）")
    concert_type: Optional[str] = Field(None, description="演出类型", max_length=50)
    description: Optional[str] = Field(None, description="演唱会描述")
    created_at: datetime = Field(..., description="创建时间")
    updated_at: datetime = Field(..., description="更新时间")
    
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "周杰伦演唱会2026",
                "artist": "周杰伦",
                "city": "北京",
                "region": "mainland",
                "date": "2026-03-15T20:00:00",
                "address": "北京工人体育馆",
                "venue": "北京工人体育馆",
                "platform": "damai",
                "price_range": "380-1880元",
                "duration": 180,
                "concert_type": "流行演唱会",
                "description": "周杰伦2026年全国巡回演唱会北京站",
                "created_at": "2026-02-08T10:00:00",
                "updated_at": "2026-02-08T10:00:00"
            }
        }

class ConcertCreate(BaseModel):
    """创建演唱会信息模型"""
    name: str = Field(..., description="演唱会名称", max_length=200)
    artist: str = Field(..., description="演唱者/乐队名称", max_length=100)
    city: str = Field(..., description="举办城市", max_length=50)
    region: Region = Field(..., description="地区")
    date: datetime = Field(..., description="演唱会日期")
    address: str = Field(..., description="详细地址", max_length=300)
    venue: str = Field(..., description="场馆名称", max_length=100)
    platform: ConcertPlatform = Field(..., description="官方合作平台")
    price_range: Optional[str] = Field(None, description="票价范围", max_length=50)
    duration: Optional[int] = Field(None, description="演出时长（分钟）")
    concert_type: Optional[str] = Field(None, description="演出类型", max_length=50)
    description: Optional[str] = Field(None, description="演唱会描述")
    
    class Config:
        schema_extra = {
            "example": {
                "name": "周杰伦演唱会2026",
                "artist": "周杰伦",
                "city": "北京",
                "region": "mainland",
                "date": "2026-03-15T20:00:00",
                "address": "北京工人体育馆",
                "venue": "北京工人体育馆",
                "platform": "damai",
                "price_range": "380-1880元",
                "duration": 180,
                "concert_type": "流行演唱会",
                "description": "周杰伦2026年全国巡回演唱会北京站"
            }
        }

class ConcertUpdate(BaseModel):
    """更新演唱会信息模型"""
    name: Optional[str] = Field(None, description="演唱会名称", max_length=200)
    artist: Optional[str] = Field(None, description="演唱者/乐队名称", max_length=100)
    city: Optional[str] = Field(None, description="举办城市", max_length=50)
    region: Optional[Region] = Field(None, description="地区")
    date: Optional[datetime] = Field(None, description="演唱会日期")
    address: Optional[str] = Field(None, description="详细地址", max_length=300)
    venue: Optional[str] = Field(None, description="场馆名称", max_length=100)
    platform: Optional[ConcertPlatform] = Field(None, description="官方合作平台")
    price_range: Optional[str] = Field(None, description="票价范围", max_length=50)
    duration: Optional[int] = Field(None, description="演出时长（分钟）")
    concert_type: Optional[str] = Field(None, description="演出类型", max_length=50)
    description: Optional[str] = Field(None, description="演唱会描述")
    
    class Config:
        schema_extra = {
            "example": {
                "name": "周杰伦演唱会2026（更新版）",
                "price_range": "480-2080元",
                "duration": 200
            }
        }

class ConcertStats(BaseModel):
    """演唱会统计信息模型"""
    total_concerts: int = Field(..., description="演唱会总数")
    total_artists: int = Field(..., description="演唱者总数")
    total_cities: int = Field(..., description="城市总数")
    total_regions: int = Field(..., description="地区总数")
    average_price: Optional[float] = Field(None, description="平均票价")
    total_revenue: Optional[float] = Field(None, description="总票房收入")
    region_stats: List[dict] = Field(..., description="地区统计")
    city_stats: List[dict] = Field(..., description="城市统计")
    artist_stats: List[dict] = Field(..., description="演唱者统计")
    
    class Config:
        schema_extra = {
            "example": {
                "total_concerts": 156,
                "total_artists": 45,
                "total_cities": 18,
                "total_regions": 4,
                "average_price": 850.5,
                "total_revenue": 12500000,
                "region_stats": [
                    {"region": "mainland", "count": 89},
                    {"region": "hongkong", "count": 23},
                    {"region": "macao", "count": 15},
                    {"region": "taiwan", "count": 29}
                ],
                "city_stats": [
                    {"city": "北京", "count": 25},
                    {"city": "上海", "count": 22},
                    {"city": "广州", "count": 18},
                    {"city": "深圳", "count": 15}
                ],
                "artist_stats": [
                    {"artist": "周杰伦", "count": 8},
                    {"artist": "林俊杰", "count": 6},
                    {"artist": "陈奕迅", "count": 5}
                ]
            }
        }

class SearchResult(BaseModel):
    """搜索结果模型"""
    total: int = Field(..., description="搜索结果总数")
    page: int = Field(..., description="当前页码")
    page_size: int = Field(..., description="每页大小")
    concerts: List[Concert] = Field(..., description="演唱会列表")
    
    class Config:
        schema_extra = {
            "example": {
                "total": 25,
                "page": 1,
                "page_size": 10,
                "concerts": [
                    {
                        "id": 1,
                        "name": "周杰伦演唱会2026",
                        "artist": "周杰伦",
                        "city": "北京",
                        "region": "mainland",
                        "date": "2026-03-15T20:00:00",
                        "address": "北京工人体育馆",
                        "venue": "北京工人体育馆",
                        "platform": "damai",
                        "price_range": "380-1880元",
                        "duration": 180,
                        "concert_type": "流行演唱会",
                        "description": "周杰伦2026年全国巡回演唱会北京站",
                        "created_at": "2026-02-08T10:00:00",
                        "updated_at": "2026-02-08T10:00:00"
                    }
                ]
            }
        }

class ScraperStatus(BaseModel):
    """抓取状态模型"""
    is_running: bool = Field(..., description="是否正在运行")
    last_scraped: Optional[datetime] = Field(None, description="最后抓取时间")
    total_scraped: int = Field(..., description="总共抓取数量")
    current_platform: Optional[str] = Field(None, description="当前抓取平台")
    error_count: int = Field(..., description="错误数量")
    success_count: int = Field(..., description="成功数量")
    
    class Config:
        schema_extra = {
            "example": {
                "is_running": True,
                "last_scraped": "2026-02-08T15:30:00",
                "total_scraped": 1250,
                "current_platform": "damai",
                "error_count": 5,
                "success_count": 1245
            }
        }

class DataServiceStatus(BaseModel):
    """数据服务状态模型"""
    database_connected: bool = Field(..., description="数据库连接状态")
    redis_connected: bool = Field(..., description="Redis连接状态")
    last_backup: Optional[datetime] = Field(None, description="最后备份时间")
    total_concerts: int = Field(..., description="演唱会总数")
    total_artists: int = Field(..., description="演唱者总数")
    total_cities: int = Field(..., description="城市总数")
    
    class Config:
        schema_extra = {
            "example": {
                "database_connected": True,
                "redis_connected": True,
                "last_backup": "2026-02-08T14:00:00",
                "total_concerts": 156,
                "total_artists": 45,
                "total_cities": 18
            }
        }