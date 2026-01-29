import os
import re

SKILLS_DIR = 'skills'
README_EN = 'README.md'
README_CN = 'README_zh-CN.md'

# 完整的技能中文翻译字典
TRANSLATIONS = {
    '1password': '设置并使用 1Password CLI (op) 管理凭证。',
    'apple-notes': '通过 memo CLI 管理 macOS 上的 Apple Notes。',
    'apple-reminders': '通过 remindctl CLI 管理 macOS 上的提醒事项。',
    'bear-notes': '通过 grizzly CLI 管理 Bear 笔记。',
    'bird': 'X/Twitter 命令行客户端，用于阅读、搜索和发布推文。',
    'blogwatcher': '监控博客更新和 RSS 源。',
    'blucli': 'BluOS 音响系统命令行控制工具。',
    'bluebubbles': 'BlueBubbles (iMessage) 插件集成与消息管理。',
    'camsnap': '从 RTSP/ONVIF 摄像头抓取画面。',
    'canvas': '与 Canvas LMS 学习管理系统交互。',
    'clawdhub': '搜索、安装和发布 ClawdHub 技能。',
    'coding-agent': '后台运行 Codex 或 Claude Code 进行编程控制。',
    'currency-converter': '使用实时汇率转换货币金额。',
    'discord': '通过 discord 工具控制 Discord 频道和消息。',
    'eightctl': '控制 Eight Sleep 智能床垫 (温度、闹钟)。',
    'food-order': 'Foodora 订餐与订单状态追踪。',
    'gemini': 'Gemini CLI，用于问答、总结和生成。',
    'gifgrep': '搜索、下载和提取 GIF 动图。',
    'github': '使用 gh CLI 管理 GitHub Issue、PR 和 CI。',
    'github-manager': 'GitHub 仓库与 Issue 管理工具。',
    'gog': 'Google Workspace CLI (Gmail, Calendar, Drive 等)。',
    'goplaces': '查询 Google Places API 获取地点详情和评论。',
    'himalaya': '命令行邮件客户端 (IMAP/SMTP) 管理邮件。',
    'imsg': 'iMessage/SMS 命令行工具，用于列出和发送信息。',
    'local-places': '本地代理搜索附近的地点 (Google Places)。',
    'mcporter': '管理和调用 MCP (Model Context Protocol) 服务器。',
    'model-usage': '统计 Codex 或 Claude 的模型使用成本。',
    'nano-banana-pro': '通过 Gemini 3 Pro 生成或编辑图像。',
    'nano-pdf': '使用自然语言指令编辑 PDF。',
    'notion': 'Notion API 接口，用于管理页面和数据库。',
    'obsidian': '通过 obsidian-cli 自动化管理 Obsidian 笔记库。',
    'openai-image-gen': '批量生成 DALL-E 图像并生成画廊。',
    'openai-whisper': '使用本地 Whisper CLI 进行语音转文字 (无 Key)。',
    'openai-whisper-api': '通过 OpenAI API 进行 Whisper 语音转录。',
    'openhue': '通过 OpenHue CLI 控制 Philips Hue 灯光。',
    'oracle': 'Oracle CLI 最佳实践 (Prompt 绑定、会话管理)。',
    'ordercli': '命令行查看 Foodora 历史订单和状态。',
    'pdf-text-extractor': '从 PDF 文件提取文本内容。',
    'peekaboo': '捕获 macOS UI 并进行自动化操作。',
    'sag': 'ElevenLabs 文本转语音工具 (Mac 风格)。',
    'session-logs': '搜索和分析 Agent 的历史会话日志。',
    'sherpa-onnx-tts': '基于 Sherpa ONNX 的本地离线语音合成。',
    'skill-creator': '创建、设计和打包新的 Agent 技能。',
    'slack': '通过 slack 工具控制频道、消息和 Reaction。',
    'songsee': '从音频生成声谱图和可视化特征。',
    'sonoscli': '控制 Sonos 音响 (播放、音量、分组)。',
    'spotify-player': '终端 Spotify 播放器与搜索工具。',
    'stock-price': '获取指定股票代码的实时价格。',
    'summarize': '总结网页、播客或本地文件的内容。',
    'system-info': '获取系统资源使用情况 (CPU, 内存, 磁盘)。',
    'things-mac': '管理 macOS 上的 Things 3 待办事项。',
    'tmux': '远程控制 Tmux 会话，发送按键和抓取输出。',
    'trello': '通过 REST API 管理 Trello 看板和卡片。',
    'video-frames': '使用 ffmpeg 从视频提取帧或片段。',
    'voice-call': '通过 Moltbot 插件发起语音通话。',
    'wacli': 'WhatsApp 命令行工具 (搜索历史、发送消息)。',
    'weather': '获取天气预报 (wttr.in) 无需 API Key。',
    'weather-lookup': '查询特定城市的实时天气状况。',
    'web-search-duckduckgo': 'DuckDuckGo 匿名网络搜索。',
    'youtube-info': '获取 YouTube 视频元数据。'
}

