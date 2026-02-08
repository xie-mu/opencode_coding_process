# Music Vocal Concert 数据与API规范

## 1. 数据规范

### 1.1 数据模型

#### 1.1.1 演唱会数据模型
```json
{
  "concert_id": "唯一标识符",
  "name": "演唱会名称",
  "artist": "演唱者/乐队名称",
  "city": "举办城市",
  "region": "地区（mainland/hongkong/macao/taiwan）",
  "date": "演唱会日期（ISO 8601格式）",
  "address": "详细地址",
  "venue": "场馆名称",
  "platform": "官方合作平台（damai/maoyan/showstart/touminglun/yongle/other）",
  "price_range": "票价范围",
  "duration": "演出时长（分钟）",
  "concert_type": "演出类型",
  "description": "演唱会描述",
  "created_at": "创建时间（ISO 8601格式）",
  "updated_at": "更新时间（ISO 8601格式）"
}
```

#### 1.1.2 用户数据模型
```json
{
  "user_id": "唯一标识符",
  "username": "用户名",
  "email": "邮箱地址",
  "password_hash": "密码哈希",
  "created_at": "创建时间（ISO 8601格式）",
  "updated_at": "更新时间（ISO 8601格式）"
}
```

#### 1.1.3 用户收藏数据模型
```json
{
  "favorite_id": "唯一标识符",
  "user_id": "用户ID",
  "concert_id": "演唱会ID",
  "created_at": "创建时间（ISO 8601格式）"
}
```

### 1.2 数据验证规则

#### 1.2.1 演唱会数据验证
```python
# 演唱会数据验证规则
from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional

class ConcertValidation(BaseModel):
    # 必填字段
    name: str = Field(..., min_length=1, max_length=200, description="演唱会名称")
    artist: str = Field(..., min_length=1, max_length=100, description="演唱者/乐队名称")
    city: str = Field(..., min_length=1, max_length=50, description="举办城市")
    date: datetime = Field(..., description="演唱会日期")
    address: str = Field(..., min_length=1, max_length=300, description="详细地址")
    venue: str = Field(..., min_length=1, max_length=100, description="场馆名称")
    platform: str = Field(..., description="官方合作平台")
    
    # 可选字段
    price_range: Optional[str] = Field(None, max_length=50, description="票价范围")
    duration: Optional[int] = Field(None, ge=1, le=600, description="演出时长（分钟）")
    concert_type: Optional[str] = Field(None, max_length=50, description="演出类型")
    description: Optional[str] = Field(None, max_length=1000, description="演唱会描述")
    
    @validator('date')
    def validate_date(cls, v):
        """验证日期"""
        if v < datetime.now():
            raise ValueError('演唱会日期不能早于当前时间')
        return v
    
    @validator('price_range')
    def validate_price_range(cls, v):
        """验证票价范围"""
        if v and not re.match(r'^\d+-\d+元$', v):
            raise ValueError('票价范围格式不正确，应为"最低价-最高价元"')
        return v
```

### 1.3 数据格式规范

#### 1.3.1 日期格式
- **格式**: ISO 8601
- **示例**: "2026-03-15T20:00:00+08:00"
- **时区**: 北京时间 (UTC+8)

#### 1.3.2 地区代码
- **mainland**: 中国大陆
- **hongkong**: 香港
- **macao**: 澳门
- **taiwan**: 台湾

#### 1.3.3 平台代码
- **damai**: 大麦网
- **maoyan**: 猫眼演出
- **showstart**: 秀动
- **touminglun**: 摩天轮
- **yongle**: 永乐票务
- **other**: 其他平台

## 2. API规范

### 2.1 RESTful API设计原则

#### 2.1.1 资源命名
- **复数形式**: 使用复数形式表示资源集合
- **路径层级**: 使用斜杠表示层级关系
- **过滤参数**: 使用查询参数进行过滤

#### 2.1.2 HTTP方法
- **GET**: 获取资源
- **POST**: 创建资源
- **PUT**: 更新资源
- **PATCH**: 部分更新资源
- **DELETE**: 删除资源

#### 2.1.3 状态码
- **200**: 成功
- **201**: 创建成功
- **400**: 请求错误
- **401**: 未授权
- **403**: 禁止访问
- **404**: 资源未找到
- **500**: 服务器错误

### 2.2 API版本控制

#### 2.2.1 版本格式
- **URL版本**: `/api/v1/concerts`
- **Header版本**: `Accept: application/vnd.music-vocal-concert.v1+json`

#### 2.2.2 版本策略
- **向后兼容**: 新版本保持向后兼容
- **弃用通知**: 提前通知API弃用
- **文档更新**: 及时更新API文档

