import os
import re

SKILLS_DIR = 'skills'
README_EN = 'README.md'
README_CN = 'README_zh-CN.md'

# 完整的技能中文翻译字典
TRANSLATIONS = {
    '1password': '使用 1Password CLI 管理密码和凭证。',
    'apple-notes': '读取和操作 Apple Notes（备忘录）。',
    'apple-reminders': '管理 Apple Reminders（提醒事项）。',
    'bear-notes': '与 Bear 笔记应用集成。',
    'bird': '与 Linux 鸟类路由守护进程交互。',
    'blogwatcher': '监控博客更新和 RSS 源。',
    'blucli': '通过命令行控制蓝牙设备。',
    'bluebubbles': '与 BlueBubbles (iMessage Android 客户端) 交互。',
    'camsnap': '从连接的摄像头拍摄快照。',
    'canvas': '与 Canvas LMS 学习管理系统交互。',
    'clawdhub': 'Moltbot 的技能中心集成。',
    'coding-agent': '自主编写和修改代码的智能代理。',
    'currency-converter': '实时货币汇率转换。',
    'discord': '发送消息或管理 Discord 频道。',
    'eightctl': '控制 8bitdo 手柄或其他输入设备。',
    'food-order': '自动化订餐流程（示例）。',
    'gemini': '调用 Google Gemini AI 模型。',
    'gifgrep': '搜索并检索 GIF 动图。',
    'github': '使用 GitHub CLI 进行仓库和 Issue 管理。',
    'github-manager': 'GitHub 仓库与 Issue 管理工具。',
    'gog': '与 GOG.com 游戏平台交互。',
    'goplaces': 'Google Maps / Places API 集成。',
    'himalaya': '命令行邮件客户端 (CLI email)。',
    'imsg': '发送和接收 iMessage 信息。',
    'local-places': '搜索附近的本地地点和服务。',
    'mcporter': 'Minecraft 服务器管理工具。',
    'model-usage': '统计和查询 AI 模型的使用量。',
    'nano-banana-pro': 'Nano Banana Pro 开发板控制工具。',
    'nano-pdf': '轻量级 PDF 阅读与处理工具。',
    'notion': '管理 Notion 页面和数据库。',
    'obsidian': '读取和写入 Obsidian 笔记库。',
    'openai-image-gen': '使用 DALL-E 生成图像。',
    'openai-whisper': '使用本地 Whisper 模型进行语音转文字。',
    'openai-whisper-api': '使用 OpenAI Whisper API 进行转录。',
    'openhue': '控制 Philips Hue 智能灯泡。',
    'oracle': '查询 Oracle 数据库或知识库。',
    'ordercli': '命令行订单管理系统。',
    'pdf-text-extractor': '从 PDF 文件提取文本。',
    'peekaboo': '系统监控与进程检视工具。',
    'sag': 'Solana 验证节点管理工具。',
    'session-logs': '记录和检索 Agent 会话日志。',
    'sherpa-onnx-tts': '使用 Sherpa ONNX 进行本地离线语音合成。',
    'skill-creator': '用于创建新技能的脚手架工具。',
    'slack': '发送 Slack 消息和管理频道。',
    'songsee': '识别或搜索歌曲信息。',
    'sonoscli': '控制 Sonos 智能音响系统。',
    'spotify-player': '控制 Spotify 播放与搜索歌曲。',
    'stock-price': '获取实时股票价格。',
    'summarize': '使用 AI 总结长文本或文件。',
    'system-info': '获取 CPU、内存等系统信息。',
    'things-mac': '管理 Things 3 (Mac) 待办事项。',
    'tmux': '管理 Tmux 终端会话。',
    'trello': '管理 Trello 看板和卡片。',
    'video-frames': '从视频中提取帧或图像。',
    'voice-call': '发起或管理语音通话。',
    'wacli': 'WhatsApp 命令行客户端集成。',
    'weather': '查询天气预报 (wttr.in)。',
    'weather-lookup': '查询天气状况。',
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
        cn_content = re.sub(r'(description:\s*)(.+)', f'\\1{desc_cn}', cn_content, count=1)
        
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
            r'# Tools': '# 工具', # Sometimes headers are level 1
        }
        for eng, chn in header_map.items():
            cn_content = re.sub(eng, chn, cn_content)

        # 3. Inject Chinese Description into Body
        # Look for the navigation block "> [English](SKILL.md)"
        # And ensure the text immediately following it is the Chinese description
        nav_marker = "> [English](SKILL.md)"
        if nav_marker in cn_content:
            # We construct a regex to match the Nav line and the immediate following paragraph
            # We replace it with Nav line + \n\n + Chinese Description
            
            # Simple approach: Find the nav line, then check if the next non-empty line is English text
            # Instead of complex regex, let's just force insert the Chinese description after the nav header
            # if it's not already there.
            
            # Check if the description is already in the body (simple check)
            if desc_cn not in cn_content.split('---')[-1]: # Check body only
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
                    # In English readme, we show both languages as requested before
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