CATEGORIES = {
    'Information & Search': ['weather', 'search', 'info', 'summarize', 'oracle', 'local-places', 'goplaces'],
    'Finance': ['stock', 'currency', 'price', 'food-order', 'ordercli'],
    'File & Media': ['pdf', 'video', 'image', 'gif', 'song', 'spotify', 'sonos', 'voice', 'whisper', 'camsnap', 'canvas', 'tts'],
    'Productivity': ['note', 'reminder', 'calendar', 'todo', 'trello', 'notion', 'obsidian', 'slack', 'discord', 'email', 'himalaya', 'imsg', 'bluebubbles', 'things', 'wacli'],
    'Developer Tools': ['git', 'code', 'terminal', 'tmux', 'shell', 'cli', 'agent', 'skill', 'gemini', 'model', 'clawd'],
    'System & IoT': ['system', 'hue', 'iot', 'mac', 'linux', 'sonos', 'nano', '8ctl', 'gog', 'bird', 'peekaboo', 'sag', 'log'],
    'Other': []
}

def get_category(name):
    name_lower = name.lower()
    for cat, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw in name_lower:
                return cat
    return 'Other'

def process_skill(skill_name):
    skill_path = os.path.join(SKILLS_DIR, skill_name)
    md_path = os.path.join(skill_path, 'SKILL.md')
    cn_path = os.path.join(skill_path, 'SKILL_zh-CN.md')
    
    if not os.path.exists(md_path):
        return None

    with open(md_path, 'r') as f:
        content = f.read()
    
    # Extract English description
    desc_match = re.search(r'description:\s*(.+)', content)
    desc_en = desc_match.group(1).strip() if desc_match else "No description available."
    
    # Get Chinese translation
    desc_cn = TRANSLATIONS.get(skill_name, desc_en)

    # Update SKILL_zh-CN.md with translated description and headers
    if os.path.exists(cn_path):
        with open(cn_path, 'r') as f:
            cn_content = f.read()
        
        # 1. Update Frontmatter Description
        cn_content = re.sub(r'(description:\s*)(.+)', f'\1{desc_cn}', cn_content, count=1)
        
        # 2. Translate Common Headers
        header_map = {
            r'## Tools': '## 工具',
            r'## Usage': '## 用法',
            r'## Example': '## 示例',
            r'## Examples': '## 示例',
            r'## Requirements': '## 要求',
            r'## Description': '## 描述',
            r'## Installation': '## 安装',
            r'## Configuration': '## 配置',
            r'# Tools': '# 工具',
        }
        for eng, chn in header_map.items():
            cn_content = re.sub(eng, chn, cn_content)

        # 3. Inject Chinese Description into Body
        nav_marker = "> [English](SKILL.md)"
        if nav_marker in cn_content:
            # Check if the description is already in the body
            if desc_cn not in cn_content.split('---')[-1]: 
                cn_content = cn_content.replace(nav_marker, f"{nav_marker}\n\n{desc_cn}\n")

        with open(cn_path, 'w') as f:
            f.write(cn_content)

    return {
        'name': skill_name,
        'desc_en': desc_en,
        'desc_cn': desc_cn,
        'category': get_category(skill_name)
    }

