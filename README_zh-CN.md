# AI Agent 技能合集 (AI Agent Skills Collection) 🤖

> [English](README.md)

> 一个为 AI Agent 精心策划的模块化技能（工具）合集。

本仓库托管了一组标准化的技能，AI Agent（如大型语言模型）可以利用这些技能与现实世界互动——获取数据、控制软件或处理文件。

每个技能都是独立的，拥有自己的文档和可执行脚本。

## 📂 可用技能 (Available Skills)

🌐 信息与搜索 (Information & Search)
| 技能名称 | 描述 |
| :--- | :--- |
| [**oracle**](skills/oracle/SKILL_zh-CN.md) | Best practices for using the oracle CLI (prompt + file bundling, engines, sessions, and file attachment patterns). |
| [**summarize**](skills/summarize/SKILL_zh-CN.md) | Summarize or extract text/transcripts from URLs, podcasts, and local files (great fallback for “transcribe this YouTube/video”). |
| [**system-info**](skills/system-info/SKILL_zh-CN.md) | Retrieve current system resource usage (CPU, Memory, Disk). |
| [**weather**](skills/weather/SKILL_zh-CN.md) | Get current weather and forecasts (no API key required). |
| [**weather-lookup**](skills/weather-lookup/SKILL_zh-CN.md) | Retrieve current weather conditions for a specific city. Use when the user asks for weather updates, temperature, or current conditions. |
| [**web-search-duckduckgo**](skills/web-search-duckduckgo/SKILL_zh-CN.md) | Perform an anonymous web search and retrieve a list of results with titles and links. |
| [**youtube-info**](skills/youtube-info/SKILL_zh-CN.md) | Retrieve metadata (title, uploader, views) for a given YouTube video URL. |

📊 金融 (Finance)
| 技能名称 | 描述 |
| :--- | :--- |
| [**currency-converter**](skills/currency-converter/SKILL_zh-CN.md) | Convert amounts between different currencies using real-time exchange rates. |
| [**stock-price**](skills/stock-price/SKILL_zh-CN.md) | Retrieve real-time stock price and market data for a given ticker symbol. |

📂 文件与媒体 (File & Media)
| 技能名称 | 描述 |
| :--- | :--- |
| [**camsnap**](skills/camsnap/SKILL_zh-CN.md) | Capture frames or clips from RTSP/ONVIF cameras. |
| [**canvas**](skills/canvas/SKILL_zh-CN.md) | No description available. |
| [**gifgrep**](skills/gifgrep/SKILL_zh-CN.md) | Search GIF providers with CLI/TUI, download results, and extract stills/sheets. |
| [**nano-pdf**](skills/nano-pdf/SKILL_zh-CN.md) | Edit PDFs with natural-language instructions using the nano-pdf CLI. |
| [**openai-image-gen**](skills/openai-image-gen/SKILL_zh-CN.md) | Batch-generate images via OpenAI Images API. Random prompt sampler + `index.html` gallery. |
| [**openai-whisper**](skills/openai-whisper/SKILL_zh-CN.md) | Local speech-to-text with the Whisper CLI (no API key). |
| [**openai-whisper-api**](skills/openai-whisper-api/SKILL_zh-CN.md) | Transcribe audio via OpenAI Audio Transcriptions API (Whisper). |
| [**pdf-text-extractor**](skills/pdf-text-extractor/SKILL_zh-CN.md) | Extract text content from local PDF files for the AI to process. |
| [**songsee**](skills/songsee/SKILL_zh-CN.md) | Generate spectrograms and feature-panel visualizations from audio with the songsee CLI. |
| [**sonoscli**](skills/sonoscli/SKILL_zh-CN.md) | Control Sonos speakers (discover/status/play/volume/group). |
| [**spotify-player**](skills/spotify-player/SKILL_zh-CN.md) | Terminal Spotify playback/search via spogo (preferred) or spotify_player. |
| [**video-frames**](skills/video-frames/SKILL_zh-CN.md) | Extract frames or short clips from videos using ffmpeg. |
| [**voice-call**](skills/voice-call/SKILL_zh-CN.md) | Start voice calls via the Moltbot voice-call plugin. |

