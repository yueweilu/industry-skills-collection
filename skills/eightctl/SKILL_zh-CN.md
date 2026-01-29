---
name: eightctl
控制 8bitdo 手柄或其他输入设备。
homepage: https://eightctl.sh
metadata: {"moltbot":{"emoji":"🎛️","requires":{"bins":["eightctl"]},"install":[{"id":"go","kind":"go","module":"github.com/steipete/eightctl/cmd/eightctl@latest","bins":["eightctl"],"label":"Install eightctl (go)"}]}}
---

# eightctl 技能

> [English](SKILL.md)

控制 8bitdo 手柄或其他输入设备。



# eightctl

Use `eightctl` for Eight Sleep pod control. Requires auth.

Auth
- Config: `~/.config/eightctl/config.yaml`
- Env: `EIGHTCTL_EMAIL`, `EIGHTCTL_PASSWORD`

Quick start
- `eightctl status`
- `eightctl on|off`
- `eightctl temp 20`

Common tasks
- Alarms: `eightctl alarm list|create|dismiss`
- Schedules: `eightctl schedule list|create|update`
- Audio: `eightctl audio state|play|pause`
- Base: `eightctl base info|angle`

Notes
- API is unofficial and rate-limited; avoid repeated logins.
- Confirm before changing temperature or alarms.
