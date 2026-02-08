#!/bin/bash
# 每日文档同步脚本

echo "开始同步OpenClaw官方文档..."
cd /root/.openclaw/workspace || exit 1

# 同步OpenClaw官方文档
if [ -d "docs/openclaw" ]; then
    cd docs/openclaw
    git pull
    cd ../..
else
    git clone https://github.com/openclaw/openclaw.git docs/openclaw
fi

# 同步ClawHub官方文档
if [ -d "docs/clawhub" ]; then
    cd docs/clawhub
    git pull
    cd ../..
else
    git clone https://github.com/openclaw/clawhub.git docs/clawhub
fi

# 同步OpenClaw技能代码库
if [ -d "skills/openclaw-skills" ]; then
    cd skills/openclaw-skills
    git pull
    cd ../..
else
    git clone https://github.com/openclaw/openclaw.git skills/openclaw-skills
fi

echo "✅ 文档同步完成！"