---
name: web-search-duckduckgo
description: Perform an anonymous web search and retrieve a list of results with titles and links.
---

# Web Search (DuckDuckGo)

> [中文](SKILL_zh-CN.md)

This skill allows the agent to search the internet using DuckDuckGo, which requires no API key.

## Tools

### search.py

**Location:** `skills/web-search-duckduckgo/search.py`

**Dependencies:**
- `duckduckgo-search`

Install via: `pip install duckduckgo-search`

**Usage:**

```bash
python skills/web-search-duckduckgo/search.py "Query String" [Max Results]
```

**Example:**

```bash
python skills/web-search-duckduckgo/search.py "latest AI news" 5
```

**Output Format:**

Returns a JSON list of objects:
- `title`: Page title
- `href`: URL
- `body`: Short snippet/description

## Acknowledgments

- Uses the [duckduckgo-search](https://github.com/deedy5/duckduckgo_search) library.
