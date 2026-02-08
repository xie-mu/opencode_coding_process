#!/usr/bin/env python3
"""
Music Vocal Concert API主文件
演唱会信息汇总系统的核心API服务
"""

from fastapi import FastAPI, HTTPException, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from typing import List, Optional
from datetime import datetime
import logging
from contextlib import asynccontextmanager

from .models.concert import Concert, ConcertCreate, ConcertUpdate
from .services.concert_service import ConcertService
from .services.data_service import DataService
from .services.scraper_service import ScraperService

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期管理"""
    # 启动时执行
    logger.info("Music Vocal Concert API 启动中...")
    
    # 初始化服务
    await app.state.concert_service.initialize()
    await app.state.data_service.initialize()
    await app.state.scraper_service.initialize()
    
    logger.info("Music Vocal Concert API 启动完成")
    yield
    
    # 关闭时执行
    logger.info("Music Vocal Concert API 关闭中...")
    await app.state.concert_service.shutdown()
    await app.state.data_service.shutdown()
    await app.state.scraper_service.shutdown()
    logger.info("Music Vocal Concert API 关闭完成")

# 创建FastAPI应用
app = FastAPI(
    title="Music Vocal Concert API",
    description="演唱会信息汇总系统API",
    version="1.0.0",
    lifespan=lifespan
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 挂载静态文件
app.mount("/static", StaticFiles(directory="static"), name="static")

# 依赖注入
def get_concert_service():
    return app.state.concert_service

def get_data_service():
    return app.state.data_service

def get_scraper_service():
    return app.state.scraper_service

@app.get("/")
async def root():
    """根路径"""
    return {
        "message": "Welcome to Music Vocal Concert API",
        "version": "1.0.0",
        "description": "演唱会信息汇总系统",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/health")
async def health_check():
    """健康检查"""
    return {
        "status": "healthy",
        "service": "Music Vocal Concert API",
        "timestamp": datetime.now().isoformat()
    }

# 演唱会信息API
@app.get("/api/concerts", response_model=List[Concert])
async def get_concerts(
    city: Optional[str] = Query(None, description="城市过滤"),
    artist: Optional[str] = Query(None, description="演唱者过滤"),
    date_from: Optional[datetime] = Query(None, description="日期范围开始"),
    date_to: Optional[datetime] = Query(None, description="日期范围结束"),
    page: int = Query(1, ge=1, description="页码"),
    page_size: int = Query(20, ge=1, le=100, description="每页大小"),
    concert_service: ConcertService = Depends(get_concert_service)
):
    """获取演唱会列表"""
    try:
        concerts = await concert_service.get_concerts(
            city=city,
            artist=artist,
            date_from=date_from,
            date_to=date_to,
            page=page,
            page_size=page_size
        )
        return concerts
    except Exception as e:
        logger.error(f"获取演唱会列表失败: {e}")
        raise HTTPException(status_code=500, detail="获取演唱会列表失败")

@app.get("/api/concerts/{concert_id}", response_model=Concert)
async def get_concert(concert_id: int, concert_service: ConcertService = Depends(get_concert_service)):
    """获取单个演唱会信息"""
    try:
        concert = await concert_service.get_concert(concert_id)
        if not concert:
            raise HTTPException(status_code=404, detail="演唱会信息未找到")
        return concert
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"获取演唱会信息失败: {e}")
        raise HTTPException(status_code=500, detail="获取演唱会信息失败")

@app.post("/api/concerts", response_model=Concert)
async def create_concert(
    concert: ConcertCreate,
    concert_service: ConcertService = Depends(get_concert_service)
):
    """创建演唱会信息"""
    try:
        new_concert = await concert_service.create_concert(concert)
        return new_concert
    except Exception as e:
        logger.error(f"创建演唱会信息失败: {e}")
        raise HTTPException(status_code=500, detail="创建演唱会信息失败")

@app.put("/api/concerts/{concert_id}", response_model=Concert)
async def update_concert(
    concert_id: int,
    concert: ConcertUpdate,
    concert_service: ConcertService = Depends(get_concert_service)
):
    """更新演唱会信息"""
    try:
        updated_concert = await concert_service.update_concert(concert_id, concert)
        if not updated_concert:
            raise HTTPException(status_code=404, detail="演唱会信息未找到")
        return updated_concert
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"更新演唱会信息失败: {e}")
        raise HTTPException(status_code=500, detail="更新演唱会信息失败")

@app.delete("/api/concerts/{concert_id}")
async def delete_concert(
    concert_id: int,
    concert_service: ConcertService = Depends(get_concert_service)
):
    """删除演唱会信息"""
    try:
        success = await concert_service.delete_concert(concert_id)
        if not success:
            raise HTTPException(status_code=404, detail="演唱会信息未找到")
        return {"message": "演唱会信息删除成功"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"删除演唱会信息失败: {e}")
        raise HTTPException(status_code=500, detail="删除演唱会信息失败")

# 数据抓取API
@app.get("/api/scraping/status")
async def scraping_status(scraper_service: ScraperService = Depends(get_scraper_service)):
    """获取抓取状态"""
    try:
        status = await scraper_service.get_status()
        return status
    except Exception as e:
        logger.error(f"获取抓取状态失败: {e}")
        raise HTTPException(status_code=500, detail="获取抓取状态失败")

@app.post("/api/scraping/start")
async def start_scraping(scraper_service: ScraperService = Depends(get_scraper_service)):
    """开始抓取数据"""
    try:
        result = await scraper_service.start_scraping()
        return result
    except Exception as e:
        logger.error(f"开始抓取数据失败: {e}")
        raise HTTPException(status_code=500, detail="开始抓取数据失败")

@app.post("/api/scraping/stop")
async def stop_scraping(scraper_service: ScraperService = Depends(get_scraper_service)):
    """停止抓取数据"""
    try:
        result = await scraper_service.stop_scraping()
        return result
    except Exception as e:
        logger.error(f"停止抓取数据失败: {e}")
        raise HTTPException(status_code=500, detail="停止抓取数据失败")

# 数据统计API
@app.get("/api/stats/concerts")
async def get_concert_stats(data_service: DataService = Depends(get_data_service)):
    """获取演唱会统计信息"""
    try:
        stats = await data_service.get_concert_stats()
        return stats
    except Exception as e:
        logger.error(f"获取演唱会统计信息失败: {e}")
        raise HTTPException(status_code=500, detail="获取演唱会统计信息失败")

@app.get("/api/stats/regions")
async def get_region_stats(data_service: DataService = Depends(get_data_service)):
    """获取地区统计信息"""
    try:
        stats = await data_service.get_region_stats()
        return stats
    except Exception as e:
        logger.error(f"获取地区统计信息失败: {e}")
        raise HTTPException(status_code=500, detail="获取地区统计信息失败")

@app.get("/api/stats/artists")
async def get_artist_stats(data_service: DataService = Depends(get_data_service)):
    """获取演唱者统计信息"""
    try:
        stats = await data_service.get_artist_stats()
        return stats
    except Exception as e:
        logger.error(f"获取演唱者统计信息失败: {e}")
        raise HTTPException(status_code=500, detail="获取演唱者统计信息失败")

# 搜索API
@app.get("/api/search")
async def search_concerts(
    query: str = Query(..., description="搜索关键词"),
    city: Optional[str] = Query(None, description="城市过滤"),
    artist: Optional[str] = Query(None, description="演唱者过滤"),
    page: int = Query(1, ge=1, description="页码"),
    page_size: int = Query(20, ge=1, le=100, description="每页大小"),
    concert_service: ConcertService = Depends(get_concert_service)
):
    """搜索演唱会"""
    try:
        results = await concert_service.search_concerts(
            query=query,
            city=city,
            artist=artist,
            page=page,
            page_size=page_size
        )
        return results
    except Exception as e:
        logger.error(f"搜索演唱会失败: {e}")
        raise HTTPException(status_code=500, detail="搜索演唱会失败")

# 错误处理
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """全局异常处理器"""
    logger.error(f"全局异常: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "内部服务器错误"}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")