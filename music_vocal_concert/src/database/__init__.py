#!/usr/bin/env python3
"""
Music Vocal Concert - 数据库配置
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
import logging
import os

# 日志配置
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseConfig:
    """数据库配置类"""
    
    def __init__(self):
        self.postgresql_url = os.getenv('DATABASE_URL', 'postgresql://music_user:secure_password@localhost:5432/music_vocal_concert')
        self.mongodb_uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/music_vocal_concert')
        self.redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
        
        # 异步PostgreSQL引擎
        self.async_engine = create_async_engine(
            self.postgresql_url,
            poolclass=QueuePool,
            pool_size=20,
            max_overflow=30,
            pool_timeout=30,
            pool_recycle=1800,
            echo=False
        )
        
        # 同步PostgreSQL引擎
        self.sync_engine = create_engine(
            self.postgresql_url,
            poolclass=QueuePool,
            pool_size=20,
            max_overflow=30,
            pool_timeout=30,
            pool_recycle=1800,
            echo=False
        )
        
        # 异步会话工厂
        self.async_session_factory = sessionmaker(
            bind=self.async_engine,
            class_=AsyncSession,
            expire_on_commit=False
        )
        
        # 同步会话工厂
        self.sync_session_factory = sessionmaker(
            bind=self.sync_engine,
            expire_on_commit=False
        )
        
        logger.info("Database configuration initialized")

# 全局数据库配置实例
db_config = DatabaseConfig()

# 异步数据库会话依赖
async def get_db_session() -> AsyncSession:
    """获取异步数据库会话"""
    async with db_config.async_session_factory() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            logger.error(f"Database session error: {e}")
            raise
        finally:
            await session.close()

# 同步数据库会话依赖
def get_sync_db_session():
    """获取同步数据库会话"""
    return db_config.sync_session_factory()

# 数据库连接测试
async def test_database_connection():
    """测试数据库连接"""
    try:
        async with db_config.async_engine.connect() as conn:
            await conn.execute("SELECT 1")
        logger.info("Database connection test passed")
        return True
    except Exception as e:
        logger.error(f"Database connection test failed: {e}")
        return False

# 数据库初始化
async def init_database():
    """初始化数据库"""
    try:
        # 测试连接
        if await test_database_connection():
            logger.info("Database initialized successfully")
            return True
        else:
            logger.error("Database initialization failed")
            return False
    except Exception as e:
        logger.error(f"Database initialization error: {e}")
        return False

# 数据库关闭
async def close_database():
    """关闭数据库连接"""
    try:
        await db_config.async_engine.dispose()
        logger.info("Database connection closed")
    except Exception as e:
        logger.error(f"Database close error: {e}")

# 导出常用函数
__all__ = [
    'db_config',
    'get_db_session',
    'get_sync_db_session',
    'test_database_connection',
    'init_database',
    'close_database'
]