✅ 生产力 (Productivity)
| 技能名称 | 描述 |
| :--- | :--- |
| [**apple-notes**](skills/apple-notes/SKILL_zh-CN.md) | Manage Apple Notes via the `memo` CLI on macOS (create, view, edit, delete, search, move, and export notes). Use when a user asks Moltbot to add a note, list notes, search notes, or manage note folders. |
| [**apple-reminders**](skills/apple-reminders/SKILL_zh-CN.md) | Manage Apple Reminders via the `remindctl` CLI on macOS (list, add, edit, complete, delete). Supports lists, date filters, and JSON/plain output. |
| [**bear-notes**](skills/bear-notes/SKILL_zh-CN.md) | Create, search, and manage Bear notes via grizzly CLI. |
| [**bluebubbles**](skills/bluebubbles/SKILL_zh-CN.md) | Build or update the BlueBubbles external channel plugin for Moltbot (extension package, REST send/probe, webhook inbound). |
| [**discord**](skills/discord/SKILL_zh-CN.md) | Use when you need to control Discord from Moltbot via the discord tool: send messages, react, post or upload stickers, upload emojis, run polls, manage threads/pins/search, create/edit/delete channels and categories, fetch permissions or member/role/channel info, or handle moderation actions in Discord DMs or channels. |
| [**himalaya**](skills/himalaya/SKILL_zh-CN.md) | "CLI to manage emails via IMAP/SMTP. Use `himalaya` to list, read, write, reply, forward, search, and organize emails from the terminal. Supports multiple accounts and message composition with MML (MIME Meta Language)." |
| [**imsg**](skills/imsg/SKILL_zh-CN.md) | iMessage/SMS CLI for listing chats, history, watch, and sending. |
| [**notion**](skills/notion/SKILL_zh-CN.md) | Notion API for creating and managing pages, databases, and blocks. |
| [**obsidian**](skills/obsidian/SKILL_zh-CN.md) | Work with Obsidian vaults (plain Markdown notes) and automate via obsidian-cli. |
| [**slack**](skills/slack/SKILL_zh-CN.md) | Use when you need to control Slack from Moltbot via the slack tool, including reacting to messages or pinning/unpinning items in Slack channels or DMs. |
| [**trello**](skills/trello/SKILL_zh-CN.md) | Manage Trello boards, lists, and cards via the Trello REST API. |

🛠 开发工具 (Developer Tools)
| 技能名称 | 描述 |
| :--- | :--- |
| [**blucli**](skills/blucli/SKILL_zh-CN.md) | BluOS CLI (blu) for discovery, playback, grouping, and volume. |
| [**coding-agent**](skills/coding-agent/SKILL_zh-CN.md) | Run Codex CLI, Claude Code, OpenCode, or Pi Coding Agent via background process for programmatic control. |
| [**gemini**](skills/gemini/SKILL_zh-CN.md) | Gemini CLI for one-shot Q&A, summaries, and generation. |
| [**github**](skills/github/SKILL_zh-CN.md) | "Interact with GitHub using the `gh` CLI. Use `gh issue`, `gh pr`, `gh run`, and `gh api` for issues, PRs, CI runs, and advanced queries." |
| [**github-manager**](skills/github-manager/SKILL_zh-CN.md) | Interact with GitHub repositories, issues, and pull requests using the GitHub CLI (gh). |
| [**model-usage**](skills/model-usage/SKILL_zh-CN.md) | Use CodexBar CLI local cost usage to summarize per-model usage for Codex or Claude, including the current (most recent) model or a full model breakdown. Trigger when asked for model-level usage/cost data from codexbar, or when you need a scriptable per-model summary from codexbar cost JSON. |
| [**ordercli**](skills/ordercli/SKILL_zh-CN.md) | Foodora-only CLI for checking past orders and active order status (Deliveroo WIP). |
| [**skill-creator**](skills/skill-creator/SKILL_zh-CN.md) | Create or update AgentSkills. Use when designing, structuring, or packaging skills with scripts, references, and assets. |
| [**tmux**](skills/tmux/SKILL_zh-CN.md) | Remote-control tmux sessions for interactive CLIs by sending keystrokes and scraping pane output. |
| [**wacli**](skills/wacli/SKILL_zh-CN.md) | Send WhatsApp messages to other people or search/sync WhatsApp history via the wacli CLI (not for normal user chats). |

