---
name: system-info
description: Retrieve current system resource usage (CPU, Memory, Disk).
---

# System Info Skill

> [中文](SKILL_zh-CN.md)

This skill allows the agent to inspect the environment it is running in.

## Tools

### sys_stats.py

**Location:** `skills/system-info/sys_stats.py`

**Dependencies:**
- `psutil`

Install via: `pip install psutil`

**Usage:**

```bash
python skills/system-info/sys_stats.py
```

**Output Format:**

Returns a JSON object with:
- `cpu_percent`: Overall CPU usage percentage
- `memory`: Object containing `total`, `available`, `percent`
- `disk`: Object containing `total`, `free`, `percent`
- `platform`: OS name

## Acknowledgments

- Uses the [psutil](https://github.com/giampaolo/psutil) library.
