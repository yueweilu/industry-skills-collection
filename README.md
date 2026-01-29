# AI Agent Skills Collection | AI Agent 技能合集 🤖

> **[English](README.md) | [简体中文](README_zh-CN.md)**

---

### 🌟 Introduction / 简介

**EN**: A curated collection of modular skills (tools) designed for AI agents. This repository hosts standardized tools that AI agents (like Large Language Models) can utilize to interact with the real world—fetching data, controlling software, or processing files.

**ZH**: 这是一个为 AI Agent 精心策划的模块化技能（工具）合集。本仓库托管了一组标准化的工具，AI Agent（如大型语言模型）可以利用这些技能与现实世界互动——获取数据、控制软件或处理文件。

---

## 📂 Available Skills / 可用技能

### 🌐 Information & Search
| Skill Name | Description |
| :--- | :--- |
| [**oracle**](skills/oracle/SKILL.md) | Best practices for using the oracle CLI (prompt + file bundling, engines, sessions, and file attachment patterns). |
| [**summarize**](skills/summarize/SKILL.md) | Summarize or extract text/transcripts from URLs, podcasts, and local files (great fallback for “transcribe this YouTube/video”). |
| [**system-info**](skills/system-info/SKILL.md) | Retrieve current system resource usage (CPU, Memory, Disk). |
| [**weather**](skills/weather/SKILL.md) | Get current weather and forecasts (no API key required). |
| [**weather-lookup**](skills/weather-lookup/SKILL.md) | Retrieve current weather conditions for a specific city. Use when the user asks for weather updates, temperature, or current conditions. |
| [**web-search-duckduckgo**](skills/web-search-duckduckgo/SKILL.md) | Perform an anonymous web search and retrieve a list of results with titles and links. |
| [**youtube-info**](skills/youtube-info/SKILL.md) | Retrieve metadata (title, uploader, views) for a given YouTube video URL. |

### 📊 Finance
| Skill Name | Description |
| :--- | :--- |
| [**currency-converter**](skills/currency-converter/SKILL.md) | Convert amounts between different currencies using real-time exchange rates. |
| [**stock-price**](skills/stock-price/SKILL.md) | Retrieve real-time stock price and market data for a given ticker symbol. |

### 📂 File & Media
| Skill Name | Description |
| :--- | :--- |
| [**camsnap**](skills/camsnap/SKILL.md) | Capture frames or clips from RTSP/ONVIF cameras. |
| [**canvas**](skills/canvas/SKILL.md) | No description available. |
| [**gifgrep**](skills/gifgrep/SKILL.md) | Search GIF providers with CLI/TUI, download results, and extract stills/sheets. |
| [**nano-pdf**](skills/nano-pdf/SKILL.md) | Edit PDFs with natural-language instructions using the nano-pdf CLI. |
| [**openai-image-gen**](skills/openai-image-gen/SKILL.md) | Batch-generate images via OpenAI Images API. Random prompt sampler + `index.html` gallery. |
| [**openai-whisper**](skills/openai-whisper/SKILL.md) | Local speech-to-text with the Whisper CLI (no API key). |
| [**openai-whisper-api**](skills/openai-whisper-api/SKILL.md) | Transcribe audio via OpenAI Audio Transcriptions API (Whisper). |
| [**pdf-text-extractor**](skills/pdf-text-extractor/SKILL.md) | Extract text content from local PDF files for the AI to process. |
| [**songsee**](skills/songsee/SKILL.md) | Generate spectrograms and feature-panel visualizations from audio with the songsee CLI. |
| [**sonoscli**](skills/sonoscli/SKILL.md) | Control Sonos speakers (discover/status/play/volume/group). |
| [**spotify-player**](skills/spotify-player/SKILL.md) | Terminal Spotify playback/search via spogo (preferred) or spotify_player. |
| [**video-frames**](skills/video-frames/SKILL.md) | Extract frames or short clips from videos using ffmpeg. |
| [**voice-call**](skills/voice-call/SKILL.md) | Start voice calls via the Moltbot voice-call plugin. |

