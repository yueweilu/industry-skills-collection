# GitHub 管理技能 (GitHub Manager)

> [English](SKILL.md)

GitHub 仓库与 Issue 管理工具。


此技能允许 AI 通过 GitHub CLI (gh) 直接在命令行管理仓库、Issue 和 Pull Request。

## 工具

### gh_tool.py

官方 `gh` CLI 的封装脚本。

**位置:** `skills/github-manager/gh_tool.py`

**要求:**
- 必须安装 GitHub CLI (`gh`) 并且已登录 (`gh auth login`)。

**用法:**
```bash
python skills/github-manager/gh_tool.py [子命令]
```

**示例:**
- `python skills/github-manager/gh_tool.py repo view` (查看当前仓库信息)
- `python skills/github-manager/gh_tool.py issue list` (列出开启的 Issue)
