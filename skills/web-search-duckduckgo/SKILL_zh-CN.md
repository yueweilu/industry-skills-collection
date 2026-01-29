---
name: web-search-duckduckgo
description: 执行匿名网络搜索并返回带有标题和链接的结果列表。
---

# 网络搜索 (DuckDuckGo)

> [English](SKILL.md)

此技能允许 Agent 使用 DuckDuckGo 搜索互联网，无需 API 密钥。

## 工具

### search.py

**位置:** `skills/web-search-duckduckgo/search.py`

**依赖:**
- `duckduckgo-search`

安装: `pip install duckduckgo-search`

**用法:**

```bash
python skills/web-search-duckduckgo/search.py "查询字符串" [最大结果数]
```

**示例:**

```bash
python skills/web-search-duckduckgo/search.py "最新 AI 新闻" 5
```

**输出格式:**

返回 JSON 列表：
- `title`: 页面标题
- `href`: 链接 URL
- `body`: 简短摘要

## 致谢

- 使用了 [duckduckgo-search](https://github.com/deedy5/duckduckgo_search) 库。
