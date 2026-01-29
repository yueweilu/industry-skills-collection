---
name: weather-lookup
查询天气状况。
---

# 天气查询技能 (Weather Lookup)

> [English](SKILL.md)

查询天气状况。


此技能允许您使用 `wttr.in` 服务获取任何城市的实时天气信息。

## 工具

### weather.py

一个获取当前天气数据并返回 JSON 格式的 Python 脚本。

**位置:** `skills/weather-lookup/weather.py`

**用法:**

要获取某城市的天气，请运行：

```bash
python skills/weather-lookup/weather.py "城市名称"
```

**示例:**

```bash
python skills/weather-lookup/weather.py "Beijing"
```

**输出格式:**

脚本返回包含以下字段的 JSON 对象：

- `city`: 请求的城市名
- `temperature_C`: 当前摄氏温度
- `weather_desc`: 天气描述（如 "Partly cloudy"）
- `humidity`: 湿度百分比
- `wind_speed_kmph`: 风速 (km/h)
- `observation_time`: 观测时间