### 2.3 请求规范

#### 2.3.1 请求头
```http
Content-Type: application/json
Accept: application/json
Authorization: Bearer <token>
X-Request-ID: <uuid>
```

#### 2.3.2 请求体
```json
{
  "name": "演唱会名称",
  "artist": "演唱者",
  "city": "城市",
  "date": "2026-03-15T20:00:00+08:00",
  "address": "详细地址",
  "venue": "场馆名称",
  "platform": "damai",
  "price_range": "380-1880元",
  "duration": 180,
  "concert_type": "流行演唱会",
  "description": "演唱会描述"
}
```

#### 2.3.3 查询参数
```http
GET /api/v1/concerts?city=北京&artist=周杰伦&page=1&page_size=20
```

### 2.4 响应规范

#### 2.4.1 成功响应
```json
{
  "status": "success",
  "data": {
    "concerts": [
      {
        "id": 1,
        "name": "周杰伦演唱会",
        "artist": "周杰伦",
        "city": "北京",
        "region": "mainland",
        "date": "2026-03-15T20:00:00+08:00",
        "address": "北京工人体育馆",
        "venue": "北京工人体育馆",
        "platform": "damai",
        "price_range": "380-1880元",
        "duration": 180,
        "concert_type": "流行演唱会",
        "description": "周杰伦2026年全国巡回演唱会北京站",
        "created_at": "2026-02-08T10:00:00+08:00",
        "updated_at": "2026-02-08T10:00:00+08:00"
      }
    ],
    "pagination": {
      "page": 1,
      "page_size": 20,
      "total": 156,
      "total_pages": 8
    }
  },
  "meta": {
    "timestamp": "2026-02-08T15:30:00+08:00",
    "request_id": "req_123456789"
  }
}
```

#### 2.4.2 错误响应
```json
{
  "status": "error",
  "error": {
    "code": "INVALID_REQUEST",
    "message": "请求参数无效",
    "details": [
      {
        "field": "date",
        "message": "演唱会日期不能早于当前时间"
      }
    ]
  },
  "meta": {
    "timestamp": "2026-02-08T15:30:00+08:00",
    "request_id": "req_123456789"
  }
}
```

### 2.5 API端点

#### 2.5.1 演唱会管理
```http
# 获取演唱会列表
GET /api/v1/concerts

# 获取单个演唱会
GET /api/v1/concerts/{id}

# 创建演唱会
POST /api/v1/concerts

# 更新演唱会
PUT /api/v1/concerts/{id}

# 删除演唱会
DELETE /api/v1/concerts/{id}
```

#### 2.5.2 搜索功能
```http
# 搜索演唱会
GET /api/v1/search

# 搜索参数
query: 搜索关键词
city: 城市过滤
artist: 演唱者过滤
date_from: 日期范围开始
date_to: 日期范围结束
page: 页码
page_size: 每页大小
```

#### 2.5.3 统计功能
```http
# 获取演唱会统计
GET /api/v1/stats/concerts

# 获取地区统计
GET /api/v1/stats/regions

# 获取演唱者统计
GET /api/v1/stats/artists
```

#### 2.5.4 数据抓取
```http
# 获取抓取状态
GET /api/v1/scraping/status

# 开始抓取
POST /api/v1/scraping/start

# 停止抓取
POST /api/v1/scraping/stop
```

## 3. 数据抓取规范

### 3.1 抓取策略

#### 3.1.1 多平台抓取
- **优先级**: 官方API > 网页抓取
- **频率**: 每小时抓取一次
- **并发**: 控制并发数量
- **错误处理**: 自动重试和错误记录

#### 3.1.2 数据验证
- **完整性验证**: 检查必填字段
- **格式验证**: 验证数据格式
- **准确性验证**: 验证数据准确性
- **重复检测**: 检测重复数据

### 3.2 抓取规则

#### 3.2.1 大麦网
```python
# 大麦网抓取规则
PLATFORM_DAMAI = {
    "base_url": "https://www.damai.cn",
    "api_url": "https://www.damai.cn/api/concerts",
    "selectors": {
        "concerts": ".concert-item",
        "name": ".title::text",
        "artist": ".artist::text",
        "city": ".city::text",
        "date": ".date::text",
        "address": ".address::text",
        "venue": ".venue::text",
        "price_range": ".price::text"
    },
    "headers": {
        "User-Agent": "Mozilla/5.0 (compatible; MusicVocalConcert/1.0)"
    },
    "delay": 1.0,
    "timeout": 30
}
```