### ✅ Productivity
| Skill Name | Description |
| :--- | :--- |
| [**apple-notes**](skills/apple-notes/SKILL.md) | Manage Apple Notes via the `memo` CLI on macOS (create, view, edit, delete, search, move, and export notes). Use when a user asks Moltbot to add a note, list notes, search notes, or manage note folders. |
| [**apple-reminders**](skills/apple-reminders/SKILL.md) | Manage Apple Reminders via the `remindctl` CLI on macOS (list, add, edit, complete, delete). Supports lists, date filters, and JSON/plain output. |
| [**bear-notes**](skills/bear-notes/SKILL.md) | Create, search, and manage Bear notes via grizzly CLI. |
| [**bluebubbles**](skills/bluebubbles/SKILL.md) | Build or update the BlueBubbles external channel plugin for Moltbot (extension package, REST send/probe, webhook inbound). |
| [**discord**](skills/discord/SKILL.md) | Use when you need to control Discord from Moltbot via the discord tool: send messages, react, post or upload stickers, upload emojis, run polls, manage threads/pins/search, create/edit/delete channels and categories, fetch permissions or member/role/channel info, or handle moderation actions in Discord DMs or channels. |
| [**himalaya**](skills/himalaya/SKILL.md) | "CLI to manage emails via IMAP/SMTP. Use `himalaya` to list, read, write, reply, forward, search, and organize emails from the terminal. Supports multiple accounts and message composition with MML (MIME Meta Language)." |
| [**imsg**](skills/imsg/SKILL.md) | iMessage/SMS CLI for listing chats, history, watch, and sending. |
| [**notion**](skills/notion/SKILL.md) | Notion API for creating and managing pages, databases, and blocks. |
| [**obsidian**](skills/obsidian/SKILL.md) | Work with Obsidian vaults (plain Markdown notes) and automate via obsidian-cli. |
| [**slack**](skills/slack/SKILL.md) | Use when you need to control Slack from Moltbot via the slack tool, including reacting to messages or pinning/unpinning items in Slack channels or DMs. |
| [**trello**](skills/trello/SKILL.md) | Manage Trello boards, lists, and cards via the Trello REST API. |

### 🛠 Developer Tools
| Skill Name | Description |
| :--- | :--- |
| [**blucli**](skills/blucli/SKILL.md) | BluOS CLI (blu) for discovery, playback, grouping, and volume. |
| [**coding-agent**](skills/coding-agent/SKILL.md) | Run Codex CLI, Claude Code, OpenCode, or Pi Coding Agent via background process for programmatic control. |
| [**gemini**](skills/gemini/SKILL.md) | Gemini CLI for one-shot Q&A, summaries, and generation. |
| [**github**](skills/github/SKILL.md) | "Interact with GitHub using the `gh` CLI. Use `gh issue`, `gh pr`, `gh run`, and `gh api` for issues, PRs, CI runs, and advanced queries." |
| [**github-manager**](skills/github-manager/SKILL.md) | Interact with GitHub repositories, issues, and pull requests using the GitHub CLI (gh). |
| [**model-usage**](skills/model-usage/SKILL.md) | Use CodexBar CLI local cost usage to summarize per-model usage for Codex or Claude, including the current (most recent) model or a full model breakdown. Trigger when asked for model-level usage/cost data from codexbar, or when you need a scriptable per-model summary from codexbar cost JSON. |
| [**ordercli**](skills/ordercli/SKILL.md) | Foodora-only CLI for checking past orders and active order status (Deliveroo WIP). |
| [**skill-creator**](skills/skill-creator/SKILL.md) | Create or update AgentSkills. Use when designing, structuring, or packaging skills with scripts, references, and assets. |
| [**tmux**](skills/tmux/SKILL.md) | Remote-control tmux sessions for interactive CLIs by sending keystrokes and scraping pane output. |
| [**wacli**](skills/wacli/SKILL.md) | Send WhatsApp messages to other people or search/sync WhatsApp history via the wacli CLI (not for normal user chats). |

