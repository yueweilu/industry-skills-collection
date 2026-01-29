---
name: system-info
获取 CPU、内存等系统信息。
---

# 系统信息技能 (System Info)

> [English](SKILL.md)

获取系统资源使用情况 (CPU, 内存, 磁盘)。


获取 CPU、内存等系统信息。


此技能允许 Agent 检查其运行环境的状态。

## 工具

### sys_stats.py

**位置:** `skills/system-info/sys_stats.py`

**依赖:**
- `psutil`

安装: `pip install psutil`

**用法:**

```bash
python skills/system-info/sys_stats.py
```

**输出格式:**

返回包含以下内容的 JSON 对象：
- `cpu_percent`: 总体 CPU 使用率百分比
- `memory`: 包含 `total` (总量), `available` (可用), `percent` (百分比)
- `disk`: 包含 `total`, `free`, `percent`
- `platform`: 操作系统名称

## 致谢

- 使用了 [psutil](https://github.com/giampaolo/psutil) 库。
