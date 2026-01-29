---
name: stock-price
description: 获取指定股票代码的实时价格和市场数据。
---

# 股票价格技能 (Stock Price)

> [English](SKILL.md)

此技能允许您使用 Yahoo Finance API 获取当前股市数据。

## 工具

### get_stock.py

**位置:** `skills/stock-price/get_stock.py`

**依赖:**
- `yfinance`

安装: `pip install yfinance`

**用法:**

```bash
python skills/stock-price/get_stock.py "股票代码"
```

**示例:**

```bash
python skills/stock-price/get_stock.py "AAPL"
```

**输出格式:**

返回包含以下内容的 JSON 对象：
- `symbol`: 股票代码
- `current_price`: 当前交易价格
- `currency`: 货币单位
- `market_cap`: 市值
- `volume`: 交易量

## 致谢

- 使用了 [yfinance](https://github.com/ranaroussi/yfinance) 库。
