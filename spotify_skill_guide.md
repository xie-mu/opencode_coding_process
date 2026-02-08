# Spotify技能使用指南

## 🎵 技能概述

**技能名称**: spotify-player
**描述**: Terminal Spotify播放/搜索
**主页**: https://www.spotify.com
**表情**: 🎵

## 📋 技能功能

### 🎯 主要功能
- 🔍 音乐搜索和播放
- 📻 播放列表管理
- 🎛️ 设备控制
- ❤️ 歌曲收藏
- 📱 Spotify Connect集成

## 🔧 安装要求

### 必需条件
- **Spotify Premium账户** ✅
- **终端环境** ✅
- **网络连接** ✅

### 工具安装

#### 推荐工具: spogo (首选)
```bash
# 使用Homebrew安装
brew install --cask spogo

# 验证安装
spogo --version
```

#### 备用工具: spotify_player
```bash
# 使用Homebrew安装
brew install spotify_player

# 验证安装
spotify_player --version
```

## 📦 安装配置

### spogo配置
```bash
# 导入浏览器cookies (推荐Chrome)
spogo auth import --browser chrome

# 检查认证状态
spogo auth status

# 如果需要，可以手动设置
spogo config set client_id <your_client_id>
```

### spotify_player配置
```bash
# 配置文件位置
~/.config/spotify-player/app.toml

# 设置Spotify Connect客户端ID
client_id = "<your_spotify_client_id>"
```

## 🎯 使用命令

### spogo (推荐) 命令

#### 🔍 搜索功能
```bash
# 搜索歌曲
spogo search track "歌曲名称"

# 搜索专辑
spogo search album "专辑名称"

# 搜索艺术家
spogo search artist "艺术家名称"

# 搜索播放列表
spogo search playlist "播放列表名称"
```

#### 🎵 播放控制
```bash
# 开始播放
spogo play

# 暂停播放
spogo pause

# 下一首
spogo next

# 上一首
spogo prev

# 停止播放
spogo stop
```

#### 📱 设备管理
```bash
# 列出所有可用设备
spogo device list

# 选择播放设备
spogo device set "设备名称"

# 获取当前设备状态
spogo device status
```

#### 📊 状态查询
```bash
# 查看当前播放状态
spogo status

# 显示当前播放信息
spogo current

# 获取播放历史
spogo history
```

### spotify_player 命令 (备用)

#### 🔍 搜索功能
```bash
# 搜索歌曲
spotify_player search "歌曲名称"

# 搜索专辑
spotify_player search "专辑名称"

# 搜索艺术家
spotify_player search "艺术家名称"
```

#### 🎵 播放控制
```bash
# 开始播放
spotify_player playback play

# 暂停播放
spotify_player playback pause

# 下一首
spotify_player playback next

# 上一首
spotify_player playback previous

# 停止播放
spotify_player playback stop
```

#### 📱 设备连接
```bash
# 连接设备
spotify_player connect

# 列出设备
spotify_player devices

# 设置设备
spotify_player device set "设备名称"
```

#### ❤️ 歌曲收藏
```bash
# 收藏当前歌曲
spotify_player like

# 取消收藏
spotify_player unlike

# 查看收藏列表
spotify_player liked
```

## 🚀 快速开始

### 第一步: 安装工具
```bash
# 安装spogo (推荐)
brew install --cask spogo

# 或者安装spotify_player
brew install spotify_player
```

### 第二步: 配置认证
```bash
# 导入浏览器cookies
spogo auth import --browser chrome
```

### 第三步: 开始使用
```bash
# 搜索歌曲
spogo search track "周杰伦"

# 播放音乐
spogo play

# 查看状态
spogo status
```

## 📝 使用示例

### 🎵 播放周杰伦的歌曲
```bash
# 搜索周杰伦的歌曲
spogo search track "周杰伦"

# 播放第一首结果
spogo play

# 暂停播放
spogo pause

# 下一首
spogo next
```

### 📻 管理播放列表
```bash
# 搜索播放列表
spogo search playlist "我的最爱"

# 列出可用设备
spogo device list

# 设置播放设备
spogo device set "客厅音响"
```

### ❤️ 收藏歌曲
```bash
# 播放歌曲
spogo play

# 收藏当前歌曲
spogo like

# 查看收藏列表
spogo liked
```

## ⚙️ 高级配置

### spogo配置
```bash
# 查看当前配置
spogo config

# 设置客户端ID
spogo config set client_id <your_client_id>

# 设置输出格式
spogo config set output_format json
```

### spotify_player配置
```bash
# 创建配置文件
mkdir -p ~/.config/spotify-player

# 编辑配置文件
nano ~/.config/spotify-player/app.toml

# 配置文件示例
[theme]
# 主题设置
[client]
# 客户端ID
client_id = "your_spotify_client_id"
```

## 🔧 故障排除

### 常见问题

#### 认证问题
```bash
# 重新导入cookies
spogo auth import --browser chrome

# 检查认证状态
spogo auth status

# 清除认证
spogo auth clear
```

#### 设备连接问题
```bash
# 重新列出设备
spogo device list

# 重新选择设备
spogo device set "设备名称"

# 重启服务
spogo restart
```

#### 播放问题
```bash
# 检查网络连接
ping api.spotify.com

# 检查Spotify状态
spogo status

# 重启播放器
spogo restart
```

## 📚 参考资料

### 官方文档
- Spotify API: https://developer.spotify.com/documentation/web-api/
- spogo GitHub: https://github.com/steipete/Spogo
- spotify_player GitHub: https://github.com/abba23/spotify-player

### 快捷键
- spogo: 按 `?` 查看快捷键
- spotify_player: 按 `?` 查看TUI界面快捷键

---

**最后更新**: 2026-02-08
**技能版本**: 1.0.0
**状态**: ✅ 完整可用