### ⚙️ System & IoT
| Skill Name | Description |
| :--- | :--- |
| [**gog**](skills/gog/SKILL.md) | Google Workspace CLI for Gmail, Calendar, Drive, Contacts, Sheets, and Docs. |
| [**nano-banana-pro**](skills/nano-banana-pro/SKILL.md) | Generate or edit images via Gemini 3 Pro Image (Nano Banana Pro). |
| [**openhue**](skills/openhue/SKILL.md) | Control Philips Hue lights/scenes via the OpenHue CLI. |
| [**things-mac**](skills/things-mac/SKILL.md) | Manage Things 3 via the `things` CLI on macOS (add/update projects+todos via URL scheme; read/search/list from the local Things database). Use when a user asks Moltbot to add a task to Things, list inbox/today/upcoming, search tasks, or inspect projects/areas/tags. |

### 🔹 Other
| Skill Name | Description |
| :--- | :--- |
| [**1password**](skills/1password/SKILL.md) | Set up and use 1Password CLI (op). Use when installing the CLI, enabling desktop app integration, signing in (single or multi-account), or reading/injecting/running secrets via op. |
| [**bird**](skills/bird/SKILL.md) | X/Twitter CLI for reading, searching, posting, and engagement via cookies. |
| [**blogwatcher**](skills/blogwatcher/SKILL.md) | Monitor blogs and RSS/Atom feeds for updates using the blogwatcher CLI. |
| [**clawdhub**](skills/clawdhub/SKILL.md) | Use the ClawdHub CLI to search, install, update, and publish agent skills from clawdhub.com. Use when you need to fetch new skills on the fly, sync installed skills to latest or a specific version, or publish new/updated skill folders with the npm-installed clawdhub CLI. |
| [**eightctl**](skills/eightctl/SKILL.md) | Control Eight Sleep pods (status, temperature, alarms, schedules). |
| [**food-order**](skills/food-order/SKILL.md) | Reorder Foodora orders + track ETA/status with ordercli. Never confirm without explicit user approval. Triggers: order food, reorder, track ETA. |
| [**goplaces**](skills/goplaces/SKILL.md) | Query Google Places API (New) via the goplaces CLI for text search, place details, resolve, and reviews. Use for human-friendly place lookup or JSON output for scripts. |
| [**local-places**](skills/local-places/SKILL.md) | Search for places (restaurants, cafes, etc.) via Google Places API proxy on localhost. |
| [**mcporter**](skills/mcporter/SKILL.md) | Use the mcporter CLI to list, configure, auth, and call MCP servers/tools directly (HTTP or stdio), including ad-hoc servers, config edits, and CLI/type generation. |
| [**peekaboo**](skills/peekaboo/SKILL.md) | Capture and automate macOS UI with the Peekaboo CLI. |
| [**sag**](skills/sag/SKILL.md) | ElevenLabs text-to-speech with mac-style say UX. |
| [**session-logs**](skills/session-logs/SKILL.md) | Search and analyze your own session logs (older/parent conversations) using jq. |
| [**sherpa-onnx-tts**](skills/sherpa-onnx-tts/SKILL.md) | Local text-to-speech via sherpa-onnx (offline, no cloud) |


 How to Use

Each skill is located in the `skills/` directory and contains a `SKILL.md` file. This file describes:
1.  **Purpose**: When the AI should use this skill.
2.  **Tools**: The specific scripts (Python/Node.js) to execute.
3.  **IO**: Expected input arguments and output JSON format.

### Interactive CLI

We provide a simple command-line interface to test these skills:

```bash
python main.py
```

## 📦 Dependencies

You can install all dependencies for the skills at once:

```bash
pip install -r requirements.txt
```

## 🤝 Contributing

We welcome contributions! If you have built a useful tool for AI agents, please submit a PR.

1.  Create a new folder in `skills/`.
2.  Add your script (e.g., `tool.py`).
3.  Add a `SKILL.md` following the standard format.
4.  Add an `Acknowledgments` section in your `SKILL.md` if adapted from another project.

## 📄 License

MIT License