⚙️ 系统与物联网 (System & IoT)
| 技能名称 | 描述 |
| :--- | :--- |
| [**gog**](skills/gog/SKILL_zh-CN.md) | Google Workspace CLI for Gmail, Calendar, Drive, Contacts, Sheets, and Docs. |
| [**nano-banana-pro**](skills/nano-banana-pro/SKILL_zh-CN.md) | Generate or edit images via Gemini 3 Pro Image (Nano Banana Pro). |
| [**openhue**](skills/openhue/SKILL_zh-CN.md) | Control Philips Hue lights/scenes via the OpenHue CLI. |
| [**things-mac**](skills/things-mac/SKILL_zh-CN.md) | Manage Things 3 via the `things` CLI on macOS (add/update projects+todos via URL scheme; read/search/list from the local Things database). Use when a user asks Moltbot to add a task to Things, list inbox/today/upcoming, search tasks, or inspect projects/areas/tags. |

🔹 其他 (Other)
| 技能名称 | 描述 |
| :--- | :--- |
| [**1password**](skills/1password/SKILL_zh-CN.md) | Set up and use 1Password CLI (op). Use when installing the CLI, enabling desktop app integration, signing in (single or multi-account), or reading/injecting/running secrets via op. |
| [**bird**](skills/bird/SKILL_zh-CN.md) | X/Twitter CLI for reading, searching, posting, and engagement via cookies. |
| [**blogwatcher**](skills/blogwatcher/SKILL_zh-CN.md) | Monitor blogs and RSS/Atom feeds for updates using the blogwatcher CLI. |
| [**clawdhub**](skills/clawdhub/SKILL_zh-CN.md) | Use the ClawdHub CLI to search, install, update, and publish agent skills from clawdhub.com. Use when you need to fetch new skills on the fly, sync installed skills to latest or a specific version, or publish new/updated skill folders with the npm-installed clawdhub CLI. |
| [**eightctl**](skills/eightctl/SKILL_zh-CN.md) | Control Eight Sleep pods (status, temperature, alarms, schedules). |
| [**food-order**](skills/food-order/SKILL_zh-CN.md) | Reorder Foodora orders + track ETA/status with ordercli. Never confirm without explicit user approval. Triggers: order food, reorder, track ETA. |
| [**goplaces**](skills/goplaces/SKILL_zh-CN.md) | Query Google Places API (New) via the goplaces CLI for text search, place details, resolve, and reviews. Use for human-friendly place lookup or JSON output for scripts. |
| [**local-places**](skills/local-places/SKILL_zh-CN.md) | Search for places (restaurants, cafes, etc.) via Google Places API proxy on localhost. |
| [**mcporter**](skills/mcporter/SKILL_zh-CN.md) | Use the mcporter CLI to list, configure, auth, and call MCP servers/tools directly (HTTP or stdio), including ad-hoc servers, config edits, and CLI/type generation. |
| [**peekaboo**](skills/peekaboo/SKILL_zh-CN.md) | Capture and automate macOS UI with the Peekaboo CLI. |
| [**sag**](skills/sag/SKILL_zh-CN.md) | ElevenLabs text-to-speech with mac-style say UX. |
| [**session-logs**](skills/session-logs/SKILL_zh-CN.md) | Search and analyze your own session logs (older/parent conversations) using jq. |
| [**sherpa-onnx-tts**](skills/sherpa-onnx-tts/SKILL_zh-CN.md) | Local text-to-speech via sherpa-onnx (offline, no cloud) |


 如何使用

每个技能都位于 `skills/` 目录下，并包含一个 `SKILL.md` (或 `SKILL_zh-CN.md`) 文件。该文件描述了：
1.  **目的**: AI 何时应该使用此技能。
2.  **工具**: 要执行的具体脚本 (Python/Node.js)。
3.  **IO**: 预期的输入参数和输出 JSON 格式。

### 交互式 CLI

我们提供了一个简单的命令行界面来测试这些技能：

```bash
python main.py
```

## 📦 安装依赖

你可以一次性安装所有技能所需的依赖：

```bash
pip install -r requirements.txt
```

## 🤝 参与贡献

我们欢迎贡献！如果您为 AI Agent 构建了有用的工具，请提交 PR。

请参阅 [贡献指南](CONTRIBUTING_zh-CN.md) 了解详细步骤。

1.  在 `skills/` 中创建一个新文件夹。
2.  添加您的脚本（例如 `tool.py`）。
3.  添加符合标准格式的 `SKILL.md`。
4.  如果是改编自其他项目，请在 `SKILL.md` 中添加 `Acknowledgments`（致谢）部分。

## 📄 许可证

MIT License
