---
name: blucli
通过命令行控制蓝牙设备。
homepage: https://blucli.sh
metadata: {"moltbot":{"emoji":"🫐","requires":{"bins":["blu"]},"install":[{"id":"go","kind":"go","module":"github.com/steipete/blucli/cmd/blu@latest","bins":["blu"],"label":"Install blucli (go)"}]}}
---

# blucli 技能

> [English](SKILL.md)

BluOS 音响系统命令行控制工具。


通过命令行控制蓝牙设备。



# blucli (blu)

Use `blu` to control Bluesound/NAD players.

Quick start
- `blu devices` (pick target)
- `blu --device <id> status`
- `blu play|pause|stop`
- `blu volume set 15`

Target selection (in priority order)
- `--device <id|name|alias>`
- `BLU_DEVICE`
- config default (if set)

Common tasks
- Grouping: `blu group status|add|remove`
- TuneIn search/play: `blu tunein search "query"`, `blu tunein play "query"`

Prefer `--json` for scripts. Confirm the target device before changing playback.