def update_readmes():
    skills_data = []
    for item in sorted(os.listdir(SKILLS_DIR)):
        if os.path.isdir(os.path.join(SKILLS_DIR, item)):
            data = process_skill(item)
            if data:
                skills_data.append(data)
    
    # Group by category
    grouped = {}
    for s in skills_data:
        grouped.setdefault(s['category'], []).append(s)
        
    # Generate Tables
    def generate_tables(is_cn=False):
        output = ""
        cat_order = ['Information & Search', 'Finance', 'File & Media', 'Productivity', 'Developer Tools', 'System & IoT', 'Other']
        
        for cat in cat_order:
            skills = grouped.get(cat, [])
            if not skills:
                continue
                
            header = cat
            if is_cn:
                headers_cn = {
                    'Information & Search': '🌐 信息与搜索 (Information & Search)',
                    'Finance': '📊 金融 (Finance)',
                    'File & Media': '📂 文件与媒体 (File & Media)',
                    'Productivity': '✅ 生产力 (Productivity)',
                    'Developer Tools': '🛠 开发工具 (Developer Tools)',
                    'System & IoT': '⚙️ 系统与物联网 (System & IoT)',
                    'Other': '🔹 其他 (Other)'
                }
                header = headers_cn.get(cat, cat)
            else:
                header = f"### {cat}"
                if cat == 'Information & Search': header = "### 🌐 Information & Search"
                if cat == 'Finance': header = "### 📊 Finance"
                if cat == 'File & Media': header = "### 📂 File & Media"
                if cat == 'Productivity': header = "### ✅ Productivity"
                if cat == 'Developer Tools': header = "### 🛠 Developer Tools"
                if cat == 'System & IoT': header = "### ⚙️ System & IoT"
                if cat == 'Other': header = "### 🔹 Other"

            output += f"\n{header}\n"
            if is_cn:
                output += "| 技能名称 | 描述 |\n| :--- | :--- |\n"
            else:
                output += "| Skill Name | Description (EN) | 描述 (ZH) |\n| :--- | :--- | :--- |\n"
            
            for s in skills:
                link = f"skills/{s['name']}/SKILL.md" if not is_cn else f"skills/{s['name']}/SKILL_zh-CN.md"
                if is_cn:
                    output += f"| [**{s['name']}**]({link}) | {s['desc_cn']} |\n"
                else:
                    output += f"| [**{s['name']}**]({link}) | {s['desc_en']} | {s['desc_cn']} |\n"
        return output

    with open(README_EN, 'r') as f:
        en_text = f.read()
    with open(README_CN, 'r') as f:
        cn_text = f.read()

    new_en_table = generate_tables(False)
    new_cn_table = generate_tables(True)
    
    en_pattern = r"(## 📂 Available Skills.*?)(## 🚀)"
    cn_pattern = r"(## 📂 可用技能.*?)(## 🚀)"
    
    new_en_text = re.sub(en_pattern, f"## 📂 Available Skills / 可用技能\n{new_en_table}\n\n\2", en_text, flags=re.DOTALL)
    new_cn_text = re.sub(cn_pattern, f"## 📂 可用技能 (Available Skills)\n{new_cn_table}\n\n\2", cn_text, flags=re.DOTALL)
    
    with open(README_EN, 'w') as f:
        f.write(new_en_text)
    with open(README_CN, 'w') as f:
        f.write(new_cn_text)

if __name__ == "__main__":
    update_readmes()
