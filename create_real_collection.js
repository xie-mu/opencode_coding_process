const fs = require('fs');
const path = require('path');

// 创建真实的qmd collection
const collection = {
  name: 'OpenClaw Docs & Skills Collection',
  version: '1.0.0',
  created: new Date().toISOString(),
  metadata: {
    totalItems: 0,
    documentCount: 0,
    skillCount: 0
  },
  items: []
};

// 扫描文档
const docsPath = '/root/.openclaw/workspace/docs';
if (fs.existsSync(docsPath)) {
  const docDirs = fs.readdirSync(docsPath);
  docDirs.forEach(dir => {
    const dirPath = path.join(docsPath, dir);
    if (fs.statSync(dirPath).isDirectory()) {
      const files = fs.readdirSync(dirPath).filter(f => f.endsWith('.md'));
      files.forEach(file => {
        const filePath = path.join(dirPath, file);
        const stats = fs.statSync(filePath);
        collection.items.push({
          id: `doc-${dir}-${file}`,
          type: 'document',
          name: file,
          path: filePath,
          size: stats.size,
          modified: stats.mtime.toISOString(),
          category: dir
        });
        collection.metadata.documentCount++;
      });
    }
  });
}

// 扫描技能
const skillsPath = '/root/.openclaw/workspace/skills';
if (fs.existsSync(skillsPath)) {
  const skillDirs = fs.readdirSync(skillsPath);
  skillDirs.forEach(dir => {
    const dirPath = path.join(skillsPath, dir);
    if (fs.statSync(dirPath).isDirectory()) {
      const files = fs.readdirSync(dirPath).filter(f => f.endsWith('SKILL.md'));
      files.forEach(file => {
        const filePath = path.join(dirPath, file);
        const stats = fs.statSync(filePath);
        collection.items.push({
          id: `skill-${dir}-${file}`,
          type: 'skill',
          name: file,
          path: filePath,
          size: stats.size,
          modified: stats.mtime.toISOString(),
          category: dir
        });
        collection.metadata.skillCount++;
      });
    }
  });
}

collection.metadata.totalItems = collection.metadata.documentCount + collection.metadata.skillCount;

// 保存collection
fs.writeFileSync('/root/.openclaw/workspace/real_qmd_collection.json', JSON.stringify(collection, null, 2));

console.log('✅ 真实qmd collection已创建:');
console.log('   文档数量:', collection.metadata.documentCount);
console.log('   技能数量:', collection.metadata.skillCount);
console.log('   总项目数:', collection.metadata.totalItems);
console.log('   保存位置: /root/.openclaw/workspace/real_qmd_collection.json');