#!/usr/bin/env python3
"""
Music Vocal Concert - 数据库迁移脚本
"""

import asyncio
import logging
from sqlalchemy import text
from .models import Base, Concert, User, UserFavorite, ScrapingLog, AuditLog, SystemConfig
from . import db_config

# 日志配置
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseMigrator:
    """数据库迁移器"""
    
    def __init__(self):
        self.async_engine = db_config.async_engine
    
    async def create_tables(self):
        """创建数据库表"""
        try:
            async with self.async_engine.begin() as conn:
                # 创建表
                await conn.run_sync(Base.metadata.create_all)
            logger.info("Database tables created successfully")
            return True
        except Exception as e:
            logger.error(f"Error creating tables: {e}")
            return False
    
    async def create_indexes(self):
        """创建数据库索引"""
        try:
            async with self.async_engine.begin() as conn:
                # 演唱会表索引
                await conn.execute(text("""
                    CREATE INDEX IF NOT EXISTS idx_concert_date ON concerts(date);
                """))
                await conn.execute(text("""
                    CREATE INDEX IF NOT EXISTS idx_concert_platform ON concerts(platform);
                """))
                await conn.execute(text("""
                    CREATE INDEX IF NOT EXISTS idx_concert_region ON concerts(region);
                """))
                await conn.execute(text("""
                    CREATE INDEX IF NOT EXISTS idx_concert_city_artist ON concerts(city, artist);
                """))
                
                # 用户表索引
                await conn.execute(text("""
                    CREATE INDEX IF NOT EXISTS idx_user_email ON users(email);
                """))
                await conn.execute(text("""
                    CREATE INDEX IF NOT EXISTS idx_user_username ON users(username);
                """))
                
                # 用户收藏表索引
                await conn.execute(text("""
                    CREATE INDEX IF NOT EXISTS idx_user_concert ON user_favorites(user_id, concert_id);
                """))
                
                # 抓取日志表索引
                await conn.execute(text("""
                    CREATE INDEX IF NOT EXISTS idx_scraping_platform ON scraping_logs(platform);
                """))
                await conn.execute(text("""
                    CREATE INDEX IF NOT EXISTS idx_scraping_status ON scraping_logs(status);
                """))
                await conn.execute(text("""
                    CREATE INDEX IF NOT EXISTS idx_scraping_time ON scraping_logs(started_at);
                """))
                
                # 审计日志表索引
                await conn.execute(text("""
                    CREATE INDEX IF NOT EXISTS idx_audit_action ON audit_logs(action);
                """))
                await conn.execute(text("""
                    CREATE INDEX IF NOT EXISTS idx_audit_resource ON audit_logs(resource_type, resource_id);
                """))
                await conn.execute(text("""
                    CREATE INDEX IF NOT EXISTS idx_audit_time ON audit_logs(timestamp);
                """))
                
                # 系统配置表索引
                await conn.execute(text("""
                    CREATE INDEX IF NOT EXISTS idx_config_category ON system_configs(category);
                """))
                
            logger.info("Database indexes created successfully")
            return True
        except Exception as e:
            logger.error(f"Error creating indexes: {e}")
            return False
    
    async def create_default_configs(self):
        """创建默认配置"""
        try:
            async with self.async_engine.begin() as conn:
                # 检查是否已有配置
                result = await conn.execute(text("""
                    SELECT COUNT(*) FROM system_configs;
                """))
                count = result.scalar()
                
                if count == 0:
                    # 创建默认配置
                    configs = [
                        ("scraper.delay", "1.0", "爬虫抓取延迟（秒）", "crawler"),
                        ("scraper.max_retries", "3", "最大重试次数", "crawler"),
                        ("scraper.timeout", "30", "抓取超时时间（秒）", "crawler"),
                        ("api.rate_limit", "1000", "API调用限制（每分钟）", "api"),
                        ("api.cache_ttl", "3600", "缓存过期时间（秒）", "api"),
                        ("security.jwt_secret", "", "JWT密钥", "security"),
                        ("security.session_timeout", "3600", "会话超时时间（秒）", "security"),
                        ("monitoring.prometheus_enabled", "true", "Prometheus监控启用", "monitoring"),
                        ("monitoring.grafana_enabled", "true", "Grafana监控启用", "monitoring"),
                    ]
                    
                    for key, value, description, category in configs:
                        await conn.execute(text("""
                            INSERT INTO system_configs (key, value, description, category)
                            VALUES (:key, :value, :description, :category);
                        """), {
                            "key": key,
                            "value": value,
                            "description": description,
                            "category": category
                        })
                    
                    logger.info("Default system configurations created")
                else:
                    logger.info("System configurations already exist, skipping creation")
            
            return True
        except Exception as e:
            logger.error(f"Error creating default configs: {e}")
            return False
    
    async def create_sample_data(self):
        """创建示例数据"""
        try:
            async with self.async_engine.begin() as conn:
                # 检查是否已有数据
                result = await conn.execute(text("""
                    SELECT COUNT(*) FROM concerts;
                """))
                count = result.scalar()
                
                if count == 0:
                    # 创建示例演唱会数据
                    sample_concerts = [
                        {
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
                        },
                        {
                            "name": "林俊杰演唱会2026",
                            "artist": "林俊杰",
                            "city": "上海",
                            "region": "mainland",
                            "date": "2026-03-20T19:30:00",
                            "address": "上海体育馆",
                            "venue": "上海体育馆",
                            "platform": "maoyan",
                            "price_range": "480-2280元",
                            "duration": 160,
                            "concert_type": "流行演唱会",
                            "description": "林俊杰2026年全国巡回演唱会上海站"
                        },
                        {
                            "name": "陈奕迅演唱会2026",
                            "artist": "陈奕迅",
                            "city": "广州",
                            "region": "mainland",
                            "date": "2026-03-25T20:00:00",
                            "address": "广州体育馆",
                            "venue": "广州体育馆",
                            "platform": "showstart",
                            "price_range": "350-1680元",
                            "duration": 150,
                            "concert_type": "流行演唱会",
                            "description": "陈奕迅2026年全国巡回演唱会广州站"
                        }
                    ]
                    
                    for concert in sample_concerts:
                        await conn.execute(text("""
                            INSERT INTO concerts (name, artist, city, region, date, address, venue, platform, price_range, duration, concert_type, description)
                            VALUES (:name, :artist, :city, :region, :date, :address, :venue, :platform, :price_range, :duration, :concert_type, :description);
                        """), concert)
                    
                    logger.info("Sample concert data created")
                else:
                    logger.info("Concert data already exists, skipping creation")
            
            return True
        except Exception as e:
            logger.error(f"Error creating sample data: {e}")
            return False
    
    async def run_migration(self):
        """运行完整迁移"""
        logger.info("Starting database migration...")
        
        # 创建表
        if not await self.create_tables():
            logger.error("Table creation failed")
            return False
        
        # 创建索引
        if not await self.create_indexes():
            logger.error("Index creation failed")
            return False
        
        # 创建默认配置
        if not await self.create_default_configs():
            logger.error("Default config creation failed")
            return False
        
        # 创建示例数据
        if not await self.create_sample_data():
            logger.error("Sample data creation failed")
            return False
        
        logger.info("Database migration completed successfully")
        return True

# 迁移函数
async def migrate_database():
    """迁移数据库"""
    migrator = DatabaseMigrator()
    return await migrator.run_migration()

# 导出函数
__all__ = [
    'DatabaseMigrator',
    'migrate_database'
]