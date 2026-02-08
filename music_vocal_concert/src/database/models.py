#!/usr/bin/env python3
"""
Music Vocal Concert - 数据库模型
"""

from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
import logging

# 日志配置
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 基础模型
Base = declarative_base()

class Concert(Base):
    """演唱会数据模型"""
    
    __tablename__ = 'concerts'
    
    # 主键
    id = Column(Integer, primary_key=True, index=True)
    
    # 基本信息
    name = Column(String(200), nullable=False, index=True)
    artist = Column(String(100), nullable=False, index=True)
    city = Column(String(50), nullable=False, index=True)
    region = Column(String(20), nullable=False, index=True)  # mainland, hongkong, macao, taiwan
    
    # 时间信息
    date = Column(DateTime, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 详细信息
    address = Column(String(300), nullable=False)
    venue = Column(String(100), nullable=False)
    platform = Column(String(50), nullable=False, index=True)  # damai, maoyan, showstart, touminglun, yongle, other
    price_range = Column(String(50))
    duration = Column(Integer)  # 分钟
    concert_type = Column(String(50))
    description = Column(Text)
    
    # 索引
    __table_args__ = (
        Index('idx_concert_date', 'date'),
        Index('idx_concert_platform', 'platform'),
        Index('idx_concert_region', 'region'),
        Index('idx_concert_city_artist', 'city', 'artist'),
    )
    
    # 关系
    favorites = relationship("UserFavorite", back_populates="concert", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Concert(id={self.id}, name='{self.name}', artist='{self.artist}', city='{self.city}')>"

class User(Base):
    """用户数据模型"""
    
    __tablename__ = 'users'
    
    # 主键
    id = Column(Integer, primary_key=True, index=True)
    
    # 用户信息
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 用户设置
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    last_login_at = Column(DateTime)
    
    # 关系
    favorites = relationship("UserFavorite", back_populates="user", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"

class UserFavorite(Base):
    """用户收藏数据模型"""
    
    __tablename__ = 'user_favorites'
    
    # 主键
    id = Column(Integer, primary_key=True, index=True)
    
    # 外键
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    concert_id = Column(Integer, ForeignKey('concerts.id'), nullable=False, index=True)
    
    # 时间信息
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    
    # 关系
    user = relationship("User", back_populates="favorites")
    concert = relationship("Concert", back_populates="favorites")
    
    # 唯一约束
    __table_args__ = (
        Index('idx_user_concert', 'user_id', 'concert_id', unique=True),
    )
    
    def __repr__(self):
        return f"<UserFavorite(id={self.id}, user_id={self.user_id}, concert_id={self.concert_id})>"

class ScrapingLog(Base):
    """数据抓取日志模型"""
    
    __tablename__ = 'scraping_logs'
    
    # 主键
    id = Column(Integer, primary_key=True, index=True)
    
    # 抓取信息
    platform = Column(String(50), nullable=False, index=True)
    concert_id = Column(Integer, ForeignKey('concerts.id'), nullable=True)
    status = Column(String(20), nullable=False, index=True)  # success, failed, partial
    message = Column(Text)
    
    # 时间信息
    started_at = Column(DateTime, default=datetime.utcnow, index=True)
    completed_at = Column(DateTime)
    
    # 抓取统计
    data_count = Column(Integer, default=0)
    error_count = Column(Integer, default=0)
    
    def __repr__(self):
        return f"<ScrapingLog(id={self.id}, platform='{self.platform}', status='{self.status}')>"

class AuditLog(Base):
    """审计日志模型"""
    
    __tablename__ = 'audit_logs'
    
    # 主键
    id = Column(Integer, primary_key=True, index=True)
    
    # 审计信息
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True, index=True)
    action = Column(String(50), nullable=False, index=True)  # create, update, delete, view
    resource_type = Column(String(50), nullable=False, index=True)  # concert, user, favorite
    resource_id = Column(Integer, nullable=True, index=True)
    old_values = Column(Text)
    new_values = Column(Text)
    
    # 时间信息
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    
    # 客户端信息
    ip_address = Column(String(45))
    user_agent = Column(String(255))
    
    def __repr__(self):
        return f"<AuditLog(id={self.id}, action='{self.action}', resource_type='{self.resource_type}')>"

class SystemConfig(Base):
    """系统配置模型"""
    
    __tablename__ = 'system_configs'
    
    # 主键
    id = Column(Integer, primary_key=True, index=True)
    
    # 配置信息
    key = Column(String(100), unique=True, nullable=False, index=True)
    value = Column(Text, nullable=False)
    description = Column(String(500))
    category = Column(String(50), index=True)
    
    # 元数据
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<SystemConfig(id={self.id}, key='{self.key}', category='{self.category}')>"

# 数据库初始化函数
def create_tables():
    """创建数据库表"""
    try:
        # 这里需要实际的数据库引擎
        # 在实际应用中，这应该由Alembic或其他迁移工具处理
        logger.info("Database tables creation function defined")
        return True
    except Exception as e:
        logger.error(f"Error creating tables: {e}")
        return False

# 数据库模型导出
__all__ = [
    'Base',
    'Concert',
    'User',
    'UserFavorite',
    'ScrapingLog',
    'AuditLog',
    'SystemConfig',
    'create_tables'
]