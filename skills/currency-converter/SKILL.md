---
name: currency-converter
description: Convert amounts between different currencies using real-time exchange rates.
---

# Currency Converter Skill | 汇率转换技能

> [English](SKILL.md) | [中文](SKILL_zh-CN.md)

Convert currency amounts using the Frankfurter API (no API key required).

## Tools

### convert.py

**Location:** `skills/currency-converter/convert.py`

**Usage:**
```bash
python skills/currency-converter/convert.py [amount] [from_currency] [to_currency]
```

**Example:**
```bash
python skills/currency-converter/convert.py 100 USD CNY
```

**Output:**
JSON containing the converted amount and the current exchange rate.