#### 3.2.2 猫眼演出
```python
# 猫眼演出抓取规则
PLATFORM_MAOYAN = {
    "base_url": "https://show.maoyan.com",
    "api_url": "https://show.maoyan.com/api/shows",
    "selectors": {
        "concerts": ".show-item",
        "name": ".title::text",
        "artist": ".artist::text",
        "city": ".city::text",
        "date": ".date::text",
        "address": ".address::text",
        "venue": ".venue::text",
        "price_range": ".price::text"
    },
    "headers": {
        "User-Agent": "Mozilla/5.0 (compatible; MusicVocalConcert/1.0)"
    },
    "delay": 1.0,
    "timeout": 30
}
```

### 3.3 数据解析

#### 3.3.1 通用解析器
```python
# 通用数据解析器
class DataParser:
    @staticmethod
    def parse_date(date_str: str) -> datetime:
        """解析日期字符串"""
        patterns = [
            r'(\d{4})-(\d{2})-(\d{2})\s+(\d{2}):(\d{2})',
            r'(\d{4})年(\d{1,2})月(\d{1,2})日\s+(\d{1,2}):(\d{2})',
            r'(\d{4})-(\d{2})-(\d{2})'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, date_str)
            if match:
                if len(match.groups()) == 5:
                    # 包含时间的格式
                    year, month, day, hour, minute = match.groups()
                    return datetime(int(year), int(month), int(day), int(hour), int(minute))
                elif len(match.groups()) == 3:
                    # 只包含日期的格式
                    year, month, day = match.groups()
                    return datetime(int(year), int(month), int(day))
        return None

    @staticmethod
    def parse_price_range(price_str: str) -> str:
        """解析票价范围"""
        match = re.search(r'(\d+)-(\d+)元', price_str)
        if match:
            return f"{match.group(1)}-{match.group(2)}元"
        return None
```

## 4. 错误处理规范

### 4.1 错误码定义

#### 4.1.1 客户端错误
- **40001**: 请求参数无效
- **40002**: 缺少必填字段
- **40003**: 数据格式错误
- **40101**: 未授权访问
- **40102**: 令牌过期
- **40301**: 权限不足
- **40401**: 资源未找到

#### 4.1.2 服务端错误
- **50001**: 服务器内部错误
- **50002**: 数据库连接失败
- **50003**: 外部服务调用失败
- **50201**: 网关错误
- **50301**: 服务不可用

### 4.2 错误响应格式
```json
{
  "status": "error",
  "error": {
    "code": "40001",
    "message": "请求参数无效",
    "details": [
      {
        "field": "date",
        "message": "演唱会日期不能早于当前时间"
      }
    ]
  },
  "meta": {
    "timestamp": "2026-02-08T15:30:00+08:00",
    "request_id": "req_123456789"
  }
}
```

## 5. 性能规范

### 5.1 响应时间
- **API响应**: < 200ms
- **页面加载**: < 2s
- **搜索响应**: < 1s
- **数据抓取**: < 30s

### 5.2 并发限制
- **API调用**: 1000请求/分钟
- **数据抓取**: 10并发抓取
- **用户并发**: 1000并发用户

### 5.3 缓存策略
- **Redis缓存**: 热点数据缓存
- **CDN缓存**: 静态资源缓存
- **浏览器缓存**: 客户端缓存

## 6. 安全规范

### 6.1 身份认证
- **JWT令牌**: 使用JWT进行身份认证
- **令牌过期**: 设置合理的过期时间
- **刷新令牌**: 支持令牌刷新

### 6.2 权限控制
- **RBAC模型**: 基于角色的访问控制
- **权限验证**: 每个API调用都验证权限
- **敏感操作**: 记录敏感操作日志

### 6.3 数据保护
- **数据加密**: 敏感数据加密存储
- **传输加密**: HTTPS加密传输
- **日志脱敏**: 日志中脱敏敏感信息

## 7. 监控规范

### 7.1 监控指标
- **API响应时间**: 平均响应时间
- **错误率**: 错误请求比例
- **吞吐量**: 每秒请求数
- **数据抓取成功率**: 抓取成功率

### 7.2 告警规则
- **响应时间过长**: > 500ms
- **错误率过高**: > 5%
- **数据抓取失败**: > 10%
- **服务不可用**: 100%错误率

## 8. 附录

### 8.1 常用工具
- **Postman**: API测试
- **Swagger**: API文档
- **JMeter**: 性能测试
- **ELK Stack**: 日志分析

### 8.2 参考文档
- **RESTful API设计指南**
- **JSON API规范**
- **OAuth 2.0协议**
- **JWT标准**

**文档版本**: 1.0
**创建时间**: 2026-02-08
**最后更新**: 2026-02-08 23:57:00