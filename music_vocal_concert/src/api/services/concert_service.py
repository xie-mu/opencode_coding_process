#!/usr/bin/env python3
"""
Music Vocal Concert - 演唱会服务
提供演唱会信息的业务逻辑处理
"""

from typing import List, Optional, Dict, Any
from datetime import datetime, timedelta
from sqlalchemy import select, and_, or_, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
import logging

from ..models.concert import Concert, ConcertCreate, ConcertUpdate
from ..database import get_db_session

logger = logging.getLogger(__name__)

class ConcertService:
    """演唱会服务类"""
    
    def __init__(self):
        self.db_session = None
    
    async def initialize(self):
        """初始化服务"""
        logger.info("ConcertService 初始化中...")
        self.db_session = get_db_session()
        logger.info("ConcertService 初始化完成")
    
    async def shutdown(self):
        """关闭服务"""
        logger.info("ConcertService 关闭中...")
        if self.db_session:
            await self.db_session.close()
        logger.info("ConcertService 关闭完成")
    
    async def get_concerts(
        self,
        city: Optional[str] = None,
        artist: Optional[str] = None,
        date_from: Optional[datetime] = None,
        date_to: Optional[datetime] = None,
        page: int = 1,
        page_size: int = 20
    ) -> List[Concert]:
        """
        获取演唱会列表
        
        Args:
            city: 城市过滤
            artist: 演唱者过滤
            date_from: 日期范围开始
            date_to: 日期范围结束
            page: 页码
            page_size: 每页大小
            
        Returns:
            演唱会列表
        """
        try:
            # 构建查询条件
            conditions = []
            
            if city:
                conditions.append(Concert.city.ilike(f"%{city}%"))
            
            if artist:
                conditions.append(Concert.artist.ilike(f"%{artist}%"))
            
            if date_from:
                conditions.append(Concert.date >= date_from)
            
            if date_to:
                conditions.append(Concert.date <= date_to)
            
            # 构建查询
            query = select(Concert).where(and_(*conditions)) if conditions else select(Concert)
            
            # 添加分页
            offset = (page - 1) * page_size
            query = query.offset(offset).limit(page_size)
            
            # 执行查询
            result = await self.db_session.execute(query)
            concerts = result.scalars().all()
            
            return concerts
            
        except Exception as e:
            logger.error(f"获取演唱会列表失败: {e}")
            raise
    
    async def get_concert(self, concert_id: int) -> Optional[Concert]:
        """
        获取单个演唱会信息
        
        Args:
            concert_id: 演唱会ID
            
        Returns:
            演唱会信息
        """
        try:
            query = select(Concert).where(Concert.id == concert_id)
            result = await self.db_session.execute(query)
            concert = result.scalar_one_or_none()
            
            return concert
            
        except Exception as e:
            logger.error(f"获取演唱会信息失败: {e}")
            raise
    
    async def create_concert(self, concert_data: ConcertCreate) -> Concert:
        """
        创建演唱会信息
        
        Args:
            concert_data: 演唱会创建数据
            
        Returns:
            创建的演唱会信息
        """
        try:
            # 创建演唱会对象
            concert = Concert(
                name=concert_data.name,
                artist=concert_data.artist,
                city=concert_data.city,
                region=concert_data.region,
                date=concert_data.date,
                address=concert_data.address,
                venue=concert_data.venue,
                platform=concert_data.platform,
                price_range=concert_data.price_range,
                duration=concert_data.duration,
                concert_type=concert_data.concert_type,
                description=concert_data.description,
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            
            # 保存到数据库
            self.db_session.add(concert)
            await self.db_session.commit()
            await self.db_session.refresh(concert)
            
            logger.info(f"创建演唱会信息成功: {concert.id}")
            return concert
            
        except Exception as e:
            logger.error(f"创建演唱会信息失败: {e}")
            await self.db_session.rollback()
            raise
    
    async def update_concert(self, concert_id: int, concert_data: ConcertUpdate) -> Optional[Concert]:
        """
        更新演唱会信息
        
        Args:
            concert_id: 演唱会ID
            concert_data: 演唱会更新数据
            
        Returns:
            更新后的演唱会信息
        """
        try:
            # 获取演唱会信息
            query = select(Concert).where(Concert.id == concert_id)
            result = await self.db_session.execute(query)
            concert = result.scalar_one_or_none()
            
            if not concert:
                return None
            
            # 更新字段
            if concert_data.name is not None:
                concert.name = concert_data.name
            if concert_data.artist is not None:
                concert.artist = concert_data.artist
            if concert_data.city is not None:
                concert.city = concert_data.city
            if concert_data.region is not None:
                concert.region = concert_data.region
            if concert_data.date is not None:
                concert.date = concert_data.date
            if concert_data.address is not None:
                concert.address = concert_data.address
            if concert_data.venue is not None:
                concert.venue = concert_data.venue
            if concert_data.platform is not None:
                concert.platform = concert_data.platform
            if concert_data.price_range is not None:
                concert.price_range = concert_data.price_range
            if concert_data.duration is not None:
                concert.duration = concert_data.duration
            if concert_data.concert_type is not None:
                concert.concert_type = concert_data.concert_type
            if concert_data.description is not None:
                concert.description = concert_data.description
            
            # 更新时间
            concert.updated_at = datetime.now()
            
            # 保存到数据库
            await self.db_session.commit()
            await self.db_session.refresh(concert)
            
            logger.info(f"更新演唱会信息成功: {concert.id}")
            return concert
            
        except Exception as e:
            logger.error(f"更新演唱会信息失败: {e}")
            await self.db_session.rollback()
            raise
    
    async def delete_concert(self, concert_id: int) -> bool:
        """
        删除演唱会信息
        
        Args:
            concert_id: 演唱会ID
            
        Returns:
            是否删除成功
        """
        try:
            # 获取演唱会信息
            query = select(Concert).where(Concert.id == concert_id)
            result = await self.db_session.execute(query)
            concert = result.scalar_one_or_none()
            
            if not concert:
                return False
            
            # 删除演唱会
            await self.db_session.delete(concert)
            await self.db_session.commit()
            
            logger.info(f"删除演唱会信息成功: {concert_id}")
            return True
            
        except Exception as e:
            logger.error(f"删除演唱会信息失败: {e}")
            await self.db_session.rollback()
            raise
    
    async def search_concerts(
        self,
        query: str,
        city: Optional[str] = None,
        artist: Optional[str] = None,
        page: int = 1,
        page_size: int = 20
    ) -> Dict[str, Any]:
        """
        搜索演唱会
        
        Args:
            query: 搜索关键词
            city: 城市过滤
            artist: 演唱者过滤
            page: 页码
            page_size: 每页大小
            
        Returns:
            搜索结果
        """
        try:
            # 构建搜索条件
            conditions = []
            
            # 关键词搜索
            conditions.append(
                or_(
                    Concert.name.ilike(f"%{query}%"),
                    Concert.artist.ilike(f"%{query}%"),
                    Concert.address.ilike(f"%{query}%"),
                    Concert.venue.ilike(f"%{query}%")
                )
            )
            
            # 城市过滤
            if city:
                conditions.append(Concert.city.ilike(f"%{city}%"))
            
            # 演唱者过滤
            if artist:
                conditions.append(Concert.artist.ilike(f"%{artist}%"))
            
            # 构建查询
            query_obj = select(Concert).where(and_(*conditions))
            
            # 获取总数
            count_query = select(func.count()).select_from(query_obj.subquery())
            total_result = await self.db_session.execute(count_query)
            total = total_result.scalar()
            
            # 添加分页
            offset = (page - 1) * page_size
            query_obj = query_obj.offset(offset).limit(page_size)
            
            # 执行查询
            result = await self.db_session.execute(query_obj)
            concerts = result.scalars().all()
            
            return {
                "total": total,
                "page": page,
                "page_size": page_size,
                "concerts": concerts
            }
            
        except Exception as e:
            logger.error(f"搜索演唱会失败: {e}")
            raise
    
    async def get_upcoming_concerts(self, days: int = 30) -> List[Concert]:
        """
        获取即将到来的演唱会
        
        Args:
            days: 天数范围
            
        Returns:
            即将到来的演唱会列表
        """
        try:
            # 计算日期范围
            date_from = datetime.now()
            date_to = date_from + timedelta(days=days)
            
            # 构建查询
            query = select(Concert).where(
                and_(
                    Concert.date >= date_from,
                    Concert.date <= date_to
                )
            ).order_by(Concert.date)
            
            # 执行查询
            result = await self.db_session.execute(query)
            concerts = result.scalars().all()
            
            return concerts
            
        except Exception as e:
            logger.error(f"获取即将到来的演唱会失败: {e}")
            raise
    
    async def get_concerts_by_artist(self, artist: str) -> List[Concert]:
        """
        获取特定演唱者的演唱会
        
        Args:
            artist: 演唱者名称
            
        Returns:
            演唱会列表
        """
        try:
            query = select(Concert).where(Concert.artist.ilike(f"%{artist}%"))
            result = await self.db_session.execute(query)
            concerts = result.scalars().all()
            
            return concerts
            
        except Exception as e:
            logger.error(f"获取演唱者演唱会失败: {e}")
            raise
    
    async def get_concerts_by_city(self, city: str) -> List[Concert]:
        """
        获取特定城市的演唱会
        
        Args:
            city: 城市名称
            
        Returns:
            演唱会列表
        """
        try:
            query = select(Concert).where(Concert.city.ilike(f"%{city}%"))
            result = await self.db_session.execute(query)
            concerts = result.scalars().all()
            
            return concerts
            
        except Exception as e:
            logger.error(f"获取城市演唱会失败: {e}")
            raise
    
    async def get_concerts_by_platform(self, platform: str) -> List[Concert]:
        """
        获取特定平台的演唱会
        
        Args:
            platform: 平台名称
            
        Returns:
            演唱会列表
        """
        try:
            query = select(Concert).where(Concert.platform == platform)
            result = await self.db_session.execute(query)
            concerts = result.scalars().all()
            
            return concerts
            
        except Exception as e:
            logger.error(f"获取平台演唱会失败: {e}")
            raise