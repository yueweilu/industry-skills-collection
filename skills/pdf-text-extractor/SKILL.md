---
name: pdf-text-extractor
description: Extract text content from local PDF files for the AI to process.
---

# pdf-text-extractor Skill

> [中文](SKILL_zh-CN.md)


# PDF Text Extractor Skill | PDF 文本提取技能

> [English](SKILL.md) | [中文](SKILL_zh-CN.md)

Allows the AI to read the content of local PDF documents.

## Tools

### extract.py

**Location:** `skills/pdf-text-extractor/extract.py`

**Dependencies:** `PyPDF2`

**Usage:**
```bash
python skills/pdf-text-extractor/extract.py [path_to_pdf]
```

**Output:**
JSON containing a preview of the text content and metadata.
