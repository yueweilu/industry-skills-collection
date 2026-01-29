---
name: github-manager
description: Interact with GitHub repositories, issues, and pull requests using the GitHub CLI (gh).
---

# github-manager Skill

> [中文](SKILL_zh-CN.md)


# GitHub Manager Skill | GitHub 管理技能

> [English](SKILL.md) | [中文](SKILL_zh-CN.md)

This skill empowers the AI to manage GitHub resources directly via the command line.

## Tools

### gh_tool.py

A wrapper around the official `gh` CLI.

**Location:** `skills/github-manager/gh_tool.py`

**Requirements:**
- GitHub CLI (`gh`) must be installed and authenticated (`gh auth login`).

**Usage:**
```bash
python skills/github-manager/gh_tool.py [subcommand]
```

**Examples:**
- `python skills/github-manager/gh_tool.py repo view` (View current repo info)
- `python skills/github-manager/gh_tool.py issue list` (List open issues)

## Acknowledgments

- Inspired by the [Moltbot](https://github.com/moltbot/molt) skills structure.
